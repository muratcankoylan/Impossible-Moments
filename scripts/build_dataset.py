#!/usr/bin/env python3
"""
Build structured dataset from Impossible Moments scenario markdown files.
Outputs: JSON, CSV, and Parquet (for Hugging Face Hub).

Usage:
    python scripts/build_dataset.py
"""

import os
import re
import json
import csv
import sys

SCENARIOS_DIR = os.path.join(os.path.dirname(__file__), "..", "scenarios")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "dataset")

TIER_ORDER = [
    "tier_1_spark",
    "tier_2_fracture",
    "tier_3_rupture",
    "tier_4_singularity",
    "tier_5_impossible",
]

TIER_MAP = {
    "tier_1_spark": {"tier_num": 1, "tier_name": "SPARK"},
    "tier_2_fracture": {"tier_num": 2, "tier_name": "FRACTURE"},
    "tier_3_rupture": {"tier_num": 3, "tier_name": "RUPTURE"},
    "tier_4_singularity": {"tier_num": 4, "tier_name": "SINGULARITY"},
    "tier_5_impossible": {"tier_num": 5, "tier_name": "IMPOSSIBLE"},
}

STATUS_NORMALIZE = {
    "KNOWN-SOLUTION": "KS",
    "KNOWN-SOLUTION (KS)": "KS",
    "KNOWN-SOLUTION (KS-MULTIPLE)": "KS",
    "KS-MULTIPLE": "KS",
    "KS (KNOWN-SOLUTION)": "KS",
    "KS": "KS",
    "CT": "CT",
    "CONTESTED": "CT",
    "CONTESTED (CT)": "CT",
    "OF": "OF",
    "OF (OPEN-FRONTIER)": "OF",
    "OPEN-FRONTIER": "OF",
    "OPEN-FRONTIER (OF)": "OF",
    "PX": "PX",
    "PX (PROVABLY IMPOSSIBLE)": "PX",
    "PARADOX": "PX",
    "PARADOX (PX)": "PX",
    "MT": "MT",
    "MT (METAMORPHIC)": "MT",
    "METAMORPHIC": "MT",
    "METAMORPHIC (MT)": "MT",
    "DG": "DG",
    "DG (DEGENERATE)": "DG",
    "DEGENERATE": "DG",
    "DEGENERATE (DG)": "DG",
}

STATUS_FULL_NAMES = {
    "KS": "Known-Solution",
    "CT": "Contested",
    "OF": "Open-Frontier",
    "PX": "Paradox",
    "MT": "Metamorphic",
    "DG": "Degenerate",
}


def extract_header_field(text, field_name):
    """Extract a **Field**: Value line from the header."""
    pattern = rf"\*\*{re.escape(field_name)}\*\*\s*:\s*(.+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    # Try without bold
    pattern2 = rf"^{re.escape(field_name)}\s*:\s*(.+)"
    match2 = re.search(pattern2, text, re.MULTILINE | re.IGNORECASE)
    if match2:
        return match2.group(1).strip()
    return ""


def extract_section(text, heading, level=2):
    """Extract content under a markdown heading (## or ###)."""
    prefix = "#" * level
    # Match the heading and capture until the next heading of same or higher level
    pattern = rf"^{prefix}\s+{re.escape(heading)}\s*\n(.*?)(?=^{'#' * level}\s|\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    # Try flexible matching
    pattern2 = rf"^{prefix}\s+.*{re.escape(heading)}.*\n(.*?)(?=^{'#' * level}\s|\Z)"
    match2 = re.search(pattern2, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if match2:
        return match2.group(1).strip()
    return ""


def extract_section_flexible(text, heading_keywords, level=2):
    """Extract section matching any of the keywords in the heading."""
    prefix = "#" * level
    for kw in heading_keywords:
        pattern = rf"^{prefix}\s+[^\n]*{re.escape(kw)}[^\n]*\n(.*?)(?=^{'#' * level}\s|\Z)"
        match = re.search(pattern, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""


def extract_objects_table(text):
    """Extract the Available Objects table as a list of dicts."""
    section = extract_section_flexible(text, ["Available Objects", "Objects"], level=3)
    if not section:
        section = extract_section_flexible(text, ["Available Objects", "Objects"], level=2)
    if not section:
        return []

    objects = []
    lines = section.strip().split("\n")
    header_idx = None
    for i, line in enumerate(lines):
        if "|" in line and ("Object" in line or "Item" in line or "Name" in line):
            header_idx = i
            break

    if header_idx is None:
        return []

    # Parse header
    headers = [h.strip() for h in lines[header_idx].split("|") if h.strip()]

    # Skip separator line
    for line in lines[header_idx + 2 :]:
        if not line.strip() or not "|" in line:
            break
        cells = [c.strip() for c in line.split("|") if c.strip()]
        if len(cells) >= 2:
            obj = {}
            for j, h in enumerate(headers):
                obj[h.lower().replace(" ", "_")] = cells[j] if j < len(cells) else ""
            objects.append(obj)

    return objects


RATING_MAP = {
    "none": 1, "minimal": 1, "very low": 1, "low": 1,
    "low-medium": 2, "low-med": 2, "low–medium": 2,
    "medium": 3, "med": 3, "moderate": 3,
    "medium-high": 4, "med-high": 4, "medium–high": 4, "high": 4,
    "very high": 5, "extreme": 5, "maximum": 5, "critical": 5,
}


def rating_to_num(text):
    """Convert a descriptive rating to 1-5 numeric."""
    t = text.lower().strip().rstrip(".")
    # Direct match
    if t in RATING_MAP:
        return RATING_MAP[t]
    # Partial match
    for key, val in RATING_MAP.items():
        if key in t:
            return val
    return None


def extract_difficulty_profile(text):
    """Extract I.D.C.B.T.X difficulty profile from various formats."""
    def make_profile(i, d, c, b, t, x):
        return {
            "insight_depth": int(i),
            "distractor_density": int(d),
            "counter_intuitive": int(c),
            "domain_bridge": int(b),
            "temporal_pressure": int(t),
            "trap_depth": int(x),
        }

    # Pattern 1: I3.D2.C2.B2.T3.X2 (with or without backticks)
    match = re.search(
        r"I(\d)\.?D(\d)\.?C(\d)\.?B(\d)\.?T(\d)\.?X(\d)", text, re.IGNORECASE
    )
    if match:
        return make_profile(*match.groups())

    # Pattern 2: backtick-wrapped like `I3.D2.C2.B2.T3.X2`
    match1b = re.search(
        r"`I(\d)\.D(\d)\.C(\d)\.B(\d)\.T(\d)\.X(\d)`", text, re.IGNORECASE
    )
    if match1b:
        return make_profile(*match1b.groups())

    # Pattern 3: from a table with I/D/C/B/T/X ratings (e.g., **I** | 5/5)
    profile = {}
    dim_patterns = [
        ("insight_depth", r"\*\*I\*\*.*?(\d)\s*/\s*5"),
        ("distractor_density", r"\*\*D\*\*.*?(\d)\s*/\s*5"),
        ("counter_intuitive", r"\*\*C\*\*.*?(\d)\s*/\s*5"),
        ("domain_bridge", r"\*\*B\*\*.*?(\d)\s*/\s*5"),
        ("temporal_pressure", r"\*\*T\*\*.*?(\d)\s*/\s*5"),
        ("trap_depth", r"\*\*X\*\*.*?(\d)\s*/\s*5"),
    ]
    for dim_name, pat in dim_patterns:
        m = re.search(pat, text, re.IGNORECASE | re.DOTALL)
        if m:
            profile[dim_name] = int(m.group(1))

    if len(profile) >= 4:
        return profile

    # Pattern 4: from header "Difficulty": "2.2.2.2.2.2" or "SINGULARITY (4.3.4.4.3.4)"
    # Also match inside parentheses
    all_six = re.findall(r"(?<!\d)(\d)\.(\d)\.(\d)\.(\d)\.(\d)\.(\d)(?!\d)", text)
    if all_six:
        # Take the first match
        return make_profile(*all_six[0])

    # Pattern 5: Dimension | Rating | Notes table rows
    dim_alt = [
        ("insight_depth", r"[Ii]nsight\s*[Dd]epth.*?(\d)\s*/\s*5"),
        ("distractor_density", r"[Dd]istractor.*?(\d)\s*/\s*5"),
        ("counter_intuitive", r"[Cc]ounter.*?[Ii]ntuiti.*?(\d)\s*/\s*5"),
        ("domain_bridge", r"[Dd]omain\s*[Bb]ridge.*?(\d)\s*/\s*5"),
        ("temporal_pressure", r"[Tt]emporal\s*[Pp]ressure.*?(\d)\s*/\s*5"),
        ("trap_depth", r"[Tt]rap\s*[Dd]epth.*?(\d)\s*/\s*5"),
    ]
    profile2 = {}
    for dim_name, pat in dim_alt:
        m = re.search(pat, text, re.DOTALL)
        if m:
            profile2[dim_name] = int(m.group(1))

    if len(profile2) >= 4:
        return profile2

    # Pattern 6: Descriptive ratings in a table (Low/Medium/High)
    # Matches lines like: | **I - Identification** | Low | ...
    # or: | **D - Distraction** | Medium | ...
    dim_desc = [
        ("insight_depth", r"\|\s*\*\*I\b[^|]*\*\*\s*\|\s*([^|]+?)\s*\|"),
        ("distractor_density", r"\|\s*\*\*D\b[^|]*\*\*\s*\|\s*([^|]+?)\s*\|"),
        ("counter_intuitive", r"\|\s*\*\*C\b[^|]*\*\*\s*\|\s*([^|]+?)\s*\|"),
        ("domain_bridge", r"\|\s*\*\*B\b[^|]*\*\*\s*\|\s*([^|]+?)\s*\|"),
        ("temporal_pressure", r"\|\s*\*\*T\b[^|]*\*\*\s*\|\s*([^|]+?)\s*\|"),
        ("trap_depth", r"\|\s*\*\*X\b[^|]*\*\*\s*\|\s*([^|]+?)\s*\|"),
    ]
    profile3 = {}
    for dim_name, pat in dim_desc:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            num = rating_to_num(m.group(1))
            if num is not None:
                profile3[dim_name] = num

    if len(profile3) >= 3:
        return profile3

    return None


def normalize_category(raw_cat):
    """Normalize category to one of the 12 standard categories."""
    cat_map = {
        "locked room": "The Locked Room",
        "wrong toolbox": "The Wrong Toolbox",
        "misdirection": "The Misdirection",
        "cascade": "The Cascade",
        "babel": "The Babel Problem",
        "lilliput": "The Lilliput Conundrum",
        "ticking trade": "The Ticking Trade",
        "ghost machine": "The Ghost Machine",
        "last ingredient": "The Last Ingredient",
        "invisible wall": "The Invisible Wall",
        "memory palace": "The Memory Palace",
        "horizon": "The Horizon Problem",
        "temporal-spatial": "The Locked Room",
    }
    lower = raw_cat.lower().strip()
    for key, val in cat_map.items():
        if key in lower:
            return val
    return raw_cat.strip()


def parse_scenario(filepath, tier_dir):
    """Parse a single scenario markdown file into a structured dict."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    filename = os.path.basename(filepath)
    id_match = re.search(r"IM-(\d+)", filename)
    if not id_match:
        return None

    scenario_id = f"IM-{int(id_match.group(1)):04d}"
    scenario_num = int(id_match.group(1))

    # Extract title from first heading
    title_match = re.search(r"^#\s+IM-\d+:\s*(.+)", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # Extract header fields
    raw_category = extract_header_field(text, "Category")
    raw_difficulty = extract_header_field(text, "Difficulty")
    raw_status = extract_header_field(text, "Status")
    raw_answer = extract_header_field(text, "Correct Answer")
    if not raw_answer:
        raw_answer = extract_header_field(text, "Correct Outcome")

    # Normalize
    category = normalize_category(raw_category)
    status = STATUS_NORMALIZE.get(raw_status.upper(), raw_status.upper()[:2])
    status_full = STATUS_FULL_NAMES.get(status, status)

    tier_info = TIER_MAP.get(tier_dir, {"tier_num": 0, "tier_name": "UNKNOWN"})

    # Extract sections
    scenario_text = extract_section(text, "Scenario")
    environment = extract_section_flexible(text, ["Environment"], level=3)
    threat = extract_section_flexible(text, ["Threat"], level=3)
    position = extract_section_flexible(
        text, ["Your Position", "Position", "Starting Position"], level=3
    )
    objects = extract_objects_table(text)
    human_caps = extract_section_flexible(
        text, ["Human Capabilities", "Human Capability", "Capabilities"], level=3
    )

    why_impossible = extract_section_flexible(
        text, ["Why This Looks Impossible", "Why This Is Impossible", "Why It Looks Impossible"], level=2
    )

    solution = extract_section_flexible(
        text,
        [
            "Verified Solution",
            "Verified Solutions",
            "Solution",
            "Evaluation Framework",
        ],
        level=2,
    )

    physics = extract_section_flexible(
        text, ["Physics Validation", "Physics"], level=3
    )
    if not physics:
        physics = extract_section_flexible(
            text, ["Physics Validation", "Physics"], level=2
        )

    eval_criteria = extract_section_flexible(
        text, ["Evaluation Criteria", "Evaluation", "Scoring"], level=2
    )

    design_notes = extract_section_flexible(
        text, ["Design Notes", "Key Insights", "Difficulty Profile"], level=2
    )

    difficulty_profile = extract_difficulty_profile(text)

    # Build the prompt (what you'd give to a model being evaluated)
    # This is the scenario WITHOUT the solution or evaluation criteria
    prompt_sections = []
    if title:
        prompt_sections.append(f"# {scenario_id}: {title}\n")
    if scenario_text:
        prompt_sections.append(scenario_text)
    if why_impossible:
        prompt_sections.append(f"\n## Why This Looks Impossible\n\n{why_impossible}")

    prompt = "\n".join(prompt_sections).strip()

    return {
        "id": scenario_id,
        "num": scenario_num,
        "title": title,
        "category": category,
        "tier_num": tier_info["tier_num"],
        "tier_name": tier_info["tier_name"],
        "status": status,
        "status_full": status_full,
        "correct_answer": raw_answer,
        "difficulty_profile": difficulty_profile,
        "prompt": prompt,
        "scenario": scenario_text,
        "environment": environment,
        "threat": threat,
        "position": position,
        "available_objects": objects,
        "human_capabilities": human_caps,
        "why_impossible": why_impossible,
        "solution": solution,
        "physics_validation": physics,
        "evaluation_criteria": eval_criteria,
        "design_notes": design_notes,
        "full_text": text,
        "source_file": f"scenarios/{tier_dir}/{filename}",
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_scenarios = []
    for tier_dir in TIER_ORDER:
        tier_path = os.path.join(SCENARIOS_DIR, tier_dir)
        if not os.path.isdir(tier_path):
            print(f"WARNING: {tier_path} not found, skipping")
            continue

        files = sorted(
            [f for f in os.listdir(tier_path) if f.endswith(".md") and f.startswith("IM-")],
            key=lambda x: int(re.search(r"IM-(\d+)", x).group(1)),
        )
        for fname in files:
            fpath = os.path.join(tier_path, fname)
            parsed = parse_scenario(fpath, tier_dir)
            if parsed:
                all_scenarios.append(parsed)

    print(f"Parsed {len(all_scenarios)} scenarios")

    # Validate
    nums = [s["num"] for s in all_scenarios]
    assert nums == list(range(1, len(nums) + 1)), "Numbering is not sequential!"

    # ---- JSON (full) ----
    json_path = os.path.join(OUTPUT_DIR, "impossible_moments.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_scenarios, f, indent=2, ensure_ascii=False)
    print(f"Wrote {json_path}")

    # ---- JSONL (for HF datasets) ----
    jsonl_path = os.path.join(OUTPUT_DIR, "impossible_moments.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for s in all_scenarios:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"Wrote {jsonl_path}")

    # ---- CSV (flat, key fields only) ----
    csv_path = os.path.join(OUTPUT_DIR, "impossible_moments.csv")
    csv_fields = [
        "id",
        "title",
        "category",
        "tier_num",
        "tier_name",
        "status",
        "status_full",
        "correct_answer",
        "source_file",
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for s in all_scenarios:
            writer.writerow({k: s[k] for k in csv_fields})
    print(f"Wrote {csv_path}")

    # ---- Parquet (requires pyarrow or pandas) ----
    try:
        import pandas as pd

        # Flatten difficulty_profile for tabular format
        flat_scenarios = []
        for s in all_scenarios:
            flat = {k: v for k, v in s.items() if k not in ("difficulty_profile", "available_objects")}
            dp = s.get("difficulty_profile") or {}
            flat["difficulty_I"] = dp.get("insight_depth", None)
            flat["difficulty_D"] = dp.get("distractor_density", None)
            flat["difficulty_C"] = dp.get("counter_intuitive", None)
            flat["difficulty_B"] = dp.get("domain_bridge", None)
            flat["difficulty_T"] = dp.get("temporal_pressure", None)
            flat["difficulty_X"] = dp.get("trap_depth", None)
            flat["available_objects"] = json.dumps(s.get("available_objects", []), ensure_ascii=False)
            flat_scenarios.append(flat)

        df = pd.DataFrame(flat_scenarios)
        parquet_path = os.path.join(OUTPUT_DIR, "impossible_moments.parquet")
        df.to_parquet(parquet_path, index=False, engine="pyarrow")
        print(f"Wrote {parquet_path}")

        # Print summary stats
        print(f"\n--- Dataset Summary ---")
        print(f"Total scenarios: {len(df)}")
        print(f"\nBy tier:")
        print(df.groupby("tier_name").size().to_string())
        print(f"\nBy status:")
        print(df.groupby("status").size().to_string())
        print(f"\nBy category:")
        print(df.groupby("category").size().to_string())
        print(f"\nFields per row: {len(df.columns)}")
        print(f"Columns: {', '.join(df.columns.tolist())}")

    except ImportError:
        print("WARNING: pandas/pyarrow not installed, skipping parquet output")
        print("Install with: pip install pandas pyarrow")


if __name__ == "__main__":
    main()

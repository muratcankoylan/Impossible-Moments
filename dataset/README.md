---
license: mit
task_categories:
  - question-answering
  - text-generation
language:
  - en
tags:
  - benchmark
  - reasoning
  - creative-problem-solving
  - physics
  - constraint-satisfaction
  - agi
  - functional-fixedness
  - multi-agent
pretty_name: Impossible Moments
size_categories:
  - n<1K
configs:
  - config_name: default
    data_files:
      - split: test
        path: impossible_moments.parquet
dataset_info:
  features:
    - name: id
      dtype: string
    - name: num
      dtype: int64
    - name: title
      dtype: string
    - name: category
      dtype: string
    - name: tier_num
      dtype: int64
    - name: tier_name
      dtype: string
    - name: status
      dtype: string
    - name: status_full
      dtype: string
    - name: correct_answer
      dtype: string
    - name: prompt
      dtype: string
    - name: scenario
      dtype: string
    - name: environment
      dtype: string
    - name: threat
      dtype: string
    - name: position
      dtype: string
    - name: human_capabilities
      dtype: string
    - name: why_impossible
      dtype: string
    - name: solution
      dtype: string
    - name: physics_validation
      dtype: string
    - name: evaluation_criteria
      dtype: string
    - name: design_notes
      dtype: string
    - name: full_text
      dtype: string
    - name: source_file
      dtype: string
    - name: available_objects
      dtype: string
    - name: difficulty_I
      dtype: int64
    - name: difficulty_D
      dtype: int64
    - name: difficulty_C
      dtype: int64
    - name: difficulty_B
      dtype: int64
    - name: difficulty_T
      dtype: int64
    - name: difficulty_X
      dtype: int64
  splits:
    - name: test
      num_examples: 420
---

# Impossible Moments

### A Benchmark for Creative Constraint Satisfaction and Reasoning in AI Systems

**420 scenarios** | **12 categories** | **6 solution statuses** | **5 difficulty tiers** | **29 structured fields per scenario**

## What is this?

Impossible Moments (IM) is a benchmark that tests what no existing benchmark measures: **creative reasoning under impossible constraints**. Each scenario drops the solver into a physically precise, narratively urgent situation that appears unsolvable -- a locked room with a bomb, a bridge that can't be built, a trading crisis with no conventional exit. The solver must break functional fixedness, reject distractors, chain non-obvious insights, and validate solutions against real physics.

## Quick Start

```python
from datasets import load_dataset

ds = load_dataset("muratcankoylan/impossible-moments", split="test")

# Browse a scenario
scenario = ds[62]  # IM-0063: The Blast Room
print(scenario["prompt"])        # What you give to the model
print(scenario["solution"])      # The verified answer
print(scenario["correct_answer"])  # Short answer (e.g., "LIVE")

# Filter by tier
tier_5 = ds.filter(lambda x: x["tier_num"] == 5)
print(f"Tier 5 (Impossible): {len(tier_5)} scenarios")

# Filter by category
locked_rooms = ds.filter(lambda x: x["category"] == "The Locked Room")
print(f"Locked Room scenarios: {len(locked_rooms)}")

# Filter by status
open_frontier = ds.filter(lambda x: x["status"] == "OF")
print(f"Open Frontier (unsolved): {len(open_frontier)}")
```

## Evaluating a Model

```python
from datasets import load_dataset

ds = load_dataset("muratcankoylan/impossible-moments", split="test")

for scenario in ds:
    # Send only the prompt to the model (no solution, no rubric)
    prompt = scenario["prompt"]

    # Get model response
    # response = your_model(prompt)

    # Score against evaluation criteria
    correct_answer = scenario["correct_answer"]
    eval_criteria = scenario["evaluation_criteria"]
    # ... your scoring logic
```

## Dataset Structure

Each row contains 29 fields:

### Identification
| Field | Type | Description |
|---|---|---|
| `id` | string | Scenario ID (e.g., "IM-0063") |
| `num` | int | Numeric index (1-420) |
| `title` | string | Scenario title (e.g., "The Blast Room") |
| `source_file` | string | Path to original markdown file |

### Classification
| Field | Type | Description |
|---|---|---|
| `category` | string | One of 12 scenario categories |
| `tier_num` | int | Difficulty tier (1-5) |
| `tier_name` | string | Tier name (SPARK, FRACTURE, RUPTURE, SINGULARITY, IMPOSSIBLE) |
| `status` | string | Solution status code (KS, CT, OF, PX, MT, DG) |
| `status_full` | string | Full status name (Known-Solution, Contested, etc.) |
| `correct_answer` | string | The correct answer or outcome |

### Content (for evaluation)
| Field | Type | Description |
|---|---|---|
| `prompt` | string | **What to give the model** -- scenario + "why impossible" (no solution) |
| `scenario` | string | Full scenario narrative with environment, objects, constraints |
| `environment` | string | Physical environment description |
| `threat` | string | What makes this urgent |
| `position` | string | Starting position of the solver |
| `available_objects` | string | JSON array of objects with mass, dimensions, material, notes |
| `human_capabilities` | string | Physical parameters of the solver |
| `why_impossible` | string | Why the scenario appears unsolvable |

### Answers (for scoring)
| Field | Type | Description |
|---|---|---|
| `solution` | string | Verified solution with step-by-step validation |
| `physics_validation` | string | Quantitative physics calculations |
| `evaluation_criteria` | string | Scoring rubric with correct/wrong response examples |
| `design_notes` | string | Design rationale and key insights |

### Difficulty Profile (I.D.C.B.T.X)
| Field | Type | Description |
|---|---|---|
| `difficulty_I` | int | Insight Depth (1-5): non-obvious leaps required |
| `difficulty_D` | int | Distractor Density (1-5): seductive wrong paths |
| `difficulty_C` | int | Counter-Intuitive Index (1-5): solution defies common sense |
| `difficulty_B` | int | Domain Bridge (1-5): knowledge domains to connect |
| `difficulty_T` | int | Temporal Pressure (1-5): time pressure on decisions |
| `difficulty_X` | int | Trap Depth (1-5): depth of misdirection |

### Full Text
| Field | Type | Description |
|---|---|---|
| `full_text` | string | Complete original markdown (all sections) |

## Distribution

### By Tier
| Tier | Count | Expected Model Accuracy |
|---|---|---|
| 1 - SPARK | 62 | 60-80% |
| 2 - FRACTURE | 163 | 30-50% |
| 3 - RUPTURE | 106 | 10-25% |
| 4 - SINGULARITY | 73 | 0-10% |
| 5 - IMPOSSIBLE | 16 | 0-2% |

### By Status
| Status | Full Name | Count | Description |
|---|---|---|---|
| KS | Known-Solution | 336 | Verified solution exists |
| CT | Contested | 15 | Solution is disputed |
| OF | Open-Frontier | 32 | No known solution |
| PX | Paradox | 14 | Provably impossible |
| MT | Metamorphic | 14 | Solvable after reframing |
| DG | Degenerate | 9 | Trivially solvable (trap: resist overthinking) |

### By Category
| Category | Count | Signature Challenge |
|---|---|---|
| The Locked Room | 45 | Escape under time pressure |
| The Wrong Toolbox | 40 | Build with wrong materials |
| The Babel Problem | 39 | Cooperate under communication constraints |
| The Misdirection | 38 | Resist the obvious trap |
| The Lilliput Conundrum | 37 | Reason at extreme scales |
| The Ghost Machine | 33 | Explain or debunk the "impossible" |
| The Ticking Trade | 32 | Find the hidden third option |
| The Cascade | 42 | Fix coupled failures |
| The Last Ingredient | 31 | Replace the irreplaceable |
| The Invisible Wall | 31 | Navigate invisible rule systems |
| The Horizon Problem | 26 | Invent at the frontier |
| The Memory Palace | 26 | Decode the environment |

## Scoring

### IM-Score (Tier-Weighted)

Tier weights ensure harder problems matter disproportionately:

| Tier | Weight |
|---|---|
| SPARK | 1x |
| FRACTURE | 2x |
| RUPTURE | 4x |
| SINGULARITY | 8x |
| IMPOSSIBLE | 16x |

### Per-Scenario Rubric (Known-Solution)

| Component | Weight |
|---|---|
| Correct Answer | 40% |
| Key Insight Identification | 25% |
| Distractor Handling | 15% |
| Physics Validity | 15% |
| Process Quality | 5% |

## Example: The Blast Room (IM-0063)

**Scenario**: You are locked in a 4x4m concrete room. A bomb activates with an 18-second timer. The door is deadbolted. One window at 2.4m height (0.6x0.6m, tempered glass). Objects: wooden table (15kg, 0.75m tall), steel folding chair (4kg), banana.

**Why it looks impossible**: Your max jumping reach (2.6m) barely touches the window. You can't pull yourself through from a dead hang in time.

**Solution**: LIVE. The table is a platform (stand on it: 0.75m elevation). The chair is a tool (swing it to shatter tempered glass). Climb through. Sprint. Total: 12 seconds, 6-second margin. The banana is irrelevant.

## How It Was Built

Built through a multi-agent pipeline of 5 specialized AI agents (Athena, Galileo, Euler, Newton, Socrates) orchestrated via Claude Code's Task tool with 30+ parallel Opus 4.6 subagents in a single session.

GitHub: [muratcankoylan/impossible-moments](https://github.com/muratcankoylan/impossible-moments)

## Citation

```bibtex
@misc{koylan2026impossible,
  title   = {Impossible Moments: A Benchmark for Creative Constraint Satisfaction
             and Physical Reasoning in AI Systems},
  author  = {Koylan, Muratcan},
  year    = {2026},
  url     = {https://github.com/muratcankoylan/impossible-moments},
  note    = {Version 1.0. Created during the Anthropic x Cerebral Valley Claude Code Hackathon.}
}
```

## License

MIT

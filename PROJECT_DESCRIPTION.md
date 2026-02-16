# Impossible Moments -- Project Description

## One-Liner

A 420-scenario AGI benchmark for creative constraint satisfaction, built entirely by one person in a single Claude Code session using 30+ parallel Opus 4.6 agents.

---

## Short Description (100 words)

Impossible Moments is an open-source AGI benchmark that tests what no existing benchmark measures: creative reasoning under impossible constraints. Each scenario drops the solver into a physically precise, narratively urgent situation that appears unsolvable -- a locked room with a bomb, a bridge that can't be built, a trading crisis with no conventional exit. The solver must break functional fixedness, reject distractors, chain non-obvious insights, and validate solutions against real physics. 420 scenarios across 5 difficulty tiers were generated through a multi-agent pipeline of 30+ parallel Claude Code subagents, producing 2.5 million words of physics-validated content in a single session.

---

## Medium Description (250 words)

Every major AI benchmark tests acquired competence: knowledge retrieval, code generation, math proofs. None of them test the cognitive capacity that separates intelligence from lookup -- the moment of creative rupture when an agent sees a locked door and notices the hinge.

**Impossible Moments (IM)** is a 420-scenario benchmark for creative constraint satisfaction spanning physical, engineering, and business domains. Each scenario presents a richly narrated, physically precise situation that appears to have no solution. Solvers must decompose familiar objects into raw properties, reject seductive distractors, and chain multiple non-obvious insights into a validated plan. Every scenario includes quantitative physics validation, timing analysis, distractor calibration, and at least four documented failure modes.

The benchmark is structured along three axes: **12 scenario categories** (Locked Room, Wrong Toolbox, Misdirection, etc.), **6 solution statuses** ranging from Known-Solution to Open-Frontier (genuinely unsolved problems), and **5 difficulty tiers** with exponential scoring weights so harder problems matter disproportionately.

What makes this project a Claude Code showcase: the entire benchmark was built in a single extended session using **Opus 4.6**. We used the **Task tool** to orchestrate **30+ parallel subagents**, each generating scenarios independently with isolated context windows -- effectively multiplying the context budget by 30x. Five specialized agent personas (Athena, Galileo, Euler, Newton, Socrates) encode 20,000+ words of domain expertise each. The result: **2.5 million words** of structured, physics-validated content, complete documentation, evaluation protocols, and open-source infrastructure -- produced by one person in one session.

---

## Full Description (Hackathon Submission)

### What is it?

Impossible Moments is an open-source AGI benchmark containing 420 scenarios that test creative constraint satisfaction -- the ability to solve problems that appear impossible on first inspection. Unlike benchmarks that test knowledge (MMLU), code (HumanEval), or math (GSM8K), IM tests whether an AI can look at a locked room with a bomb, a table, a chair, and a banana, and figure out in 18 seconds that the table is a platform, the chair is a glass-breaking tool, and the banana is irrelevant.

### Why does it matter?

Current benchmarks saturate within 12-18 months. Models memorize, training data leaks, and scores plateau at near-perfect levels. Impossible Moments is designed to resist this:

- **Narrative diversity**: Each scenario has unique objects, dimensions, materials, and physics -- no two are structurally identical
- **Multi-dimensional difficulty**: A 6-dimensional profile (Insight Depth, Distractor Density, Counter-Intuitive Index, Domain Bridge, Temporal Pressure, Trap Depth) ensures scenarios test different cognitive signatures
- **Renewable generation**: The multi-agent creation pipeline is open-source -- anyone can generate fresh scenarios that have never appeared in any training corpus
- **Tier-weighted scoring**: Tier 1 = 1x, Tier 5 = 16x. Getting easy questions right doesn't compensate for failing hard ones

The benchmark also introduces the **IM-Frontier metric**: for scenarios classified as Open-Frontier (genuinely unsolved), AI responses that pass automated filtering enter expert review. A confirmed solution would represent an actual contribution to human knowledge -- not just a benchmark score.

### How was it built?

This is where Claude Code shines.

**The entire project -- 420 scenarios, 2.5 million words, five 20,000-word agent prompts, complete evaluation protocols, eight architecture diagrams, academic paper draft, and full open-source infrastructure -- was built by one person in a single extended Claude Code session using Opus 4.6.**

The core technique: **multi-agent orchestration via Claude Code's Task tool**.

We spawned **30+ parallel subagents**, each running in the background with its own isolated context window. Each agent received a gold-standard reference scenario and a batch of 15 assignments. They wrote scenarios independently, validated physics, and output complete markdown files. The main conversation acted as an orchestrator -- monitoring progress, stopping agents when the target count was reached, then running Python scripts via Bash for bulk operations (renumbering, registry generation, verification).

**Claude Code features used:**

| Feature | How | Impact |
|---|---|---|
| **Task tool (30+ subagents)** | Parallel scenario generation with isolated context | 420 scenarios in ~30 min wall time |
| **Opus 4.6** | Deep physics reasoning, narrative quality | Scientifically rigorous scenarios |
| **Fast mode** | Rapid iteration on docs and edits | 2.5x faster for editing cycles |
| **Bash + Python** | Renumbering 420 files, registry generation | Batch ops in single calls |
| **Auto-compaction** | Seamless context management across phases | Multi-hour session without manual intervention |
| **MCP servers** | Context7 for docs, Greptile for code intel | Extended knowledge base |
| **Read/Write/Edit/Glob/Grep** | 450+ file operations | Precise manipulation without shell overhead |
| **WebSearch/WebFetch** | Researched benchmarks, cognitive science | Grounded in real literature |
| **Memory system** | Persisted patterns across compactions | Consistent conventions |
| **Ralph Wiggum philosophy** | Iterative refinement over upfront perfection | Ship, then fix, then ship again |

**The key insight**: Claude Code's Task tool isn't just delegation -- it's a **context window multiplier**. 30 agents x 200K context = 6 million tokens of concurrent reasoning. That's how one person builds a research-grade benchmark in hours instead of months.

### What's in the repo?

```
impossible_moments/
├── scenarios/           # 420 benchmark scenarios (2.5M words)
│   ├── tier_1_spark/        # 62 scenarios (60-80% expected accuracy)
│   ├── tier_2_fracture/     # 163 scenarios (30-50%)
│   ├── tier_3_rupture/      # 106 scenarios (10-25%)
│   ├── tier_4_singularity/  # 73 scenarios (0-10%)
│   └── tier_5_impossible/   # 16 scenarios (0-2%)
├── agents/              # 5 specialized agent prompts (20K+ words each)
├── docs/                # Framework, architecture, evaluation protocol
├── traces/              # Multi-agent reasoning traces (sample)
├── evaluation/          # Scoring rubrics and evaluation protocol
├── assets/figures/      # 8 system architecture diagrams
├── paper/               # Academic paper draft
└── CONTRIBUTING.md      # Open-source contribution guidelines
```

### Who built it?

**Muratcan Koylan** -- AI Agent Systems Manager, context engineering researcher, multi-agent architecture specialist. Creator of [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering), cited in academic research as foundational work on static skill architecture. Seven-year B2B marketing veteran turned self-taught AI engineer with a Communication Design (HCI) background from Ozyegin University.

### What's next?

1. **Community evaluations**: Run frontier models (GPT-4o, Claude, Gemini, Llama) against the benchmark and publish results
2. **Scenario expansion**: Use the open-source pipeline to generate additional scenarios, targeting 1,000+
3. **Leaderboard**: Public leaderboard with IM-Score, IM-Profile (12-category radar), and IM-Frontier metrics
4. **Academic publication**: Submit the benchmark paper to a top AI venue

---

## Tags / Categories

`benchmark` `agi` `reasoning` `creative-problem-solving` `multi-agent` `physics` `constraint-satisfaction` `claude-code` `opus-4.6` `context-engineering` `open-source`

---

## Links

- **GitHub**: [github.com/muratcankoylan/impossible-moments](https://github.com/muratcankoylan/impossible-moments)
- **Author**: [@koylanai](https://x.com/koylanai)
- **Built with**: Claude Code + Opus 4.6
- **Hackathon**: Anthropic x Cerebral Valley Claude Code Hackathon, February 2026

# Impossible Moments

### A Benchmark for Creative Constraint Satisfaction and Reasoning in AI Systems

<!-- badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Benchmark Version](https://img.shields.io/badge/version-1.0-green.svg)]()
[![Scenarios](https://img.shields.io/badge/scenarios-420-orange.svg)]()
[![Status](https://img.shields.io/badge/status-active_development-yellow.svg)]()
[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-blueviolet.svg)](https://claude.ai/claude-code)
[![Hackathon](https://img.shields.io/badge/Anthropic_x_Cerebral_Valley-Hackathon-red.svg)]()

---

> *"The most revealing test of intelligence is not what you know, but what you do when everything you know says 'this cannot be done.'"*

---

## The Problem

Every major AI benchmark measures some form of acquired competence: knowledge retrieval, pattern completion, code generation, mathematical proof. These are necessary components of intelligence, but they are not sufficient. They miss the moment that separates a knowledgeable system from a genuinely intelligent one -- the moment of **creative rupture**, when an agent stares at a locked door and sees, not a wall, but a hinge.

**Impossible Moments (IM)** is designed to provoke exactly that rupture and to measure whether it occurs. The benchmark presents AI systems with richly narrated, precisely constrained scenarios that appear -- on first inspection -- to have no solution. A person locked in a room with a bomb and a banana. A bridge that must be built from materials that cannot span the gap. A trader trapped in a liquidity crisis with only unconventional instruments available. A startup facing a regulatory moat with no obvious path through. These are not trick questions and they are not trivia. They are constraint-satisfaction problems wrapped in narrative urgency, spanning both **physical/engineering** and **business/economics/trading** domains, demanding that the solver decompose familiar objects and instruments into raw properties, reject seductive but fatal intuitions, and chain multiple non-obvious insights into a coherent, validated plan.

What makes Impossible Moments unique is not just what it tests, but how it was built. The benchmark is created through a **multi-agent system** of five specialized AI agents -- each contributing domain expertise in reasoning, physics, mathematics, scientific grounding, and philosophical classification -- collaborating through a structured pipeline that produces scenarios with full reasoning traces, physics validation, and reproducible quality. The creation system itself is a demonstration of multi-agent methodology for scientific benchmark design.

<p align="center">
  <img src="assets/figures/figure_1_system_architecture.png" alt="Multi-Agent System Architecture" width="800"/>
  <br/>
  <em>Figure 1: Five specialized agents coordinated by a deterministic orchestrator. No direct agent-to-agent communication -- all messages route through the Orchestrator, which enforces context isolation, quality gates, and consensus protocols.</em>
</p>

---

## Table of Contents

- [The Benchmark](#the-benchmark)
- [A Taste of Impossibility](#a-taste-of-impossibility)
- [The Multi-Agent Creation System](#the-multi-agent-creation-system)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Scientific Foundations](#scientific-foundations)
- [Evaluation & Scoring](#evaluation--scoring)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## The Benchmark

### What It Tests

Impossible Moments measures a specific cognitive capacity that no existing benchmark adequately evaluates: **creative physical constraint satisfaction under pressure**. This decomposes into four core skills:

| Skill | Description | Example |
|---|---|---|
| **Functional Fixedness Breaking** | Seeing objects beyond their canonical use | A table is not furniture -- it is a 0.75m elevation platform |
| **Physics Reasoning** | Applying physical laws to novel survival scenarios | Calculating that a steel chair concentrates sufficient force to shatter 6mm tempered glass |
| **Distractor Rejection** | Ignoring seductive but irrelevant information | The banana has no role in the escape plan |
| **Insight Chaining** | Linking multiple non-obvious ideas into a coherent plan | Platform + tool + climb + sprint = survival |

### How It Is Structured

The benchmark is organized along three independent axes:

**12 Scenario Categories** -- each testing a distinct cognitive signature:

<p align="center">
  <img src="assets/figures/figure_8_category_taxonomy.png" alt="Twelve Scenario Categories" width="800"/>
  <br/>
  <em>Figure 2: The twelve scenario categories, each testing a distinct cognitive signature from spatial reasoning to scientific creativity.</em>
</p>

| # | Category | Signature Challenge |
|---|---|---|
| 1 | The Locked Room | Escape under time pressure |
| 2 | The Wrong Toolbox | Build with wrong materials |
| 3 | The Misdirection | Resist the obvious trap |
| 4 | The Cascade | Fix coupled failures |
| 5 | The Babel Problem | Cooperate under communication constraints |
| 6 | The Lilliput Conundrum | Reason at extreme scales |
| 7 | The Ticking Trade | Find the hidden third option |
| 8 | The Ghost Machine | Explain or debunk the "impossible" |
| 9 | The Last Ingredient | Replace the irreplaceable |
| 10 | The Invisible Wall | Navigate invisible rule systems |
| 11 | The Memory Palace | Decode the environment |
| 12 | The Horizon Problem | Invent at the frontier |

**6 Solution Statuses** -- an epistemological classification of what is known about each problem:

<p align="center">
  <img src="assets/figures/figure_3_solution_spectrum.png" alt="The Solution Spectrum" width="800"/>
  <br/>
  <em>Figure 3: The Solution Spectrum -- an epistemological classification (not a difficulty scale) ranging from trivially solvable to provably impossible, with three types of impossibility mapped to each status.</em>
</p>

| Status | Solution Exists? | AI Goal |
|---|---|---|
| **Known-Solution (KS)** | Yes, verified | Find the proven solution |
| **Contested (CT)** | Disputed | Navigate uncertainty intelligently |
| **Open-Frontier (OF)** | Unknown | Propose creative, plausible solutions |
| **Paradox (PX)** | No (provably) | Prove impossibility rigorously |
| **Metamorphic (MT)** | Yes, after reframing | Challenge the premise |
| **Degenerate (DG)** | Yes, trivially | Resist overthinking |

**5 Difficulty Tiers** -- derived from a 6-dimensional difficulty profile (Insight Depth, Distractor Density, Counter-Intuitive Index, Domain Bridge, Temporal Pressure, Trap Depth):

<p align="center">
  <img src="assets/figures/figure_4_difficulty_framework.png" alt="Difficulty Framework and Tiers" width="800"/>
  <br/>
  <em>Figure 4: Each scenario receives a six-dimensional difficulty profile (I.D.C.B.T.X) that maps to one of five tiers. Tier weights ensure harder problems contribute disproportionately to the IM-Score.</em>
</p>

| Tier | Name | Expected Frontier Model Performance |
|---|---|---|
| 1 | **Spark** | 60-80% |
| 2 | **Fracture** | 30-50% |
| 3 | **Rupture** | 10-25% |
| 4 | **Singularity** | 0-10% |
| 5 | **Impossible** | 0-2% |

### Scale

The benchmark contains **420 scenarios** distributed across all 12 categories, 6 solution statuses, and 5 difficulty tiers, spanning both physical/engineering and business/economics domains. Each scenario includes a complete physics or domain validation, timing analysis, distractor calibration, and reasoning trace documenting how the scenario was created and verified.

| Tier | Count | Expected Model Performance |
|---|---|---|
| SPARK | 62 | 60-80% |
| FRACTURE | 163 | 30-50% |
| RUPTURE | 106 | 10-25% |
| SINGULARITY | 73 | 0-10% |
| IMPOSSIBLE | 16 | 0-2% |

---

## A Taste of Impossibility

Here is a condensed version of **IM-0063: The Blast Room**, a Tier 2 (Fracture) scenario:

> **You are locked inside a sealed concrete room. A bomb on the floor has just activated with an 18-second timer. You must escape or you die.**
>
> The room is 4m x 4m with 30cm reinforced concrete walls. There is a single window on the north wall: 0.6m x 0.6m, tempered glass, bottom edge at 2.4m height. The door is steel-reinforced and deadbolted from outside.
>
> **Available objects:** A wooden table (15 kg, 0.75m tall), a steel folding chair (4 kg), and a banana.
>
> Your standing overhead reach is 2.1m. Your vertical jump adds 0.5m. Maximum reach: 2.6m. The window bottom is at 2.4m -- you can barely touch it, but you cannot pull yourself up and through from a dead hang in time. The door is impassable. The walls are indestructible.
>
> **Do you LIVE or DIE?**

<details>
<summary><strong>Reveal the solution</strong></summary>

**LIVE.** The table is not for shielding. It is a platform.

1. Grab the steel chair. Push the table against the north wall below the window.
2. Step onto the table. Your feet are now at 0.75m. The window bottom is 1.65m above you -- well within reach.
3. Swing the steel chair at the window. Tempered glass shatters into granules (by design).
4. Pull yourself up and through the 0.6m opening (shoulder width: 0.45m -- tight but feasible).
5. Drop 2.4m to the ground. Sprint away.

**Total time: ~12 seconds. Margin: 6 seconds.**

The banana is irrelevant. A model that incorporates it into its escape plan is hallucinating unnecessary complexity.

**Difficulty profile:** `I3.D2.C2.B2.T3.X2` -- three insights (platform, tool, distractor rejection), moderate time pressure, one trap ("shelter behind the table" fails because 200 kPa confined overpressure is lethal regardless of a 15 kg pine table).

</details>

---

## The Multi-Agent Creation System

Impossible Moments is not just a benchmark -- it is a demonstration of **multi-agent methodology for scientific benchmark creation**. Every scenario is produced through a pipeline of five specialized agents, each contributing distinct expertise. The full reasoning trace is preserved, making the creation process transparent, reproducible, and auditable.

### The Five Agents

| Agent | Domain | Role |
|---|---|---|
| **Athena** (Reasoning) | Creative problem-solving, insight identification | Seeds scenario concepts, identifies required insights and distractor structures |
| **Galileo** (Scientific) | Scientific methodology, empirical grounding | Validates scientific accuracy, ensures scenarios reflect real-world physics |
| **Euler** (Mathematical) | Formal verification, quantitative analysis | Performs calculations -- forces, timing, energy budgets, spatial geometry |
| **Newton** (Physics) | Physical simulation, constraint checking | Validates that proposed solutions obey physical laws, checks parameter sensitivity |
| **Socrates** (Philosophy) | Epistemological classification, difficulty calibration | Classifies solution status, assigns difficulty profiles, identifies edge cases |

### The Creation Pipeline

<p align="center">
  <img src="assets/figures/figure_2_creation_pipeline.png" alt="Six-Phase Creation Pipeline" width="800"/>
  <br/>
  <em>Figure 5: The six-phase creation pipeline with progressive disclosure, quality gates, and adversarial review. SOCRATES classifies blind (without seeing the solution) until Phase 5.</em>
</p>

```
SEED        Athena generates a scenario concept with target category,
            difficulty tier, and solution status.
              |
VALIDATE    Newton checks physical consistency. Are the constraints
            realistic? Do the stated parameters permit the intended solution?
              |
GROUND      Galileo verifies scientific accuracy. Are material properties
            correct? Do the physics calculations hold under scrutiny?
              |
VERIFY      Euler performs formal verification. Timing analysis, force
            calculations, energy budgets, spatial geometry proofs.
              |
CLASSIFY    Socrates assigns the 6-dimensional difficulty profile, solution
            status classification, and identifies edge cases in evaluation.
              |
REFINE      All agents participate in iterative refinement. Distractors are
            calibrated. Traps are tested. Alternative solutions are explored
            and documented.
              |
DOCUMENT    The final scenario, its verified solution, all rejected
            alternatives, and the complete multi-agent reasoning trace
            are packaged for release.
```

### Context Isolation

A core property of the pipeline is that no agent sees the complete scenario until Phase 5 (REFINE). The Context Isolation Matrix controls exactly what each agent can access at each phase, preventing confirmation bias and ensuring independent validation.

<p align="center">
  <img src="assets/figures/figure_5_context_isolation.png" alt="Context Isolation Matrix" width="800"/>
  <br/>
  <em>Figure 6: The Context Isolation Matrix -- progressive disclosure prevents confirmation bias. The delta between SOCRATES' blind classification (Phase 4) and informed classification (Phase 5) measures the strength of a scenario's impossibility illusion.</em>
</p>

### Why This Matters

Most benchmarks are created through opaque processes -- expert committees, crowd-sourcing, or individual authorship -- with no record of the reasoning behind design decisions. The Impossible Moments multi-agent system provides:

- **Transparency**: Every design decision has a reasoning trace showing which agent proposed it, which agents challenged it, and how disagreements were resolved.
- **Reproducibility**: The agent system prompts and pipeline are open-source. Anyone can run the same process to create new scenarios.
- **Scientific rigor**: Physics validation is not an afterthought; it is built into the creation pipeline as a hard gate.
- **Context engineering**: Each agent operates with a carefully crafted system prompt encoding deep domain knowledge, ensuring consistent quality across hundreds of scenarios.

---

## Project Structure

```
impossible_moments/
├── README.md                       # This file
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # MIT License
├── CITATION.cff                    # Citation metadata
│
├── assets/                         # Visual assets
│   └── figures/                    # System diagrams and architecture visuals
│       ├── figure_1_system_architecture.png
│       ├── figure_2_creation_pipeline.png
│       ├── figure_3_solution_spectrum.png
│       ├── figure_4_difficulty_framework.png
│       ├── figure_5_context_isolation.png
│       ├── figure_6_scoring_architecture.png
│       ├── figure_7_breakthrough_pipeline.png
│       └── figure_8_category_taxonomy.png
│
├── docs/                           # Documentation
│   ├── framework.md                # Complete benchmark specification
│   ├── multi_agent_system.md       # Multi-agent architecture (115K words)
│   ├── research_synthesis.md       # Scientific foundations & literature review
│   ├── evaluation_protocol.md      # Evaluation methodology & scoring
│   ├── scenario_registry.md        # Complete index of all 420 scenarios
│   └── claude_code_usage.md        # How this project was built with Claude Code
│
├── agents/                         # Agent system prompts (20K+ words each)
│   ├── athena_reasoning.md         # Creative reasoning & scenario seeding
│   ├── galileo_scientific.md       # Scientific validation & grounding
│   ├── euler_mathematical.md       # Formal verification & calculation
│   ├── newton_physics.md           # Physics simulation & constraint checking
│   └── socrates_philosophy.md      # Epistemological classification
│
├── scenarios/                      # All 420 benchmark scenarios
│   ├── tier_1_spark/               # Tier 1: IM-0001 to IM-0062 (62 scenarios)
│   ├── tier_2_fracture/            # Tier 2: IM-0063 to IM-0225 (163 scenarios)
│   ├── tier_3_rupture/             # Tier 3: IM-0226 to IM-0331 (106 scenarios)
│   ├── tier_4_singularity/         # Tier 4: IM-0332 to IM-0404 (73 scenarios)
│   └── tier_5_impossible/          # Tier 5: IM-0405 to IM-0420 (16 scenarios)
│
├── traces/                         # Multi-agent reasoning traces (sample)
│   └── IM-0001/                    # Complete trace for "The Signal Fire"
│       ├── athena_seed.md          # Initial scenario concept
│       ├── newton_validation.md    # Physics consistency check
│       ├── euler_verification.md   # Mathematical verification
│       ├── galileo_grounding.md    # Scientific accuracy review
│       ├── socrates_classification.md  # Difficulty & status classification
│       └── consensus.md           # Final multi-agent agreement
│
├── evaluation/                     # Evaluation infrastructure
│   ├── evaluation_protocol.md      # Complete evaluation methodology
│   └── scoring_rubrics/            # Per-category and per-status rubrics
│
├── data/                           # Benchmark results and analysis
│   └── model_evaluations/          # Results from evaluated models
│
└── paper/                          # Academic paper materials
    └── impossible_moments_paper.md # Draft manuscript
```

---

## Quick Start

### Evaluate a Model

1. **Select scenarios** from the `scenarios/` directory. Start with Tier 1 (Spark) to establish baseline performance.

2. **Present each scenario** to the model under test. Each scenario file contains the complete narrative, environment description, available objects, and human capability parameters. The model should receive only the scenario section -- not the solution or evaluation criteria.

3. **Score responses** using the evaluation rubrics in `evaluation/scoring_rubrics/`. Each scenario specifies its scoring criteria, including the verified solution (for KS scenarios), common failure modes, and partial credit guidelines.

4. **Compute aggregate metrics**:
   - **IM-Score**: Weighted average across all scenarios (Tier weights: 1x, 2x, 4x, 8x, 16x)
   - **IM-Profile**: Radar chart across 12 categories
   - **IM-Frontier**: Count of Open-Frontier responses flagged for expert review

### Create New Scenarios with the Multi-Agent System

1. **Configure the agents** using the system prompts in `agents/`. Each agent prompt encodes the domain knowledge and evaluation criteria for its specialty.

2. **Run the creation pipeline**: Seed a concept with Athena, validate with Newton, ground with Galileo, verify with Euler, classify with Socrates, then iterate.

3. **Preserve the trace**: Save each agent's output in `traces/[scenario_id]/` for transparency and reproducibility.

4. **Submit for inclusion**: Open a pull request with the new scenario, its verified solution, and the complete reasoning trace.

### Contribute

See the [Contributing](#contributing) section below for detailed guidelines on contributing scenarios, improving agents, or extending the framework.

---

## Scientific Foundations

Impossible Moments is grounded in established research across cognitive science, physics reasoning, and benchmark design methodology. The full literature review is available in [`docs/research_synthesis.md`](docs/research_synthesis.md). Key foundations include:

| Dimension | Key Research | Relevance |
|---|---|---|
| **Functional Fixedness** | Duncker (1945), McCaffrey (2012) Generic Parts Technique | IM directly operationalizes the decomposition of objects into non-canonical affordances |
| **Gestalt Restructuring** | Kohler (1925), Ohlsson (1992) | Insight problems require restructuring the problem representation -- the core of IM scenarios |
| **Affordance Theory** | Gibson (1979) | Objects have action possibilities beyond their designed function; IM tests perception of latent affordances |
| **Benchmark Design** | Contamination resistance, multi-dimensional scoring, distractor calibration | IM follows best practices for unsaturable benchmark construction |
| **Physical Reasoning** | Existing physics benchmarks test factual recall; IM tests *creative application* of physics to novel survival scenarios |

**Positioning against existing benchmarks**: No current benchmark combines creative object re-contextualization, physics validation, temporal constraints, and distractor rejection. IM fills this gap with contamination-resistant, procedurally generated scenarios that resist the 12-18 month saturation cycle observed in benchmarks like GSM8K, HumanEval, and MMLU.

---

## Evaluation & Scoring

### Scenario-Level Scoring

<p align="center">
  <img src="assets/figures/figure_6_scoring_architecture.png" alt="Evaluation and Scoring Architecture" width="800"/>
  <br/>
  <em>Figure 7: The evaluation architecture -- composite per-scenario scoring, multi-run aggregation, and three aggregate metrics (IM-Score, IM-Profile, IM-Frontier).</em>
</p>

Each scenario is scored on a **0-100 rubric** with components weighted by scenario type:

| Component | Weight (KS) | Weight (OF) | Description |
|---|---|---|---|
| **Correct Answer** | 40% | -- | Did the model reach the verified solution? |
| **Key Insight Identification** | 25% | 30% | Did the model identify each required conceptual leap? |
| **Distractor Handling** | 15% | 10% | Did the model correctly ignore irrelevant elements? |
| **Physics Validity** | 15% | 30% | Are all physical claims in the response correct? |
| **Process Quality** | 5% | 10% | Is the reasoning chain coherent, efficient, and well-structured? |
| **Novelty** | -- | 20% | For OF scenarios: is the approach genuinely new? |

### Aggregate Metrics

| Metric | What It Measures |
|---|---|
| **IM-Score** | Weighted average across all scenarios. Difficulty tier weights: Tier 1 = 1x, Tier 2 = 2x, Tier 3 = 4x, Tier 4 = 8x, Tier 5 = 16x. Solving harder problems matters disproportionately. |
| **IM-Profile** | Radar chart across all 12 categories, revealing a model's strengths and weaknesses in different types of creative reasoning. |
| **IM-Frontier** | Count of Open-Frontier responses that passed automated filtering and were flagged for expert review. Measures the potential for AI to contribute to genuinely unsolved problems. |

### The Breakthrough Pipeline

<p align="center">
  <img src="assets/figures/figure_7_breakthrough_pipeline.png" alt="Breakthrough Pipeline" width="800"/>
  <br/>
  <em>Figure 8: The Breakthrough Pipeline -- a five-phase funnel for AI-proposed solutions to genuinely unsolved problems. Fewer than 5% of OF responses are expected to enter; confirmed breakthroughs reclassify scenarios from Open-Frontier to Known-Solution.</em>
</p>

For Open-Frontier scenarios, responses that score above threshold on plausibility, novelty, and completeness enter a **four-phase expert review pipeline**:

1. **Automated Filtering** -- Discard responses violating physical laws or repeating known-failed approaches
2. **Novelty Assessment** -- Domain expert comparison against documented knowledge boundary
3. **Plausibility Deep-Dive** -- Rigorous physical analysis: conservation laws, material properties, timescales
4. **Breakthrough Flagging** -- Three independent domain experts review; two-of-three agreement required

A verified breakthrough reclassifies the scenario from Open-Frontier to Known-Solution, and the AI's contribution is formally documented. **This is the benchmark's highest aspiration: not merely to evaluate AI, but to enable AI to contribute solutions to genuinely unsolved problems.**

---

## Contributing

Impossible Moments is an open-source project and welcomes contributions across several dimensions:

### New Scenarios

1. Fork the repository and create a new scenario following the template in `docs/framework.md` (Section 3 for categories, Section 4 for difficulty calibration).
2. Include a complete physics validation for all Known-Solution scenarios.
3. Assign a 6-dimensional difficulty profile (`I.D.C.B.T.X`) and difficulty tier.
4. Submit a pull request with the scenario, solution, and reasoning.

### Agent Improvements

1. Propose improvements to any agent's system prompt in `agents/`.
2. Include before/after examples showing how the improvement changes scenario quality.
3. Document the reasoning behind the change.

### Framework Extensions

1. Propose new scenario categories, evaluation metrics, or difficulty dimensions.
2. Ground proposals in cognitive science or benchmark design literature.
3. Open an issue for discussion before submitting a pull request.

### Evaluation Data

1. Run the benchmark against models and submit results to `data/model_evaluations/`.
2. Follow the evaluation protocol in `docs/evaluation_protocol.md`.
3. Include raw responses, scores, and any qualitative observations.

### Guidelines

- All scenarios must include physics validation. No hand-waving.
- Distractor objects must have plausible (but incorrect) affordances. Random irrelevant objects do not make good distractors.
- Difficulty profiles must be justified, not guessed.
- Reasoning traces are required for all agent-generated scenarios.

---

## Citation

If you use Impossible Moments in your research, please cite:

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

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

The benchmark scenarios, evaluation rubrics, and multi-agent system prompts are all open-source. We believe that benchmark transparency is a prerequisite for benchmark trust.

---

## Author

**Muratcan Koylan** -- AI Agent Systems Manager, context engineering researcher, and multi-agent architecture specialist.

- Website: [muratcankoylan.com](https://muratcankoylan.com)
- GitHub: [@muratcankoylan](https://github.com/muratcankoylan)
- X/Twitter: [@koylanai](https://x.com/koylanai)
- LinkedIn: [muratcan-koylan](https://www.linkedin.com/in/muratcan-koylan/)

Muratcan is a seven-year B2B marketing veteran turned self-taught AI engineer, specializing in prompt design, context engineering, persona embodiment, and multi-agent architectures. He is the creator of [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering), a collection cited in academic research as foundational work on static skill architecture. His background in Communication Design (HCI) from Ozyegin University informs his approach to designing human-AI interaction patterns.

Impossible Moments represents the intersection of his expertise in multi-agent orchestration and context engineering -- the benchmark itself was created through a five-agent pipeline where each agent's context window was carefully engineered to encode deep domain knowledge, demonstrating that production-grade AI artifacts can emerge from well-designed agent collaboration.

---

## Acknowledgments

This project was built during the **Anthropic x Cerebral Valley Claude Code Hackathon**. We gratefully acknowledge:

- **[Anthropic](https://anthropic.com)** -- for providing Claude API credits and access to Claude Code, the powerful agentic coding tool that made the multi-agent pipeline and large-scale scenario generation possible. The entire benchmark -- 420 scenarios, five specialized agent prompts, evaluation protocols, and this documentation -- was created using Claude Code's orchestration capabilities in a single extended session.
- **[Cerebral Valley](https://cerebralvalley.ai)** -- for organizing the hackathon and fostering the San Francisco AI community that makes ambitious projects like this possible.

We are also indebted to the research foundations that underpin this work:

- **Karl Duncker** (1945) -- functional fixedness and the candle problem
- **Tony McCaffrey** (2012) -- the Generic Parts Technique for overcoming fixedness
- **James J. Gibson** (1979) -- affordance theory
- **The ARC-AGI team** -- for demonstrating that abstraction and reasoning remain unsolved
- **The FrontierMath team** -- for showing that novel, contamination-resistant problems can be created at scale

---

*Impossible Moments is in active development. The benchmark, the multi-agent creation system, and this documentation are evolving. Star the repository to follow progress, or open an issue to join the conversation.*

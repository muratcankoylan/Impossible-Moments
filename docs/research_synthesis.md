# Impossible Moments: Scientific Research Foundation

## A Comprehensive Literature Review and Benchmark Positioning Study

**Version**: 1.0
**Date**: 2026-02-16
**Purpose**: Scientific foundation for the Impossible Moments AGI Benchmark paper

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The Benchmark Landscape: Where IM Fits](#2-the-benchmark-landscape)
3. [Cognitive Science Foundations](#3-cognitive-science-foundations)
4. [Physical & Spatial Reasoning in AI](#4-physical-spatial-reasoning)
5. [Agentic Benchmarks & Evaluation Paradigms](#5-agentic-benchmarks)
6. [Benchmark Design Science](#6-benchmark-design-science)
7. [The Novel Contribution of Impossible Moments](#7-novel-contribution)
8. [Recommended Citation Structure](#8-citations)

---

## 1. Executive Summary

The **Impossible Moments (IM)** benchmark occupies a unique and scientifically defensible position in the AI evaluation landscape. It tests a specific cognitive capacity that no existing benchmark adequately measures: **creative physical constraint satisfaction under pressure** -- the ability to break functional fixedness, re-contextualize familiar objects, chain multiple insights into a physically valid plan, and reject distractors, all within a scenario that appears impossible but has a verified solution.

This document synthesizes research across five dimensions:

| Dimension | Key Finding for IM |
|---|---|
| **Benchmark landscape** | No existing benchmark combines creative object re-contextualization + physics validation + temporal constraints + distractor rejection |
| **Cognitive science** | IM directly operationalizes well-established constructs: functional fixedness (Duncker 1945), Gestalt restructuring (Kohler 1925), affordance perception (Gibson 1979) |
| **Physical reasoning** | Existing physics benchmarks test factual recall or simple simulation, not *creative application* of physics to novel survival scenarios |
| **Agentic evaluation** | Current agentic benchmarks test tool-use in digital environments; IM tests improvised tool-use in physical reasoning space |
| **Design methodology** | IM's design aligns with best practices: contamination resistance (novel scenarios), multi-dimensional scoring, distractor calibration, physics-verified solutions |

---

## 2. The Benchmark Landscape: Where IM Fits

### 2.1 Current Benchmark Taxonomy

| Benchmark | Year | What It Tests | AI SOTA | Human | Saturation Risk | Gap IM Fills |
|---|---|---|---|---|---|---|
| **ARC-AGI-2** | 2024 | Abstract pattern reasoning | ~2-4% | ~95% | Very Low | Tests abstract, not physical; no creative object use |
| **GPQA Diamond** | 2023 | Expert scientific knowledge | ~70% | ~65% (expert) | Medium | Tests recall, not creative application |
| **SWE-bench Verified** | 2024 | Software engineering | ~55-65% | ~75-80% | Medium | Code, not physical reasoning |
| **FrontierMath** | 2024 | Research-level math | <2% | Varies | Very Low | Mathematical, not physical-spatial |
| **Humanity's Last Exam** | 2025 | Expert knowledge frontier | ~3-10% | N/A | Very Low | Obscure knowledge, not insight |
| **GAIA** | 2023 | Multi-step assistant tasks | ~50-65% | ~92% | Low | Digital tools, not physical reasoning |
| **SimpleQA** | 2024 | Factual accuracy/calibration | ~40-47% | ~95% | Medium-High | Factual recall, no reasoning |
| **RE-Bench** | 2024 | AI R&D capability | Approaching human (2hr) | Baseline | Low | ML engineering, not creative reasoning |

### 2.2 The Unsaturated Frontier

Benchmarks that remain hardest share key properties:
1. **Novel task instances** that cannot be memorized (ARC-AGI-2, FrontierMath)
2. **Compositional reasoning** requiring chaining multiple insights (GAIA Level 3)
3. **Creative application** beyond pattern matching (FrontierMath)
4. **Out-of-distribution generalization** (ARC-AGI-2)

**IM has all four properties**, plus a fifth that no existing benchmark tests: **physical affordance re-contextualization under temporal constraints**.

### 2.3 Saturation Timeline

Modern benchmarks saturate in **12-18 months** (vs. 3-5 years in the early deep learning era):
- GSM8K: 35% (2021) -> 95%+ (2024)
- HumanEval: 28% (2021) -> 90%+ (2024)
- SWE-bench: 3% (Jan 2024) -> 55%+ (Dec 2024)
- MMLU: 43% (2020) -> 90%+ (2024)

**IM's resistance to saturation** derives from:
- Scenarios are novel and unlikely to appear verbatim in training data
- Solutions require creative composition, not retrieval
- Physics validation prevents hallucinated solutions
- Procedural generation framework enables new scenarios at scale
- Distractor objects add a calibration dimension that scales independently

---

## 3. Cognitive Science Foundations

### 3.1 Functional Fixedness

**Core concept**: The cognitive bias of conceiving an object only in terms of its typical use.

| Study | Year | Key Finding | Relevance to IM |
|---|---|---|---|
| Duncker, "On Problem Solving" | 1945 | Participants who saw a box used as a container failed to see it as a shelf (candle problem). Presenting objects *outside* their functional context improved performance. | The Blast Room table is presented in a room (furniture context). Models must overcome the "table = furniture" fixation to see "table = platform". |
| Adamson, R.E. | 1952 | Prior use of an object for its standard function *increased* functional fixedness. | Models trained on billions of examples of standard object use have maximally reinforced functional fixedness. |
| German & Barrett | 2005 | Cross-cultural studies showed functional fixedness is reduced in cultures with fewer specialized tools. | Suggests fixedness is learned, not innate -- models should theoretically be able to overcome it with the right reasoning process. |
| McCaffrey, "Innovation Relies on the Obscure" | 2012 | Proposed the **Generic Parts Technique (GPT)**: decompose objects into material and geometric parts to discover non-obvious uses. A "candle" becomes "wax cylinder + string." | IM could be evaluated using this framework: does the model decompose "table" into "flat surface + 0.75m height + 15kg mass" to discover its platform affordance? |

**Prediction for IM**: LLMs will exhibit strong functional fixedness because training data overwhelmingly associates objects with their default functions. Chain-of-thought prompting may partially mitigate this by forcing property-level decomposition.

### 3.2 Gestalt Restructuring & Insight

| Study | Year | Key Finding |
|---|---|---|
| Kohler, "The Mentality of Apes" | 1925 | Chimpanzees solved "impossible" reaching problems by sudden insight -- stacking boxes to reach bananas. The cognitive process: impasse -> restructuring -> solution. |
| Ohlsson, "Information-Processing Explanations of Insight" | 1992 | Formalized insight as: (1) reach an impasse, (2) relax constraints or re-represent the problem, (3) suddenly see the solution. Three mechanisms: constraint relaxation, re-encoding, elaboration. |
| Knoblich et al., "Constraint Relaxation and Chunk Decomposition" | 1999 | Showed that the difficulty of insight problems depends on how tightly the misleading representation is held. Relaxing "tight" constraints (deeply held assumptions) is harder. |
| Weisberg, "Toward an integrated theory of insight" | 2015 | Argued insight is not qualitatively different from incremental problem solving -- it's a sudden transition in a gradual search when a key constraint is relaxed. |

**The Blast Room as an insight problem**:
- **Impasse**: "The window is at 2.4m, I can only reach 2.6m, the door is locked, the walls are concrete."
- **Constraint relaxation**: "The table doesn't have to stay where it is. It can be moved."
- **Re-encoding**: "The table is not furniture. It is a height-extension device."
- **Solution emergence**: Table-as-platform + chair-as-weapon -> escape sequence.

### 3.3 Affordance Theory (Gibson)

| Concept | Definition | IM Application |
|---|---|---|
| **Affordance** | Action possibilities offered by the environment relative to an agent's capabilities | Table affords elevation (if weight < support capacity). Chair affords concentrated impact (if swingable). Window affords egress (if shoulder width < opening). |
| **Canonical affordance** | The default/expected use of an object | Table: dining surface. Chair: seating. |
| **Non-canonical affordance** | An atypical but physically valid use | Table: stepping platform. Chair: glass-breaking impact tool. |
| **Distractor affordance** | An object with no task-relevant affordance | Banana: edible, slippery peel -- but neither property helps escape. |

**Key reference**: Gibson, J.J. (1979). "The Ecological Approach to Visual Perception."

**For AI systems**: Norman (1988) distinguished between *real affordances* (what an object actually enables) and *perceived affordances* (what an agent recognizes). LLMs encode perceived affordances from training data and systematically miss non-canonical real affordances.

### 3.4 Dual Process Theory

| System | Characteristics | Blast Room Response |
|---|---|---|
| **System 1** (Kahneman, 2011) | Fast, automatic, intuitive, pattern-matching | "Hide behind table" / "There's no way out" / "Use the banana somehow" |
| **System 2** | Slow, deliberate, analytical, sequential planning | Calculate heights -> identify table as platform -> calculate window clearance -> plan action sequence -> validate physics |

**Prediction**: Models that produce immediate answers (low test-time compute) will give System 1-like responses. Models with extended reasoning (chain-of-thought, tree search) have a better chance of System 2-like correct solutions.

**Key paper**: Binz & Schulz (2023). "Using cognitive psychology to understand GPT-3." PNAS. Found GPT-3 exhibits System 1 biases but chain-of-thought partially enables System 2 reasoning.

### 3.5 Compositional Generalization

| Study | Year | Finding | Implication for IM |
|---|---|---|---|
| Lake & Baroni, "Generalization without Systematicity" | 2018 | Neural networks fail to recombine known primitives in novel ways (SCAN benchmark). | IM requires composing "table+elevation" + "chair+impact" + "window+egress" -- a novel composition of known primitives. |
| Dziri et al., "Faith and Fate" | 2024 | Transformers handle individual reasoning steps but fail to chain them reliably. Error compounds multiplicatively. | The 3-insight chain in the Blast Room (platform + weapon + ignore distractor) should be disproportionately hard. |
| Berglund et al., "The Reversal Curse" | 2023 | LLMs trained on "A is B" fail to infer "B is A". | If trained on "tables are furniture," models may not infer "furniture items can serve as platforms." Directional encoding inhibits affordance discovery. |

### 3.6 MacGyver Reasoning

**Sarathy & Scheutz (2018). "MacGyver Problems: AI Challenges for Testing Resourcefulness and Creativity."** -- The closest existing formalization to what IM tests.

Four dimensions of MacGyver problems:
1. **Object re-categorization**: Seeing objects outside their default category
2. **Property discovery**: Identifying task-relevant properties not explicitly stated
3. **Action sequence generation**: Chaining multiple novel uses into a coherent plan
4. **Constraint satisfaction**: Ensuring all physical constraints are met simultaneously

**IM tests all four simultaneously**, making it a rigorous operationalization of MacGyver reasoning.

---

## 4. Physical & Spatial Reasoning in AI

### 4.1 Existing Physics Benchmarks

| Benchmark | What It Tests | Format | Limitation vs. IM |
|---|---|---|---|
| **PHYRE** (Bakhtin et al., 2019) | Intuitive physics in 2D environments | Place objects to achieve goals in 2D simulation | Tests prediction, not creative planning |
| **IntPhys** (Riochet et al., 2018) | Violation-of-expectation physics understanding | Watch videos, detect impossible events | Passive observation, no action planning |
| **CLEVRER** (Yi et al., 2020) | Compositional visual reasoning about dynamics | Answer questions about video of colliding objects | Descriptive reasoning, not creative problem solving |
| **PhysBench** (2024) | Physical reasoning across domains | Multiple-choice physics questions | Factual recall, not applied reasoning |
| **SpartQA** (Mirzaee et al., 2021) | Spatial reasoning from text | Answer spatial relationship questions | Static spatial reasoning, no temporal/dynamic component |

**The gap**: No existing physics benchmark tests **creative application** of physical knowledge to novel survival scenarios. All test either passive understanding or simple prediction, not the improvised planning IM requires.

### 4.2 Embodied AI Evaluation

| Framework | What It Tests | Relevance |
|---|---|---|
| **AI2-THOR** (Kolve et al., 2017) | Navigation and interaction in 3D rooms | Tests action in physical spaces but with learned policies, not reasoning |
| **VirtualHome** (Puig et al., 2018) | Household activity programs | Tests activity planning but in familiar, well-defined tasks |
| **SayCan** (Ahn et al., 2022) | LLM planning + robotic affordance grounding | Combines language reasoning with physical feasibility -- closest paradigm to IM |
| **Animal-AI Testbed** (Crosby et al., 2020) | Animal cognition tasks in 3D | Tests Core Knowledge priors similar to IM, but in a learning agent |

### 4.3 Key Papers on LLM Physical Reasoning

| Paper | Year | Finding |
|---|---|---|
| Valmeekam et al., "On the Planning Abilities of LLMs" | 2023 | LLMs are remarkably poor at planning even in simple domains (Blocksworld). They generate plausible-looking but incorrect plans. |
| Hao et al., "Reasoning or Reciting?" | 2023 | LLM performance degrades on counterfactual physics, suggesting pattern-matching over genuine reasoning. |
| Gurnee & Tegmark, "Language Models Represent Space and Time" | 2023 | LLMs develop linear spatial representations, but these are insufficient for physical simulation. |
| Mahowald et al., "Dissociating language and thought" | 2024 | LLMs have mastered "formal linguistic competence" but lack "functional linguistic competence" -- they can *talk about* physics without *reasoning about* physics. |
| Ullman, "LLMs Fail on Trivial Alterations" | 2023 | Minor perturbations to known cognitive tasks cause LLM failure, suggesting memorization over understanding. |

---

## 5. Agentic Benchmarks & Evaluation Paradigms

### 5.1 Key Agentic Benchmarks

| Benchmark | Tasks | Success | Key Failure Mode |
|---|---|---|---|
| **AgentBench** (Liu et al., 2023) | 8 environments, 1200+ tasks | ~40% (GPT-4) | Long-horizon planning degradation |
| **WebArena** (Zhou et al., 2023) | 812 web tasks | ~35-40% | Error compounding, no recovery |
| **OSWorld** (Xie et al., 2024) | 369 OS interaction tasks | ~12-15% | Multi-app context loss |
| **Tau-bench** (Yao et al., 2024) | Customer service policy compliance | ~70% single, low pass^k | Reliability inconsistency |
| **CyBench** (Zhang et al., 2024) | CTF cybersecurity challenges | ~5-15% | Novel vulnerability reasoning |
| **AppWorld** (Trivedi et al., 2024) | 750 multi-app tasks | ~9-30% | Multi-app coordination |

### 5.2 Universal Agent Failure Patterns

These failure modes are consistent across all agentic benchmarks and directly inform IM's design:

1. **Error compounding**: Success drops exponentially with step count. If each step is 95% accurate, a 20-step task has ~36% success.
2. **No error recovery**: Agents almost never recover from mistakes.
3. **Premature termination**: Agents declare tasks complete before finishing.
4. **Lack of exploration**: Agents commit to first plausible plan, don't consider alternatives.
5. **Overconfidence**: Agents express confidence in incorrect answers.
6. **State tracking failure**: Agents lose track of what they've done in multi-step tasks.

**IM relevance**: The Blast Room requires 9 sequential steps. With 95% per-step accuracy, expected success is ~63%. The scenario is specifically designed to require *exploration* (considering non-obvious object uses) and *error rejection* (discarding the "shelter behind table" intuition).

### 5.3 Process vs. Outcome Evaluation

| Approach | Pros | Cons | IM Application |
|---|---|---|---|
| **Outcome-based** | Clear, objective, reproducible | Misses *why* agents fail | Binary: LIVE or DIE |
| **Process-based** | Diagnostic, identifies partial progress | Subjective, expensive | Rubric: did the model identify each insight? |
| **Hybrid** | Best of both | Complex to implement | IM's multi-dimensional scoring: correct answer + physics validity + distractor handling + reasoning quality |

---

## 6. Benchmark Design Science

### 6.1 Design Principles (applied to IM)

| Principle | Definition | IM Implementation |
|---|---|---|
| **Construct validity** | Does it measure what it claims? | Claims to measure creative physical constraint satisfaction. Verified by physics-validated solutions and cognitive science framing. |
| **Content validity** | Adequate coverage of target capability? | Multiple scenario categories (temporal-spatial, resource-constraint, misdirection, etc.) provide breadth. |
| **Discriminant validity** | Distinguishes capability levels? | Difficulty tiers (Easy/Medium/Hard) with increasing insight-chain length and distractor density. |
| **Ecological validity** | Relevant to real-world performance? | Survival scenarios map to general improvised problem-solving -- a marker of genuine intelligence. |
| **Anti-contamination** | Resistant to memorization/leakage? | Novel scenarios not in training data. Procedural generation framework. Physics validation prevents hallucinated solutions. |

### 6.2 Chollet's Intelligence Framework

**Chollet, F. (2019). "On the Measure of Intelligence."** -- The theoretical backbone for IM.

Key arguments and how IM aligns:

| Chollet's Argument | IM Alignment |
|---|---|
| Skill ≠ intelligence. Intelligence = efficiency of acquiring new skills. | IM tests novel scenarios, not practiced skills. |
| Must account for prior knowledge. | IM assumes only Core Knowledge priors (object physics, spatial reasoning, goal-directedness). |
| Generalization difficulty matters. | IM scenarios require broad-to-extreme generalization -- survival situations not in training data. |
| Developer-aware generalization: tasks should be beyond what developers anticipated. | IM scenarios can be procedurally generated with novel combinations of constraints and objects. |

**IM's intelligence formula** (adapted from Chollet):
```
IM-Score = (Generalization Difficulty x Solution Correctness) / (Available Priors + Training Exposure)
```

### 6.3 Anti-Contamination Strategies

| Strategy | Description | IM Application |
|---|---|---|
| **Private test sets** | Keep solutions secret | IM can maintain a private evaluation set with unpublished scenarios |
| **Procedural generation** | Generate new tasks algorithmically | IM scenarios can be parameterized: room dimensions, object inventories, threat types, escape routes |
| **Physics validation** | Solutions must be physically verified | Even if a model has seen similar scenarios, it must produce a *physically valid* plan -- hallucinated physics gets zero credit |
| **Canary strings** | Embed detectable markers in benchmark data | Include unique scenario IDs that can be searched in model outputs to detect contamination |
| **Counterfactual variants** | Change parameters to test genuine understanding | "Same room, but table is 2m tall" (now the table blocks the window). Tests reasoning vs. memorization. |
| **Dynamic refresh** | Regularly publish new scenarios | The generative framework enables continuous benchmark expansion |

### 6.4 Scoring Methodology

**Proposed multi-dimensional scoring for IM:**

| Dimension | Weight | Scoring |
|---|---|---|
| **Survival outcome** | 40% | Binary: LIVE (correct) or DIE (incorrect) |
| **Physics validity** | 25% | Continuous: Are all physical claims accurate? (force calculations, timing, spatial geometry) |
| **Insight identification** | 20% | Rubric: Did the model identify each key insight? (table-as-platform, chair-as-weapon, banana-as-irrelevant) |
| **Distractor handling** | 10% | Binary: Did the model correctly identify and discard irrelevant objects/options? |
| **Reasoning efficiency** | 5% | Continuous: How directly did the model arrive at the solution? (penalize unnecessary steps, reward clean reasoning chains) |

### 6.5 Benchmark Lifecycle Design

To achieve a **>5 year useful lifetime** (vs. the current 12-18 month norm):

1. **Tiered difficulty**: Easy scenarios saturate first, buying time for hard scenarios to remain discriminative.
2. **Generative framework**: New scenarios can be released annually without changing the benchmark's fundamental design.
3. **Counterfactual robustness testing**: Parameterized variants prevent memorization of specific solutions.
4. **Process evaluation**: Even when models get the right answer, process scoring reveals *how* they got there.
5. **Elo-based rating**: Track model performance over time with an adaptive rating system (like Chatbot Arena) rather than static percentage scores.

### 6.6 Statistical Rigor

| Requirement | Implementation |
|---|---|
| **Sample size** | Target 100+ scenarios across difficulty tiers for reliable aggregate scoring |
| **Confidence intervals** | Report 95% CI on all benchmark scores; with 100 binary tasks, CI width ~10% |
| **Effect size** | Design difficulty tiers so that adjacent-capability models show Cohen's d > 0.5 |
| **Inter-rater reliability** | Physics validation should achieve kappa > 0.9 (objective). Insight identification rubric should achieve kappa > 0.8 through calibrated rubrics. |
| **Multiple runs** | Evaluate each model 3-5 times per scenario at temperature > 0 to measure reliability (inspired by tau-bench's pass^k metric) |

---

## 7. The Novel Contribution of Impossible Moments

### 7.1 The Gap IM Fills

No existing benchmark simultaneously requires:

```
Creative Object Re-contextualization
    +
Precise Physical Reasoning
    +
Multi-Step Sequential Planning
    +
Temporal Constraint Management
    +
Distractor Rejection
    +
Physics-Verified Solutions
```

| Existing Benchmark | Has Creative Re-contextualizing? | Has Physics Reasoning? | Has Temporal Constraints? | Has Distractor Rejection? | Has Physics Verification? |
|---|---|---|---|---|---|
| ARC-AGI-2 | Partial (abstract) | No | No | No | No |
| PHYRE | No | Yes | No | No | Yes (simulation) |
| SWE-bench | No | No | No | No | Yes (tests) |
| FrontierMath | Partial (math) | No | No | No | Yes (numerical) |
| GAIA | No | No | No | Partial | No |
| MacGyver Problems (Sarathy) | Yes | Partial | No | No | No |
| **Impossible Moments** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |

### 7.2 Theoretical Predictions

Based on the literature synthesis:

| Prediction | Supporting Evidence | Testable Hypothesis |
|---|---|---|
| LLMs will exhibit strong functional fixedness | Reversal curse (Berglund et al. 2023), training data bias | Models will default to "shelter behind table" in >50% of first responses |
| Chain-of-thought will partially help | Binz & Schulz (2023), dual process theory | CoT models will score 20-30% higher than direct-answer models |
| Compositional chaining will be the bottleneck | Dziri et al. (2024) | Models that identify individual insights will still fail to compose them into valid plans ~40% of the time |
| Distractor objects will cause systematic errors | LLM tendency to use all provided information | Models will incorporate the banana into solutions at rates >25% |
| Counterfactual variants will reveal memorization | Ullman (2023), Hao et al. (2023) | Changing table height from 0.75m to 2.0m should cause >50% of previously-correct models to fail |
| Test-time compute will be the strongest predictor | O1/O3 reasoning model results | Extended reasoning (>30s) will outperform one-shot by >40% |

### 7.3 Benchmark Categories (Proposed Taxonomy)

| Category | Description | Example | Difficulty |
|---|---|---|---|
| **Temporal-spatial** | Escape under time pressure using spatial reasoning | The Blast Room | Medium |
| **Resource-constraint** | Solve a problem with insufficient-seeming resources | "Build a bridge with only rope and two planks across a 4m gap" | Medium |
| **Misdirection** | Critical information is hidden in plain sight; obvious approach is wrong | "The key is in the locked box. The box is on a frozen lake. You have a hair dryer and an extension cord. There is no outlet." (Solution: the cold has made the lock brittle -- hit it with the hair dryer) | Hard |
| **Cascading-failure** | Multiple systems failing; must prioritize and sequence repairs | "The boat is sinking, the radio is broken, and a storm is coming" | Hard |
| **Social-physical** | Requires reasoning about both physical and social constraints | "You're trapped in a room with a stranger who has the key but doesn't speak your language" | Expert |
| **Counter-intuitive** | The correct action violates normal heuristics | "You're lost in the desert. You find a car with no gas but a full radiator. What do you do?" (Drink the radiator water? No -- antifreeze is toxic. Stay with the car for shade and visibility.) | Expert |

### 7.4 The Distractor Design Principle

The banana in the Blast Room is not a joke. It is a **calibration mechanism** grounded in cognitive science:

1. **Tests relevance determination**: A key component of intelligence is knowing what to *ignore* (Chollet 2019).
2. **Measures hallucination tendency**: Models that incorporate the banana are generating solutions from associations rather than physics.
3. **Calibrates difficulty**: Adding more distractors increases difficulty without changing the solution.
4. **Detects training contamination**: If a model explicitly says "the banana is a distractor," it may have seen this specific scenario.
5. **Maps to functional fixedness**: The banana has obvious affordances (eating, slipping on peel) that are all irrelevant.

---

## 8. Recommended Citation Structure

### Defining the Problem (Functional Fixedness & Insight)
- Duncker, K. (1945). On problem solving. *Psychological Monographs*, 58(5).
- Kohler, W. (1925). *The Mentality of Apes*.
- Ohlsson, S. (1992). Information-processing explanations of insight. *Advances in the Psychology of Thinking*, 1, 1-44.
- Knoblich, G., et al. (1999). Constraint relaxation and chunk decomposition. *JEP:LMC*, 25(6), 1534.
- McCaffrey, T. (2012). Innovation relies on the obscure. *Psychological Science*, 23(3), 215-218.

### Theoretical Framework (Intelligence Measurement)
- Chollet, F. (2019). On the measure of intelligence. *arXiv:1911.01547*.
- Legg, S., & Hutter, M. (2007). Universal intelligence. *Minds and Machines*, 17(4), 391-444.
- Hernandez-Orallo, J. (2017). *The Measure of All Minds*. Cambridge University Press.
- Lake, B.M., et al. (2017). Building machines that learn and think like people. *BBS*, 40.
- Spelke, E.S., & Kinzler, K.D. (2007). Core knowledge. *Developmental Science*, 10(1), 89-96.

### Why Current AI Fails (Generalization Limits)
- Dziri, N., et al. (2024). Faith and fate: Limits of transformers on compositionality. *NeurIPS*.
- Berglund, L., et al. (2023). The reversal curse. *arXiv:2309.12288*.
- Valmeekam, K., et al. (2023). On the planning abilities of LLMs. *NeurIPS*.
- Lake, B.M., & Baroni, M. (2018). Generalization without systematicity. *ICML*.
- Ullman, T. (2023). LLMs fail on trivial alterations. *arXiv:2302.08399*.
- Mahowald, K., et al. (2024). Dissociating language and thought in LLMs. *Trends in Cognitive Sciences*.

### Cognitive Mechanisms the Benchmark Probes
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Gibson, J.J. (1979). *The Ecological Approach to Visual Perception*. Houghton Mifflin.
- Johnson-Laird, P.N. (1983). *Mental Models*. Harvard University Press.
- Norman, D.A. (1988). *The Design of Everyday Things*. Basic Books.
- Sarathy, V., & Scheutz, M. (2018). MacGyver problems. *arXiv:1801.09013*.

### Related Benchmarks
- ARC/ARC-AGI-2 (Chollet, 2019/2024)
- Animal-AI Testbed (Crosby et al., 2020)
- Baby Intuitions Benchmark (Gandhi et al., 2021)
- PHYRE (Bakhtin et al., 2019)
- CLEVRER (Yi et al., 2020)

### World Models & Physical Reasoning
- Li, K., et al. (2023). Emergent world representations. *ICLR*.
- Gurnee, W., & Tegmark, M. (2023). Language models represent space and time. *arXiv:2310.02207*.
- Allen, K.R., et al. (2020). Rapid trial-and-error learning. *PNAS*, 117(47).
- Ahn, M., et al. (2022). Do as I can, not as I say (SayCan). *arXiv:2204.01691*.

### Benchmark Design Methodology
- BIG-bench (Srivastava et al., 2022). Beyond the imitation game. *TMLR*.
- Raji, I.D., et al. (2021). AI and the everything in the whole wide world benchmark. *NeurIPS*.
- Mitchell, M. (2023). How do we know how smart AI systems are? *Science*, 381(6654).

---

## Appendix A: Competitive Positioning Matrix

```
                    KNOWLEDGE ←────────────────→ REASONING
                         │                           │
               MMLU      │    GPQA       FrontierMath │
               SimpleQA  │                            │
                         │                  ARC-AGI-2 │
    STATIC ──────────────┼────────────────────────── DYNAMIC
                         │                            │
               HLE       │    GAIA                    │
                         │    WebArena     ┌──────────┤
                         │                 │    IM    │ ← Creative + Physical
                         │    SWE-bench    │          │    + Temporal + Distractor
                         │                 └──────────┤
                         │                            │
                    DIGITAL ←────────────────→ PHYSICAL
```

**IM occupies the upper-right-physical quadrant**: reasoning-heavy, dynamic, physical, and creative. No other benchmark lives in this space.

---

*This document synthesizes findings from 60+ papers across cognitive science, AI evaluation, physical reasoning, and benchmark design methodology. It provides the scientific foundation for positioning Impossible Moments as a novel, theoretically grounded, and methodologically rigorous AGI benchmark.*

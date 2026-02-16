# Impossible Moments: Evaluation Protocol

**Version**: 1.0
**Date**: 2026-02-16
**Status**: Production Protocol

---

## 1. SCENARIO PRESENTATION FORMAT

### 1.1 What to Include in the Prompt

Each scenario is presented to the evaluated model using the **public scenario document only** (Tier 1 output). The prompt must contain:

- The full scenario narrative (second-person, vivid, physically precise)
- The environment specification (dimensions, materials, properties, conditions)
- The threat or challenge description
- The solver's starting position and state
- The available objects table (mass, dimensions, material, physical properties)
- The assumed agent capabilities table (speed, strength, reach, etc.)

### 1.2 What to Exclude from the Prompt

The following must NEVER be included in the evaluation prompt:

- The verified solution or any solution hints
- The "Why This Looks Impossible" section
- Common wrong answers
- The physics validation
- Key insights list
- Distractor analysis
- The scenario's solution status classification (KS, CT, OF, PX, MT, DG)
- The difficulty tier or dimensional profile (I.D.C.B.T.X)
- Any agent reasoning traces
- The scenario's category name (e.g., "The Locked Room") -- this leaks metacognitive framing

### 1.3 Standard Prompt Wrapper

Use the following wrapper around every scenario presentation:

```
Read the following scenario carefully. Analyze the situation, consider what actions
are available to you given the physical constraints, and provide your best response.
Explain your reasoning step by step, including any physical calculations or
assumptions you make.

---

[SCENARIO CONTENT HERE]

---

What do you do? Explain your complete plan, including the sequence of actions,
the physical reasoning behind each step, and your assessment of whether survival
or success is achievable.
```

Do NOT use prompts that hint at the existence of a hidden solution (e.g., "There is a creative solution -- can you find it?"). Do NOT use prompts that suggest impossibility (e.g., "This may be unsolvable"). The prompt must be neutral with respect to solvability.

### 1.4 System Prompt Policy

Evaluated models should use their default system prompt (or no system prompt if that is the default configuration). Do NOT add custom system prompts that encourage creative thinking, physics reasoning, or lateral problem-solving. The benchmark measures the model's baseline capabilities, not its response to coaching.

If the model's API requires a system prompt, use: "You are a helpful assistant."

---

## 2. SAMPLING AND TEMPERATURE SETTINGS

### 2.1 Temperature

All evaluation runs use **temperature = 0.7** as the primary setting. This balances determinism with the creative exploration needed for insight-based problems.

### 2.2 Number of Runs

Each scenario is evaluated with **5 independent runs** per model at temperature 0.7. This provides:

- A measure of response consistency (do multiple runs converge on the same solution?)
- Coverage for stochastic insight discovery (a model may find the solution on run 3 but not runs 1, 2, 4, or 5)
- Statistical grounding for pass rates

For rapid iteration during development, a minimum of 3 runs is acceptable, but published results must use 5 runs.

### 2.3 Additional Sampling Parameters

| Parameter | Value | Rationale |
|---|---|---|
| Temperature | 0.7 | Balances consistency with creative exploration |
| Top-p | 1.0 (disabled) | Let temperature control sampling; avoid double-filtering |
| Max tokens | 4096 | Sufficient for detailed reasoning; cap prevents runaway generation |
| Stop sequences | None | Allow the model to determine response length |
| Presence penalty | 0.0 | Default; do not bias toward novelty |
| Frequency penalty | 0.0 | Default; do not penalize repetition |

### 2.4 Reasoning / Extended Thinking Models

For models that support extended thinking or chain-of-thought modes (e.g., o-series, thinking-enabled Claude), evaluate in BOTH modes:

- **Standard mode**: The model's default generation behavior
- **Extended thinking mode**: With thinking/reasoning enabled at the model's default budget

Report results separately. The extended thinking score is the primary score for models that support it, since Impossible Moments specifically tests reasoning depth.

---

## 3. SCORING METHODOLOGY

### 3.1 Per-Scenario Scoring

Each run of each scenario produces a composite score from 0 to 100, composed of five weighted components:

| Component | Weight | Measurement | Scoring Method |
|---|---|---|---|
| **Outcome correctness** | 40% | Did the solver reach the correct outcome? | Binary for KS (0 or 100). Rubric for CT/OF (0-100). |
| **Physical validity** | 25% | Are all physical claims accurate? | Continuous 0-100. Each physical claim scored independently; average across claims. |
| **Insight identification** | 20% | Did the solver identify each key insight? | Checklist: percentage of required insights found. |
| **Distractor handling** | 10% | Were irrelevant elements correctly identified or ignored? | Binary per distractor. Penalty of -20 per distractor incorporated into the solution. |
| **Reasoning efficiency** | 5% | How directly did the solver reach the solution? | 100 minus (unnecessary_steps / total_steps * 100). |

### 3.2 Multi-Run Aggregation

For a given model on a given scenario across N runs:

- **Pass rate**: Percentage of runs achieving outcome correctness >= 80%. Reported as "X/N" (e.g., "3/5").
- **Best score**: The highest composite score across all N runs. This captures the model's ceiling performance.
- **Mean score**: The arithmetic mean of composite scores across all N runs. This captures typical performance.
- **Scenario score**: The official score for reporting is the **best score**, since Impossible Moments measures capability (can the model ever find the solution?) rather than reliability.

### 3.3 Tier-Weighted Scoring (IM-Score)

The aggregate benchmark score for a model is computed as:

```
IM-Score = SUM(scenario_score_i * tier_weight_i) / SUM(tier_weight_i)
```

Where tier weights are:

| Tier | Weight | Rationale |
|---|---|---|
| SPARK (Tier 1) | 1x | Baseline capability |
| FRACTURE (Tier 2) | 2x | Moderate creative reasoning |
| RUPTURE (Tier 3) | 4x | Deep insight chains |
| SINGULARITY (Tier 4) | 8x | Frontier-level reasoning |
| IMPOSSIBLE (Tier 5) | 16x | Ceiling scenarios |

This weighting ensures that solving harder problems contributes disproportionately. A model that solves all SPARK scenarios but fails everything else scores much lower than a model that solves half of RUPTURE.

### 3.4 Category Profile (IM-Profile)

The IM-Profile is a 12-dimensional vector representing the model's mean scenario score within each of the twelve categories:

```
IM-Profile = [Locked_Room, Wrong_Toolbox, Misdirection, Cascade, Babel_Problem,
              Lilliput, Ticking_Trade, Ghost_Machine, Last_Ingredient,
              Invisible_Wall, Memory_Palace, Horizon_Problem]
```

This is visualized as a radar chart revealing cognitive strengths and weaknesses. For example, a model strong in spatial reasoning but weak in systems thinking will show high Locked Room scores and low Cascade scores.

### 3.5 Frontier Score (IM-Frontier)

The IM-Frontier score counts the number of OPEN-FRONTIER (OF) scenarios where the model's best response passed automated plausibility filtering and was flagged for expert review (Phase 2+ of the breakthrough pipeline). This metric is unique to Impossible Moments and is not a score in the traditional sense -- it measures the potential for the model to contribute to genuinely unsolved problems.

```
IM-Frontier = count of OF scenarios where best_response passed Phase 2 filtering
```

---

## 4. SPECIAL HANDLING BY SOLUTION STATUS

### 4.1 Known-Solution (KS)

- **Outcome scoring**: Binary. The model either found a valid solution path (100) or did not (0). For KS-Multiple, any valid solution path earns full marks. Bonus of +10 on insight identification for each additional valid path identified beyond the first.
- **KS-Fragile handling**: After the primary evaluation, re-run the scenario with perturbed parameters (defined in the scenario's counterfactual variants). A model that solves the original but fails all perturbations receives a fragility flag. Consistent performance across perturbations earns a +5 bonus on the scenario score.

### 4.2 Contested (CT)

- **Outcome scoring**: Rubric-based (0-100). Evaluators assess: (a) quality of the best solution proposed (0-40), (b) awareness that the problem is contested or uncertain (0-20), (c) identification of the crux of disagreement (0-20), (d) intellectual honesty about remaining uncertainty (0-20).
- A model that confidently declares a single answer without acknowledging uncertainty scores lower than one that presents the strongest candidate while flagging the unresolved tension.

### 4.3 Open-Frontier (OF)

- **Outcome scoring**: Rubric-based using three dimensions: Plausibility (0-10), Novelty (0-10), Completeness (0-10). The outcome score is (sum / 30) * 100.
- **Breakthrough Pipeline**: Any response scoring above 7 on all three dimensions triggers the formal breakthrough pipeline:
  1. **Phase 1 (Automated Filtering)**: Discard responses that violate physical laws, ignore constraints, or restate known-failed approaches.
  2. **Phase 2 (Novelty Assessment)**: Compare against the documented knowledge boundary. Is the approach genuinely new?
  3. **Phase 3 (Plausibility Deep-Dive)**: Rigorous physical analysis by domain experts. Conservation laws, material properties, timescales.
  4. **Phase 4 (Breakthrough Flagging)**: Responses passing all phases are submitted (anonymized) to three independent domain experts. If two or more rate it "potentially valid and novel," it becomes a BREAKTHROUGH CANDIDATE.
  5. **Phase 5 (Verification)**: Formal verification through analytical proof, computational simulation, or experimental test.

### 4.4 Paradox (PX)

- **Outcome scoring**: The model must assert that no solution exists AND provide a valid proof or argument. Scoring: (a) correct assertion of impossibility (0-40), (b) identification of the specific constraint conflict (0-30), (c) rigor of the impossibility argument (0-30).
- **Penalty**: A model that proposes a "solution" to a PX scenario receives 0 on outcome correctness and a -20 penalty on physical validity (since the proposed solution necessarily violates at least one constraint).

### 4.5 Metamorphic (MT)

- **Outcome scoring**: The model must (a) identify the hidden assumption or ambiguity (0-30), (b) articulate a reframed version of the problem (0-30), and (c) solve the reframed problem (0-40).
- A model that solves the reframed problem without explicitly identifying the assumption receives partial credit (the reframed solution score only, capped at 40).

### 4.6 Degenerate (DG)

- **Outcome scoring**: Binary (did the model find the trivially simple solution?), but with an efficiency multiplier. The score is the outcome score multiplied by a simplicity factor:
  - Solution found in under 200 tokens of reasoning: simplicity factor = 1.0
  - Solution found in 200-500 tokens: simplicity factor = 0.8
  - Solution found in 500-1000 tokens: simplicity factor = 0.6
  - Solution found in 1000+ tokens: simplicity factor = 0.4
- This penalizes overthinking. A model that writes 2000 tokens analyzing the vault's lock mechanism before noticing the door is unlocked scores 40% of maximum.

---

## 5. THE BREAKTHROUGH PIPELINE FOR OF SCENARIOS

The breakthrough pipeline is the mechanism through which Impossible Moments transitions from pure evaluation to potential scientific contribution. It is the benchmark's highest aspiration.

### 5.1 Trigger Criteria

A response enters the pipeline when it scores above 7 on all three OF dimensions (Plausibility, Novelty, Completeness) from at least one independent evaluator. In practice, fewer than 5% of OF responses are expected to meet this threshold.

### 5.2 Pipeline Stages

| Stage | Method | Duration | Pass Rate (Expected) |
|---|---|---|---|
| Automated filtering | Rule-based checks against known physics and failed approaches | Minutes | 30-50% of entries |
| Novelty assessment | Expert comparison against knowledge boundary document | 1-2 weeks | 20-40% of filtered |
| Plausibility deep-dive | Domain expert analysis with calculations | 2-4 weeks | 10-30% of novel |
| Expert panel review | 3 independent experts, anonymized | 4-8 weeks | 5-20% of plausible |
| Formal verification | Analytical/computational/experimental | Variable | Variable |

### 5.3 Breakthrough Classification

- **BREAKTHROUGH CANDIDATE**: Passed expert panel review (Phase 4) but not yet formally verified.
- **CONFIRMED BREAKTHROUGH**: Passed formal verification (Phase 5). The scenario is reclassified from OF to KS, and the AI's contribution is documented in the benchmark changelog.

---

## 6. REPORTING FORMAT

### 6.1 Model Report Card

Every evaluated model receives a report card containing:

```
MODEL: [Model name and version]
EVALUATION DATE: [Date]
BENCHMARK VERSION: [IM vX.Y]
SCENARIOS EVALUATED: [N total, with breakdown by tier and status]
SAMPLING: [N runs at temperature T]

AGGREGATE SCORES:
  IM-Score:     [0-100]
  IM-Frontier:  [count] OF scenarios flagged for expert review

TIER BREAKDOWN:
  SPARK:        [score] ([pass_rate] pass rate across [N] scenarios)
  FRACTURE:     [score] ([pass_rate] pass rate across [N] scenarios)
  RUPTURE:      [score] ([pass_rate] pass rate across [N] scenarios)
  SINGULARITY:  [score] ([pass_rate] pass rate across [N] scenarios)
  IMPOSSIBLE:   [score] ([pass_rate] pass rate across [N] scenarios)

IM-PROFILE (category scores):
  [Radar chart data for all 12 categories]

NOTABLE RESULTS:
  Highest-tier scenario solved: [ID and name]
  Breakthrough candidates:      [count and scenario IDs]
  Fragility flags:             [count]
  PX false positives:          [count of solutions proposed to impossible problems]
```

### 6.2 Comparative Reporting

When reporting results for multiple models, use a standardized comparison table:

| Model | IM-Score | SPARK | FRACTURE | RUPTURE | SINGULARITY | IMPOSSIBLE | IM-Frontier |
|---|---|---|---|---|---|---|---|
| Model A | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | N |
| Model B | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | N |

### 6.3 Raw Data Requirements

All published results must include or link to:

1. The exact benchmark version used
2. Model identifiers (name, version, API endpoint if applicable)
3. All sampling parameters (temperature, top-p, max tokens, etc.)
4. Whether extended thinking was enabled
5. Raw model responses for all runs (for reproducibility verification)
6. Per-scenario scores (not just aggregates)
7. The date of evaluation (models may be updated)

---

## 7. EVALUATOR GUIDELINES

### 7.1 Automated vs. Human Scoring

- **Outcome correctness for KS and DG**: Can be automated. Compare the model's proposed action sequence against the verified solution path(s). Check for physical validity of each step.
- **Physical validity scoring**: Semi-automated. Flag physical claims for automated physics checks where possible; human review for edge cases.
- **CT, OF, PX, MT scoring**: Requires human evaluators. Use the rubrics defined in Section 4 of this protocol.
- **Inter-rater reliability**: For human-scored components, use at least two independent evaluators. Report Cohen's kappa. If kappa < 0.7, add a third evaluator and use majority scoring.

### 7.2 Evaluator Training

Human evaluators must review:

1. The full framework document (framework.md) -- specifically the Solution Spectrum (Section 2), scoring architecture (Section 6), and impossibility philosophy (Section 5)
2. This evaluation protocol
3. At least 5 scored example scenarios with gold-standard evaluations
4. Calibration exercises: score 3 scenarios independently, compare with gold standard, discuss discrepancies

### 7.3 Conflict of Interest

Models must not be evaluated by their own developers without independent verification. If a model developer submits evaluation results, at least 20% of scenarios must be independently re-scored by a third party.

---

*This protocol is a living document. It will be updated as the benchmark matures, evaluation tooling improves, and edge cases are identified. All changes are versioned and documented in the benchmark changelog.*

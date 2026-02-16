# Contributing to Impossible Moments

Thank you for your interest in contributing to Impossible Moments. This document provides guidelines and information for contributors.

---

## Ways to Contribute

### 1. New Scenarios

Create new benchmark scenarios following the established format:

1. Fork the repository and create a branch for your scenarios.
2. Follow the template format -- see any scenario in `scenarios/` for reference (e.g., `scenarios/tier_1_spark/IM-0001.md`).
3. Include a complete physics or domain validation for all Known-Solution (KS) scenarios.
4. Assign a 6-dimensional difficulty profile (`I.D.C.B.T.X`) and difficulty tier.
5. Submit a pull request with the scenario, solution, and reasoning.

**Scenario requirements:**
- All scenarios must include physics/domain validation with quantitative calculations
- Distractor objects must have plausible (but incorrect) affordances
- Difficulty profiles must be justified, not guessed
- Include at least 4 common wrong answers with explanations for why each fails
- Reasoning traces are encouraged for all contributed scenarios

### 2. Agent Improvements

Improve the multi-agent creation system:

1. Propose improvements to any agent's system prompt in `agents/`.
2. Include before/after examples showing how the improvement changes scenario quality.
3. Document the reasoning behind the change.

### 3. Framework Extensions

Extend the benchmark's theoretical foundation:

1. Propose new scenario categories, evaluation metrics, or difficulty dimensions.
2. Ground proposals in cognitive science or benchmark design literature.
3. Open an issue for discussion before submitting a pull request.

### 4. Evaluation Data

Contribute model evaluation results:

1. Run the benchmark against models following `docs/evaluation_protocol.md`.
2. Submit results to `data/model_evaluations/`.
3. Include raw responses, scores, and any qualitative observations.
4. Use 5 independent runs at temperature 0.7 for published results.

### 5. Bug Reports and Fixes

- Report physics errors, inconsistencies, or format issues via GitHub Issues.
- Include the scenario ID (e.g., IM-0042) and specific section where the error occurs.
- For physics errors, include the correct calculation.

---

## Scenario Format

Every scenario follows a consistent 15-section format:

| Section | Required | Description |
|---|---|---|
| Header | Yes | ID, title, category, tier, status, correct answer |
| Scenario Narrative | Yes | Second-person, vivid, physically precise prose |
| Environment | Yes | Dimensions, materials, properties, conditions |
| Threat/Challenge | Yes | What makes this urgent or constrained |
| Your Position | Yes | Starting state and orientation |
| Available Objects | Yes | Table with mass, dimensions, material, notes |
| Human Capabilities | Yes | Physical parameters of the solver |
| Why This Looks Impossible | Yes | Explanation of the apparent impossibility |
| Common Wrong Answers | Yes | Table of failed approaches with physics explanations |
| Verified Solution | Yes (KS) | Step-by-step with time costs and physics validation |
| Physics Validation | Yes | Quantitative calculations supporting the solution |
| Key Insights | Yes | Numbered list of conceptual breakthroughs |
| Distractor Analysis | Yes | Role of each misleading element |
| Evaluation Criteria | Yes | Scoring rubric for responses |
| Design Notes | Yes | Difficulty profile (I.D.C.B.T.X) |

---

## Difficulty Calibration

When assigning difficulty profiles, use the 6-dimensional system:

| Dimension | Code | Scale | Measures |
|---|---|---|---|
| Insight Depth | I | 1-5 | How many non-obvious leaps required |
| Distractor Density | D | 1-5 | How many seductive wrong paths exist |
| Counter-Intuitive Index | C | 1-5 | How much the solution defies common sense |
| Domain Bridge | B | 1-5 | How many knowledge domains must be connected |
| Temporal Pressure | T | 1-5 | How much time pressure affects decision quality |
| Trap Depth | X | 1-5 | How deeply buried the trap/misdirection is |

**Tier assignment** is derived from the composite difficulty score. See `docs/framework.md` Section 4 for calibration details.

---

## Code of Conduct

- Be respectful and constructive in all interactions.
- Focus feedback on the work, not the person.
- Physics disagreements should be resolved with calculations, not assertions.
- Credit prior work when building on others' scenarios or ideas.

---

## Questions?

Open an issue on GitHub or reach out to [@koylanai](https://x.com/koylanai).

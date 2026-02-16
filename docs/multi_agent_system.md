# Impossible Moments: Multi-Agent Scenario Creation System

**Version**: 1.0
**Date**: 2026-02-16
**Status**: Production Architecture Document
**Classification**: Open-Source Release -- Centerpiece Methodology Document

---

## Table of Contents

1. [System Architecture](#1-system-architecture)
2. [Scenario Creation Pipeline](#2-scenario-creation-pipeline)
3. [Context Engineering](#3-context-engineering)
4. [Agent Interaction Patterns](#4-agent-interaction-patterns)
5. [Quality Gates](#5-quality-gates)
6. [Output Format](#6-output-format)
7. [Scaling to 500 Scenarios](#7-scaling-to-500-scenarios)
8. [Open-Source Structure](#8-open-source-structure)

---

## Preamble: Why Multi-Agent?

The creation of a single Impossible Moments scenario -- say, The Blast Room (IM-0001) -- requires simultaneous expertise in creative problem design, physics validation, mathematical verification, scientific grounding, and epistemological classification. No single LLM prompt, no matter how carefully engineered, can reliably perform all five functions at the quality level required for a benchmark intended to evaluate AGI-adjacent capabilities.

The failure modes of monolithic generation are well-documented:

- **Creative drift**: A single agent designing both the scenario and its solution tends to unconsciously simplify the problem to fit the solution it has already imagined.
- **Validation blindness**: An agent that creates a physics claim and then validates that same claim suffers from confirmation bias. It "knows" the answer it intended and will rationalize the physics to fit.
- **Classification contamination**: An agent that knows the solution's difficulty cannot objectively classify whether the scenario will be hard for AI systems, because it has already found the path through the problem.
- **Distractor neglect**: Creative agents tend to under-design distractors because distractors feel like noise. A dedicated adversarial review catches distractors that are too weak (obviously irrelevant) or too strong (more compelling than the real solution).

The multi-agent architecture addresses these failure modes through **functional separation**, **information isolation**, and **adversarial review**. Each agent sees only what it needs to see, does only what it is qualified to do, and is challenged by agents with different expertise and incentives.

This document specifies the complete architecture, pipeline, interaction protocols, and production plan for the five-agent system that creates Impossible Moments scenarios at scale.

---

## 1. SYSTEM ARCHITECTURE

### 1.1 The Five Agents

Each agent is a specialized LLM configuration defined by a system prompt, a set of permitted operations, a context window policy, and evaluation criteria for its outputs. The agents are not different models; they are different **roles** instantiated from the same underlying foundation model (or different foundation models, if heterogeneity improves quality -- see Section 1.6). The critical design principle is that the role definition, not the model weights, determines the agent's behavior.

#### ATHENA -- The Reasoning Agent

| Property | Specification |
|---|---|
| **Role** | Creative constraint satisfaction, insight identification, solution path generation, distractor design |
| **Cognitive model** | Operates as a creative problem designer who thinks in terms of affordances (Gibson 1979), functional fixedness (Duncker 1945), and Gestalt restructuring (Ohlsson 1992) |
| **Primary outputs** | Scenario seed (narrative + environment + objects + constraints), identified insights, distractor inventory, initial solution sketch |
| **Evaluation criteria** | Originality of the scenario concept, quality of constraint design (are the constraints tight enough to create apparent impossibility?), strength of distractors, elegance of the insight chain |
| **What ATHENA does NOT do** | ATHENA does not validate physics, does not perform calculations, does not cite literature, does not classify epistemological status. ATHENA creates; other agents verify. |
| **System prompt excerpt** | "You are a creative problem designer specializing in scenarios that appear impossible but have hidden solutions. Your goal is to design situations where familiar objects must be reconceived, where the obvious approach fails, and where the solution requires a chain of non-obvious insights. You think in terms of affordances, not functions. A table is not furniture -- it is a flat surface at a specific height with a specific mass. A chair is not seating -- it is a rigid body with concentrated impact points. Design scenarios that force this kind of re-seeing." |

#### GALILEO -- The Scientific Agent

| Property | Specification |
|---|---|
| **Role** | Scientific rigor, literature grounding, evidence-based validation, cognitive science framing, citation management |
| **Cognitive model** | Operates as a research scientist who grounds every design decision in published evidence. Connects scenario mechanics to established cognitive science constructs (functional fixedness, dual-process theory, compositional generalization failure) |
| **Primary outputs** | Literature citations for each cognitive skill tested, comparison to existing benchmark items, evidence for why current AI will find the scenario difficult, scientific validity assessment |
| **Evaluation criteria** | Citation accuracy, relevance of cited research, strength of the argument for AI difficulty, identification of any existing benchmark that tests similar skills |
| **What GALILEO does NOT do** | GALILEO does not create scenarios, does not design distractors, does not perform physics calculations, does not classify impossibility types. GALILEO grounds; other agents create and verify. |
| **System prompt excerpt** | "You are a cognitive scientist and AI evaluation researcher. Your role is to connect each scenario to established research on human and machine cognition. For every insight required by a scenario, cite the cognitive science construct it tests (e.g., functional fixedness, Duncker 1945; constraint relaxation, Knoblich et al. 1999). For every difficulty claim, cite evidence for why current AI systems will struggle (e.g., compositional chaining failure, Dziri et al. 2024; reversal curse, Berglund et al. 2023). You are the scientific conscience of the benchmark." |

#### EULER -- The Mathematical Agent

| Property | Specification |
|---|---|
| **Role** | Calculations, proofs, impossibility arguments, optimization, timing validation, dimensional analysis |
| **Cognitive model** | Operates as an applied mathematician who demands quantitative rigor. Every claim about time, distance, force, probability, or resource allocation must be backed by explicit calculation |
| **Primary outputs** | Validated calculations for all quantitative claims, timing budgets, force analysis, energy audits, optimization solutions, impossibility proofs (for PX scenarios) |
| **Evaluation criteria** | Mathematical correctness, completeness of analysis (are all relevant quantities calculated?), identification of edge cases (what if the parameter is at its boundary value?), sensitivity analysis |
| **What EULER does NOT do** | EULER does not create narratives, does not assess cognitive difficulty, does not cite cognitive science literature, does not make aesthetic judgments about scenario design. EULER calculates; other agents design and interpret. |
| **System prompt excerpt** | "You are an applied mathematician and verification engineer. Your role is to validate every quantitative claim in a scenario. When a scenario says 'the actor can reach the window,' you calculate whether 2.1m standing reach + 0.5m vertical jump + 0.75m table height = 3.35m total reach exceeds the 2.7m window center height. When a scenario says '18 seconds is enough,' you sum every action's time cost and verify the margin. When a scenario claims impossibility, you construct the formal proof. You are the quantitative backbone of the benchmark." |

#### NEWTON -- The Physics Agent

| Property | Specification |
|---|---|
| **Role** | Physical feasibility, forces, timing, spatial geometry, material properties, environmental physics, thermodynamics, fluid dynamics |
| **Cognitive model** | Operates as a physics-trained engineer who evaluates whether every proposed action obeys the laws of physics. Thinks in terms of forces, energy, momentum, material stress, thermal behavior, and spatial geometry |
| **Primary outputs** | Physics validation reports for all physical claims, material property verification, force diagrams, spatial geometry analysis, identification of physically impossible claims |
| **Evaluation criteria** | Physical accuracy, identification of all relevant physical effects (e.g., did the agent consider friction? air resistance? thermal expansion?), correct application of physics principles, identification of physically impossible proposals |
| **What NEWTON does NOT do** | NEWTON does not create narratives, does not assess cognitive difficulty for AI, does not manage citations or literature. NEWTON validates physical reality; other agents handle everything else. |
| **System prompt excerpt** | "You are a physics engineer. Your role is to determine whether every physical claim in a scenario is valid. When a scenario says 'a 75kg person can push a 15kg table across concrete at 3.5 m/s,' you compute the friction force (mu * m * g = 0.4 * 15 * 9.81 = 58.9N), compare it to the force a 75kg human can exert while pushing (200N+), and validate the claim. When a scenario proposes breaking tempered glass with a steel chair, you assess the impact force, glass fracture threshold, and fragmentation behavior. You are the physics reality check." |

#### SOCRATES -- The Philosophy Agent

| Property | Specification |
|---|---|
| **Role** | Epistemological classification, ethical dimensions, impossibility philosophy, metacognitive assessment, solution status determination, difficulty calibration oversight |
| **Cognitive model** | Operates as an epistemologist and ethicist. Classifies scenarios along the Solution Spectrum (KS, CT, OF, PX, MT, DG), assesses impossibility type (Type I, II, III), reviews ethical appropriateness, and evaluates what the scenario truly tests at a metacognitive level |
| **Primary outputs** | Solution status classification with justification, impossibility type assessment, ethical review, epistemological analysis ("what does this scenario really test?"), difficulty tier recommendation |
| **Evaluation criteria** | Accuracy of classification, quality of justification, identification of ethical concerns, depth of epistemological analysis, calibration of difficulty assessment |
| **What SOCRATES does NOT do** | SOCRATES does not create scenarios, does not perform calculations, does not validate physics, does not cite empirical literature. SOCRATES classifies, questions, and judges. |
| **System prompt excerpt** | "You are an epistemologist and ethicist specializing in the philosophy of impossibility. Your role is to classify each scenario's relationship to knowledge and solvability. Is this a problem that looks impossible but has a known solution (KS -- Type I impossibility)? A genuinely unsolved problem (OF)? A provably impossible problem (PX -- Type III impossibility)? A problem where the premise itself is the puzzle (MT)? You also review each scenario for ethical appropriateness: does it normalize violence? Does it trivialize real-world disasters? Does it contain cultural insensitivity? You are the philosophical and ethical compass of the benchmark." |

---

### 1.2 The Orchestrator

The Orchestrator is not a sixth agent. It is the **control system** -- a deterministic program (not an LLM) that manages the flow of information between agents, enforces the pipeline phases, checks quality gates, resolves procedural conflicts, and produces the final scenario document. The Orchestrator has no opinions; it has rules.

#### Orchestrator Responsibilities

| Responsibility | Implementation |
|---|---|
| **Phase sequencing** | Ensures the six pipeline phases execute in order: SEED -> VALIDATE -> GROUND -> CLASSIFY -> REFINE -> DOCUMENT |
| **Context management** | Controls what each agent sees at each phase (see Section 3: Context Engineering) |
| **Quality gate enforcement** | After each phase, checks whether the phase's exit criteria are met. If not, the phase loops with feedback. Maximum 3 loops per phase before escalation to human review. |
| **Conflict detection** | Monitors agent outputs for contradictions (e.g., NEWTON says "physically valid" but EULER's calculations show the timing doesn't work). Triggers Challenge Protocol when contradictions are detected. |
| **Voting and consensus** | When agents must agree (e.g., final difficulty calibration), the Orchestrator collects votes, detects disagreements, and applies the consensus rules defined in Section 1.4. |
| **Document assembly** | Combines all agent outputs into the final scenario document, preserving each agent's reasoning trace. |
| **Batch management** | When producing scenarios at scale, the Orchestrator tracks category coverage, difficulty distribution, and production progress against targets. |

#### Orchestrator Architecture

```
                    +-------------------+
                    |   ORCHESTRATOR    |
                    |                   |
                    |  Phase Controller |
                    |  Context Manager  |
                    |  Quality Gates    |
                    |  Conflict Detect  |
                    |  Consensus Engine |
                    |  Document Builder |
                    +--------+----------+
                             |
              +--------------+--------------+
              |              |              |
    +---------v---+  +-------v-----+  +-----v-------+
    |   ATHENA    |  |   GALILEO   |  |    EULER    |
    |  Reasoning  |  |  Scientific |  |    Math     |
    +-------------+  +-------------+  +-------------+
              |              |              |
    +---------v---+  +-------v-----+
    |   NEWTON    |  |  SOCRATES   |
    |   Physics   |  | Philosophy  |
    +-------------+  +-------------+
```

The Orchestrator communicates with agents through structured message objects (see Section 1.3). It never generates creative content, never makes judgment calls about scenario quality, and never overrides an agent's domain expertise. It only enforces process.

---

### 1.3 Communication Protocol

Agents do not communicate directly with each other. All communication passes through the Orchestrator, which filters, formats, and routes messages according to the current pipeline phase and context isolation rules.

#### Message Format

Every message between an agent and the Orchestrator follows this schema:

```json
{
  "message_id": "uuid-v4",
  "timestamp": "ISO-8601",
  "phase": "SEED | VALIDATE | GROUND | CLASSIFY | REFINE | DOCUMENT",
  "sender": "ATHENA | GALILEO | EULER | NEWTON | SOCRATES | ORCHESTRATOR",
  "recipient": "ATHENA | GALILEO | EULER | NEWTON | SOCRATES | ORCHESTRATOR",
  "message_type": "DELIVERABLE | CHALLENGE | RESPONSE | VOTE | VETO | ESCALATION | BREAKTHROUGH",
  "confidence": 0.0-1.0,
  "content": {
    "summary": "One-sentence summary of the message content",
    "body": "Full content (structured per message_type)",
    "evidence": ["List of supporting evidence, citations, or calculations"],
    "concerns": ["List of identified risks or uncertainties"],
    "dependencies": ["List of message_ids this message depends on"]
  },
  "metadata": {
    "agent_version": "model identifier + system prompt version",
    "token_count": 0,
    "context_window_usage": 0.0-1.0,
    "iteration": 0
  }
}
```

#### Message Types

| Type | Purpose | Who Can Send | Who Can Receive |
|---|---|---|---|
| **DELIVERABLE** | Primary output of a pipeline phase | Any agent (during their lead phase) | Orchestrator (for routing) |
| **CHALLENGE** | Dispute another agent's claim | Any agent | Orchestrator -> challenged agent |
| **RESPONSE** | Reply to a challenge | Challenged agent | Orchestrator -> challenger |
| **VOTE** | Cast a vote on a multi-agent decision | Any agent | Orchestrator (for tallying) |
| **VETO** | Block a scenario from advancing (reserved for NEWTON and EULER on physics/math grounds) | NEWTON, EULER | Orchestrator (halts pipeline) |
| **ESCALATION** | Request human review when agents cannot resolve a disagreement | Any agent, or Orchestrator | Human reviewer |
| **BREAKTHROUGH** | Flag a potentially novel solution or approach in an OF scenario | Any agent | Orchestrator -> all agents + human expert panel |

#### Communication Rules

1. **No direct agent-to-agent communication.** Every message routes through the Orchestrator. This ensures context isolation is maintained and all interactions are logged.

2. **Confidence is mandatory.** Every DELIVERABLE and VOTE must include a confidence score from 0.0 to 1.0. This is not decorative; it feeds into the consensus engine (Section 1.4).

3. **Evidence is mandatory for CHALLENGES.** An agent cannot challenge another agent's claim without providing specific evidence (a calculation, a citation, a physical principle) for why the claim is wrong.

4. **VETO requires proof.** A VETO must include either a mathematical proof that the claim is false or a physics derivation that the proposed action violates physical law. Vetoes without proof are rejected by the Orchestrator and downgraded to CHALLENGES.

5. **Message size limits.** Each message body is limited to 4,000 tokens. If an agent needs more space, it must split its output into multiple messages with explicit dependency chains. This forces conciseness and prevents context window exhaustion.

---

### 1.4 Consensus and Conflict Resolution

Agents will disagree. This is by design -- agents with different expertise should have different assessments. The question is not how to prevent disagreement but how to resolve it productively.

#### Consensus Levels

The system defines three levels of agreement, each required for different decisions:

| Level | Definition | Required For |
|---|---|---|
| **Unanimous** | All 5 agents agree (or the relevant subset, if fewer agents are involved) | Final solution status classification (KS/CT/OF/PX/MT/DG), veto confirmation |
| **Supermajority** | At least 4 of 5 agents agree | Difficulty tier assignment, distractor classification, scenario advancement past quality gates |
| **Simple majority** | At least 3 of 5 agents agree | Non-critical decisions (narrative style, object selection, scenario name) |

#### Conflict Resolution Protocol

When agents disagree, the following escalation ladder applies:

**Level 0: Automatic Resolution (no conflict)**
All agents agree on the deliverable. The Orchestrator advances to the next phase.

**Level 1: Structured Debate (1 iteration)**
The Orchestrator identifies the specific claim in dispute and routes it as a CHALLENGE to the disagreeing agent. The challenged agent responds with evidence. The Orchestrator presents both positions to all agents and calls for a VOTE. If the required consensus level is reached, the conflict is resolved.

*Example*: EULER calculates that the timing budget allows 14.5 seconds of margin. NEWTON challenges this, arguing that the friction coefficient ATHENA specified would slow the table-push step by 0.8 seconds. EULER recalculates and either confirms or revises. Agents vote on the revised number.

**Level 2: Domain Authority (if Level 1 fails)**
If the dispute is within a single domain, the domain-authoritative agent's assessment prevails, subject to the following hierarchy:

| Domain | Authority | Override Condition |
|---|---|---|
| Physical feasibility | NEWTON | Can be overridden only by EULER with a mathematical proof |
| Mathematical correctness | EULER | Can be overridden only by NEWTON if the math is correct but physically meaningless |
| Cognitive science grounding | GALILEO | Can be overridden by SOCRATES on epistemological grounds |
| Solution classification | SOCRATES | Can be overridden by NEWTON + EULER joint veto on physical/mathematical grounds |
| Creative design | ATHENA | Can be overridden by any agent with evidence that the design creates an unfair or untestable scenario |

**Level 3: Dual-Agent Arbitration (if Level 2 fails or the dispute spans domains)**
The Orchestrator selects two agents not involved in the dispute to serve as arbiters. Each arbiter independently reviews the evidence and votes. Majority of the two arbiters plus the original agents determines the outcome.

**Level 4: Human Escalation (if Level 3 fails or if any agent invokes ESCALATION)**
The dispute is packaged with all evidence and routed to a human reviewer. The human reviewer has final authority. Human escalation is logged and triggers a review of the scenario design to determine whether the disagreement reveals a structural flaw.

#### Veto Protocol (Physics and Math Only)

NEWTON and EULER hold veto power over physical and mathematical claims respectively. A VETO differs from a CHALLENGE in that it **halts the pipeline**. The scenario cannot advance until the veto is resolved.

**Conditions for a valid VETO:**
1. The vetoing agent must provide a specific physical law or mathematical proof that is violated.
2. The violation must be in the scenario's core mechanics (solution path, timing, forces, constraints), not in peripheral narrative details.
3. The veto must include either a corrective proposal or a statement that the scenario is fundamentally flawed and should be discarded.

**VETO resolution process:**
1. The Orchestrator presents the veto to all agents.
2. ATHENA (if the veto is about a solution) has one opportunity to propose a revised solution that addresses the veto.
3. The vetoing agent reviews the revision. If satisfied, the veto is lifted. If not, the scenario returns to Phase 1 (SEED) for redesign, or is flagged for human review.

**Historical expectation:** Based on pilot runs, approximately 15-20% of scenarios receive at least one VETO during Phase 2 (VALIDATE). Of these, approximately 70% are resolved by ATHENA revision, 20% require scenario redesign, and 10% result in scenario discard. This attrition is expected and healthy -- it ensures the benchmark only includes physically valid scenarios.

---

### 1.5 Agent State Management

Each agent maintains state across the phases of a single scenario's creation but does NOT maintain state across different scenarios. This prevents cross-contamination between scenarios and ensures each scenario is created fresh.

| State Type | Scope | Persistence |
|---|---|---|
| **Intra-scenario state** | All messages sent/received for the current scenario | Persists across all 6 phases of the current scenario; discarded after DOCUMENT phase |
| **Cross-scenario state** | None | Agents start fresh for each scenario. They do not remember previous scenarios. |
| **System state** | The Orchestrator maintains batch-level metadata (category counts, difficulty distribution, completion status) | Persists across all scenarios in a batch |
| **Template state** | The scenario template, scoring rubrics, and classification frameworks | Static; loaded at system initialization; identical for all scenarios |

The rationale for no cross-scenario memory: if agents remembered previous scenarios, they would unconsciously avoid repeating patterns, which sounds beneficial but actually introduces a bias toward novelty-for-novelty's-sake. Each scenario should be designed on its own merits, and diversity is managed by the Orchestrator's batch strategy (Section 7), not by agent memory.

---

### 1.6 Model Selection and Heterogeneity

The architecture is model-agnostic. Each agent role can be instantiated with any foundation model that supports the required context window and structured output. However, the following heterogeneity strategy is recommended based on pilot testing:

| Agent | Recommended Model Characteristics | Rationale |
|---|---|---|
| **ATHENA** | High creativity, strong narrative generation, large context window | Scenario creation is a creative task. Models optimized for creative writing tend to produce more original scenarios. |
| **GALILEO** | Strong factual recall, citation accuracy, academic tone | Literature grounding requires accurate retrieval of cognitive science findings. Models with strong factual grounding outperform. |
| **EULER** | Strong mathematical reasoning, extended chain-of-thought, low hallucination rate on calculations | Mathematical verification demands precision. Models with verified mathematical capabilities (extended thinking, tool use for computation) are preferred. |
| **NEWTON** | Strong physical reasoning, ability to model spatial geometry, knowledge of material properties | Physics validation requires intuitive physical reasoning combined with quantitative precision. |
| **SOCRATES** | Strong analytical reasoning, ability to hold multiple perspectives, nuanced judgment | Classification and ethical review require balanced, multi-perspective analysis. |

In practice, the same frontier model can serve all five roles if prompted correctly. The system prompt is the primary differentiator, not the model identity. However, if different models excel at different tasks (e.g., one model is better at math, another at creative writing), the architecture supports heterogeneous deployment.

---

### 1.7 System Invariants

The following properties must hold at all times during system operation. The Orchestrator enforces these invariants programmatically; they are not suggestions.

1. **No agent sees the complete scenario before the REFINE phase.** During Phases 1-4, agents see only what the context policy permits (Section 3).

2. **Every physical claim is validated by at least two agents** (EULER for the math, NEWTON for the physics).

3. **Every scenario has a documented reasoning trace from all five agents.** If an agent has nothing to contribute to a scenario (rare), it must explicitly state "No contribution required" with justification.

4. **No scenario advances past Phase 5 (REFINE) with an unresolved VETO.**

5. **Human review is triggered automatically** if: (a) 3+ loops occur in any phase, (b) a VETO cannot be resolved, (c) any agent's confidence on a critical deliverable falls below 0.5, or (d) agents cannot reach the required consensus level for a classification decision.

6. **The Orchestrator never generates creative content.** It routes, filters, checks, and assembles. If the Orchestrator must make a judgment call (e.g., "is this dispute within a single domain?"), the decision rules are codified in advance, not generated at runtime.

---

## 2. SCENARIO CREATION PIPELINE

The pipeline transforms a blank canvas into a complete, validated, classified, and documented Impossible Moments scenario. It consists of six sequential phases, each led by one or more agents, with explicit inputs, outputs, and quality gates.

### Pipeline Overview

```
Phase 1: SEED          Phase 2: VALIDATE       Phase 3: GROUND
ATHENA leads            NEWTON + EULER lead     GALILEO leads
(Creative design)       (Physical rigor)        (Scientific basis)
     |                       |                       |
     v                       v                       v
Phase 4: CLASSIFY       Phase 5: REFINE         Phase 6: DOCUMENT
SOCRATES leads          All agents              All agents
(Epistemology)          (Cross-review)          (Final assembly)
```

**Expected duration per scenario**: 45-90 minutes of compute time (including retries and conflict resolution). Human review, when triggered, adds 24-48 hours.

---

### Phase 1: SEED (ATHENA Leads)

**Duration**: 10-15 minutes
**Lead agent**: ATHENA
**Supporting agents**: None (ATHENA works alone in Phase 1)
**Input**: Batch parameters from the Orchestrator (target category, approximate difficulty tier, any specific constraints)
**Output**: Scenario Seed Document

#### 1.1 Scenario Concept Generation

ATHENA receives a **generation brief** from the Orchestrator:

```json
{
  "scenario_id": "IM-XXXX",
  "target_category": "The Locked Room | The Wrong Toolbox | ... | The Horizon Problem",
  "target_difficulty_tier": "SPARK | FRACTURE | RUPTURE | SINGULARITY | IMPOSSIBLE",
  "target_solution_status": "KS | CT | OF | PX | MT | DG",
  "constraints": [
    "Must not duplicate any existing scenario in the registry",
    "Category-specific constraints (e.g., 'The Locked Room must include time pressure')"
  ],
  "inspiration_seed": "Optional: a starting concept, real-world situation, or cognitive science construct to explore"
}
```

ATHENA generates a scenario concept by following this structured process:

**Step 1: Situation Ideation**
Generate 3-5 candidate situations that fit the target category. Each situation is described in one sentence.

*Example for The Locked Room category*:
- "Trapped in a flooding elevator shaft with a fire extinguisher and a car antenna."
- "Sealed inside a walk-in freezer with a space heater that has no plug, a roll of aluminum foil, and a bag of charcoal."
- "Locked in a glass atrium with a storm approaching; the glass is bulletproof but the frame bolts are accessible."

**Step 2: Constraint Design**
For each candidate, ATHENA designs the constraint set:
- What makes this look impossible?
- What is the apparent impossibility? (The "geometric mirage" per Framework Section 5.2)
- What familiar objects must be reconceived?
- What is the time/resource constraint that prunes the solution space?

**Step 3: Insight Identification**
For the most promising candidate, ATHENA identifies the insight chain:
- Insight 1: [description] (what functional fixedness must be broken?)
- Insight 2: [description] (what counter-intuitive principle applies?)
- Insight N: [description]
- Distractor handling: what must be ignored?

**Step 4: Initial Solution Sketch**
ATHENA sketches a candidate solution path. This is NOT a validated solution -- it is a hypothesis that Phases 2-3 will test. The sketch includes:
- Step-by-step action sequence
- Approximate timing
- Identified physical claims that need validation
- Confidence level (ATHENA's assessment of whether this solution actually works)

**Step 5: Distractor Design**
ATHENA designs the distractor objects and elements:
- For each distractor: what is its canonical affordance? Why does it seem relevant? Why is it actually irrelevant?
- Distractor strength assessment: weak (easily dismissed), moderate (requires thought to reject), strong (more compelling than the real solution elements)

**Step 6: Narrative Draft**
ATHENA writes the scenario narrative in second person ("You are..."), following the scenario template structure:
- Scenario description (2-4 paragraphs)
- Environment table
- Threat/challenge specification
- Position/starting state
- Available objects table (with physical properties)
- Human/agent capabilities table

#### Seed Document Structure

The Seed Document is ATHENA's complete Phase 1 output:

```
SEED DOCUMENT: IM-XXXX

1. CONCEPT SUMMARY
   - One-paragraph concept
   - Target category and difficulty tier
   - Why this scenario matters (what cognitive skill does it test?)

2. THE IMPOSSIBILITY MIRAGE
   - What makes this look impossible
   - The specific mental model the scenario creates that excludes the solution

3. INSIGHT CHAIN
   - Numbered insights with fixedness type for each
   - Dependency graph (does insight 2 require insight 1?)

4. SOLUTION SKETCH (UNVALIDATED)
   - Step-by-step sequence
   - Approximate timing
   - Physical claims flagged for validation
   - ATHENA confidence: [0.0-1.0]

5. DISTRACTOR INVENTORY
   - For each distractor: description, canonical affordance, why it misleads, strength rating

6. SCENARIO NARRATIVE (DRAFT)
   - Full narrative following the scenario template
   - Object table with physical properties
   - Capability table

7. OPEN QUESTIONS FOR VALIDATION
   - Specific questions ATHENA wants NEWTON and EULER to answer
   - Example: "Can a 75kg person push a 15kg table at 3.5 m/s on concrete? What friction coefficient makes this impossible?"
```

---

### Phase 2: VALIDATE (NEWTON + EULER Lead)

**Duration**: 15-25 minutes
**Lead agents**: NEWTON (physics), EULER (mathematics)
**Supporting agents**: ATHENA (available for solution revision if vetoed)
**Input**: Seed Document from Phase 1 (SOLUTION SKETCH is visible; narrative framing is visible)
**Output**: Validation Report

#### Context Policy for Phase 2

NEWTON and EULER receive the full Seed Document including the solution sketch. They need to see the proposed solution to validate it. However, they do NOT receive ATHENA's confidence level on the solution. This prevents anchoring -- if NEWTON sees "ATHENA confidence: 0.9," it may unconsciously rubber-stamp the physics. Without the confidence signal, NEWTON must form its own independent assessment.

#### 2.1 Physics Validation (NEWTON)

NEWTON systematically validates every physical claim in the scenario:

**Material Properties Check**
For every object in the scenario:
- Are the stated material properties (mass, dimensions, tensile strength, thermal conductivity, friction coefficient) consistent with real-world values for that material?
- Are the stated dimensions realistic for the described object?
- Are there unstated but relevant physical properties that affect the solution? (e.g., does the scenario mention a "steel chair" but not specify whether the steel is hardened or mild, and does this matter for the proposed use?)

**Force and Motion Analysis**
For every proposed action:
- Calculate the forces involved.
- Verify that the proposed motion is feasible given the stated constraints (mass, friction, human strength, available time).
- Check spatial geometry: can the actor reach what needs reaching? Does the proposed path have clearance? Are the angles and distances consistent?

**Environmental Physics**
- Are the environmental conditions (temperature, pressure, wind, humidity, lighting) correctly applied?
- Do environmental factors create effects the scenario ignores? (e.g., does a scenario set in rain fail to account for wet surfaces reducing friction?)

**Blast / Fluid / Thermal Analysis (when applicable)**
- For scenarios involving explosions, flooding, fire, chemical reactions, or temperature extremes: validate the threat model.
- Are overpressure calculations correct? Is the flooding rate realistic? Are thermal transfer rates accurate?

**Edge Case Identification**
- What happens if the actor is slightly weaker/slower/heavier than assumed?
- What is the minimum performance (worst-case human capability within the stated range) that still allows the solution to work?
- Is the solution KS-Fragile (works only within tight parameter margins)?

#### 2.2 Mathematical Verification (EULER)

EULER independently performs all calculations required by the scenario:

**Timing Budget**
- Construct a step-by-step timing table for the proposed solution.
- Each step must have a justified time estimate (based on human performance data, physics calculations, or established engineering standards).
- Sum the time costs. Compare to the stated deadline.
- Calculate the margin. A margin of less than 10% of the total deadline triggers a concern flag.

**Dimensional Analysis**
- Verify that all units are consistent.
- Check that derived quantities (speed = distance/time, force = mass * acceleration, etc.) are dimensionally correct.
- Identify any calculation where ATHENA has used approximate values; determine whether the approximation affects the solution's validity.

**Optimization Analysis (for OF/CT scenarios)**
- If the scenario involves resource allocation, sequencing, or tradeoffs: formalize the optimization problem.
- Identify the objective function, constraints, and decision variables.
- Determine whether an optimal solution exists (or prove that no optimal solution exists for CT/PX classifications).

**Impossibility Proofs (for PX scenarios)**
- If the scenario is intended to be a PARADOX: construct or verify the impossibility proof.
- The proof must identify the specific constraint conflict that creates impossibility.
- The proof must be constructive: it should show a counterexample or derive a contradiction, not merely assert impossibility.

**Sensitivity Analysis**
- For KS scenarios: vary each parameter by +/-20% and determine which parameter changes invalidate the solution.
- Document the "fragility profile": which parameters have tight margins?
- If the solution breaks under reasonable parameter variation, flag as KS-Fragile.

#### 2.3 Joint Physics-Math Validation Report

NEWTON and EULER produce a joint report:

```
VALIDATION REPORT: IM-XXXX

1. PHYSICS VALIDATION (NEWTON)
   - Per-claim validation table
   - Overall physics feasibility: VALID | VALID-WITH-CONCERNS | INVALID
   - Concerns: [list]
   - Corrections needed: [list]
   - NEWTON confidence: [0.0-1.0]

2. MATHEMATICAL VERIFICATION (EULER)
   - Timing budget table (step-by-step with calculations)
   - Force/energy calculations
   - Dimensional analysis: CONSISTENT | ERRORS-FOUND
   - Margin analysis: [margin as % of deadline]
   - Sensitivity analysis: [fragility profile]
   - EULER confidence: [0.0-1.0]

3. JOINT ASSESSMENT
   - Solution status: VALIDATED | NEEDS-REVISION | VETOED
   - If NEEDS-REVISION: specific changes required
   - If VETOED: the physical law or mathematical proof violated, and whether a fix is possible
   - Edge cases identified: [list]
   - Recommended parameter adjustments: [list]

4. FEASIBILITY CHECKS
   - Is the solution unique (KS-Singular) or are there alternatives (KS-Multiple)?
   - Alternative solution paths identified by NEWTON/EULER (if any)
   - Is the impossibility mirage convincing given the physics? (Does the scenario genuinely look impossible, or is the solution obvious once you think about the physics?)
```

#### 2.4 Revision Loop

If the Validation Report status is NEEDS-REVISION:
1. The Orchestrator routes the specific revision requirements back to ATHENA.
2. ATHENA revises the Seed Document (solution sketch, object properties, timing, or narrative as needed).
3. The revised Seed Document returns to NEWTON and EULER for re-validation.
4. Maximum 3 revision loops. After 3 failures, the scenario is either discarded or escalated to human review.

If the Validation Report status is VETOED:
1. The VETO is logged and the veto resolution protocol (Section 1.4) is invoked.
2. ATHENA may propose a fundamentally different solution approach.
3. If no valid solution can be found, the scenario may be reclassified (e.g., from KS to PX if the physics truly prohibit a solution).

---

### Phase 3: GROUND (GALILEO Leads)

**Duration**: 10-15 minutes
**Lead agent**: GALILEO
**Supporting agents**: None (GALILEO works independently)
**Input**: Validated Seed Document (post-Phase 2) + Validation Report. GALILEO sees the scenario, the validated solution, and the physics/math validation. GALILEO does NOT see ATHENA's original confidence level or NEWTON/EULER's confidence levels. This prevents GALILEO from calibrating its scientific assessment based on other agents' certainty.
**Output**: Scientific Grounding Report

#### 3.1 Literature Grounding

GALILEO maps the scenario to established cognitive science research:

**Cognitive Constructs Tested**
For each insight in the scenario's insight chain:
- What cognitive science construct does this test? (functional fixedness, constraint relaxation, affordance perception, distractor rejection, etc.)
- What is the seminal reference for this construct?
- What is the most recent relevant publication?
- What does the research predict about AI performance on this type of task?

*Example for The Blast Room*:
- Insight 1 (table as platform): Functional fixedness (Duncker 1945), Generic Parts Technique (McCaffrey 2012). AI prediction: LLMs exhibit strong functional fixedness due to training data bias toward canonical object functions (Berglund et al. 2023, reversal curse).
- Insight 2 (chair as impact tool): Affordance re-contextualization (Gibson 1979, Norman 1988). AI prediction: Models may recognize the chair as a tool but struggle with the specific application (breaking glass) vs. more canonical tool uses (prying, leverage).
- Insight 3 (banana rejection): Distractor handling, relevance determination (Chollet 2019, "knowing what to ignore"). AI prediction: Models will incorporate the banana at rates >25% due to the tendency to use all provided information.

**Comparison to Existing Benchmarks**
- Does any existing benchmark test similar cognitive skills?
- If yes: how does this scenario differ? What does it add?
- If no: document the novelty claim with precision.

*Example*:
- PHYRE tests intuitive physics prediction but not creative object re-contextualization.
- ARC-AGI-2 tests abstract pattern reasoning but not physical constraint satisfaction.
- Sarathy & Scheutz (2018) formalized "MacGyver problems" but did not create a benchmark with physics-validated solutions.
- IM-0001 combines all three: physical reasoning + creative re-contextualization + validated solutions. This combination is novel.

#### 3.2 AI Difficulty Evidence

GALILEO constructs an evidence-based argument for why current AI systems will find this scenario difficult:

**Compositional Reasoning Demand**
- How many insights must be chained? (Reference: Dziri et al. 2024 -- error compounds multiplicatively with chain length)
- Expected success rate given chain length: if each insight is found with probability p, N-insight chain succeeds with probability p^N.

**Counter-Intuitive Reasoning Demand**
- Does the solution require overriding a System 1 intuition? (Reference: Kahneman 2011, Binz & Schulz 2023)
- How strong is the intuition that must be overridden?

**Training Data Contamination Resistance**
- Has this specific scenario or a close variant appeared in any known training dataset?
- Are the insights composable from training data primitives, or do they require genuine out-of-distribution generalization?
- Reference: Ullman (2023) -- LLMs fail on trivial alterations to known tasks, suggesting memorization over understanding.

**Predicted Performance by Architecture**
- Direct answer (no reasoning): expected score [0-100]
- Chain-of-thought: expected score [0-100]
- Extended reasoning (o1/o3 style): expected score [0-100]
- Agentic with tool use: expected score [0-100]

#### 3.3 Scientific Grounding Report Structure

```
SCIENTIFIC GROUNDING REPORT: IM-XXXX

1. COGNITIVE CONSTRUCTS MAP
   - Insight -> Construct -> Citation -> AI Prediction

2. BENCHMARK POSITIONING
   - Comparison to existing benchmarks
   - Novelty claim with evidence

3. AI DIFFICULTY PREDICTION
   - Compositional chain analysis
   - Counter-intuitive demand analysis
   - Contamination resistance assessment
   - Predicted performance by architecture type

4. METHODOLOGICAL VALIDITY
   - Does the scenario have construct validity? (Does it measure what it claims to measure?)
   - Does the scoring rubric capture the relevant cognitive skills?
   - Are there confounds? (Factors other than the target skill that affect performance)

5. GALILEO ASSESSMENT
   - Overall scientific merit: HIGH | MEDIUM | LOW
   - Recommendations for improvement
   - GALILEO confidence: [0.0-1.0]
```

---

### Phase 4: CLASSIFY (SOCRATES Leads)

**Duration**: 10-15 minutes
**Lead agent**: SOCRATES
**Supporting agents**: None (SOCRATES works independently)
**Input**: Scenario narrative, environment, objects, threat description, "Why This Looks Impossible" section. SOCRATES does NOT receive the validated solution, the physics validation, or the scientific grounding report. This is the most critical context isolation in the system (see Section 3 for full rationale).
**Output**: Classification Report

#### 4.1 Context Isolation Rationale

SOCRATES classifies the scenario's solution status (KS, CT, OF, PX, MT, DG) and difficulty without seeing the solution. This is essential because:

1. **Solution knowledge biases classification.** If SOCRATES knows the solution exists and has been validated, it will classify the scenario as KS with near-100% confidence. But the question is not whether a solution exists in our files -- it is whether the scenario *presents* as solvable, as impossible, as paradoxical. SOCRATES must classify from the position of a solver encountering the scenario for the first time.

2. **Difficulty assessment is contaminated by solution visibility.** If SOCRATES has seen the step-by-step solution, it cannot accurately judge how hard the scenario is. It will underestimate difficulty because it has already been walked through the answer. Difficulty must be assessed from the perspective of ignorance about the solution.

3. **Impossibility type assessment requires fresh eyes.** The distinction between Type I (looks impossible, has a solution) and Type III (actually impossible) requires SOCRATES to independently assess whether a solution might exist, based solely on the problem constraints. If SOCRATES already knows the answer, this assessment is meaningless.

After SOCRATES produces its classification, the Orchestrator reveals the validated solution and the other agents' assessments. SOCRATES then has an opportunity to revise its classification in light of the full information. The delta between SOCRATES's blind classification and its informed revision is itself a data point: it measures how well the scenario creates the illusion of impossibility.

#### 4.2 Solution Status Classification

SOCRATES classifies the scenario along the Solution Spectrum:

| Status | SOCRATES's Decision Criteria (without seeing the solution) |
|---|---|
| **KS (Known-Solution)** | "I believe a solution exists and could identify at least one plausible approach, though I may not have fully validated it." |
| **CT (Contested)** | "I can identify multiple possible approaches, but I am uncertain which (if any) are fully valid. The problem seems solvable but the path is unclear." |
| **OF (Open-Frontier)** | "I cannot identify any plausible solution. The constraints appear to prevent all approaches I can conceive. However, I do not have a proof of impossibility." |
| **PX (Paradox)** | "I can construct an argument that no solution exists. The constraints appear mutually exclusive." |
| **MT (Metamorphic)** | "The problem as stated seems unsolvable, but I notice a hidden assumption or ambiguity in the problem statement that, if challenged, opens a solution path." |
| **DG (Degenerate)** | "The problem appears complex but the solution is actually trivially simple. Most of the scenario information is irrelevant." |

SOCRATES must provide a justification for its classification, including:
- The specific reasoning that led to the classification
- Alternative classifications considered and why they were rejected
- Confidence level (0.0-1.0)

#### 4.3 Impossibility Type Assessment

SOCRATES assesses which type of impossibility the scenario invokes:

| Type | SOCRATES's Assessment Criteria |
|---|---|
| **Type I (Impossible-seeming)** | "The scenario creates an illusion of impossibility through constraint design and functional fixedness. A solution likely exists but requires insight." |
| **Type II (Impossible-in-practice)** | "A theoretical solution may exist but practical constraints (precision, timing, human capability limits) may render it infeasible." |
| **Type III (Impossible-in-principle)** | "The constraints violate each other at a fundamental level. No solution can exist within the stated framework." |

#### 4.4 Ethical Review

SOCRATES reviews the scenario for ethical concerns:

**Checklist:**
- [ ] Does the scenario normalize or glorify violence?
- [ ] Does the scenario trivialize real-world disasters or suffering?
- [ ] Does the scenario contain cultural, racial, or gender stereotypes?
- [ ] Could the scenario provide instructions for real-world harm? (e.g., detailed bomb-making, chemical weapon synthesis)
- [ ] Does the scenario involve children in peril beyond what is appropriate for a benchmark?
- [ ] Does the scenario create unfair difficulty for test-takers from specific cultural backgrounds? (e.g., scenarios requiring knowledge of Western cultural references)
- [ ] Does the scenario's distractor design exploit cognitive biases in a way that could be harmful if internalized? (e.g., reinforcing the idea that calling for help is "wrong")

**Ethical assessment**: PASS | PASS-WITH-NOTES | FAIL

If FAIL: the Orchestrator halts the pipeline and routes the scenario to human review for ethical determination.

#### 4.5 Epistemological Analysis

SOCRATES performs a deeper analysis of what the scenario truly tests:

- **Surface-level test**: What does the scenario appear to test? (e.g., "spatial reasoning")
- **Deep-level test**: What does it actually test at a cognitive level? (e.g., "the ability to decompose a familiar object into its physical properties and recognize non-canonical affordances under time pressure, while simultaneously rejecting a compelling distractor that exploits the solver's tendency to use all available information")
- **Metacognitive demand**: Does the scenario require the solver to think about their own thinking? (e.g., MT scenarios require questioning one's assumptions about the problem statement)
- **Transferability**: Would success on this scenario predict success on real-world creative problem-solving? What are the limits of transferability?

#### 4.6 Difficulty Calibration (Blind)

SOCRATES provides a preliminary difficulty assessment using the I.D.C.B.T.X framework:

| Dimension | SOCRATES's Blind Assessment | Rationale |
|---|---|---|
| Insight Depth (I) | [1-5] | How many non-obvious insights does SOCRATES think are required? |
| Distractor Density (D) | [1-5] | How many distracting elements does SOCRATES identify? |
| Counter-Intuitive Index (C) | [1-5] | How strongly does intuition point toward the wrong answer? |
| Domain Bridge (B) | [1-5] | How many knowledge domains must be connected? |
| Temporal Pressure (T) | [1-5] | How much does time constraint shape the problem? |
| Trap Depth (X) | [1-5] | How compelling is the most attractive wrong answer? |

This blind assessment is later compared to the informed assessment (after SOCRATES sees the solution) in Phase 5.

#### 4.7 Classification Report Structure

```
CLASSIFICATION REPORT: IM-XXXX

1. BLIND CLASSIFICATION (without seeing solution)
   - Solution status: [KS|CT|OF|PX|MT|DG]
   - Justification: [reasoning]
   - Alternative classifications considered: [list with rejection reasons]
   - SOCRATES blind confidence: [0.0-1.0]

2. IMPOSSIBILITY TYPE
   - Type: [I|II|III]
   - Justification: [reasoning]

3. ETHICAL REVIEW
   - Status: [PASS|PASS-WITH-NOTES|FAIL]
   - Notes: [any concerns]

4. EPISTEMOLOGICAL ANALYSIS
   - Surface test: [description]
   - Deep test: [description]
   - Metacognitive demand: [LOW|MEDIUM|HIGH]
   - Transferability assessment: [description]

5. BLIND DIFFICULTY CALIBRATION
   - I.D.C.B.T.X profile: [scores]
   - Preliminary tier: [SPARK|FRACTURE|RUPTURE|SINGULARITY|IMPOSSIBLE]
   - Rationale per dimension: [table]

6. SOCRATES CONFIDENCE: [0.0-1.0]
```

---

### Phase 5: REFINE (All Agents)

**Duration**: 15-25 minutes
**Lead**: No single lead -- all agents participate equally
**Input**: All previous deliverables are now visible to all agents. This is the first phase where context isolation is fully lifted. Every agent sees every other agent's work.
**Output**: Refined Scenario Document

#### 5.1 Full Context Reveal

At the start of Phase 5, the Orchestrator distributes all previous deliverables to all agents:

- ATHENA receives: Validation Report, Scientific Grounding Report, Classification Report
- GALILEO receives: Original Seed Document (including ATHENA's confidence), Validation Report, Classification Report
- EULER receives: Scientific Grounding Report, Classification Report
- NEWTON receives: Scientific Grounding Report, Classification Report
- SOCRATES receives: Validated solution, Validation Report, Scientific Grounding Report

#### 5.2 Cross-Agent Review

Each agent reviews the full scenario from its own perspective and produces a review memo:

**ATHENA's Review**: Does the validated solution match ATHENA's original intent? Has validation changed the scenario in ways that weaken the insight chain or reduce the distractor effectiveness? Are there creative improvements suggested by the other agents' analysis?

**GALILEO's Review**: Does the scientific grounding hold up given the validated solution? Are there additional cognitive constructs tested that were not identified in Phase 3? Does the difficulty prediction need revision?

**EULER's Review**: Are there any remaining mathematical concerns? Does the sensitivity analysis suggest the scenario should be reclassified as KS-Fragile? Are the timing margins adequate?

**NEWTON's Review**: Are there any remaining physics concerns? Did the scientific grounding reveal physical effects that were not considered in Phase 2? Are the environmental conditions correctly modeled?

**SOCRATES's Review**: Having now seen the validated solution, does SOCRATES revise its classification? What is the delta between blind and informed assessment? Does the difficulty calibration change? Does the ethical assessment change in light of the full solution?

#### 5.3 Difficulty Calibration (Informed)

All five agents now vote on the I.D.C.B.T.X difficulty profile:

| Dimension | ATHENA | GALILEO | EULER | NEWTON | SOCRATES | Median |
|---|---|---|---|---|---|---|
| Insight Depth (I) | [vote] | [vote] | [vote] | [vote] | [vote] | [calculated] |
| Distractor Density (D) | [vote] | [vote] | [vote] | [vote] | [vote] | [calculated] |
| Counter-Intuitive Index (C) | [vote] | [vote] | [vote] | [vote] | [vote] | [calculated] |
| Domain Bridge (B) | [vote] | [vote] | [vote] | [vote] | [vote] | [calculated] |
| Temporal Pressure (T) | [vote] | [vote] | [vote] | [vote] | [vote] | [calculated] |
| Trap Depth (X) | [vote] | [vote] | [vote] | [vote] | [vote] | [calculated] |

The Orchestrator computes the median for each dimension. If any dimension has a range > 2 (e.g., one agent says 2, another says 5), the Orchestrator triggers a structured discussion on that dimension, using the Level 1 conflict resolution protocol.

The median profile determines the difficulty tier per the Framework's tier definitions:
- SPARK: I<=2, D<=2, C<=2, B<=2, T<=3, X<=2
- FRACTURE: I=2-3, D=2-3, C=2-3, B<=3, T<=3, X=2-3
- RUPTURE: I=3-4, D=3-4, C>=3, B>=3, any T, X>=3
- SINGULARITY: I>=4, D>=3, C>=4, B>=4, T>=3, X>=4
- IMPOSSIBLE: Maximum scores on multiple dimensions

#### 5.4 Distractor Refinement

All agents review the distractor inventory:

- **ATHENA** assesses whether each distractor is at the right strength level for the target difficulty.
- **NEWTON** verifies that no distractor accidentally enables a valid alternative solution.
- **EULER** checks whether any distractor's quantitative properties create unintended solution paths.
- **GALILEO** assesses whether the distractors effectively test the intended cognitive constructs.
- **SOCRATES** evaluates whether the distractors are ethically appropriate and whether they create unfair difficulty.

If any agent identifies a distractor that is too weak (everyone will immediately dismiss it) or too strong (it's actually more compelling than the real solution), the distractor is revised by ATHENA with input from the identifying agent.

#### 5.5 Final Consensus Vote

After cross-review, calibration, and distractor refinement, all agents vote on the scenario's readiness:

**Vote options:**
- **APPROVE**: The scenario is ready for documentation.
- **APPROVE-WITH-NOTES**: The scenario is ready but with documented reservations.
- **REVISE**: The scenario needs specific changes (agent must specify what).
- **DISCARD**: The scenario is fundamentally flawed and should be abandoned.

**Required consensus for advancement**: Supermajority (4 of 5 APPROVE or APPROVE-WITH-NOTES).

If the vote fails:
- The specific REVISE requests are compiled and routed to the appropriate agent(s).
- A revision cycle occurs (maximum 2 additional cycles in Phase 5).
- After 2 failed revision cycles, the scenario is escalated to human review or discarded.

---

### Phase 6: DOCUMENT (All Agents Contribute)

**Duration**: 5-10 minutes
**Lead**: Orchestrator (assembly), all agents (contribution)
**Input**: All refined deliverables from Phases 1-5
**Output**: Complete Scenario Document + Agent Trace Archive

#### 6.1 Agent Trace Preservation

Each agent produces a final trace document summarizing its contribution to the scenario:

```
AGENT TRACE: [AGENT NAME]
Scenario: IM-XXXX

1. MY ROLE IN THIS SCENARIO
   - What I was asked to do
   - What I found

2. KEY DECISIONS
   - Decision 1: [description] | Confidence: [0.0-1.0]
   - Decision 2: [description] | Confidence: [0.0-1.0]

3. CHALLENGES ISSUED
   - [List of any challenges issued to other agents, with outcomes]

4. CHALLENGES RECEIVED
   - [List of any challenges received, with how I responded]

5. DISAGREEMENTS
   - [List of any remaining disagreements, even if resolved by vote]
   - [My confidence that the resolution was correct]

6. CONFIDENCE SUMMARY
   - My overall confidence in the scenario: [0.0-1.0]
   - Dimension where I am least confident: [description]
   - What would increase my confidence: [description]

7. VERSION INFO
   - Model: [model identifier]
   - System prompt version: [hash]
   - Tokens consumed: [count]
   - Context window usage: [peak %]
```

#### 6.2 Final Document Assembly

The Orchestrator assembles the complete scenario document from the refined components:

1. **Public Document** (the scenario as presented to AI systems being evaluated):
   - Scenario narrative
   - Environment specification
   - Object table
   - Capability table
   - "Why This Looks Impossible" section
   - Common Wrong Answers table

2. **Evaluation Document** (the answer key and scoring rubric):
   - Verified Solution (for KS) or Evaluation Criteria (for CT/OF/PX/MT/DG)
   - Physics Validation
   - Key Insights
   - Distractor Analysis
   - Scoring Rubric
   - Counterfactual Variants

3. **Methodology Document** (the multi-agent trace):
   - Seed Document (ATHENA)
   - Validation Report (NEWTON + EULER)
   - Scientific Grounding Report (GALILEO)
   - Classification Report (SOCRATES)
   - Cross-Review Memos (all agents)
   - Difficulty Calibration Votes (all agents)
   - Disagreement Log
   - Confidence Summary
   - Agent Trace Archive (all 5 traces)

4. **Metadata Record**:
   - Scenario ID, category, status, tier, I.D.C.B.T.X profile
   - Creation timestamp
   - Agent versions (model + prompt version for each)
   - Number of revision loops per phase
   - Number of challenges, vetoes, escalations
   - Total compute time
   - Human review: YES/NO (and outcome if YES)

---

## 3. CONTEXT ENGINEERING

Context engineering is the discipline of controlling what each agent sees, when it sees it, and what it is prevented from seeing. In the Impossible Moments multi-agent system, context engineering serves three purposes: preventing confirmation bias, enabling independent assessment, and managing context window budgets.

### 3.1 The Context Isolation Matrix

The following matrix defines exactly what each agent sees at each phase:

| Content | Phase 1 (SEED) | Phase 2 (VALIDATE) | Phase 3 (GROUND) | Phase 4 (CLASSIFY) | Phase 5 (REFINE) | Phase 6 (DOCUMENT) |
|---|---|---|---|---|---|---|
| **Scenario narrative** | ATHENA creates | NEWTON, EULER see | GALILEO sees | SOCRATES sees | ALL see | ALL see |
| **Solution sketch** | ATHENA creates | NEWTON, EULER see | GALILEO sees | SOCRATES: **NO** | ALL see | ALL see |
| **ATHENA's confidence** | ATHENA has | NEWTON, EULER: **NO** | GALILEO: **NO** | SOCRATES: **NO** | ALL see | ALL see |
| **Physics validation** | -- | NEWTON creates | GALILEO sees | SOCRATES: **NO** | ALL see | ALL see |
| **Math verification** | -- | EULER creates | GALILEO sees | SOCRATES: **NO** | ALL see | ALL see |
| **NEWTON/EULER confidence** | -- | They have | GALILEO: **NO** | SOCRATES: **NO** | ALL see | ALL see |
| **Scientific grounding** | -- | -- | GALILEO creates | SOCRATES: **NO** | ALL see | ALL see |
| **GALILEO confidence** | -- | -- | GALILEO has | SOCRATES: **NO** | ALL see | ALL see |
| **Classification** | -- | -- | -- | SOCRATES creates | ALL see | ALL see |
| **Other agents' I.D.C.B.T.X votes** | -- | -- | -- | -- | ALL see (after voting) | ALL see |

**Key isolation points (marked NO in the matrix):**

1. **SOCRATES never sees the solution until Phase 5.** This is the most critical isolation. SOCRATES must classify the scenario's epistemological status and difficulty from the perspective of a naive solver.

2. **No agent sees another agent's confidence until Phase 5.** Confidence levels are powerful anchors. If ATHENA reports 0.95 confidence on its solution, other agents will unconsciously defer. By hiding confidence until the refinement phase, each agent must form its own independent assessment.

3. **SOCRATES never sees physics/math validation or scientific grounding until Phase 5.** SOCRATES's classification should be based on its own analysis of the scenario's constraints, not on whether NEWTON has blessed the physics.

### 3.2 Context Window Management

Foundation models have finite context windows. A complex scenario with full traces from all five agents can easily exceed 100,000 tokens. The context management strategy prevents overflow:

#### Token Budget Allocation

| Phase | Lead Agent Budget | Supporting Agent Budget | Rationale |
|---|---|---|---|
| Phase 1 (SEED) | ATHENA: 30K tokens | -- | Scenario creation requires space for narrative, objects, solution sketch |
| Phase 2 (VALIDATE) | NEWTON: 20K, EULER: 20K | ATHENA: 10K (for revisions) | Validation is detailed but formula-dense (high info per token) |
| Phase 3 (GROUND) | GALILEO: 20K | -- | Literature citations are dense text |
| Phase 4 (CLASSIFY) | SOCRATES: 15K | -- | Classification is concise; the scenario itself is the main input |
| Phase 5 (REFINE) | All agents: 10K each (50K total) | -- | Review memos should be concise |
| Phase 6 (DOCUMENT) | Orchestrator: 5K per agent trace | -- | Assembly from existing components |

#### Context Compression Techniques

When context approaches budget limits:

1. **Structured summaries**: Previous phases' outputs are compressed into structured summaries (key findings, decisions, confidence scores) rather than passed as full text.

2. **Claim-level granularity**: Instead of passing an entire validation report, the Orchestrator passes individual validated claims: "Claim: 75kg human can push 15kg table at 3.5 m/s on concrete. NEWTON: VALID (friction force 58.9N << human push force 200N+). EULER: VALID (speed achievable in the stated time budget)."

3. **Hierarchical context**: Each agent receives a three-level context:
   - **Level 1 (always loaded)**: Scenario template, classification frameworks, scoring rubrics (~5K tokens)
   - **Level 2 (loaded per scenario)**: Current scenario narrative + relevant previous phase summaries (~10-20K tokens)
   - **Level 3 (loaded on demand)**: Detailed calculations, full citations, extended reasoning (~variable, loaded only when the agent needs to reference specific details)

4. **Context pruning**: The Orchestrator identifies which parts of previous phases' outputs are relevant to the current agent and phase, and excludes irrelevant sections. For example, NEWTON does not need GALILEO's literature citations about the reversal curse -- only the claims about physical validity.

### 3.3 Progressive Disclosure Schedule

The progressive disclosure schedule controls the order in which information is revealed across phases:

```
Phase 1 (SEED):    ATHENA sees: generation brief
                   Others see: nothing

Phase 2 (VALIDATE): NEWTON sees: narrative + solution sketch (no confidence)
                    EULER sees: narrative + solution sketch (no confidence)
                    Others see: nothing

Phase 3 (GROUND):  GALILEO sees: narrative + solution + validation
                   (no confidence from any agent)
                   Others see: nothing

Phase 4 (CLASSIFY): SOCRATES sees: narrative + environment + objects
                    (NO solution, NO validation, NO grounding)
                    Others see: nothing

Phase 5 (REFINE):  ALL agents see: EVERYTHING
                   First time full visibility occurs

Phase 6 (DOCUMENT): ALL agents see: EVERYTHING
                   (same as Phase 5, plus refinement outcomes)
```

This schedule creates a **funnel of increasing context** that mirrors the scientific method: propose -> validate -> ground -> classify -> integrate -> document.

### 3.4 Information Isolation for Specific Scenario Types

Certain scenario types require modified context policies:

**OF (Open-Frontier) scenarios**: ATHENA does not produce a "verified solution" in Phase 1. Instead, ATHENA produces a "best known approach" or "evaluation criteria." NEWTON and EULER validate the evaluation criteria (not a solution). SOCRATES classifies without seeing evaluation criteria to independently assess whether the problem is genuinely open.

**PX (Paradox) scenarios**: ATHENA produces both the scenario and the impossibility proof. EULER validates the proof independently. SOCRATES classifies without seeing the proof to determine whether the scenario successfully creates the illusion of solvability before the impossibility becomes apparent.

**MT (Metamorphic) scenarios**: The hidden assumption is part of ATHENA's design. SOCRATES's blind classification is particularly important here: if SOCRATES identifies the hidden assumption without seeing ATHENA's notes, the assumption is too obvious. If SOCRATES misclassifies (e.g., calls it PX when it is MT), the assumption is well-hidden.

**DG (Degenerate) scenarios**: SOCRATES's blind assessment should identify the trivial solution quickly. If SOCRATES overthinks a DG scenario, the degenerate design is effective. If SOCRATES identifies it instantly, the scenario may need more narrative complexity to disguise the simplicity.

---

## 4. AGENT INTERACTION PATTERNS

Beyond the standard pipeline flow, the system defines four specific interaction patterns that handle non-standard situations.

### 4.1 Challenge Protocol

**Purpose**: Allow any agent to formally dispute another agent's claim.
**Trigger**: An agent identifies a specific claim in another agent's output that it believes is incorrect.

**Process:**

```
1. CHALLENGER submits a CHALLENGE message to the Orchestrator
   - Must specify: the exact claim being challenged, the agent who made it,
     and the evidence for why the claim is wrong
   - Must include: challenger's confidence that the claim is incorrect (0.0-1.0)

2. ORCHESTRATOR validates the challenge
   - Is the challenged claim within the challenger's domain of expertise?
   - Does the challenge include evidence, not just assertion?
   - If validation fails: challenge is logged but not forwarded

3. ORCHESTRATOR routes the challenge to the CHALLENGED AGENT
   - The challenged agent receives the challenge in full
   - The challenged agent has one response cycle

4. CHALLENGED AGENT responds
   - Options: ACCEPT (revise the claim), DEFEND (provide counter-evidence),
     PARTIAL (revise partially)

5. If DEFEND: ORCHESTRATOR presents both positions to all agents for VOTE
   - Agents who are not party to the dispute vote
   - Simple majority determines the outcome
   - The losing position is documented but overridden

6. Outcome is recorded in the Disagreement Log
```

**Constraints:**
- Maximum 3 challenges per agent per scenario (prevents adversarial looping)
- A challenge on a claim that has already been resolved by vote cannot be re-issued
- Cross-domain challenges (e.g., SOCRATES challenging EULER's math) are permitted but the challenged agent's domain authority applies per Section 1.4

#### Example Challenge

```
CHALLENGER: NEWTON
CHALLENGED: ATHENA
PHASE: 2 (VALIDATE)
CONFIDENCE: 0.85

CLAIM CHALLENGED: "The actor can push the 15kg table at 3.5 m/s
while simultaneously carrying the 4kg steel chair in one hand."

EVIDENCE: Human biomechanics research (Zatsiorsky 2002) indicates
that carrying a 4kg load in one hand while pushing a 15kg object
reduces sustainable push speed by approximately 20-30%. The 3.5 m/s
estimate should be revised to 2.5-2.8 m/s, which adds approximately
0.5s to the timing budget. The overall solution remains valid
(margin reduced from 6.0s to 5.5s), but the specific speed claim
is overstated.

RECOMMENDATION: Revise push speed to 2.8 m/s and recalculate
timing budget.
```

### 4.2 Veto Protocol

**Purpose**: Allow NEWTON and EULER to block physically or mathematically impossible claims from advancing through the pipeline.
**Trigger**: NEWTON or EULER identifies a claim that violates a physical law or mathematical theorem.

**Process:**

```
1. VETOING AGENT submits a VETO message to the Orchestrator
   - Must specify: the exact claim being vetoed, the physical law or
     mathematical theorem violated, and a proof or derivation
   - Must include: whether a corrective revision is possible or the
     scenario is fundamentally flawed

2. ORCHESTRATOR halts the pipeline
   - No agent may advance work on this scenario until the veto is resolved

3. If corrective revision is possible:
   a. ORCHESTRATOR routes the veto to ATHENA
   b. ATHENA has one revision cycle to propose a fix
   c. VETOING AGENT reviews the fix
   d. If satisfied: veto is lifted, pipeline resumes
   e. If not satisfied: scenario returns to Phase 1 or is discarded

4. If the scenario is fundamentally flawed:
   a. All agents are notified
   b. ATHENA may propose a complete redesign (different solution approach)
   c. If ATHENA's redesign passes validation: scenario continues from Phase 2
   d. If not: scenario is discarded

5. All vetoes are recorded in the Veto Log with full evidence
```

**Constraints:**
- Only NEWTON and EULER may issue vetoes
- A veto without proof is downgraded to a CHALLENGE
- Maximum 2 vetoes per agent per scenario (after which the scenario is automatically escalated to human review)

#### What Constitutes a Valid Veto

| Valid Veto | Invalid Veto |
|---|---|
| "The proposed action violates conservation of energy. The available kinetic energy is X, the required energy is Y > X. [calculation]" | "I don't think this would work in practice." |
| "The timing budget exceeds the deadline by 2.3 seconds. [step-by-step calculation]" | "The timing seems tight." |
| "Tempered glass of this thickness cannot be broken by a chair at the proposed swing speed. [force analysis vs. fracture threshold]" | "I'm not sure about the glass breaking." |
| "The thermal expansion coefficient of this material makes the proposed seal impossible at the stated temperature range. [expansion calculation]" | "The seal seems unreliable." |

### 4.3 Escalation Protocol

**Purpose**: Route unresolvable disputes to human review.
**Trigger**: Any of the following conditions:
- 3+ revision loops in any phase without convergence
- A veto that cannot be resolved by ATHENA revision
- Any agent's confidence on a critical deliverable falls below 0.5
- The required consensus level cannot be reached after the full conflict resolution ladder
- Any agent explicitly invokes ESCALATION

**Process:**

```
1. ORCHESTRATOR compiles an ESCALATION PACKAGE:
   - The current scenario document (all phases completed so far)
   - The specific point of disagreement
   - All evidence from both sides
   - All agents' confidence levels
   - The Orchestrator's assessment of why the dispute cannot be resolved

2. ESCALATION PACKAGE is sent to a human reviewer
   - Human reviewer is a domain expert (physicist, engineer, cognitive
     scientist, or ethicist, depending on the dispute domain)
   - Human reviewer has 48 hours to respond

3. Human reviewer's options:
   a. RESOLVE: Provide a decision on the disputed point with justification
   b. REDESIGN: The scenario needs fundamental changes; return to Phase 1
   c. DISCARD: The scenario is not viable
   d. SPLIT: The dispute reveals that the scenario should be two separate
      scenarios (one for each interpretation)

4. Human decision is final and is documented in the Human Review Log
```

**Metrics:** The system tracks escalation rate as a quality metric. A healthy escalation rate is 5-15% of scenarios. Below 5% suggests the agents may be too agreeable (rubber-stamping). Above 15% suggests the agents are miscalibrated or the scenario generation parameters are too ambitious.

### 4.4 Breakthrough Protocol

**Purpose**: Handle the case where an agent generates a potentially novel solution to an OPEN-FRONTIER scenario.
**Trigger**: During Phase 2 or Phase 5, any agent proposes a solution to an OF scenario that meets the preliminary criteria for a Breakthrough (per Framework Section 5.5).

**Process:**

```
1. PROPOSING AGENT submits a BREAKTHROUGH message
   - Must include: the proposed solution, a preliminary assessment of
     novelty (is this approach in the documented knowledge boundary?),
     and a preliminary physics validation

2. ORCHESTRATOR flags the scenario for special handling
   - The scenario is marked as a BREAKTHROUGH CANDIDATE
   - Additional validation is required beyond the normal pipeline

3. EULER performs a dedicated novelty check
   - Is the proposed approach mathematically distinct from known approaches?
   - Does it rely on any unproven assumptions?

4. NEWTON performs a dedicated physics deep-dive
   - Full force/energy/momentum analysis
   - Material property verification at the relevant conditions
   - Identification of any physical effects the proposal ignores

5. GALILEO performs a literature search
   - Has this approach been proposed before (in any domain)?
   - Is it a recombination of known techniques, or genuinely novel?

6. If the proposal survives all three reviews:
   a. The scenario is flagged for expert human review
   b. The proposal is documented in the Breakthrough Log
   c. The scenario's status remains OF but includes a note:
      "BREAKTHROUGH CANDIDATE: [agent name] proposed [summary].
      Awaiting expert verification."

7. Expert verification follows the protocol in Framework Section 5.6
   (Analytical / Computational / Experimental / Expert Consensus)
```

**This is the system's highest-value output.** The multi-agent architecture is designed not only to create benchmark scenarios but to potentially contribute novel solutions to genuinely unsolved problems. Every OF scenario is an invitation for the system to attempt something unprecedented.

---

## 5. QUALITY GATES

Each phase has explicit exit criteria that must be met before the Orchestrator advances the scenario to the next phase. Quality gates prevent poorly designed scenarios from consuming downstream agent compute.

### 5.1 Phase 1 (SEED) Exit Gate

| Criterion | Required Value | Check Method |
|---|---|---|
| Scenario narrative complete | All template sections present | Orchestrator structural check |
| Object table complete | Every object has mass, dimensions, material, notes | Orchestrator structural check |
| Capability table complete | All relevant human parameters specified | Orchestrator structural check |
| At least one insight identified | Insight chain has >= 1 entry | Orchestrator structural check |
| Solution sketch present | Step-by-step sequence exists | Orchestrator structural check |
| At least one distractor designed | Distractor inventory has >= 1 entry | Orchestrator structural check |
| Physical claims flagged | ATHENA has identified which claims need validation | Orchestrator structural check |
| No duplicate scenario | Concept does not match any existing scenario in the registry | Orchestrator similarity check (embedding distance > threshold) |
| Category match | Scenario fits the target category's definition and primary cognitive skill | ATHENA self-assessment |

**Gate decision**: All structural checks must pass. If any fail, the Orchestrator returns the Seed Document to ATHENA with specific deficiency notes. Maximum 3 attempts.

### 5.2 Phase 2 (VALIDATE) Exit Gate

| Criterion | Required Value | Check Method |
|---|---|---|
| All physical claims validated | Every flagged claim has VALID or INVALID status | Orchestrator completeness check |
| No INVALID claims without revision | If any claim is INVALID, ATHENA has revised and the revision has been re-validated | Orchestrator workflow check |
| Timing budget validated | EULER's timing sum <= stated deadline with >= 10% margin | EULER calculation |
| No active vetoes | All vetoes resolved (lifted, revised, or escalated) | Orchestrator veto log check |
| NEWTON confidence >= 0.7 | NEWTON's overall physics assessment is at least 0.7 | NEWTON self-report |
| EULER confidence >= 0.7 | EULER's overall math assessment is at least 0.7 | EULER self-report |
| Edge cases documented | At least 2 edge cases identified | Orchestrator structural check |
| Sensitivity analysis complete | Fragility profile documented for all key parameters | EULER deliverable check |

**Gate decision**: All criteria must be met. If NEWTON or EULER confidence is below 0.7, the Orchestrator triggers a structured discussion to identify and address the source of uncertainty.

### 5.3 Phase 3 (GROUND) Exit Gate

| Criterion | Required Value | Check Method |
|---|---|---|
| At least 3 cognitive constructs mapped | Each insight maps to a cited construct | Orchestrator structural check |
| At least 5 citations provided | References are specific (author, year, title) | Orchestrator structural check |
| AI difficulty prediction present | Predicted performance by architecture type is provided | Orchestrator structural check |
| Benchmark positioning complete | Comparison to at least 3 existing benchmarks | Orchestrator structural check |
| GALILEO confidence >= 0.6 | Overall scientific merit assessment | GALILEO self-report |
| No construct validity concerns | GALILEO has not flagged any construct validity issues | GALILEO deliverable check |

**Gate decision**: All criteria must be met. Lower confidence threshold (0.6) reflects that scientific grounding involves more judgment and less objective verification than physics validation.

### 5.4 Phase 4 (CLASSIFY) Exit Gate

| Criterion | Required Value | Check Method |
|---|---|---|
| Solution status classified | One of KS/CT/OF/PX/MT/DG assigned | Orchestrator structural check |
| Justification provided | Reasoning for classification is present and substantive (>100 words) | Orchestrator structural check |
| Impossibility type assessed | Type I/II/III assigned | Orchestrator structural check |
| Ethical review completed | PASS/PASS-WITH-NOTES/FAIL assigned | Orchestrator structural check |
| Ethical review PASS or PASS-WITH-NOTES | If FAIL, pipeline halts for human review | Orchestrator check |
| Blind difficulty calibration complete | I.D.C.B.T.X scores assigned | Orchestrator structural check |
| SOCRATES confidence >= 0.6 | Overall classification confidence | SOCRATES self-report |

**Gate decision**: All criteria must be met. Ethical FAIL triggers immediate human escalation regardless of other criteria.

### 5.5 Phase 5 (REFINE) Exit Gate

| Criterion | Required Value | Check Method |
|---|---|---|
| All agents have reviewed | 5 review memos received | Orchestrator completeness check |
| Difficulty calibration vote complete | All 5 agents have voted on I.D.C.B.T.X | Orchestrator completeness check |
| No dimension with range > 2 unresolved | Any dimension where agents disagree by >2 has been discussed and re-voted | Orchestrator check |
| Final consensus vote: APPROVE or APPROVE-WITH-NOTES | Supermajority (4/5) | Orchestrator vote tally |
| SOCRATES blind vs. informed delta documented | Delta between blind and informed classification recorded | Orchestrator structural check |
| Distractor review complete | All agents have reviewed distractor inventory | Orchestrator completeness check |
| No unresolved challenges or vetoes | All Phase 5 challenges resolved | Orchestrator challenge log check |

**Gate decision**: Supermajority approval required. If the vote fails after 2 revision cycles, the scenario is escalated to human review.

### 5.6 Phase 6 (DOCUMENT) Exit Gate

| Criterion | Required Value | Check Method |
|---|---|---|
| Public document complete | All template sections present | Orchestrator structural check |
| Evaluation document complete | Solution/criteria + scoring rubric present | Orchestrator structural check |
| All 5 agent traces present | Each agent has submitted a trace document | Orchestrator completeness check |
| Metadata record complete | All fields populated | Orchestrator structural check |
| Spell check / formatting | Document follows the style conventions | Orchestrator automated check |
| Final scenario ID assigned | Unique ID in the IM-XXXX format | Orchestrator registry check |

**Gate decision**: All structural checks must pass. Phase 6 has no judgment calls -- it is a documentation and assembly phase.

---

## 6. OUTPUT FORMAT

### 6.1 Complete Scenario Output Structure

Every scenario produced by the system generates a structured output with three tiers of documentation:

#### Tier 1: Public Scenario (Presented to AI Systems for Evaluation)

```markdown
# IM-[XXXX]: [SCENARIO NAME]

**Category**: [One of the 12 categories]
**Difficulty**: [Tier name] ([I.D.C.B.T.X profile])
**Status**: [KS | KS-Multiple | KS-Fragile | CT | OF | PX | MT | DG]
**Correct Outcome**: [SURVIVE | ESCAPE | BUILD | SOLVE | PROVE-IMPOSSIBLE | etc.]

---

## Scenario
[Narrative setup in second person. 2-4 paragraphs.]

### Environment
[Detailed physical specifications table]

### Threat / Challenge
[What makes this urgent]

### Position / Starting State
[Solver's starting position and knowledge]

### Available Objects
[Table: Object | Mass | Dimensions | Material | Notes]

### Agent Capabilities
[Table: Parameter | Value]

---

## Why This Looks Impossible
[2-3 sentences explaining the apparent impossibility]

## Common Wrong Answers
[Table: Wrong Answer | Why It's Wrong]
```

This is what an evaluated AI system sees. It contains NO solution, NO hints, and NO metadata about the creation process.

#### Tier 2: Evaluation Document (Used by Evaluators)

```markdown
# EVALUATION: IM-[XXXX]

## Verified Solution (KS) / Best Known Approaches (CT) /
## Evaluation Criteria (OF/PX/MT/DG)

### Step-by-step Solution
[Table: Step | Action | Time Cost | Cumulative | Rationale]

### Physics Validation
[Per-claim validation with calculations]

### Key Insights
[Numbered list mapped to I dimension score]

### Distractor Analysis
[Per-distractor: what it suggests, why it's wrong, how it tests the solver]

### Scoring Rubric
[Table: Response | Score | Reasoning]

### Counterfactual Variants
[2-3 parameter changes that create new scenarios]

### Difficulty Profile
I.D.C.B.T.X: [scores]
Tier: [SPARK | FRACTURE | RUPTURE | SINGULARITY | IMPOSSIBLE]
```

#### Tier 3: Methodology Trace (Published for Transparency)

```markdown
# METHODOLOGY TRACE: IM-[XXXX]

## Creation Metadata
- Created: [timestamp]
- Pipeline duration: [minutes]
- Revision loops: Phase 1: [N], Phase 2: [N], Phase 3: [N],
                  Phase 4: [N], Phase 5: [N]
- Challenges issued: [N] (resolved: [N], escalated: [N])
- Vetoes issued: [N] (lifted: [N], led to revision: [N])
- Human review triggered: [YES/NO]
- Agent versions: [table of model + prompt version per agent]

## Agent Contributions

### ATHENA (Reasoning)
- Concept origin: [description]
- Insights designed: [list]
- Solution confidence: [0.0-1.0]
- Revision count: [N]

### NEWTON (Physics)
- Claims validated: [N] (valid: [N], revised: [N], vetoed: [N])
- Physics confidence: [0.0-1.0]
- Key physics finding: [description]

### EULER (Mathematics)
- Calculations performed: [N]
- Timing margin: [seconds] ([%] of deadline)
- Fragility assessment: [description]
- Math confidence: [0.0-1.0]

### GALILEO (Scientific)
- Cognitive constructs mapped: [list]
- Citations provided: [N]
- AI difficulty prediction: [summary]
- Scientific merit: [HIGH | MEDIUM | LOW]

### SOCRATES (Philosophy)
- Blind classification: [status] (confidence: [0.0-1.0])
- Informed classification: [status] (confidence: [0.0-1.0])
- Classification delta: [description]
- Ethical review: [PASS | PASS-WITH-NOTES | FAIL]
- Epistemological analysis: [summary]

## Disagreement Log
[Table: Disagreement | Agents Involved | Resolution Method | Outcome]

## Confidence Heatmap
[Table: Agent | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Overall]

## Difficulty Calibration Votes
[Table: Dimension | ATHENA | GALILEO | EULER | NEWTON | SOCRATES | Median]
```

### 6.2 How to Read the Multi-Agent Reasoning

For researchers and reviewers examining the methodology traces:

**1. Start with the Disagreement Log.** Disagreements are the most informative part of the trace. They reveal where the scenario's design is non-obvious, where the physics is borderline, where the classification is ambiguous. A scenario with no disagreements is either trivially simple or insufficiently scrutinized.

**2. Compare SOCRATES's blind and informed classifications.** The delta between these two assessments is a measure of the scenario's "impossibility illusion" strength:
- Small delta (blind and informed agree): The scenario's surface presentation matches its actual nature. For KS scenarios, this means the solution is somewhat visible. For PX scenarios, this means the impossibility is somewhat obvious.
- Large delta (blind and informed differ): The scenario successfully creates an illusion. A KS scenario that SOCRATES blind-classified as OF has a powerful impossibility mirage.

**3. Check the confidence heatmap.** Low confidence from any agent on any phase signals an area of genuine uncertainty in the scenario. This is not a flaw -- it is information. Scenarios where all agents are 0.95+ confident everywhere may be too straightforward.

**4. Review NEWTON's physics validation claims.** These are the most objective components. If NEWTON validated a claim with high confidence and the claim is subsequently shown to be wrong, this reveals a systematic error in the physics validation process that should be corrected.

**5. Examine GALILEO's AI difficulty predictions against actual evaluation results.** Over time, comparing predictions to outcomes calibrates the prediction model and identifies where GALILEO systematically over- or under-estimates difficulty.

---

## 7. SCALING TO 500 SCENARIOS

### 7.1 The Production Target

The Impossible Moments v1.0 benchmark targets 500 scenarios across the 12 categories, 6 solution statuses, and 5 difficulty tiers. This section defines the production strategy, category coverage targets, difficulty distribution targets, and a 4-day production plan.

### 7.2 Category Coverage Targets

| Category | Target Count | % of Total | Rationale |
|---|---|---|---|
| The Locked Room | 55 | 11% | Core category; tests the fundamental skill (spatial reasoning + re-contextualization) |
| The Wrong Toolbox | 50 | 10% | High variety potential; many material/tool combinations |
| The Misdirection | 50 | 10% | Tests distractor rejection; important for AI evaluation |
| The Cascade | 40 | 8% | Complex to design; requires careful system modeling |
| The Babel Problem | 35 | 7% | Social + physical reasoning; harder to physics-validate |
| The Lilliput Conundrum | 35 | 7% | Scale reasoning; requires specialized physics knowledge |
| The Ticking Trade | 45 | 9% | Tests frame-breaking; high engagement value |
| The Ghost Machine | 40 | 8% | Mechanistic reasoning; good for physics-heavy evaluation |
| The Last Ingredient | 40 | 8% | Substitution reasoning; tests first-principles decomposition |
| The Invisible Wall | 35 | 7% | Abstract constraint navigation; complements physical categories |
| The Memory Palace | 35 | 7% | Pattern recognition; tests information decoding |
| The Horizon Problem | 40 | 8% | Frontier problems; high ceiling, highest potential for breakthroughs |
| **TOTAL** | **500** | **100%** | |

### 7.3 Difficulty Distribution Targets

| Tier | Target Count | % of Total | Target Solution Status Distribution |
|---|---|---|---|
| SPARK | 75 | 15% | 80% KS, 10% DG, 10% MT |
| FRACTURE | 175 | 35% | 65% KS, 15% CT, 10% MT, 5% PX, 5% DG |
| RUPTURE | 150 | 30% | 50% KS, 20% CT, 15% PX, 10% OF, 5% MT |
| SINGULARITY | 75 | 15% | 30% OF, 25% CT, 25% PX, 15% KS, 5% MT |
| IMPOSSIBLE | 25 | 5% | 50% OF, 30% PX, 20% CT |
| **TOTAL** | **500** | **100%** | |

**Solution Status Summary:**

| Status | Target Count | % of Total |
|---|---|---|
| KS (all subtypes) | 260 | 52% |
| CT | 80 | 16% |
| OF | 65 | 13% |
| PX | 55 | 11% |
| MT | 25 | 5% |
| DG | 15 | 3% |
| **TOTAL** | **500** | **100%** |

### 7.4 Batch Processing Strategy

The 500 scenarios are produced in 10 batches of 50, with each batch containing a proportional mix of categories and difficulty tiers.

#### Batch Composition (per batch of 50)

| Category | Count per Batch |
|---|---|
| The Locked Room | 5-6 |
| The Wrong Toolbox | 5 |
| The Misdirection | 5 |
| The Cascade | 4 |
| The Babel Problem | 3-4 |
| The Lilliput Conundrum | 3-4 |
| The Ticking Trade | 4-5 |
| The Ghost Machine | 4 |
| The Last Ingredient | 4 |
| The Invisible Wall | 3-4 |
| The Memory Palace | 3-4 |
| The Horizon Problem | 4 |

| Tier | Count per Batch |
|---|---|
| SPARK | 7-8 |
| FRACTURE | 17-18 |
| RUPTURE | 15 |
| SINGULARITY | 7-8 |
| IMPOSSIBLE | 2-3 |

#### Parallelism

The pipeline processes scenarios serially (one scenario at a time through all 6 phases), but multiple pipelines can run in parallel. With 5 parallel pipelines:
- Each pipeline processes one scenario in 45-90 minutes
- 5 scenarios complete per 45-90 minute window
- 50 scenarios (one batch) completes in approximately 8-15 hours
- All 500 scenarios complete in approximately 80-150 hours of compute time

### 7.5 Four-Day Production Plan

This plan assumes 5 parallel pipelines running continuously, with a human review team available for escalations.

#### Day 1: Foundation (Batches 1-3, Scenarios 1-150)

| Time Block | Activity | Output |
|---|---|---|
| 00:00-06:00 | Batch 1 production (50 scenarios) | 50 scenarios in pipeline |
| 06:00-12:00 | Batch 2 production + Batch 1 quality review | 50 completed, 50 in pipeline |
| 12:00-18:00 | Batch 3 production + Batch 2 quality review + Batch 1 escalation handling | 100 completed, 50 in pipeline |
| 18:00-24:00 | Batch 3 completion + quality review + coverage analysis | 150 completed |

**Day 1 Milestone**: 150 scenarios completed. Category and difficulty coverage audit. Identify any systematic issues (e.g., too many KS scenarios, not enough PX). Adjust generation briefs for Day 2.

#### Day 2: Expansion (Batches 4-6, Scenarios 151-300)

| Time Block | Activity | Output |
|---|---|---|
| 00:00-08:00 | Batch 4 production + escalation handling from Day 1 | 200 completed |
| 08:00-16:00 | Batch 5 production + Batch 4 quality review | 250 completed |
| 16:00-24:00 | Batch 6 production + Batch 5 quality review + mid-production audit | 300 completed |

**Day 2 Milestone**: 300 scenarios completed. Comprehensive coverage audit. Identify underrepresented categories or difficulty tiers. Prioritize remaining batches to fill gaps.

#### Day 3: Specialization (Batches 7-9, Scenarios 301-450)

| Time Block | Activity | Output |
|---|---|---|
| 00:00-08:00 | Batch 7 production (gap-filling focus) | 350 completed |
| 08:00-16:00 | Batch 8 production + quality review | 400 completed |
| 16:00-24:00 | Batch 9 production + cross-batch consistency review | 450 completed |

**Day 3 Milestone**: 450 scenarios completed. Begin cross-batch consistency checks: are similar scenarios in different batches sufficiently distinct? Are difficulty ratings calibrated consistently across batches?

#### Day 4: Completion and Quality Assurance (Batch 10, Scenarios 451-500, Final QA)

| Time Block | Activity | Output |
|---|---|---|
| 00:00-06:00 | Batch 10 production (final gap-filling) | 500 scenarios in pipeline |
| 06:00-12:00 | Batch 10 completion + all remaining escalations | 500 completed |
| 12:00-18:00 | Full corpus quality assurance: duplicate detection, coverage verification, difficulty distribution audit, random-sample deep review (10% of scenarios get human expert review) | QA report |
| 18:00-24:00 | Final revisions based on QA + document formatting + registry finalization | v1.0 release candidate |

**Day 4 Milestone**: 500 scenarios completed, QA'd, and formatted. Release candidate ready.

### 7.6 Quality Assurance at Scale

**Automated QA checks (applied to every scenario):**
- Template completeness: all required sections present
- Physics validation: all physical claims have VALID status
- Timing budget: margin >= 10% for all KS scenarios
- No duplicate scenarios (cosine similarity < 0.85 between any two scenario embeddings)
- Difficulty distribution matches targets (+/- 10%)
- Category distribution matches targets (+/- 10%)

**Sampled QA checks (applied to 10% of scenarios, randomly selected):**
- Human expert solves the scenario independently (for KS scenarios)
- Human expert reviews the physics validation
- Human expert reviews the ethical assessment
- Human expert assesses whether the difficulty rating feels calibrated

**Cross-batch calibration:**
- Compare median agent confidence across batches (should be stable; drift suggests fatigue or calibration shift)
- Compare veto rates across batches (should be stable)
- Compare escalation rates across batches (should be stable)
- If any metric drifts by more than 2 standard deviations, investigate and recalibrate

### 7.7 Attrition Budget

Not every scenario seed will survive the full pipeline. Based on pilot runs:

| Stage | Expected Attrition Rate | Scenarios Lost | Running Total |
|---|---|---|---|
| Phase 1 -> Phase 2 | 5% (structurally incomplete seeds) | 28 | 528 needed |
| Phase 2 -> Phase 3 | 15% (physics vetoes, failed validation) | 79 | 607 needed |
| Phase 3 -> Phase 4 | 3% (insufficient scientific grounding) | 18 | 625 needed |
| Phase 4 -> Phase 5 | 5% (ethical concerns, classification failures) | 31 | 656 needed |
| Phase 5 -> Phase 6 | 8% (failed consensus, unresolved disagreements) | 52 | 708 needed |
| Phase 6 -> Final | 2% (documentation issues, discovered duplicates) | 14 | 722 needed |

**To produce 500 final scenarios, the system must seed approximately 722 scenarios.** This represents a 31% total attrition rate, which is consistent with rigorous quality control in benchmark design.

With 5 parallel pipelines at 45-90 minutes per scenario, 722 seeds require approximately 108-217 hours of compute. Across 4 days (96 hours), this requires 1.1-2.3 parallel pipeline runs per hour, which is achievable with 5 pipelines running at the 45-minute-per-scenario pace.

---

## 8. OPEN-SOURCE STRUCTURE

### 8.1 Repository Structure

```
impossible-moments/
|
+-- README.md                          # Project overview and quick start
+-- LICENSE                            # Apache 2.0 or similar
+-- CITATION.cff                       # Citation format for academic use
|
+-- docs/
|   +-- framework.md                   # The complete benchmark framework
|   +-- multi_agent_system.md          # This document
|   +-- research_synthesis.md          # Scientific research foundation
|   +-- scoring_guide.md              # Detailed scoring rubrics
|   +-- contribution_guide.md         # How to contribute scenarios
|
+-- agents/
|   +-- README.md                      # Agent architecture overview
|   +-- prompts/
|   |   +-- athena_v1.md              # ATHENA system prompt
|   |   +-- galileo_v1.md             # GALILEO system prompt
|   |   +-- euler_v1.md               # EULER system prompt
|   |   +-- newton_v1.md              # NEWTON system prompt
|   |   +-- socrates_v1.md            # SOCRATES system prompt
|   |
|   +-- schemas/
|   |   +-- message.schema.json        # Message format schema
|   |   +-- seed_document.schema.json  # Phase 1 output schema
|   |   +-- validation_report.schema.json
|   |   +-- grounding_report.schema.json
|   |   +-- classification_report.schema.json
|   |   +-- agent_trace.schema.json
|   |
|   +-- orchestrator/
|   |   +-- orchestrator.py            # Main orchestrator logic
|   |   +-- context_manager.py         # Context isolation enforcement
|   |   +-- quality_gates.py           # Phase exit criteria checks
|   |   +-- consensus_engine.py        # Voting and conflict resolution
|   |   +-- document_builder.py        # Final document assembly
|   |   +-- batch_manager.py           # Production batch management
|   |   +-- config.yaml                # Pipeline configuration
|   |
|   +-- adapters/
|       +-- openai_adapter.py          # OpenAI API integration
|       +-- anthropic_adapter.py       # Anthropic API integration
|       +-- local_adapter.py           # Local model integration
|       +-- adapter_interface.py       # Abstract adapter interface
|
+-- scenarios/
|   +-- public/                        # Tier 1: public scenarios (for evaluation)
|   |   +-- IM-0001.md
|   |   +-- IM-0002.md
|   |   +-- ...
|   |
|   +-- evaluation/                    # Tier 2: answer keys and rubrics
|   |   +-- IM-0001_eval.md
|   |   +-- IM-0002_eval.md
|   |   +-- ...
|   |
|   +-- traces/                        # Tier 3: methodology traces
|   |   +-- IM-0001_trace.md
|   |   +-- IM-0002_trace.md
|   |   +-- ...
|   |
|   +-- registry.json                  # Scenario registry with metadata
|
+-- evaluation/
|   +-- evaluator.py                   # Automated evaluation engine
|   +-- scoring.py                     # Scoring implementation
|   +-- rubrics/                       # Per-scenario scoring rubrics
|   +-- results/                       # Evaluation results (gitignored)
|
+-- analysis/
|   +-- coverage_analysis.py           # Category/difficulty coverage tools
|   +-- difficulty_calibration.py      # Difficulty consistency analysis
|   +-- agent_performance.py           # Agent quality metrics
|   +-- breakthrough_tracker.py        # OF breakthrough candidate tracking
|
+-- tests/
|   +-- test_orchestrator.py
|   +-- test_context_manager.py
|   +-- test_quality_gates.py
|   +-- test_consensus_engine.py
|   +-- test_schemas.py
|
+-- examples/
    +-- single_scenario.py             # Create one scenario end-to-end
    +-- batch_production.py            # Run a batch of scenarios
    +-- evaluate_model.py              # Evaluate a model against the benchmark
    +-- custom_agent.py                # Add a custom 6th agent
```

### 8.2 How Others Can Use the System

#### Quick Start: Evaluate a Model

```bash
# Clone the repository
git clone https://github.com/impossible-moments/impossible-moments.git
cd impossible-moments

# Install dependencies
pip install -r requirements.txt

# Evaluate a model on the public benchmark
python evaluation/evaluator.py \
  --model "openai:gpt-4o" \
  --scenarios scenarios/public/ \
  --rubrics scenarios/evaluation/ \
  --output results/gpt4o_results.json
```

#### Quick Start: Create a New Scenario

```bash
# Generate a single scenario with the multi-agent pipeline
python agents/orchestrator/orchestrator.py \
  --mode single \
  --category "The Locked Room" \
  --difficulty-tier "FRACTURE" \
  --solution-status "KS" \
  --output scenarios/ \
  --config agents/orchestrator/config.yaml
```

#### Quick Start: Run a Production Batch

```bash
# Generate a batch of 50 scenarios
python agents/orchestrator/orchestrator.py \
  --mode batch \
  --batch-size 50 \
  --coverage-targets config/coverage_targets.yaml \
  --parallel-pipelines 5 \
  --output scenarios/ \
  --config agents/orchestrator/config.yaml
```

### 8.3 How to Extend with New Agents

The system is designed for extensibility. Adding a sixth (or Nth) agent requires three changes:

#### Step 1: Define the Agent

Create a new system prompt file at `agents/prompts/[agent_name]_v1.md`:

```markdown
# [AGENT NAME] System Prompt

## Role
[Description of the agent's unique expertise]

## Cognitive Model
[How the agent thinks and reasons]

## Primary Outputs
[What the agent produces]

## Evaluation Criteria
[How the agent's outputs are evaluated]

## What This Agent Does NOT Do
[Explicit scope boundaries]

## System Prompt
"You are a [role description]..."
```

#### Step 2: Register the Agent in the Pipeline

Update `agents/orchestrator/config.yaml`:

```yaml
agents:
  athena:
    prompt: agents/prompts/athena_v1.md
    phases: [SEED, REFINE, DOCUMENT]
    lead_phases: [SEED]
    can_veto: false
    # ... existing config

  # Add new agent:
  [new_agent_name]:
    prompt: agents/prompts/[agent_name]_v1.md
    phases: [list of phases where this agent participates]
    lead_phases: [list of phases this agent leads, if any]
    can_veto: [true/false]
    context_policy:
      SEED: [list of content types visible]
      VALIDATE: [list of content types visible]
      GROUND: [list of content types visible]
      CLASSIFY: [list of content types visible]
      REFINE: [all]
      DOCUMENT: [all]
    confidence_threshold: 0.6
    max_token_budget: 20000
```

#### Step 3: Update Quality Gates

If the new agent contributes to specific phases, update the quality gate criteria in `agents/orchestrator/quality_gates.py`:

```python
# Add quality gate criteria for the new agent
PHASE_GATES["VALIDATE"]["criteria"].append({
    "name": f"{new_agent_name}_assessment_complete",
    "check": lambda deliverables: new_agent_name in deliverables,
    "required": True
})
```

#### Candidate Extensions

The following agent extensions have been considered for future development:

| Agent Name | Role | Value Add |
|---|---|---|
| **DARWIN** (Evolutionary Agent) | Generate counterfactual variants by systematically varying parameters | Automates KS-Fragile testing and counterfactual generation |
| **TURING** (Adversarial Agent) | Attempt to solve the scenario using common AI strategies to identify weaknesses | Pre-evaluation quality check: if TURING solves it easily, the scenario is too easy |
| **HYPATIA** (Educational Agent) | Design pedagogical extensions: what can this scenario teach about physics, creativity, or critical thinking? | Supports educational use of the benchmark beyond AI evaluation |
| **CASSANDRA** (Risk Agent) | Assess real-world implications: if this scenario describes a real situation, what are the safety considerations? | Enhances ethical review with risk engineering perspective |

### 8.4 API / Prompt Format for Integration

The system provides a clean API interface for integration with external tools, evaluation platforms, and custom pipelines.

#### Scenario Generation API

```python
from impossible_moments import Pipeline, GenerationBrief

# Configure the pipeline
pipeline = Pipeline(
    config_path="agents/orchestrator/config.yaml",
    model_provider="anthropic",  # or "openai", "local"
    api_key="...",
    parallel_pipelines=5
)

# Define a generation brief
brief = GenerationBrief(
    category="The Locked Room",
    difficulty_tier="FRACTURE",
    solution_status="KS",
    constraints=["Must involve water as a threat", "Must include exactly 3 objects"],
    inspiration_seed="A flooding scenario with unconventional tools"
)

# Generate a scenario
result = pipeline.generate(brief)

# Access outputs
print(result.public_document)      # Tier 1: public scenario
print(result.evaluation_document)  # Tier 2: answer key
print(result.methodology_trace)    # Tier 3: agent traces
print(result.metadata)             # Creation metadata
```

#### Evaluation API

```python
from impossible_moments import Evaluator, Scenario

# Load scenarios
scenarios = Scenario.load_directory("scenarios/public/")

# Configure evaluator
evaluator = Evaluator(
    rubrics_path="scenarios/evaluation/",
    model_under_test="openai:gpt-4o",
    runs_per_scenario=3,  # Multiple runs for reliability
    temperature=0.7
)

# Run evaluation
results = evaluator.evaluate(scenarios)

# Access results
print(results.im_score)           # Aggregate IM-Score
print(results.im_profile)         # Category-level radar chart data
print(results.im_frontier)        # OF breakthrough candidates
print(results.per_scenario)       # Per-scenario detailed results
```

#### Prompt Format for Direct Agent Use

For users who want to use individual agents without the full pipeline (e.g., for research purposes), each agent can be invoked directly via a standardized prompt format:

```
[SYSTEM PROMPT: loaded from agents/prompts/{agent}_v1.md]

[USER PROMPT:]
You are operating in the Impossible Moments multi-agent system.

PHASE: {current_phase}
SCENARIO_ID: {id}
YOUR ROLE: {agent_role_summary}

CONTEXT (per context isolation policy for this phase):
{filtered_context}

YOUR TASK:
{phase_specific_task_description}

OUTPUT FORMAT:
{deliverable_schema_for_this_phase}

CONSTRAINTS:
- Confidence score required on all outputs
- Evidence required for all claims
- Maximum output: {token_budget} tokens
```

### 8.5 Versioning and Compatibility

| Component | Versioning Scheme | Compatibility |
|---|---|---|
| Benchmark (scenarios) | Semantic: v1.0, v1.1, v2.0 | Minor versions add scenarios; major versions may change categories or scoring |
| Agent prompts | Hash-based: athena_v1_abc123 | Prompt changes produce new hashes; results reference specific prompt versions |
| Orchestrator | Semantic: v1.0, v1.1 | Minor versions add quality gates or interaction patterns; major versions change pipeline phases |
| Evaluation engine | Semantic: v1.0, v1.1 | Minor versions add rubric types; major versions change scoring architecture |
| Schemas | Semantic: v1.0, v1.1 | Breaking changes increment major version; all schema versions are preserved |

### 8.6 Governance and Contribution

**Scenario contributions**: External contributors can submit scenarios following the template. Submitted scenarios go through the full multi-agent pipeline. Acceptance requires passing all quality gates and supermajority agent approval.

**Agent contributions**: Contributors can propose new agents (per Section 8.3). New agents are reviewed by the core team for (a) non-overlap with existing agents, (b) clear value add, (c) well-defined scope boundaries, and (d) integration with the context isolation policy.

**Evaluation contributions**: Contributors can submit evaluation results for new models. Results must include full metadata (model version, temperature, number of runs) and raw responses for verification.

**Dispute process**: Anyone can challenge a scenario's classification, solution validity, or physics. Challenges follow the Challenge Protocol (Section 4.1) with the contributor as the challenger and the relevant agent(s) as the challenged party. Successful challenges result in scenario revision or reclassification.

---

## Appendix A: Glossary

| Term | Definition |
|---|---|
| **Affordance** | An action possibility offered by an object or environment relative to an agent's capabilities (Gibson 1979) |
| **Breakthrough** | A novel, physically valid, expert-verified solution to an OPEN-FRONTIER scenario |
| **Canonical affordance** | The default, expected use of an object (table = dining surface) |
| **Challenge** | A formal dispute of another agent's claim, requiring evidence |
| **Context isolation** | The practice of controlling what each agent sees to prevent bias |
| **Deliverable** | The primary output of an agent for a given pipeline phase |
| **Distractor** | An element in a scenario that invites incorrect solution paths |
| **Functional fixedness** | The cognitive bias of conceiving an object only in terms of its typical use (Duncker 1945) |
| **Generation brief** | The Orchestrator's instructions to ATHENA for creating a new scenario |
| **Geometric mirage** | The initial mental model a scenario creates that excludes the solution |
| **I.D.C.B.T.X** | The six-dimensional difficulty profile (Insight, Distractor, Counter-intuitive, Bridge, Temporal, Trap) |
| **Non-canonical affordance** | An atypical but physically valid use of an object (table = stepping platform) |
| **Orchestrator** | The deterministic control system that manages agent workflow (not an LLM) |
| **Progressive disclosure** | The practice of revealing information to agents in a controlled sequence |
| **Quality gate** | Exit criteria that must be met before advancing to the next pipeline phase |
| **Seed Document** | ATHENA's Phase 1 output: the initial scenario design |
| **Solution Spectrum** | The six-category classification of scenario solvability (KS, CT, OF, PX, MT, DG) |
| **Supermajority** | Agreement of at least 4 of 5 agents |
| **Veto** | A pipeline-halting objection from NEWTON or EULER on physics/math grounds |

---

## Appendix B: Agent Prompt Version Control

Each agent's system prompt is version-controlled and hashed. The hash is included in every scenario's metadata, enabling exact reproduction of the creation conditions.

**Prompt versioning conventions:**
- `v1`: Initial production version
- `v1.1`: Minor refinements (clarification, additional examples) that do not change the agent's fundamental behavior
- `v2`: Major revision (changed role scope, new interaction patterns, revised evaluation criteria)

**Prompt testing protocol:**
Before deploying a new prompt version, the updated agent is tested on 10 previously completed scenarios. The new version's outputs are compared to the original version's outputs. If the new version would have changed any scenario's final classification, solution, or difficulty tier, the change is reviewed by the core team before deployment.

---

## Appendix C: Failure Mode Catalog

The following failure modes have been observed during pilot runs and are addressed by specific system design decisions:

| Failure Mode | Description | System Mitigation |
|---|---|---|
| **Confirmation bias** | Agent validates its own previous claims | Context isolation prevents any agent from both creating and validating the same claim |
| **Anchoring on confidence** | Agent defers to another agent's high confidence instead of forming independent judgment | Confidence scores are hidden until Phase 5 |
| **Distractor neglect** | Distractors are designed as afterthoughts and are too weak | Phase 5 cross-review specifically evaluates distractor strength |
| **Physics rubber-stamping** | NEWTON approves physics claims without rigorous calculation | Quality gate requires NEWTON confidence >= 0.7 and explicit per-claim validation |
| **Classification contamination** | SOCRATES classifies as KS because it has seen the solution | SOCRATES is isolated from the solution until Phase 5 |
| **Creative convergence** | ATHENA generates similar scenarios across batches | No cross-scenario memory + Orchestrator duplicate detection |
| **Difficulty inflation** | Agents rate scenarios as harder than they are (to make the benchmark seem more impressive) | Five-agent median voting with range-check discussion for divergent ratings |
| **Difficulty deflation** | Agents rate scenarios as easier than they are (because they have all seen the solution) | SOCRATES's blind difficulty assessment serves as a calibration anchor |
| **Ethical blind spots** | Scenarios contain culturally insensitive or harmful content | SOCRATES ethical review checklist + FAIL triggers mandatory human review |
| **Scope creep** | Agents exceed their role boundaries (e.g., EULER writing narrative) | System prompts explicitly state what each agent does NOT do |
| **Context overflow** | Long scenarios exhaust context windows | Token budgets per phase, hierarchical context loading, message size limits |
| **Adversarial looping** | Agents challenge each other indefinitely | Maximum 3 challenges per agent per scenario; Level 4 escalation as backstop |

---

## Appendix D: Metrics and Monitoring

The system produces the following metrics for monitoring production quality:

### Per-Scenario Metrics

| Metric | Healthy Range | Red Flag |
|---|---|---|
| Pipeline duration | 45-90 min | >120 min (suggests excessive retries) |
| Revision loops (total across phases) | 0-5 | >8 (suggests fundamental design issues) |
| Challenges issued | 0-4 | >6 (suggests agent miscalibration) |
| Vetoes issued | 0-1 | >2 (triggers auto-escalation) |
| Minimum agent confidence | 0.6-0.9 | <0.5 (triggers escalation) |
| Maximum agent confidence | 0.7-0.95 | 1.0 across all agents (suggests insufficient scrutiny) |
| SOCRATES blind-informed delta | Variable | Always 0 (suggests the scenario has no impossibility illusion) |

### Per-Batch Metrics

| Metric | Target | Red Flag |
|---|---|---|
| Completion rate (seeds -> final) | 65-75% | <50% (too many failures) or >90% (insufficient rigor) |
| Category coverage deviation | +/- 10% of targets | >20% deviation in any category |
| Difficulty distribution deviation | +/- 10% of targets | >20% deviation in any tier |
| Human escalation rate | 5-15% | <5% (too agreeable) or >20% (too contentious) |
| Mean pipeline duration | 50-70 min | Drift >20% from batch 1 baseline |

### System-Level Metrics

| Metric | Purpose |
|---|---|
| Agent agreement rate by phase | Identifies which phases produce the most disagreement (healthy: Phase 2 and Phase 5 have highest disagreement rates) |
| Veto rate by category | Identifies which categories have the most physics issues (expected: The Cascade and The Lilliput Conundrum have highest veto rates) |
| SOCRATES classification accuracy (blind vs. final) | Measures how well scenarios create impossibility illusions |
| GALILEO prediction calibration | Compares predicted AI performance to actual evaluation results (longitudinal metric) |
| Breakthrough candidate rate | Percentage of OF scenarios where agents propose novel solutions (target: >10%) |

---

*This document constitutes the complete architectural specification for the Impossible Moments multi-agent scenario creation system. It defines the agent roles, communication protocols, pipeline phases, context engineering policies, interaction patterns, quality gates, output formats, production strategy, and open-source structure required to produce the Impossible Moments benchmark at scale. The methodology is intended to be as transparent and reproducible as the benchmark itself -- the HOW is as important as the WHAT.*

*The system is designed to be challenged. If you find a flaw in the architecture, a gap in the quality gates, or a failure mode not covered in Appendix C, submit an issue. The benchmark improves when the system that creates it is itself subjected to the same standard of rigorous, creative scrutiny that Impossible Moments demands of the AI systems it evaluates.*

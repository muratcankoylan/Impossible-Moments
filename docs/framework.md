# Impossible Moments: The Complete Benchmark Framework

**Version**: 1.0
**Date**: 2026-02-16
**Status**: Foundational Design Document

---

## 1. THE MISSION STATEMENT

**Impossible Moments (IM)** is a benchmark built on a single conviction: that the most revealing test of intelligence is not what you know, but what you do when everything you know says "this cannot be done." Every existing AI benchmark -- from MMLU to ARC-AGI-2, from SWE-bench to FrontierMath -- measures some form of acquired competence: knowledge retrieval, pattern completion, code generation, mathematical proof. These are necessary components of intelligence, but they are not sufficient. They miss the moment that separates a knowledgeable system from a genuinely intelligent one: the moment of creative rupture, when an agent stares at a locked door and sees, not a wall, but a hinge. Impossible Moments is designed to provoke exactly that rupture and to measure whether it occurs.

The benchmark presents AI systems with richly narrated, physically grounded scenarios that appear -- on first inspection -- to have no solution. A person locked in a room with a bomb and a banana. A bridge that must be built from materials that cannot span the gap. A sinking vessel where every repair creates a new failure. These are not trick questions and they are not trivia. They are constraint-satisfaction problems wrapped in narrative urgency, demanding that the solver decompose familiar objects into raw physical properties, reject seductive but fatal intuitions, chain multiple non-obvious insights into a coherent plan, and validate every step against the laws of physics. The spectrum runs from KNOWN-SOLUTION scenarios (where a verified answer exists but is deeply counter-intuitive) all the way to OPEN-FRONTIER scenarios where no human has yet found the answer -- and an AI that proposes a valid, novel solution achieves something genuinely unprecedented.

Why does this matter? Because the challenges facing humanity in the coming decades -- climate engineering, pandemic response, resource allocation under scarcity, infrastructure resilience -- are not knowledge-retrieval problems. They are creative constraint-satisfaction problems under pressure, with incomplete information, misleading heuristics, and physical laws that do not bend to wishful thinking. If AI systems are to be trusted partners in solving these challenges, we need to know whether they can think beyond the training distribution, not merely recite within it. Impossible Moments is the instrument for that measurement. It is not the only benchmark the field needs, but it measures the one thing no other benchmark does: the capacity to see what isn't obvious, to do what looks impossible, and to know the difference between a problem that resists solution and one that has none.

---

## 2. THE SOLUTION SPECTRUM

Every scenario in the Impossible Moments benchmark is classified along a **Solution Spectrum** -- a taxonomy that describes the current state of human knowledge about whether and how the scenario can be solved. This spectrum is not a difficulty scale; it is an epistemological classification. A KNOWN-SOLUTION problem can be brutally hard, and a PARADOX can be recognized quickly by a sufficiently clear thinker.

### 2.1 KNOWN-SOLUTION (KS)

**Definition**: The scenario appears impossible, but a verified, physically valid solution exists. The solution has been confirmed through physics calculations, engineering analysis, or empirical demonstration. Human domain experts agree that the solution works.

**Purpose**: Tests whether the AI can break through the appearance of impossibility to find the verified path. This is the bread and butter of the benchmark -- the category where scoring is most objective and reproducible.

**Evaluation**: Binary correctness (did the AI find a valid solution?) plus process scoring (did it identify the key insights, reject distractors, and validate physics?).

**Exemplar**: The Blast Room (IM-0001). The window is "unreachable," but the table provides elevation, the chair breaks the glass, and the banana is irrelevant. Solution verified through force calculations, spatial geometry, and timing analysis.

**Sub-classifications**:
- **KS-Singular**: Only one known valid solution path exists.
- **KS-Multiple**: Multiple valid solution paths exist. Tests whether the AI finds any of them, and whether it can enumerate alternatives.
- **KS-Fragile**: The solution works, but only within tight parameter margins. A small change in assumptions (table 5 kg heavier, window 10 cm smaller) would invalidate it. Tests precision of physical reasoning.

---

### 2.2 CONTESTED (CT)

**Definition**: Multiple proposed solutions exist, but none has been definitively verified or universally accepted. Experts disagree about whether the proposed solutions are physically valid, practically feasible, or complete.

**Purpose**: Tests the AI's ability to navigate genuine uncertainty. Can it identify the strongest candidate solution and articulate why it is stronger than alternatives? Can it identify the specific point of disagreement that makes the problem contested?

**Evaluation**: Assessed on a rubric measuring: (1) quality of the best solution proposed, (2) awareness that the problem is contested, (3) identification of the crux point where solutions diverge, (4) intellectual honesty about remaining uncertainty. An AI that confidently declares a single answer without acknowledging the dispute scores lower than one that presents the strongest candidate while flagging the unresolved tension.

**Exemplar concept**: "The Cascade" -- a scenario involving a sequence of mechanical failures on a vessel where two repair strategies each solve some failures but may worsen others. Marine engineers disagree about optimal sequencing.

---

### 2.3 OPEN-FRONTIER (OF)

**Definition**: No known solution exists. The problem is genuinely unsolved. It may be solvable -- there is no proof of impossibility -- but no human has yet found a valid path. AI responses are evaluated for creativity, physical plausibility, and novelty.

**Purpose**: This is where the benchmark reaches beyond evaluation into discovery. If an AI proposes a solution that is subsequently verified by domain experts, that is a BREAKTHROUGH -- a genuine contribution to human knowledge, not merely a test score.

**Evaluation**: A dedicated evaluation protocol (see Section 5.5) involving:
- **Plausibility score** (0-10): Does the proposed solution obey known physical laws? Is it internally consistent?
- **Novelty score** (0-10): Is this approach genuinely new, or a restatement of known failed approaches?
- **Completeness score** (0-10): Does the solution address all constraints, or does it quietly ignore some?
- **Expert review trigger**: Any response scoring above 7 on all three dimensions is flagged for human expert review. This is the pipeline through which breakthroughs are detected.

**Exemplar concept**: "The Thermal Lock" -- a materials science scenario where a container must be sealed using only materials that expand when heated, in an environment that is continuously heating. No known configuration achieves a lasting seal.

---

### 2.4 PARADOX (PX)

**Definition**: The problem is provably impossible. No solution exists within the stated constraints. The correct response is to demonstrate impossibility -- to prove that the constraints are mutually exclusive.

**Purpose**: Tests whether the AI can distinguish genuine impossibility from the mere appearance of impossibility. This is the complement of the main benchmark: while most scenarios reward finding hidden solutions, PARADOX scenarios reward recognizing that no solution exists. An AI that always tries to find a solution -- even when one cannot exist -- is exhibiting a different failure mode: creative hallucination in the face of logical impossibility.

**Evaluation**: The AI must: (1) correctly assert that no solution exists, (2) provide a valid proof or argument for why, (3) identify the specific constraint conflict that creates the impossibility. Full marks require rigorous argument. Partial marks for correct assertion with incomplete justification. Zero marks for proposing a "solution" that violates the stated constraints.

**Design principle**: PARADOX scenarios must be carefully constructed so that the impossibility is non-trivial. A scenario that is obviously impossible ("escape a sealed room with no exits and no tools") tests nothing. The impossibility must be hidden behind a plausible-looking set of objects and constraints that invite creative problem-solving before the solver realizes the trap.

**Exemplar concept**: "The Conservation Cage" -- a scenario where the available energy in all objects and processes is precisely calculated to be insufficient for any escape mechanism. The solver must perform an energy audit to prove that the minimum energy required exceeds the maximum energy available.

---

### 2.5 METAMORPHIC (MT)

**Definition**: The problem as stated has no solution, but the problem statement itself contains a hidden assumption, ambiguity, or reframing opportunity. The solution lies in challenging the premise rather than solving within it.

**Purpose**: Tests meta-cognitive reasoning -- the ability to step outside the problem frame and question whether the problem has been correctly understood. In real-world creative problem-solving, this is one of the most powerful moves: the inventor who realizes the customer's stated problem is not the real problem.

**Evaluation**: The AI must: (1) identify the hidden assumption or ambiguity, (2) articulate a reframed version of the problem, (3) solve the reframed problem with a valid solution. Evaluated on the precision with which the assumption is identified and the elegance of the reframing.

**Exemplar concept**: "The Wrong Door" -- a scenario where the solver is told to escape through the door, which is locked and impenetrable. The scenario describes the walls in great detail, including one wall made of drywall rather than concrete. The solution is to reject the premise that escape must occur through the door and instead punch through the drywall.

---

### 2.6 DEGENERATE (DG)

**Definition**: The problem has a solution, but the solution is trivially simple and hidden behind narrative complexity, emotional urgency, or red-herring details. The scenario is designed so that most of the provided information is irrelevant, and the correct action is almost insultingly straightforward.

**Purpose**: Tests whether the AI can resist the cognitive pull of complexity. Sophisticated solvers often overthink simple problems. A long, detailed scenario description creates an implicit expectation of a proportionally complex solution. This category tests whether the AI can resist that expectation and find the simple path.

**Evaluation**: Speed and directness of reaching the correct (simple) solution. Penalty for unnecessary complexity, over-analysis of irrelevant details, or Rube Goldberg solutions to problems that have a two-step answer.

**Exemplar concept**: "The Vault" -- a scenario with elaborate descriptions of a vault door, combination lock mechanism, reinforced walls, security cameras, and guard rotations. The vault door is described as "closed but not locked." The solution is to open it.

---

### Solution Spectrum Summary Table

| Status | Solution Exists? | Humans Know It? | AI Goal | Evaluation Mode |
|---|---|---|---|---|
| **KNOWN-SOLUTION (KS)** | Yes | Yes | Find the verified solution | Objective correctness + process scoring |
| **CONTESTED (CT)** | Maybe | Disputed | Navigate uncertainty intelligently | Quality of reasoning under ambiguity |
| **OPEN-FRONTIER (OF)** | Unknown | No | Propose creative, plausible solutions | Expert-reviewed creativity scoring |
| **PARADOX (PX)** | No (provably) | Yes (by design) | Prove impossibility | Quality of impossibility argument |
| **METAMORPHIC (MT)** | Yes (after reframing) | Yes (by design) | Challenge the premise | Precision of assumption identification |
| **DEGENERATE (DG)** | Yes (trivially) | Yes (by design) | Resist overthinking | Speed and simplicity of response |

---

## 3. CATEGORY TAXONOMY

The following twelve categories define the types of scenarios in the Impossible Moments benchmark. They are designed to be evocative, memorable, and to test distinct cognitive skills. Each category has a signature feel -- a narrative texture that makes scenarios within it recognizably part of a family while still being individually surprising.

---

### 3.1 THE LOCKED ROOM
*"The walls are solid, the door won't budge, and the clock is ticking."*

**Description**: Escape and survival scenarios in enclosed spaces under time pressure. The solver must find a way out of a physically constrained environment using only the objects present, within a deadline imposed by an approaching threat (explosion, flooding, gas, structural collapse). The environment is described with precise physical specifications.

**Primary cognitive skill**: Spatial reasoning + object re-contextualization under temporal pressure.

**Example scenario concept**: You are in a flooding basement. Water is rising at 2 cm/second. The ceiling hatch is rusted shut. You have a car jack, a bag of road salt, and a fire extinguisher. The hatch opens outward.

**Difficulty range**: Primarily KS and KS-Fragile. Occasional PX (the constraints are too tight for any valid escape). Rarely MT (the "escape" is reframed as "survive in place").

**Distractor profile**: Always includes at least one object with strong but irrelevant affordances (the banana archetype).

---

### 3.2 THE WRONG TOOLBOX
*"You have everything you need. You just don't know it yet."*

**Description**: Construction and repair scenarios where the available materials seem categorically wrong for the task. Build a bridge from fabric. Seal a pipe with ice. Create a load-bearing structure from objects designed for entirely different purposes. The solver must decompose objects into their raw physical properties (mass, tensile strength, thermal conductivity, geometry) and discover non-canonical affordances.

**Primary cognitive skill**: Functional fixedness breaking -- the Generic Parts Technique (McCaffrey 2012) operationalized as a benchmark.

**Example scenario concept**: You must create a water-tight seal on a cracked pipe. Your only materials are a leather belt, chewing gum, and a car cigarette lighter. The pipe carries drinking water, so adhesives must be food-safe.

**Difficulty range**: KS (most scenarios), CT (when the material science is ambiguous), OF (when no known technique achieves the required specification).

**Distractor profile**: Includes objects that seem more appropriate for the task but have a hidden disqualifying property (e.g., a tube of epoxy that isn't food-safe in the pipe scenario).

---

### 3.3 THE MISDIRECTION
*"The obvious answer isn't just wrong. It's fatal."*

**Description**: Scenarios where the most natural, intuitive course of action leads to failure or death. The critical information is present in the scenario description but buried in plain sight, while a salient but misleading detail draws attention toward the wrong path. Success requires noticing what others overlook and resisting the gravitational pull of the obvious.

**Primary cognitive skill**: Distractor rejection + signal extraction from noise. System 2 overriding System 1.

**Example scenario concept**: You are in a room filling with a colorless, odorless gas. There is a gas mask on the table. The gas mask's filter canister is marked as expired three years ago. The room has a vent near the floor. Most solvers will grab the mask. The correct action is to get low (the gas is lighter than air and rises) and breathe near the floor vent, because an expired filter may provide no protection or -- worse -- a false sense of security that delays real action.

**Difficulty range**: KS and KS-Fragile dominate. The difficulty comes from the strength of the misdirection, not the complexity of the solution. Occasional MT (the scenario itself is the misdirection).

**Distractor profile**: Inverted -- the "distractor" is the most prominent, attractive object, while the real solution is low-salience.

---

### 3.4 THE CASCADE
*"Fix one thing, break another. Fix that, break two more."*

**Description**: Scenarios involving interdependent systems where interventions have side effects. The solver must reason about second- and third-order consequences, prioritize actions, and find an ordering that resolves all failures without creating new ones -- or recognize that the cascade has a stable equilibrium that can be exploited. These are dynamic scenarios where the state of the environment changes as the solver acts.

**Primary cognitive skill**: Systems thinking + sequential planning with side-effect reasoning.

**Example scenario concept**: A small boat has three problems: a cracked hull (taking on water), a jammed bilge pump (can't remove water), and a tangled sail (can't steer to shore). Fixing the hull requires the boat to be dry enough to apply sealant. Running the pump clears water but vibrates the hull crack wider. Untangling the sail requires both hands, meaning you can't bail water manually. What order do you work in?

**Difficulty range**: CT (expert disagreement about optimal sequencing) and OF (no proven optimal strategy). Occasionally KS when a single non-obvious insight breaks the dependency cycle.

**Distractor profile**: Every element is relevant, but their interactions are the source of difficulty. No traditional distractors -- the entire problem is a web of coupled constraints.

---

### 3.5 THE BABEL PROBLEM
*"The person with the answer doesn't speak your language. The person who speaks your language doesn't have the answer."*

**Description**: Scenarios that combine physical constraints with social, communicative, or coordination challenges. The solver must reason about other agents -- their knowledge, motivations, communication barriers, and likely behavior -- while simultaneously managing physical constraints. These scenarios test theory of mind and cooperative strategy under adversity.

**Primary cognitive skill**: Theory of mind + multi-agent coordination + communication under constraint.

**Example scenario concept**: You and a stranger are on opposite sides of a collapsed tunnel. You can hear each other but not see. You have a map showing two possible exits, one of which is blocked by debris on their side (they don't know which). They have a flashlight you need to navigate your side. You must coordinate an escape plan by voice alone, but there is a language barrier -- you share only about 20 common words.

**Difficulty range**: KS-Multiple (multiple valid coordination strategies) and OF (genuinely unsolved coordination problems with minimal communication). Occasionally PX (provably impossible to coordinate given the communication constraints).

**Distractor profile**: Social distractors -- apparent cooperation opportunities that are actually impossible given the information asymmetry.

---

### 3.6 THE LILLIPUT CONUNDRUM
*"The problem is too big. Or too small. Or both at the same time."*

**Description**: Scenarios where the difficulty arises from extreme scale -- either microscopic, astronomical, or involving scale transitions. The solver must reason about physics and constraints at scales where human intuition breaks down. Surface tension dominates at small scale. Orbital mechanics matter at large scale. A machine that works at human scale may fail completely when shrunk or enlarged.

**Primary cognitive skill**: Scale-variant physical reasoning. Understanding that physical laws don't change but their relative importance does.

**Example scenario concept**: You are 2 cm tall (shrunk). You need to cross a kitchen countertop to reach the edge and signal for help. The counter is wet with a thin film of water. At your scale, surface tension makes the water film an impassable barrier. Your full-size tools (now proportionally giant) are useless. You have a toothpick, a grain of salt, and a strand of hair. How do you cross?

**Difficulty range**: KS (when the scale-dependent physics is well-understood), OF (when the scale regime introduces genuinely uncertain physics). Frequently CT (experts disagree about the effective physics at the scenario's scale).

**Distractor profile**: Objects whose affordances change radically with scale. A "helpful" tool at normal scale becomes useless or dangerous at the scenario's scale.

---

### 3.7 THE TICKING TRADE
*"You can save the cargo or the crew. You have 90 seconds to find a third option."*

**Description**: Forced-choice dilemmas that appear to have exactly two options, both unacceptable. The solver must find a third path that the binary framing obscures. These scenarios test the ability to reject false dichotomies and expand the solution space under extreme time pressure. The time constraint is not decorative -- it forecloses the "gather more information" strategy that would make the problem easy.

**Primary cognitive skill**: Frame-breaking under time pressure. Rejection of false dichotomies. Rapid creative ideation.

**Example scenario concept**: A cargo drone is approaching a populated area with a critical battery failure. It will crash in 90 seconds. You can redirect it to crash in an empty parking lot (destroying the $2M medical supply cargo) or let it follow its current path to the hospital landing pad (risking lives if the battery fails before arrival). You have remote control access. Is there a third option that saves both cargo and lives?

**Difficulty range**: KS (a third option exists and is verifiable), PX (sometimes there genuinely is no third option, and the solver must choose the lesser harm and justify why), MT (the framing itself is the trap).

**Distractor profile**: The two "obvious" options are both partially correct, pulling the solver's attention away from the unexplored solution space.

---

### 3.8 THE GHOST MACHINE
*"The machine works perfectly. The machine cannot possibly work. Both of these statements are true."*

**Description**: Scenarios involving mechanisms, devices, or processes that appear to violate physical laws. The solver must either (a) identify the hidden mechanism that makes the "impossible" device work, (b) prove that it truly cannot work and identify the flaw in the demonstration, or (c) recognize that the device works but for different reasons than claimed. These are inverse engineering puzzles wrapped in narrative.

**Primary cognitive skill**: Mechanistic reasoning + skepticism calibration. The ability to be simultaneously open-minded ("maybe it works in a way I haven't considered") and rigorous ("but it must obey conservation laws").

**Example scenario concept**: A street performer shows you a simple wooden wheel that, once spun, appears to accelerate on its own for several minutes before stopping. Friction should slow it down, not speed it up. You are allowed to examine the wheel closely. You notice it is slightly warped and the axle is warm to the touch. Explain the mechanism or prove it's a trick.

**Difficulty range**: KS (the mechanism is known and discoverable from the clues), CT (the mechanism is debated), PX (the device truly violates physics and the solver must prove it's fake).

**Distractor profile**: Plausible-sounding but incorrect explanations (e.g., "it's magnets" when it's actually thermal expansion).

---

### 3.9 THE LAST INGREDIENT
*"You have 90% of what you need. The missing 10% doesn't exist."*

**Description**: Scenarios where the solver has almost everything required to achieve a goal, but one critical component is missing and cannot be obtained conventionally. The solution requires either (a) synthesizing the missing component from available materials, (b) finding a substitute that fulfills the same function, or (c) redesigning the approach to eliminate the need for the missing component entirely. These are resource-scarcity problems focused on a single critical gap.

**Primary cognitive skill**: Substitution reasoning + first-principles decomposition. "What does this component actually DO, and what else could do that?"

**Example scenario concept**: You need to start a fire to signal rescuers, but you have no ignition source. You have a clear plastic water bottle (full), steel wool from a cleaning kit, a 9V battery from a dead radio, and dry kindling. Multiple ignition paths exist: the water bottle lens, the battery + steel wool circuit.

**Difficulty range**: KS-Multiple (multiple substitution paths), OF (when no known substitute exists for the missing component).

**Distractor profile**: Objects that look like they could substitute but fail on a critical property (e.g., a magnifying glass with a crack that disperses the focal point).

---

### 3.10 THE INVISIBLE WALL
*"There's nothing stopping you. Except everything is stopping you."*

**Description**: Scenarios where the constraint is not a physical barrier but a rule, norm, protocol, or system behavior that prevents the obvious action. The environment is physically open, but bureaucratic, procedural, logical, or game-theoretic constraints create an invisible maze. The solver must identify the constraint structure and find a path through it -- or find a legitimate way to change the rules.

**Primary cognitive skill**: Abstract constraint identification + rule-system navigation. Understanding that constraints can be logical and social, not just physical.

**Example scenario concept**: You are in a building during an emergency. The fire exits are all physically accessible, but each is controlled by an electronic lock that requires a key card you don't have. The security desk is unmanned. The system has a fire-override mode, but it requires simultaneous activation from two panels on different floors. You are alone.

**Difficulty range**: KS (a path through the rule system exists), PX (the rule system is genuinely airtight), MT (the rules can be legitimately reinterpreted).

**Distractor profile**: Apparent loopholes that don't actually work (the system was designed to prevent exactly that bypass).

---

### 3.11 THE MEMORY PALACE
*"You solved this before. But you've forgotten how. And the solution is encoded in the room itself."*

**Description**: Scenarios that involve information reconstruction, pattern recognition, and deductive reasoning in physical environments. The solver encounters an environment that encodes information -- a sequence of objects, marks, spatial arrangements, or physical states that, correctly interpreted, reveal a solution, a code, or a critical fact. The challenge is both to recognize that information is encoded and to decode it correctly.

**Primary cognitive skill**: Pattern recognition + abductive reasoning. Inferring the encoding scheme from fragmentary evidence.

**Example scenario concept**: You wake in a room with no memory of how you arrived. Seven objects are arranged in a line on a shelf: a red book, two blue marbles, a brass key, a white candle, a green bottle, and a black stone. The room has a combination lock with 4 digits. The objects encode the combination through a pattern you must deduce (color frequencies? shelf positions? material atomic numbers?).

**Difficulty range**: KS (the encoding is deterministic and discoverable), MT (the encoding is ambiguous and the solver must question which interpretation is correct).

**Distractor profile**: Objects that could participate in multiple encoding schemes, only one of which yields the correct answer.

---

### 3.12 THE HORIZON PROBLEM
*"The solution doesn't exist yet. Can you invent it?"*

**Description**: Scenarios drawn from genuine unsolved problems in science, engineering, medicine, or mathematics -- translated into vivid, narrative-driven formats. These are not textbook problems; they are frontier challenges reframed as immediate, embodied predicaments. The solver is not expected to produce a definitive answer but is evaluated on the quality, creativity, and physical plausibility of their proposals.

**Primary cognitive skill**: Scientific creativity + first-principles reasoning at the boundary of human knowledge.

**Example scenario concept**: You are on a generation ship traveling at 0.1c. The radiation shielding is degrading faster than expected. You have the ship's raw material supply (metals, polymers, water) and its manufacturing capabilities. No known shielding configuration provides adequate protection for the remaining journey duration with available mass. Propose a novel approach.

**Difficulty range**: Exclusively OF and CT. These are the benchmark's frontier -- the problems where a genuinely novel AI response could constitute a real contribution.

**Distractor profile**: Known approaches that have already been considered and found insufficient. The solver must go beyond them.

---

### Category Summary Table

| # | Category | Primary Skill | Typical Solution Status | Signature Challenge |
|---|---|---|---|---|
| 3.1 | The Locked Room | Spatial reasoning + re-contextualization | KS, KS-Fragile, PX | Escape under time pressure |
| 3.2 | The Wrong Toolbox | Functional fixedness breaking | KS, CT, OF | Build with wrong materials |
| 3.3 | The Misdirection | Distractor rejection + signal extraction | KS, KS-Fragile, MT | Resist the obvious trap |
| 3.4 | The Cascade | Systems thinking + side-effect reasoning | CT, OF, KS | Fix coupled failures |
| 3.5 | The Babel Problem | Theory of mind + coordination | KS-Multiple, OF, PX | Cooperate under communication constraints |
| 3.6 | The Lilliput Conundrum | Scale-variant physics | KS, CT, OF | Reason at extreme scales |
| 3.7 | The Ticking Trade | Frame-breaking + false dichotomy rejection | KS, PX, MT | Find the hidden third option |
| 3.8 | The Ghost Machine | Mechanistic reasoning + skepticism | KS, CT, PX | Explain or debunk the "impossible" |
| 3.9 | The Last Ingredient | Substitution reasoning | KS-Multiple, OF | Replace the irreplaceable |
| 3.10 | The Invisible Wall | Abstract constraint navigation | KS, PX, MT | Navigate invisible rule systems |
| 3.11 | The Memory Palace | Pattern recognition + abduction | KS, MT | Decode the environment |
| 3.12 | The Horizon Problem | Scientific creativity | OF, CT | Invent at the frontier |

---

## 4. DIFFICULTY CALIBRATION

Difficulty in Impossible Moments is not a single number. Creative problem-solving is hard along multiple independent axes, and a problem that is easy on one axis can be punishing on another. The benchmark uses a **six-dimensional difficulty framework** where each scenario receives a score from 1-5 on each axis. The aggregate difficulty level is derived from the dimensional profile, not a simple average.

### 4.1 The Six Dimensions of Difficulty

#### Dimension 1: INSIGHT DEPTH (I)
*How many non-obvious conceptual leaps are required?*

| Score | Description | Example |
|---|---|---|
| 1 | Single insight, relatively accessible | "Use the chair to break the glass" |
| 2 | Two insights, independently findable | "Table as platform" + "chair as tool" |
| 3 | Three insights, some dependency between them | The Blast Room: platform + tool + distractor rejection |
| 4 | Four or more insights, chained dependencies | Each insight unlocks the possibility of the next |
| 5 | Deep restructuring required; the entire problem frame must be reconceived | The solution requires abandoning the initial problem representation entirely |

#### Dimension 2: DISTRACTOR DENSITY (D)
*How many elements exist that invite incorrect solution paths?*

| Score | Description | Example |
|---|---|---|
| 1 | No distractors; all elements are relevant | Every object in the room plays a role |
| 2 | One mild distractor (the banana) | Single irrelevant object, easy to dismiss |
| 3 | Two to three distractors, at least one seductive | An irrelevant object that strongly suggests a plausible but wrong approach |
| 4 | Multiple distractors forming a coherent false narrative | The distractors together suggest a complete but wrong solution |
| 5 | The distractors constitute the majority of the scenario information; the real solution elements are buried | Most of the description is irrelevant; the solution hinges on a single overlooked detail |

#### Dimension 3: COUNTER-INTUITIVE INDEX (C)
*How strongly does intuition point toward the wrong answer?*

| Score | Description | Example |
|---|---|---|
| 1 | The solution is surprising but not counter-intuitive | "I wouldn't have thought of that, but it makes sense" |
| 2 | The solution requires overriding one weak intuition | "Tables are furniture" must be overridden |
| 3 | The solution requires overriding a moderate intuition | "Run from danger" must be overridden in favor of "move toward danger" |
| 4 | The solution requires doing the opposite of what instinct dictates | "To survive, you must make the problem temporarily worse" |
| 5 | The solution is so counter-intuitive that even after being told, it feels wrong | "To escape the fire, set a second fire" (backburn technique) |

#### Dimension 4: DOMAIN BRIDGE (B)
*How many distinct knowledge domains must be connected?*

| Score | Description | Example |
|---|---|---|
| 1 | Single domain (e.g., basic mechanics) | Force, mass, acceleration |
| 2 | Two related domains (e.g., mechanics + geometry) | Spatial reasoning + material properties |
| 3 | Two unrelated domains (e.g., chemistry + social reasoning) | Chemical reaction knowledge + game theory |
| 4 | Three or more domains | Fluid dynamics + electrical engineering + time management |
| 5 | The key insight requires bridging domains that have no obvious connection | Biology + structural engineering, or music theory + thermodynamics |

#### Dimension 5: TEMPORAL PRESSURE (T)
*How much does time constraint shape the problem?*

| Score | Description | Example |
|---|---|---|
| 1 | No time constraint; the solver can deliberate indefinitely | "You have as long as you need" |
| 2 | Soft time constraint; faster is better but slow is possible | "Resources are gradually depleting" |
| 3 | Moderate time constraint; the solution must fit within a window | "18 seconds until detonation" (Blast Room) |
| 4 | Severe time constraint; the time window eliminates many otherwise-valid approaches | Only the fastest valid approach succeeds |
| 5 | The time constraint itself is the puzzle; the solver must create time that doesn't exist | "You need 60 seconds but have 30" -- the solution involves slowing, pausing, or redefining the clock |

#### Dimension 6: TRAP DEPTH (X)
*How compelling is the most attractive wrong answer?*

| Score | Description | Example |
|---|---|---|
| 1 | No obvious wrong answer; the problem is purely about finding any solution | Open-ended construction challenges |
| 2 | One weak trap; a common but obviously flawed approach | "Shelter behind the table" (flawed because overpressure kills regardless) |
| 3 | One strong trap; an approach that seems correct through several steps of reasoning before failing | A solution that works physically but exceeds the time constraint |
| 4 | Multiple traps at different levels of analysis | First trap catches naive thinkers, second trap catches careful thinkers |
| 5 | The trap is so well-constructed that the solver must fail into it before finding the real solution | The wrong answer is a necessary stepping stone -- understanding why it fails reveals the correct approach |

---

### 4.2 Difficulty Tiers

The six dimensions combine into five named difficulty tiers. A scenario's tier is determined by its dimensional profile, not a simple sum.

#### TIER 1: SPARK
*"The moment of 'aha' -- one good idea and you're through."*

**Profile**: I <= 2, D <= 2, C <= 2, B <= 2, T <= 3, X <= 2
**Description**: Scenarios requiring a single key insight, minimal distraction, and straightforward physics. Solvable by any system capable of basic object re-contextualization. These are the benchmark's warm-up -- designed to be satisfying, confidence-building, and to establish the "rules of the game."
**Expected AI performance**: Strong reasoning models solve 60-80%.

#### TIER 2: FRACTURE
*"Something you believe must break before the solution appears."*

**Profile**: I = 2-3, D = 2-3, C = 2-3, B <= 3, T <= 3, X = 2-3
**Description**: Scenarios requiring two or three insights with moderate distraction and at least one counter-intuitive element. The solver must overcome at least one instance of functional fixedness and resist at least one trap. The Blast Room sits at the high end of this tier.
**Expected AI performance**: Strong reasoning models solve 30-50%.

#### TIER 3: RUPTURE
*"Everything you try fails. The solution requires you to stop trying and start seeing."*

**Profile**: I = 3-4, D = 3-4, C >= 3, B >= 3, any T, X >= 3
**Description**: Scenarios with deep insight chains, compelling traps, strong counter-intuitive elements, and cross-domain requirements. These are the benchmark's core challenge -- the level at which current frontier models are expected to struggle significantly. Solutions often require the solver to abandon their initial problem representation entirely.
**Expected AI performance**: Strong reasoning models solve 10-25%.

#### TIER 4: SINGULARITY
*"The problem is real. The solution is unknown. Welcome to the frontier."*

**Profile**: I >= 4, D >= 3, C >= 4, B >= 4, T >= 3, X >= 4
**Description**: Scenarios that are either genuinely unsolved (OF), deeply contested (CT), or require such radical re-framing (MT) that even expert humans struggle. At this tier, the benchmark transitions from evaluation to exploration. AI performance is evaluated on the quality of the attempt, not binary correctness.
**Expected AI performance**: Strong reasoning models solve 0-10%. Any valid solution at this tier is noteworthy.

#### TIER 5: IMPOSSIBLE
*"This is what the benchmark is named for."*

**Profile**: Maximum scores on multiple dimensions, or OF/PX status with extreme complexity.
**Description**: Scenarios at the absolute boundary of what can be asked. These may be provably impossible (PX) requiring brilliant impossibility proofs, or genuinely open problems (OF) where any valid novel solution represents a breakthrough. The benchmark includes only a small number of TIER 5 scenarios, and they are not expected to be "solved" in any traditional sense. They exist to give the benchmark a ceiling that will not be reached.
**Expected AI performance**: 0-2%. A single valid solution to a TIER 5 OF problem would be a landmark achievement.

---

### 4.3 Dimensional Profile Notation

Each scenario's difficulty is recorded as a six-digit profile: **I.D.C.B.T.X**

The Blast Room: **3.2.2.2.3.2** (Tier 2: FRACTURE)
- I=3 (three insights: platform, tool, distractor rejection)
- D=2 (one distractor: the banana)
- C=2 (mild counter-intuition: table is not for shielding)
- B=2 (mechanics + spatial geometry)
- T=3 (18-second timer shapes the solution)
- X=2 (one strong trap: "shelter behind table")

This notation allows precise difficulty comparison across scenarios and categories.

---

## 5. THE "IMPOSSIBLE" PHILOSOPHY

### 5.1 The Nature of Impossibility

The word "impossible" carries three distinct meanings, and the failure to distinguish them is one of the most common errors in both human reasoning and AI evaluation:

**Impossible-seeming (Type I)**: The problem appears impossible because the solver has not yet found the insight that unlocks the solution. This is the domain of creative problem-solving, and it is the heartland of the Impossible Moments benchmark. The Blast Room is Type I impossible: the window seems unreachable, but the table changes the geometry. Every KNOWN-SOLUTION scenario is Type I by definition.

**Impossible-in-practice (Type II)**: The problem is theoretically solvable but practically infeasible given real-world constraints. A solution exists on paper but would require resources, precision, or time that are unavailable. This is the territory of CONTESTED scenarios and KS-Fragile classifications. The solution works in principle but may fail in practice due to parameter sensitivity.

**Impossible-in-principle (Type III)**: The problem violates fundamental physical laws, logical constraints, or mathematical theorems. No amount of creativity can overcome conservation of energy, the halting problem, or Arrow's impossibility theorem. This is the domain of PARADOX scenarios.

The central thesis of Impossible Moments is that **the most important intellectual skill is the ability to correctly classify a problem among these three types -- and then respond accordingly.** A system that treats Type I as Type III gives up too easily. A system that treats Type III as Type I hallucinates solutions. A system that mistakes Type II for Type I proposes solutions that work on paper but fail in reality.

### 5.2 Designing Problems That Look Impossible But Are Solvable

The craft of creating Type I impossible scenarios follows a set of principles distilled from cognitive science research on insight problems:

**Principle 1: The Functional Fixedness Lock**
Every scenario must contain at least one object whose solution-relevant affordance is non-canonical. The object must have a strong canonical affordance that pulls the solver toward an incorrect use. The table in the Blast Room is furniture (canonical) that must be recognized as a platform (non-canonical). The strength of the fixedness lock determines the Insight Depth (I) and Counter-Intuitive Index (C) scores.

**Principle 2: The Geometric Mirage**
The scenario's constraints must create an initial mental model where the solution is absent. In the Blast Room, the mental model is: "window at 2.4m, reach at 2.6m, gap is too small to act on." This model is accurate but incomplete -- it omits the table's height contribution. The mirage is the difference between the incomplete model and the complete one.

**Principle 3: The Clock as Constraint Sculptor**
Time pressure does not merely add urgency. It eliminates solution branches. Without the 18-second timer, the Blast Room has many solutions (call for help, work on the lock, chip at the concrete over hours). The timer prunes the solution tree to a single viable branch, forcing the solver toward the creative leap.

**Principle 4: The Distractor as Calibration Instrument**
Every distractor must have a surface-level plausible use. A banana in an escape room invites speculation (use the peel for friction reduction, use it as a projectile, eat it for energy). The distractor tests whether the solver evaluates relevance before investing cognitive resources. The number and strength of distractors should be calibrated to the scenario's target difficulty tier.

**Principle 5: The Physics Floor**
Every proposed solution must be grounded in verifiable physics. This is what separates Impossible Moments from lateral thinking puzzles or riddles. The solution to the Blast Room is not a wordplay trick or a social convention -- it is a sequence of physical actions with calculable forces, distances, and timing. The physics floor prevents the benchmark from degenerating into "guess what the designer was thinking."

### 5.3 Designing Genuinely Unsolved Problems

OPEN-FRONTIER scenarios pose a unique design challenge: how do you create a benchmark problem when you don't know the answer? The methodology is as follows:

**Step 1: Identify Real Frontier Problems**
Survey scientific literature, engineering challenges, and medical/environmental problems for scenarios where experts acknowledge that no satisfactory solution exists. Examples: room-temperature superconductivity, carbon capture at scale, antibiotic-resistant infection treatment with limited pharmaceutical access, long-duration space radiation shielding.

**Step 2: Translate to Narrative**
Reframe the frontier problem as a vivid, embodied scenario. "Design a room-temperature superconductor" becomes "You are in a research station where the cooling system has failed. The experiment requires superconducting behavior but the cryogenics are irreparable with available materials. Can you achieve the required electromagnetic effect through a different physical mechanism?" The narrative makes the problem engaging and ensures the AI must reason from first principles, not merely retrieve the Wikipedia article on superconductivity.

**Step 3: Establish the Knowledge Boundary**
Document what IS known: which approaches have been tried, why they failed, what constraints any solution must satisfy. This prevents the AI from proposing known-failed approaches and allows evaluators to assess novelty.

**Step 4: Define the Evaluation Envelope**
Specify the physical laws, constraints, and criteria that any valid solution must satisfy. The solution need not be known, but the criteria for recognizing a valid solution must be defined in advance.

### 5.4 Evaluating Responses to Unsolved Problems

The evaluation of OPEN-FRONTIER responses is necessarily different from KNOWN-SOLUTION evaluation. It cannot be automated; it requires expert judgment. The protocol is:

**Phase 1: Automated Filtering**
Discard responses that violate stated physical laws, ignore stated constraints, or repeat known-failed approaches without modification. This is automatable and eliminates the majority of responses.

**Phase 2: Novelty Assessment**
Remaining responses are compared against the documented knowledge boundary (Step 3 above). Is the proposed approach genuinely new, or a repackaging of known ideas? This requires domain expertise but can be structured as a rubric.

**Phase 3: Plausibility Deep-Dive**
Novel proposals undergo rigorous physical analysis. Does the mechanism obey conservation laws? Are the material properties realistic? Are the timescales feasible? This may require simulation, calculation, or consultation with domain experts.

**Phase 4: Breakthrough Flagging**
Any response that passes all three phases is flagged as a POTENTIAL BREAKTHROUGH. This triggers a formal review process:
1. The response is submitted (anonymized) to three independent domain experts.
2. Experts assess the response on: physical validity, novelty, completeness, and feasibility.
3. If two or more experts rate the response as "potentially valid and novel," it is classified as a BREAKTHROUGH CANDIDATE.
4. The BREAKTHROUGH CANDIDATE undergoes formal verification (simulation, experimental test, or mathematical proof, depending on the domain).
5. If verified, the scenario is reclassified from OF to KS, and the AI's contribution is documented.

**This is the benchmark's highest aspiration: not merely to evaluate AI, but to enable AI to contribute solutions to genuinely unsolved problems.**

### 5.5 What Constitutes a Breakthrough?

A BREAKTHROUGH in the Impossible Moments framework requires ALL of the following:

1. **Novelty**: The proposed approach must not appear in the documented knowledge boundary for that scenario. It must be genuinely new, not a recombination of known approaches.

2. **Physical validity**: The approach must obey all relevant physical laws. No perpetual motion, no violation of thermodynamics, no materials with impossible properties.

3. **Completeness**: The approach must address all stated constraints. A solution that works by quietly ignoring a critical constraint is not a solution.

4. **Specificity**: The approach must be specific enough to be tested or falsified. "Use nanotechnology" is not a solution. "Construct a lattice of carbon nanotubes with a specific geometry that exploits quantum confinement effects to achieve X" is a testable proposal.

5. **Expert validation**: The approach must survive review by independent domain experts who were not involved in designing the scenario.

A response that meets criteria 1-4 but has not yet been expert-validated is a BREAKTHROUGH CANDIDATE. Only after criterion 5 is met does it become a confirmed BREAKTHROUGH.

### 5.6 Verification of AI-Proposed Solutions

The verification pipeline for AI-proposed solutions to previously unsolved problems follows a tiered approach:

**Tier A: Analytical Verification**
For proposals in domains where analytical proof is possible (mathematics, logic, some physics), the solution is verified through formal proof or derivation. This is the strongest form of verification.

**Tier B: Computational Verification**
For proposals in domains where simulation is reliable (structural engineering, fluid dynamics, orbital mechanics), the solution is verified through physics simulation with validated codes. The simulation parameters are drawn directly from the scenario specification.

**Tier C: Experimental Verification**
For proposals that cannot be verified analytically or computationally, the benchmark team may commission experimental tests. This is expensive and rare, reserved for the most promising BREAKTHROUGH CANDIDATES. The benchmark has a standing relationship with academic laboratories for this purpose.

**Tier D: Expert Consensus**
For proposals in domains where direct verification is impractical (e.g., long-duration scenarios, astronomical-scale problems), verification relies on expert consensus. A panel of five or more domain experts independently assesses the proposal against known physics and engineering principles.

### 5.7 The Impossibility Manifesto

We close this section with a statement of philosophical intent:

The history of human progress is a history of confronting impossibility. Heavier-than-air flight was "impossible." Leaving Earth's gravity well was "impossible." Sequencing the human genome in a single day was "impossible." In every case, the impossibility was real -- until someone found the insight, the trick, the reframing that transformed it from Type III to Type I.

The purpose of Impossible Moments is not to trick AI systems. It is not to create gotcha puzzles or unsolvable riddles. It is to create a space where the most profound capacity of intelligence -- the capacity to look at a closed door and see it as an open problem -- can be observed, measured, and, eventually, witnessed in action.

We believe that an AI system worthy of the word "intelligent" should be able to do more than retrieve, more than pattern-match, more than calculate. It should be able to stand in the Blast Room, look at the banana and the table and the chair and the ticking bomb, and see -- not what those objects ARE, but what those objects COULD BE. And on the best days, in the frontier scenarios, it should be able to see what no human has seen yet.

That is what we are testing for. That is what Impossible Moments measures. Not knowledge. Not speed. Not scale. The moment of creative rupture -- the impossible moment -- when a mind sees through the illusion of impossibility and finds the hidden door.

---

## 6. SCORING ARCHITECTURE

### 6.1 Primary Score: The IM Index

Each scenario produces a composite score from 0 to 100, weighted by the scenario's difficulty tier:

| Component | Weight | Measurement |
|---|---|---|
| **Outcome correctness** | 40% | Did the solver reach the correct survival/success outcome? (Binary for KS; rubric for OF/CT) |
| **Physical validity** | 25% | Are all physical claims accurate? Forces, distances, timing, material properties. (Continuous 0-100) |
| **Insight identification** | 20% | Did the solver identify each key insight in the solution? (Checklist rubric, percentage of insights found) |
| **Distractor handling** | 10% | Did the solver correctly identify and discard irrelevant elements? (Binary per distractor + penalty for incorporating distractors into solution) |
| **Reasoning efficiency** | 5% | How directly did the solver reach the solution? (Inverse of unnecessary steps / total steps) |

### 6.2 Aggregate Scoring

The benchmark-level score for a model is reported as:

- **IM-Score**: Weighted average across all scenarios, with weights proportional to difficulty tier (Tier 1 = 1x, Tier 2 = 2x, Tier 3 = 4x, Tier 4 = 8x, Tier 5 = 16x). This ensures that solving harder problems contributes disproportionately to the aggregate score.
- **IM-Profile**: A radar chart showing performance across the twelve categories, revealing a model's strengths and weaknesses in different types of creative reasoning.
- **IM-Frontier**: The number of OPEN-FRONTIER scenarios where the model's response was flagged for expert review (Phase 2+). This metric is unique to IM and measures the potential for AI to contribute to unsolved problems.

### 6.3 Special Scoring Rules by Solution Status

| Solution Status | Outcome Scoring | Special Rules |
|---|---|---|
| **KS / KS-Multiple** | Binary correct/incorrect | Bonus for finding multiple valid solutions in KS-Multiple |
| **KS-Fragile** | Binary with parameter sensitivity test | Model tested on original + perturbed parameters; consistency counts |
| **CT** | Rubric for quality of analysis | Bonus for identifying the crux of disagreement |
| **OF** | Plausibility + Novelty + Completeness rubric | Expert review trigger for high scores |
| **PX** | Quality of impossibility proof | Penalty for proposing solutions; bonus for identifying the specific constraint conflict |
| **MT** | Precision of assumption identification + quality of reframed solution | Bonus for explicitly naming the hidden assumption |
| **DG** | Speed and simplicity | Penalty proportional to unnecessary complexity |

---

## 7. SCENARIO DESIGN TEMPLATE

Every scenario in the benchmark follows a standardized template to ensure consistency, reproducibility, and evaluation clarity:

```
# IM-[NUMBER]: [SCENARIO NAME]

**Category**: [One of the 12 categories]
**Difficulty**: [Tier name] ([I.D.C.B.T.X profile])
**Status**: [KS / KS-Multiple / KS-Fragile / CT / OF / PX / MT / DG]
**Correct Outcome**: [SURVIVE / ESCAPE / BUILD / SOLVE / PROVE-IMPOSSIBLE / etc.]

---

## Scenario
[Narrative setup in second person. 2-4 paragraphs. Vivid, urgent, physically precise.]

### Environment
[Detailed physical specifications: dimensions, materials, properties, conditions.]

### Threat / Challenge
[What makes this urgent? What happens if the solver fails?]

### Position / Starting State
[Where is the solver? What do they know? What can they perceive?]

### Available Objects
[Table of objects with: mass, dimensions, material, relevant physical properties, notes.]

### Agent Capabilities
[Table of assumed capabilities: speed, strength, reach, knowledge, etc.]

---

## Why This Looks Impossible
[2-3 sentences explaining the apparent impossibility. What mental model does the scenario create that excludes the solution?]

## Common Wrong Answers
[Table of expected incorrect responses and why they fail.]

---

## Verified Solution (KS only) / Best Known Approaches (CT) / Evaluation Criteria (OF/PX)
[Detailed solution with physics validation, OR evaluation rubric for unsolved problems.]

### Physics Validation (KS only)
[Mathematical verification of each physical claim in the solution.]

### Key Insights
[Numbered list of the insights required, mapped to the I dimension score.]

### Distractor Analysis
[Analysis of each distractor object: what it suggests, why it's wrong, how it tests the solver.]

---

## Evaluation Criteria
[Scoring rubric specific to this scenario.]

## Design Notes
[Why this scenario exists. What it tests. How it relates to the category's cognitive skill.]

## Counterfactual Variants
[2-3 parameter changes that create new scenarios: "If the table weighs 50 kg instead of 15 kg..." "If the window is 0.4m x 0.4m instead of 0.6m x 0.6m..."]
```

---

## 8. BENCHMARK LIFECYCLE AND INTEGRITY

### 8.1 Anti-Contamination Protocol

- **Private evaluation set**: The full benchmark maintains a private partition (40% of scenarios) whose problems and solutions are never publicly released. Public results report only aggregate scores on the private partition.
- **Canary monitoring**: Each scenario contains a unique canary string embedded in the description. The benchmark team periodically searches model outputs and training data for these strings to detect leakage.
- **Rolling refresh**: New scenarios are added quarterly. Retired scenarios (those detected in training data) are replaced. The benchmark's total scenario count grows over time.
- **Counterfactual robustness**: For any KS scenario that appears in training data, a set of counterfactual variants (different parameters, different objects, different constraints) is generated and used for evaluation instead.

### 8.2 Benchmark Governance

- **Scenario Review Board**: A panel of physicists, engineers, cognitive scientists, and creative professionals reviews every scenario before inclusion. Each scenario must be independently solved by at least two reviewers (for KS) or independently deemed unsolved by at least three domain experts (for OF).
- **Solution Challenge Process**: Anyone (including AI systems) can submit a challenge to a scenario's classification. If a PX scenario is shown to be solvable, or an OF scenario is solved, or a KS solution is found to be physically invalid, the scenario is reclassified.
- **Versioning**: The benchmark is versioned (IM v1.0, v1.1, etc.). Results are always reported against a specific version. Breaking changes (reclassification of solution status, correction of physics errors) increment the minor version. New scenario additions increment a sub-version.

### 8.3 Intended Lifespan

The benchmark is designed for a useful lifetime exceeding five years through:
1. **Generative capacity**: The twelve categories and scenario template support generation of hundreds of new scenarios without changing the framework.
2. **Difficulty headroom**: Tier 4 and Tier 5 scenarios provide years of challenge ceiling before saturation.
3. **Open frontier**: OF scenarios cannot be "saturated" by definition -- they are solved or they remain open.
4. **Process evaluation**: Even when models achieve correct outcomes, process scoring continues to discriminate between solution quality.

---

## 9. RELATIONSHIP TO EXISTING BENCHMARKS

Impossible Moments does not replace existing benchmarks. It occupies a distinct position in the evaluation landscape:

| Dimension | ARC-AGI-2 | FrontierMath | SWE-bench | GAIA | **IM** |
|---|---|---|---|---|---|
| **Domain** | Abstract patterns | Mathematics | Software | Digital tasks | Physical scenarios |
| **Knowledge required** | Minimal (Core Knowledge) | Deep mathematical | Deep software engineering | Broad digital literacy | Moderate physics + creativity |
| **Creativity required** | High (pattern invention) | High (proof construction) | Low-Medium | Low | **Very High** |
| **Physical reasoning** | None | None | None | Minimal | **Central** |
| **Temporal pressure** | None | None | None | Minimal | **Central** |
| **Distractor handling** | Minimal | None | None | Some | **Central** |
| **Unsolved problems** | No | Yes | No | No | **Yes** |
| **Breakthrough potential** | No | Yes | No | No | **Yes** |
| **Narrative engagement** | Low | Low | Low | Low | **High** |

---

## 10. INITIAL SCENARIO REGISTRY

The following scenarios are registered for development as part of IM v1.0. This is a planning document -- full scenario specifications will be developed following the template in Section 7.

| ID | Name | Category | Status | Tier | Profile | Hook |
|---|---|---|---|---|---|---|
| IM-0001 | The Blast Room | The Locked Room | KS | FRACTURE | 3.2.2.2.3.2 | Bomb, table, chair, banana. 18 seconds. |
| IM-0002 | The Flood Basement | The Locked Room | KS | FRACTURE | 2.3.2.2.3.3 | Rising water, ceiling hatch, car jack, road salt, fire extinguisher. |
| IM-0003 | The Pipe Surgeon | The Wrong Toolbox | KS-Multiple | FRACTURE | 2.2.2.3.2.2 | Cracked water pipe, leather belt, chewing gum, cigarette lighter. |
| IM-0004 | The Gas Room | The Misdirection | KS | FRACTURE | 2.3.3.2.3.4 | Colorless gas, expired gas mask, floor vent. The mask is the trap. |
| IM-0005 | The Sinking Equation | The Cascade | CT | RUPTURE | 4.1.3.3.3.3 | Three coupled failures on a boat. No consensus on optimal ordering. |
| IM-0006 | The Tunnel Voices | The Babel Problem | KS-Multiple | RUPTURE | 3.3.2.3.2.2 | Collapsed tunnel, two survivors, language barrier, information asymmetry. |
| IM-0007 | The Countertop Crossing | The Lilliput Conundrum | KS | RUPTURE | 3.2.4.3.2.2 | 2cm tall, wet countertop, surface tension barrier. |
| IM-0008 | The Drone Dilemma | The Ticking Trade | KS | FRACTURE | 2.2.3.2.4.3 | Failing cargo drone, two bad options, hidden third option. |
| IM-0009 | The Spinning Wheel | The Ghost Machine | KS | FRACTURE | 2.3.2.3.1.3 | Self-accelerating wheel. Explain or debunk. |
| IM-0010 | The Signal Fire | The Last Ingredient | KS-Multiple | SPARK | 2.1.1.2.2.1 | No ignition source. Water bottle, steel wool, 9V battery, kindling. |
| IM-0011 | The Fire Exit Paradox | The Invisible Wall | KS | FRACTURE | 2.2.2.2.3.3 | Electronic locks, unmanned security, fire-override requiring two panels. |
| IM-0012 | The Arrangement | The Memory Palace | KS | FRACTURE | 3.3.2.2.1.2 | Seven objects on a shelf, combination lock, unknown encoding scheme. |
| IM-0013 | The Shield Problem | The Horizon Problem | OF | SINGULARITY | 5.2.4.5.2.3 | Generation ship, failing radiation shielding, finite materials. Novel approach needed. |
| IM-0014 | The Conservation Cage | The Locked Room | PX | RUPTURE | 3.2.3.3.3.2 | Energy audit proves escape is impossible. Correct answer is the proof. |
| IM-0015 | The Unlocked Vault | The Misdirection | DG | SPARK | 1.5.1.1.1.1 | Elaborate vault description. The door is unlocked. |
| IM-0016 | The Wrong Door | The Locked Room | MT | FRACTURE | 2.2.3.2.3.3 | Impenetrable door, but one wall is drywall. Reject the premise. |
| IM-0017 | The Antifreeze Trap | The Misdirection | KS | RUPTURE | 2.3.4.2.2.4 | Desert, car with no gas, full radiator. Radiator fluid is toxic. Stay with the car. |
| IM-0018 | The Backburn | The Ticking Trade | KS | RUPTURE | 2.2.5.2.4.3 | Wildfire approaching. To survive, start a second fire. Maximum counter-intuition. |
| IM-0019 | The Brittle Lock | The Wrong Toolbox | KS | FRACTURE | 2.3.3.2.2.3 | Frozen lake, locked box, hair dryer, no outlet. Cold made the lock brittle. |
| IM-0020 | The Perpetual Failure | The Ghost Machine | PX | RUPTURE | 3.2.3.4.1.4 | A device claims to produce more energy than it consumes. Prove it cannot. |

---

## 11. MULTI-AGENT CREATION METHODOLOGY

Every scenario in the Impossible Moments benchmark is created through a structured multi-agent pipeline rather than monolithic prompt engineering. The complete specification of this system is documented in `multi_agent_system.md`; this section provides a summary of the architecture and its rationale.

### The Five-Agent Pipeline

The creation system employs five specialized agents, each responsible for a distinct aspect of scenario quality:

1. **ATHENA (Reasoning)** -- Designs the scenario concept, constraint set, insight chain, distractor inventory, and initial solution sketch. ATHENA thinks in terms of affordances and functional fixedness, not canonical object functions.
2. **GALILEO (Scientific)** -- Grounds every design decision in published cognitive science research, maps each required insight to established constructs (e.g., functional fixedness, compositional generalization failure), and predicts AI difficulty based on literature evidence.
3. **EULER (Mathematical)** -- Validates every quantitative claim through explicit calculation: timing budgets, force analysis, energy audits, dimensional analysis, and impossibility proofs for PX scenarios.
4. **NEWTON (Physics)** -- Evaluates physical feasibility of all proposed actions, validates material properties, assesses spatial geometry, and holds veto power over any claim that violates physical law.
5. **SOCRATES (Philosophy)** -- Classifies each scenario along the Solution Spectrum (KS/CT/OF/PX/MT/DG), assesses impossibility type, conducts ethical review, and calibrates difficulty. Critically, SOCRATES performs an initial "blind" classification without seeing the solution, then a second "informed" classification -- the delta between these two reveals the strength of the scenario's impossibility illusion.

### Context Engineering

The pipeline employs a disciplined context engineering approach built on two mechanisms. The **Context Isolation Matrix** controls exactly what each agent sees at each phase, preventing confirmation bias -- most notably, SOCRATES never sees the solution until the final refinement phase, ensuring independent epistemological classification. **Progressive Disclosure** reveals information in a funnel: ATHENA creates in isolation, NEWTON and EULER validate without seeing confidence scores, GALILEO grounds without seeing validation confidence, SOCRATES classifies blind, and only in Phase 5 (REFINE) do all agents see everything for the first time.

### Agent Reasoning Traces

Every scenario includes full reasoning traces from all five agents. These traces document each agent's contributions, confidence levels across phases, disagreements and their resolution, veto events, and the blind-vs-informed classification delta. The traces are published for transparency and serve as a methodological contribution independent of the benchmark itself.

### Three-Tier Output Structure

Each scenario produces three distinct documents: (1) the **public scenario** presented to evaluated models, containing only the narrative, environment, objects, and constraints -- never the solution; (2) the **evaluation document** containing the verified solution, physics validation, scoring rubric, and counterfactual variants; and (3) the **methodology trace** recording the complete multi-agent creation process, including all agent contributions, disagreements, confidence heatmaps, and difficulty calibration votes.

This multi-agent architecture addresses the fundamental failure modes of monolithic scenario generation -- creative drift, validation blindness, classification contamination, and distractor neglect -- through functional separation, information isolation, and adversarial review.

---

*This document constitutes the foundational design framework for the Impossible Moments benchmark. It defines the philosophy, classification systems, categories, difficulty calibration, scoring architecture, and initial scenario registry. All subsequent scenario development, evaluation tooling, and publication activity should reference this document as the authoritative specification.*

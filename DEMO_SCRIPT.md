# Impossible Moments -- Demo Script (3 Minutes)

### Anthropic x Cerebral Valley Claude Code Hackathon

**Presenter**: Muratcan Koylan
**Runtime**: 3:00 sharp
**Submit to**: cerebralvalley.ai/e/claude-code-hackathon/hackathon/submit
**Format**: Screen recording (YouTube / Loom / Google Drive)
**Repo**: Must be public on GitHub

---

## JUDGING CRITERIA (optimize for these)

| Criteria | Weight | Our angle |
|---|---|---|
| **Demo** | **30%** | Blast Room hook + live terminal proof |
| **Impact** | 25% | No benchmark tests creative reasoning; IM fills the gap |
| **Opus 4.6 Use** | 25% | 30+ parallel subagents = context window multiplier |
| **Depth & Execution** | 20% | 420 scenarios, physics-validated, full research foundation |

---

## PRE-RECORDING CHECKLIST

- [ ] GitHub repo is **public**
- [ ] Terminal open at repo root, font size 16pt+
- [ ] GitHub repo page open in browser for README/figures
- [ ] These commands pre-typed or ready to paste:
  - `find scenarios -name "IM-*.md" | wc -l`
  - `for d in scenarios/tier_*; do echo "$(basename $d): $(ls $d | wc -l)"; done`
  - `head -60 scenarios/tier_2_fracture/IM-0063.md`
  - `ls agents/ && wc -w agents/*.md`
  - `ls traces/IM-0001/`

---

## SCRIPT (3:00)

---

### BEAT 1: THE HOOK (0:00 - 0:30)

**[SCREEN: GitHub README -- the quote and badges visible]**

**[VOICEOVER]**

"You're locked in a concrete room. A bomb just activated -- 18-second timer. The door is steel, deadbolted from outside. The walls are reinforced concrete. There's one small window at 2.4 meters, but your max jumping reach is only 2.6 meters -- you can touch the glass but you can't pull yourself through in time. Your available objects: a wooden table, a steel folding chair, and a banana.

Do you live or die?

This is **Impossible Moments** -- a 420-scenario AGI benchmark for creative constraint satisfaction. Every scenario looks impossible. Every scenario has a physics-validated solution -- or is genuinely unsolved. And the entire thing was built by one person in a single Claude Code session with Opus 4.6."

---

### BEAT 2: WHAT IT IS + SCALE (0:30 - 1:10)

**[SCREEN: Terminal -- run the commands]**

```bash
find scenarios -name "IM-*.md" | wc -l
```
*(show: 420)*

```bash
for d in scenarios/tier_*; do echo "$(basename $d): $(ls $d | wc -l)"; done
```
*(show tier counts: 62, 163, 106, 73, 16)*

**[VOICEOVER]**

"420 scenarios across 5 difficulty tiers. Tier 1, Spark -- models should get 60-80% right. Tier 5, Impossible -- we expect under 2%. These aren't trivia questions. Each one has full physics validation, quantitative calculations, distractor analysis, and documented failure modes.

And it's not just physics -- we have business scenarios too. Liquidity crises, regulatory moats, supply chain collapses. Creative constraint satisfaction applies everywhere.

No existing benchmark tests this. MMLU tests knowledge. HumanEval tests code. GSM8K tests math. Nothing tests what happens when an AI stares at an impossible situation and has to *invent* the way out."

**[SCREEN: Quick scroll through IM-0063 to show depth and physics validation]**

```bash
head -60 scenarios/tier_2_fracture/IM-0063.md
```

"Every scenario has precise dimensions, material properties, human capability parameters, and at least four common wrong answers with explanations of why each fails."

---

### BEAT 3: HOW IT WAS BUILT -- OPUS 4.6 + CLAUDE CODE (1:10 - 2:20)

**[SCREEN: Show architecture diagram from README, then switch to terminal]**

**[VOICEOVER]**

"Here's how one person builds a 2.5-million-word benchmark in a single session.

I used Claude Code's **Task tool** to spawn **30+ parallel Opus 4.6 subagents**. Each agent got its own isolated context window, a reference scenario as a template, and a batch of 15 assignments. They all ran simultaneously in the background."

**[SCREEN: Show agent prompts]**

```bash
ls agents/ && wc -w agents/*.md
```

"Five specialized agents -- Athena for creative reasoning, Galileo for scientific validation, Euler for math verification, Newton for physics simulation, Socrates for epistemological classification. Each system prompt is 20,000+ words of encoded domain expertise. This is context engineering -- not generic prompts, but deep knowledge baked into every agent.

The key insight: **the Task tool is a context window multiplier**. 30 agents times 200K context each equals 6 million tokens of concurrent reasoning. That's how you generate 420 physics-validated scenarios in 30 minutes of wall time.

Then Bash plus Python for batch operations -- renumbering all 420 files sequentially by tier, generating the scenario registry, verifying zero gaps -- all in single script calls. Fast mode for rapid doc iterations. Auto-compaction to keep the session coherent across hours of work.

And the Ralph Wiggum philosophy -- iterate, don't perfect. Generate broadly, then refine. Each pass made it better without starting over."

**[SCREEN: Show reasoning traces]**

```bash
ls traces/IM-0001/
```

"Full multi-agent reasoning traces preserved. You can see exactly how each agent contributed to every scenario. Complete transparency."

---

### BEAT 4: IMPACT + CLOSE (2:20 - 3:00)

**[SCREEN: Show GitHub README -- scoring section with tier weights]**

**[VOICEOVER]**

"Why this matters beyond the hackathon: this benchmark is designed to be **unsaturable**. The creation pipeline is open source -- anyone can generate fresh scenarios that have never appeared in any training corpus. The tier-weighted scoring means harder problems matter exponentially more. And the Open Frontier scenarios? Those are genuinely unsolved. If an AI finds a solution, that's a real contribution to human knowledge, not just a benchmark score.

420 scenarios. 2.5 million words. Five specialized agents. Full physics validation. Complete documentation. Open source.

One person. One Claude Code session. Opus 4.6.

I'm Muratcan Koylan. This is **Impossible Moments**.

Oh -- and the answer to the Blast Room? You live. The table is a platform. Stand on it, swing the chair at the window, climb through, sprint away. 12 seconds. 6-second margin. The banana is irrelevant."

**[SCREEN: Fade on the repo]**

---

## RECORDING TIPS (for a 30% judging weight on demo)

1. **Energy in the first 10 seconds.** The bomb scenario hooks. Don't read it monotonously -- deliver it with urgency.
2. **Show real terminal output.** Every claim backed by a command. The judges want to see this is real, not slides.
3. **Pause on "context window multiplier."** This is your Opus 4.6 differentiator. Let it land.
4. **End on the Blast Room answer.** It's memorable, it's satisfying, it's a mic drop.
5. **Stay at 3:00.** Do NOT go over. Rehearse with a timer.
6. **Clean terminal.** Run `clear` before each command. Big font. No visual clutter.

---

## SUBMISSION CHECKLIST

- [ ] 3-minute video uploaded to YouTube/Loom/Google Drive
- [ ] GitHub repo is **public**: github.com/muratcankoylan/impossible-moments
- [ ] Project description written (use PROJECT_DESCRIPTION.md medium or full version)
- [ ] Submit at: cerebralvalley.ai/e/claude-code-hackathon/hackathon/submit
- [ ] Double-check video link is accessible (not private/restricted)

---

## IF YOU MAKE TOP 6 -- FINALS PREP (Feb 18, 12:00 PM ET)

**Judges**: Boris Cherny, Cat Wu, Thariq Shihpar, Lydia Hallie, Ado Kukic, Jason Bigman

**They will watch your video live and give reactions.** The video IS your finals presentation.

**Boris Cherny angle**: He formalized the Ralph Wiggum pattern. Call it out explicitly -- he'll appreciate seeing it applied at scale.

**Cat Wu angle**: She's the Claude Code product lead. The Task tool as context multiplier is a product insight she'd value.

**Key talking points if they ask questions**:
- "30 agents, 6 million tokens of concurrent context"
- "Physics-validated, not LLM-generated fluff"
- "Open Frontier scenarios -- the benchmark discovers new knowledge"
- "The creation pipeline is open source and renewable"

---

## BACKUP Q&A

**"How do you prevent contamination?"**
> Scenarios are procedurally generated through a multi-agent pipeline -- they don't exist in training data. The narrative structure is unique each time. And the pipeline is open source, so anyone can generate fresh scenarios.

**"Have you tested models on it?"**
> The evaluation protocol is complete and the scoring rubrics are defined. That's the next phase. This is an open invitation for the community.

**"What's the hardest scenario?"**
> IM-0420, The Biological Computer. Build a non-electronic computing system at the bottom of the ocean in 72 hours. It's Open Frontier -- we don't know if it's possible. If an AI solves it, that's a real contribution to computer science.

**"How much did it cost?"**
> Roughly 6.2 million tokens across all agents. The parallelization via Task tool made it feasible -- 30x faster wall time than sequential generation.

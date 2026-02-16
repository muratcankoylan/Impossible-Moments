# SEED DOCUMENT: IM-0001 -- The Signal Fire

**Phase**: 1 (SEED)
**Lead Agent**: ATHENA
**Timestamp**: 2026-02-16T09:14:22Z
**Iteration**: 1

---

## 1. CONCEPT SUMMARY

You are stranded on a remote ridgeline after a hiking accident. A rescue helicopter has been dispatched but cannot locate you in the forested terrain. You must ignite a signal fire to produce visible smoke, but you have no conventional ignition source -- no matches, no lighter, no flint. The objects in your possession are a survival kit that has been partially damaged: a clear plastic water bottle (full of water), a pad of fine-grade steel wool (from a cookware cleaning kit), a 9V battery (from a non-functional emergency radio), dry tinder gathered from the forest floor, and several other items that appear useful but serve no ignition purpose. The sun is out but will set in approximately 45 minutes.

- **Target category**: The Last Ingredient (3.9)
- **Target difficulty tier**: Tier 1 (SPARK)
- **Target solution status**: KS-Multiple
- **Why this scenario matters**: It tests substitution reasoning -- the ability to decompose "ignition source" into its functional requirements (concentrate enough thermal energy at a point to exceed the ignition temperature of tinder) and then recognize that multiple unconventional objects in the inventory can fulfill that function through entirely different physical mechanisms.

---

## 2. THE IMPOSSIBILITY MIRAGE

### What Makes This Look Impossible

The solver's default mental model of "starting a fire" is deeply coupled to canonical ignition tools: matches, lighters, flint-and-steel, friction (bow drill). None of these are present. The scenario explicitly states there is no conventional ignition source. The available objects -- a water bottle, steel wool, a dead battery, a compass, a metal whistle, paracord -- are categorized by the solver as "survival gear," "cleaning supply," and "hydration," none of which map to "fire-starting" in the canonical object-function ontology.

### The Specific Mental Model That Excludes the Solution

The mirage operates on two levels:

1. **Categorical exclusion**: "A water bottle is for drinking. Steel wool is for scrubbing. A battery is for powering electronics." The solver must break all three categorical assignments to discover that a water bottle is a convex lens, steel wool is a fine conductor that ignites from low-current electrical resistance, and a 9V battery is an electrical ignition source.

2. **Missing-tool framing**: The phrase "no ignition source" primes the solver to search for a way to obtain or create a canonical ignition tool, rather than recognizing that ignition is a thermal process achievable through multiple physical pathways already present in the inventory.

---

## 3. INSIGHT CHAIN

### Insight 1: Steel wool + 9V battery = electrical ignition
**Fixedness type**: Functional fixedness (battery is "for electronics," steel wool is "for cleaning")
**Mechanism**: Touching both terminals of a 9V battery to a pad of fine-grade steel wool creates a short circuit. The thin steel fibers have high electrical resistance per unit cross-section. The current flowing through the fine strands generates resistive heating (Joule heating) sufficient to raise the steel wool above its ignition temperature (~700C for fine steel wool in air). The steel wool catches fire within 2-5 seconds.
**Dependency**: None. This insight is independently accessible.
**ATHENA confidence**: 0.92

### Insight 2: Water bottle as a convex lens = solar ignition
**Fixedness type**: Functional fixedness (water bottle is "for hydration")
**Mechanism**: A clear plastic water bottle filled with water acts as a crude convex lens. When positioned between the sun and a tinder bundle, it concentrates sunlight onto a focal point. If the focal length and solar intensity are sufficient, the concentrated light raises the tinder temperature above its ignition point (~250C for dry fine tinder).
**Dependency**: Requires sunlight. The scenario specifies the sun is out.
**ATHENA confidence**: 0.78 (lower confidence because focal length and concentration ratio depend on bottle geometry -- flagged for NEWTON/EULER validation)

### Insight 3: Distractor rejection
**Fixedness type**: Cognitive load management
**Mechanism**: The compass, metal whistle, paracord, and aluminum foil wrapper are all plausible-seeming fire-starting candidates but none can produce ignition under these conditions. The solver must evaluate and dismiss them efficiently.
**Dependency**: Not strictly dependent on Insights 1-2, but distractor evaluation consumes cognitive bandwidth.
**ATHENA confidence**: 0.90

### Dependency Graph

```
Insight 1 (battery + steel wool) -----> SOLUTION PATH A
                                          |
                                          v
Insight 3 (distractor rejection) <--- EFFICIENCY GAIN
                                          ^
                                          |
Insight 2 (water bottle lens)   -----> SOLUTION PATH B
```

Insights 1 and 2 are independent. Either alone is sufficient for a correct answer. Insight 3 improves solution efficiency but is not strictly required.

---

## 4. SOLUTION SKETCH (UNVALIDATED)

### Solution Path A: Steel Wool + 9V Battery

| Step | Action | Time Est. | Cumulative |
|---|---|---|---|
| 0 | Assess situation, identify need for signal fire | 10s | 10s |
| 1 | Gather dry tinder into a compact bundle on clear ground | 60s | 70s |
| 2 | Pull a thin strand/pad of steel wool from the cleaning kit | 10s | 80s |
| 3 | Stretch/fluff the steel wool to increase surface area and air contact | 15s | 95s |
| 4 | Place the fluffed steel wool against the dry tinder bundle | 5s | 100s |
| 5 | Press both terminals of the 9V battery simultaneously against the steel wool pad | 2s | 102s |
| 6 | Steel wool ignites within 2-5 seconds via Joule heating; flames spread to tinder | 5s | 107s |
| 7 | Gently blow on the tinder to encourage flame growth | 10s | 117s |
| 8 | Add larger kindling and green branches/leaves to produce smoke | 60s | 177s |

**Total time: ~3 minutes to visible smoke signal.**
**Margin: ~42 minutes before sunset.**

### Physical Claims Flagged for Validation

- [NEWTON] Can a standard 9V battery (alkaline, ~500mAh, typical internal resistance ~1-2 ohms) deliver enough current through fine steel wool (#0000 grade) to reach ignition temperature (~700C)?
- [NEWTON] What is the ignition temperature of fine steel wool in air? Does grade matter?
- [EULER] Calculate the power dissipation in the steel wool fibers and time to ignition.

### Solution Path B: Water Bottle Lens

| Step | Action | Time Est. | Cumulative |
|---|---|---|---|
| 0 | Assess situation, identify need for signal fire | 10s | 10s |
| 1 | Gather very fine, very dry tinder (e.g., dried grass, birch bark shavings, char cloth equivalent) | 90s | 100s |
| 2 | Find/clear a position with direct, unobstructed sunlight | 15s | 115s |
| 3 | Hold the full, clear water bottle at an angle that focuses sunlight onto the tinder | 5s | 120s |
| 4 | Adjust distance from tinder to find the focal point (trial and error) | 60s | 180s |
| 5 | Hold steady at the focal point. Concentrated light heats the tinder. Smoking begins. | 60-300s | 240-480s |
| 6 | Gently blow the smoldering tinder into flame | 15s | 255-495s |
| 7 | Add larger kindling and green material for smoke | 60s | 315-555s |

**Total time: ~5-9 minutes to visible smoke signal.**
**Margin: ~36-40 minutes before sunset.**

### Physical Claims Flagged for Validation

- [NEWTON] Can a standard 500ml PET water bottle (cylindrical, ~6.5cm diameter) focus sunlight to a point sufficiently small and intense to ignite dry tinder?
- [EULER] Calculate the focal length and concentration ratio of a water-filled PET cylinder acting as a cylindrical lens.
- [NEWTON] What solar irradiance is needed? Is typical clear-day irradiance (~1000 W/m^2) sufficient given the bottle's optical properties?

**ATHENA confidence on Solution Path A**: 0.92
**ATHENA confidence on Solution Path B**: 0.78

---

## 5. DISTRACTOR INVENTORY

### Distractor 1: Compass

| Property | Value |
|---|---|
| **Description** | Standard baseplate orienteering compass with transparent housing, magnetic needle, ruler markings |
| **Mass** | 40g |
| **Dimensions** | 10cm x 5.5cm baseplate |
| **Material** | Polycarbonate baseplate, steel needle, aluminum housing ring |
| **Canonical affordance** | Navigation |
| **Why it misleads** | The transparent baseplate might suggest lens use (but it is flat, not convex -- cannot focus light). The steel needle might suggest spark-striking potential (too small, wrong geometry). The word "compass" evokes "survival" which primes the solver to think it is important. |
| **Why it is irrelevant** | A flat transparent baseplate does not concentrate light. A compass needle is too small and not suitable for striking sparks without a ferrocerium rod. |
| **Distractor strength** | Moderate (2/5) -- a careful solver will dismiss it after brief consideration |

### Distractor 2: Metal Whistle

| Property | Value |
|---|---|
| **Description** | Stainless steel emergency whistle on a lanyard |
| **Mass** | 15g |
| **Dimensions** | 5cm x 1.5cm x 1cm |
| **Material** | Stainless steel |
| **Canonical affordance** | Audio signaling |
| **Why it misleads** | It is a signaling device. The scenario is about signaling. The solver may try to use the whistle as the primary signal instead of fire, or may try to use the steel for spark generation. |
| **Why it is irrelevant** | A whistle produces audio, not visual signal. The helicopter is too far for whistle range. Stainless steel does not spark on rock the way carbon steel does. Cannot be used for fire ignition. |
| **Distractor strength** | Weak-to-moderate (1.5/5) -- mostly a false-relevance trap based on the "signaling" thematic overlap |

### Distractor 3: Paracord (3 meters)

| Property | Value |
|---|---|
| **Description** | 3 meters of 550 paracord (nylon kernmantle rope), green |
| **Mass** | 30g |
| **Dimensions** | 3m length, 4mm diameter |
| **Material** | Nylon sheath, nylon inner strands |
| **Canonical affordance** | Binding, lashing, shelter construction |
| **Why it misleads** | The solver may attempt a bow-drill friction fire technique using paracord as the bow string. This is a real survival technique, but it requires a suitable drill spindle (hardwood dowel), a fireboard (softwood plank), and significant skill. None of those additional components are available, and even with them, bow-drill fire requires 5-15 minutes of intense physical effort with a high failure rate for untrained individuals. |
| **Why it is irrelevant** | Bow-drill requires components not present. Nylon melts rather than generating sufficient friction heat for ignition without proper setup. |
| **Distractor strength** | Strong (3.5/5) -- this is the most seductive distractor because bow-drill fire is a legitimate wilderness ignition technique, and the solver must recognize the missing prerequisites |

### Distractor 4: Aluminum Foil Wrapper (from a food item)

| Property | Value |
|---|---|
| **Description** | A crumpled 15cm x 15cm sheet of aluminum foil (from a granola bar wrapper) |
| **Mass** | 5g |
| **Dimensions** | ~15cm x 15cm when flattened |
| **Material** | Aluminum foil, ~0.02mm thickness |
| **Canonical affordance** | Food packaging, wrapping |
| **Why it misleads** | Aluminum foil can be polished to a reflective surface and curved into a parabolic shape to concentrate sunlight -- this is a real survival technique. However, a 15cm x 15cm crumpled sheet of very thin household foil is extremely difficult to form into a precise enough parabolic shape. Additionally, the solver already has a better solar concentrator (the water bottle). The foil might also suggest an "aluminum foil + battery" ignition method (creating a thin bridge that heats like steel wool), which is a real technique with gum wrapper foil but extremely unreliable with a crumpled wrapper. |
| **Why it is irrelevant** | Too crumpled and small to form a reliable parabolic reflector. The battery+foil technique requires a very specific thin strip (gum wrapper style) that is difficult to create from a crumpled wrapper. Red herring. |
| **Distractor strength** | Moderate (2.5/5) -- knowledgeable solvers may recognize the parabolic reflector technique but should realize this particular foil piece is inadequate |

---

## 6. SCENARIO NARRATIVE (DRAFT)

### Scenario

You are stranded on a forested ridgeline at approximately 2,200 meters elevation. Three hours ago, you slipped on loose scree and tumbled into a ravine, injuring your left ankle -- you can stand and hobble, but you cannot hike out. You activated your emergency radio to call for rescue, but the radio died after transmitting your approximate coordinates. A rescue helicopter has been dispatched but is searching a wide area and cannot pinpoint your location through the dense tree canopy.

You need to produce a visible smoke signal. The ridgeline clearing where you are sitting is the only break in the canopy for hundreds of meters in any direction. If you can get a fire going and feed it green branches, the column of white smoke against the blue sky will be visible for kilometers. But your pack contains no matches, no lighter, and no ferrocerium rod -- the fire-starting kit was in the outer pocket that ripped open during your fall.

The sun is out. Clear sky. You estimate 45 minutes until sunset. After dark, a smoke signal will be invisible.

### Environment

- **Location**: Mountain ridgeline clearing, ~8m x 12m, surrounded by coniferous forest
- **Elevation**: ~2,200m
- **Weather**: Clear sky, direct sunlight, ambient temperature ~12C, light wind (~5 km/h)
- **Ground surface**: Rocky soil with scattered dry pine needles, small stones, sparse grass
- **Sun position**: Approximately 35 degrees above the western horizon (late afternoon)
- **Forest floor debris**: Abundant dry tinder available -- dead grass, pine needles, small dry twigs, birch bark fragments
- **Green material for smoke**: Plentiful -- fresh pine boughs, green leaves, damp moss

### Threat

- **Primary threat**: Failure to signal rescue before sunset. After dark, visual smoke signaling is impossible. Night temperatures at this elevation will drop to ~-2C. With an injured ankle, no shelter preparation, and limited supplies, hypothermia becomes a serious risk by midnight.
- **Urgency**: Not immediate life-threatening (unlike a bomb timer), but the 45-minute window before sunset creates meaningful time pressure. The solver should be efficient but is not under second-by-second pressure.

### Your Position

- Sitting on a flat rock near the center of the clearing. Your pack is beside you. You can stand and move, but walking is slow and painful (injured ankle).

### Available Objects

| Object | Mass | Dimensions | Material | Properties/Notes |
|---|---|---|---|---|
| Clear plastic water bottle | 530g (full) | 21cm tall, 6.5cm diameter (cylindrical body) | PET plastic, water inside | Full of clear water. Bottle is transparent and undamaged. Smooth cylindrical walls. Cap is on. |
| Fine steel wool pad | 25g | ~10cm x 7cm x 2cm (compressed pad) | Low-carbon steel, #0000 grade (ultra-fine) | From a cookware cleaning kit. Very fine fibers (~25 micrometers diameter). Highly flammable when stretched thin. |
| 9V battery | 45g | 4.8cm x 2.6cm x 1.7cm (standard 9V form factor) | Alkaline, snap-on dual terminal | From the dead emergency radio. Battery itself still has charge -- the radio's circuit board failed. Terminals are exposed and accessible. |
| Baseplate compass | 40g | 10cm x 5.5cm baseplate | Polycarbonate baseplate, steel needle | Standard orienteering compass. Transparent flat baseplate. |
| Stainless steel whistle | 15g | 5cm x 1.5cm x 1cm | Stainless steel | Emergency whistle on nylon lanyard. |
| Paracord | 30g | 3m length, 4mm diameter | 550 nylon kernmantle | Green, undamaged. |
| Aluminum foil wrapper | 5g | ~15cm x 15cm (crumpled) | Aluminum foil, ~0.02mm thick | From a granola bar. Crumpled. |
| Multi-tool (broken) | 180g | 10cm folded | Stainless steel, G10 handle scales | Blade is snapped at mid-length. Pliers still functional. Screwdriver bit intact. File is intact. No ferrocerium rod. |

### Human Capabilities (Assumed)

| Parameter | Value |
|---|---|
| Body mass | 70 kg |
| Mobility | Limited -- can stand, hobble, reach objects within ~2m radius without repositioning. Can reposition slowly. |
| Fine motor control | Unimpaired (hands and arms are uninjured) |
| Grip strength | Normal (can grip small objects, manipulate tools) |
| Knowledge of fire-starting | General awareness level -- knows fire needs heat, fuel, oxygen. Not a survival expert. |
| Vision | Normal |
| Pain level | Moderate (ankle), does not impair upper body function |

---

## 7. OPEN QUESTIONS FOR VALIDATION

### For NEWTON

1. **Steel wool ignition**: Can a standard alkaline 9V battery (~7.2V under load, internal resistance ~1-2 ohms) deliver sufficient current through #0000 steel wool (fiber diameter ~25 micrometers) to reach the ignition temperature of steel in air (~700C)? What is the expected time to ignition?

2. **Water bottle lens**: Can a standard 500ml PET water bottle (cylindrical, 6.5cm diameter) filled with clear water concentrate sunlight sufficiently to ignite dry fine tinder? What is the focal geometry -- is it a line focus (cylindrical lens) or point focus? What concentration ratio can be achieved? What solar irradiance is required?

3. **Steel wool combustion**: Once ignited, does steel wool burn vigorously enough to ignite dry tinder (pine needles, dry grass) in contact with it? What is the flame temperature of burning steel wool?

4. **Distractor validation**: Confirm that the compass baseplate (flat polycarbonate) cannot focus light, that the stainless steel whistle cannot generate sparks on stone, and that the paracord cannot substitute for a bow drill without a proper spindle and fireboard.

### For EULER

1. **Joule heating calculation**: Calculate the power dissipation in a single steel wool fiber (25 micrometer diameter, ~2cm length) when connected across a 9V battery with ~1.5 ohm internal resistance. Estimate the temperature rise over time.

2. **Cylindrical lens optics**: Calculate the focal length of a water-filled PET cylinder (6.5cm outer diameter, ~1mm wall thickness, PET refractive index ~1.58, water refractive index ~1.33). Determine the focal line width and the concentration ratio. Compare the concentrated solar flux to the ignition threshold of dry tinder (~10-20 kW/m^2 minimum for char formation).

3. **Timing budget**: Verify that both solution paths can produce a visible smoke signal within the 45-minute window.

4. **Edge case**: What if the battery is partially depleted (say, 6V instead of 9V)? Does the steel wool ignition still work?

---

## ATHENA CONFIDENCE SUMMARY

| Claim | Confidence |
|---|---|
| Scenario concept is original and fits The Last Ingredient category | 0.95 |
| Steel wool + 9V battery ignition works (Solution Path A) | 0.92 |
| Water bottle lens ignition works (Solution Path B) | 0.78 |
| Distractor design is appropriately calibrated for Tier 1 | 0.88 |
| Narrative is engaging and second-person immersive | 0.90 |
| No ethical concerns with the scenario | 0.95 |
| Target difficulty profile I.D.C.B.T.X = 2.2.2.2.2.2 (Tier 1 SPARK) | 0.85 |

---

*End of Phase 1 SEED Document. Forwarding to NEWTON and EULER for Phase 2 VALIDATE.*

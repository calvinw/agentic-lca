# Skill Recommendations — Elementary LCA Skills for Beginners

## How Skills Work

Skills are stored in `.skillshare/skills/<skill-name>/SKILL.md`. When a student types `/functional-unit wool_yarn`, the skill named `functional-unit` is loaded and `wool_yarn` is passed as the argument.

The skill instructs the AI to:
1. Read the relevant file(s) from `skills_references/wool_yarn/`
2. Apply a fixed pedagogical sequence using data from those files
3. Ask Socratic questions based on the actual numbers in the case study

The skill file never contains product-specific facts. All product knowledge lives in the `skills_references/` folders. This means:
- New case studies are immediately available to all skills without editing the skill
- Updating a recipe card automatically updates what the skill teaches
- Skills stay short and maintainable

## Invocation Pattern

```
/<skill-name> <case-study-name>
```

Examples:

```
/functional-unit wool_yarn
/functional-unit polyester_tshirt
/supply-chain cotton_fiber
/scaling-vector wool_yarn
/lcia-method cotton_fiber
/damage-pathway cotton_fiber
/hotspots polyester_tshirt
```

Case study names correspond to folder names in `skills_references/`.

---

Recommended order for a student with no science or coding background.
Skills already built are marked ✅. Skills recommended but not yet built are marked ⬜.

---

## Recommended Learning Path

| Order | Skill | Status | What it teaches |
|---|---|---|---|
| **Introduction** | | | |
| 1 | `what-is-lca` | ✅ Built | What LCA is, why fashion professionals need it, the four phases |
| **Phase 1 — Goal & Scope** | | | |
| 2 | `goal-and-scope` | ✅ Built | Why the study is being done, who it is for, what is included or excluded |
| 3 | `system-boundary` | ✅ Built | Every study has edges — what is inside gets counted, what is outside does not |
| 4 | `life-cycle-stages` | ✅ Built | The named boundary types — cradle to gate, cradle to grave, cradle to cradle, gate to grave |
| 5 | `functional-unit` | ✅ Built | The precise definition of what is being measured |
| **Phase 2 — Life Cycle Inventory** | | | |
| 6 | `supply-chain` | ✅ Built | How to read a product graph, what processes and flows are |
| 7 | `scaling-vector` | ✅ Built | How much each process in the supply chain must run to deliver one functional unit |
| 8 | `technosphere-and-ecosphere` | ✅ Built | The difference between human-made flows (products) and natural flows (emissions, resources) that cross into the natural world |
| 9 | `life-cycle-inventory` | ✅ Built | What an inventory is, how emissions and resource use are collected and totalled across all processes |
| 10 | `allocation` | ⬜ Recommended | What to do when a process produces more than one useful output — how to divide the environmental burden fairly between co-products |
| **Phase 3 — Impact Assessment** | | | |
| 11 | `what-is-impact-assessment` | ⬜ Recommended | How raw inventory emissions are converted into environmental scores — global warming, acidification, smog, and more |
| 12 | `impact-characterization` | ⬜ Recommended | How each emission is multiplied by a characterization factor to produce an impact score — the maths behind the conversion |
| 13 | `damage-characterization` | ⬜ Recommended | How midpoint impact scores are translated into damage to human health, ecosystems, and natural resources |
| 14 | `normalization-and-weighting` | ⬜ Recommended | How to convert impact scores to a common scale so you can add them up into a single score — and why that's controversial |
| **Phase 4 — Interpretation** | | | |
| 15 | `hotspot-analysis` | ⬜ Recommended | How to read a contribution breakdown, identify the biggest sources of impact, connect to business decisions |
| 16 | `sensitivity-analysis` | ⬜ Recommended | How to test whether results change when you swap an assumption — key for credibility and for understanding what really drives the score |
| 17 | `uncertainty` | ⬜ Recommended | Why LCA numbers are ranges, not precise values; Monte Carlo basics in plain language |
| 18 | `comparing-products` | ⬜ Recommended | How to set up a fair comparison between two products, when comparisons are misleading |
| 19 | `interpretation` | ⬜ Recommended | The final LCA phase — checking whether results are trustworthy, identifying what drives them, and turning the numbers into a business recommendation |

---

## Operational Skills (outside the learning path)

These skills are built and working but are tools for running analyses, not teaching concepts. They are not part of the student learning sequence above.

| Skill | What it does |
|---|---|
| `run-lca` | Runs the full LCA pipeline for a case study — sends the recipe card to openLCA, saves results and diagrams |
| `lca-from-url` | Builds a recipe card from a published LCA study URL or well-known study name, then offers to run it |
| `skill-creator` | Creates, edits, and evaluates skills; runs evals and benchmarks skill performance |

---

## All Skills — Detail

### Introduction

### `what-is-lca` ✅
The entry point for every student. Explains what Life Cycle Assessment is, why it
matters to fashion and retail professionals, and previews the four phases (goal and
scope, inventory, impact assessment, interpretation). No case study argument — this
skill stands alone as a brief, engaging introduction before any supply chain data
is introduced.

**Key insight for students:** LCA is not a scientific exercise for engineers — it is
a business decision tool. Knowing the carbon footprint of a product is only useful
if it changes what you buy, make, or sell.

---

### Phase 1 — Goal & Scope

### `goal-and-scope` ✅
Covers the opening decisions in every LCA study: why it is being done, who it is for,
and what is included or excluded. Students learn that these choices are not neutral —
they shape every number that comes out at the end. Uses a case study to show how two
studies of the same product can reach different conclusions if their goals and scopes
differ.

**Key insight for students:** The goal and scope section is the most important part of
any LCA report — it tells you whether you can trust the numbers and whether they are
relevant to your question.

---

### `system-boundary` ✅
The most basic idea in LCA, explained without any technical vocabulary. Every study
has to decide what to include and what to leave out — and whatever is left out does
not get counted, no matter how significant it might be. Uses a simple everyday analogy
(a shopping receipt that only covers certain items) to make the idea feel obvious, then
shows how the same principle applies to a supply chain diagram. Students practise
pointing to what is inside and outside the boundary using the product graph.

Short, visual, and conversational. No science required. Four to five exchanges to complete.

**Key insight for students:** A study can only tell you about what is inside its
boundary. If something is left out, the number you get at the end is incomplete —
and knowing what was left out is just as important as knowing what was included.

---

### `life-cycle-stages` ✅
Once students understand that a study has a boundary, the natural next question is:
*where do researchers typically draw it?* Introduces the four named boundary types
used across the fashion and retail industry, using plain-English descriptions and
concrete product examples for each:

- **Cradle to gate** — from raw material in the ground to the factory exit. Stops
  before the product is sold. Most supplier certifications use this scope because
  they can only control what happens on their side of the gate.
- **Cradle to grave** — the full life of the product, from raw material all the way
  through to the customer disposing of it. Used when the use phase matters — for
  example, comparing fast fashion (washed frequently, short life) to a premium
  garment (washed less, lasts years).
- **Cradle to cradle** — same as cradle to grave but the end-of-life loops back into
  production as recycled material. Used for circular economy and recycled content
  claims (e.g. recycled polyester from plastic bottles).
- **Gate to grave** — starts at the warehouse or retail store and ends at disposal.
  Used when production is already fixed and the question is purely about what happens
  after purchase — for example, comparing delivery packaging options.

Uses a single product (a T-shirt or a pair of jeans) and shows how the same product
gets a very different footprint number depending on which boundary is chosen.

**Key insight for students:** The same product can have four different carbon footprint
numbers depending on where the boundary is drawn. When comparing two studies, always
check that they use the same boundary type — otherwise the comparison is meaningless.

---

### `functional-unit` ✅
The precise definition of what is being measured. Students learn that a functional unit
is not just "a shirt" but "one shirt worn 50 times before disposal" — and that changing
the functional unit changes the entire comparison. Uses a case study to practise writing
a functional unit and spotting when one has been defined poorly.

**Key insight for students:** If two studies use different functional units, their
numbers cannot be directly compared — even if they are studying the same product.

---

### Phase 2 — Life Cycle Inventory

### `supply-chain` ✅
How to read a product graph: what the boxes (processes) represent, what the arrows
(flows) represent, and how to trace a path from raw material to finished product.
Introduces the vocabulary of processes and flows without any maths. Students practise
reading the diagram for a real case study and identifying which step they think
contributes the most impact before the numbers are revealed.

**Key insight for students:** Every product has a supply chain. LCA makes that supply
chain visible — and that visibility is what makes it possible to find where the
biggest environmental problems are hiding.

---

### `scaling-vector` ✅
How much each process in the supply chain must run to deliver exactly one functional
unit. Students work through the calculation using plain division, not matrix algebra —
starting from the finished product and working backwards through the supply chain to
find how much of each upstream process is needed. Uses a real case study with actual
numbers.

**Key insight for students:** A factory doesn't always run at full capacity to make
one shirt. The scaling vector tells you the exact fraction of each step that is needed
— and that fraction is what drives the final impact number.

---

### `technosphere-and-ecosphere` ✅
The supply chain lives entirely in the human-made world (the technosphere — factories,
farms, energy grids, products). The natural world (the ecosphere — air, water, soil,
climate) sits outside it. LCA is really about what *crosses the boundary between the
two*: emissions flow out of the technosphere into the ecosphere, and natural resources
flow in. These crossing flows are called **elementary flows**, and they are the only
things LCA counts as environmental impact. A product moving from one factory to another
stays inside the technosphere and is never counted as an environmental impact.

Uses the wool yarn or cotton fiber case study to show students which flows cross the
boundary (CO₂ to air, CH4 to air, Water) and which do not (raw wool moving from farm
to mill).

**Key insight for students:** Not all flows in a supply chain cause environmental
damage — only the ones that cross into the natural world. Understanding this boundary
is what separates an impact from a transaction.

---

### `life-cycle-inventory` ✅
Once students understand what flows cross the boundary between the technosphere and the
ecosphere, the next question is: *how do you actually count them?* This skill would
introduce the life cycle inventory (LCI) — the process of collecting and totalling all
the emissions and resource uses across every step in the supply chain. Students would
see how the individual emissions from each process (farm, mill, factory) are added
together, weighted by the scaling vector, to produce a single inventory table.

**Key insight for students:** The inventory is the raw data behind every LCA result.
Before any environmental score is calculated, someone has to add up every kilogram of
CO₂, methane, and water used across the entire supply chain — that list is the inventory.

---

### `allocation` ⬜
Many industrial processes produce more than one useful output. A sheep farm produces
both wool and meat. An oil refinery produces petrol, diesel, jet fuel, and plastics
all at once. A cotton gin produces lint and cottonseed. When you are studying just
one of those outputs — say, wool — you still have to decide how much of the farm's
total environmental burden belongs to the wool and how much belongs to the meat.
This is called **allocation**.

There is no single correct answer, and ISO 14044 provides three approaches, each
with different implications:

- **Mass allocation** — divide the burden in proportion to the physical mass of each
  co-product. Simple but often misleading when co-products have very different economic
  value (a gram of saffron versus a tonne of straw).
- **Economic allocation** — divide by the market value of each co-product. Reflects
  economic reality but makes results sensitive to price fluctuations.
- **System expansion** — instead of dividing, expand the system boundary to include
  the alternative product the co-product replaces, and subtract its burden. Avoids
  arbitrary splitting but makes the study more complex.

Students work through a simple two-output example (wool + meat, or cotton lint +
cottonseed) using all three methods and see how the allocated footprint for the
primary product changes depending on which method is chosen.

**Key insight for students:** The same farm, with the same real-world emissions, can
appear to have a wool footprint of 3.2 kg CO₂ eq or 1.8 kg CO₂ eq depending purely
on the allocation method chosen. This is one of the biggest sources of disagreement
between competing LCA studies of the same product.

---

### Phase 3 — Impact Assessment

### `what-is-impact-assessment` ⬜
Once students understand the inventory — the raw list of kilograms of CO₂, methane,
water, and other emissions — the next question is: *what does that list actually mean
for the environment?* This skill introduces life cycle impact assessment (LCIA), the
phase that converts the inventory into a set of environmental scores. Students learn
that raw emissions are translated into categories like global warming, acidification,
smog formation, and water use using a standardised method (in this course, TRACI 2.2).
They also learn why different emissions get different weights — a kilogram of methane,
for example, is counted as 28 times more damaging to the climate than a kilogram of
CO₂.

Uses a case study to show students the before (the inventory table) and the after (the
TRACI 2.2 impact scores), and asks them to explain in plain language what each category
means for a fashion brand.

**Key insight for students:** Raw emissions data — kilograms of CO₂, grams of methane —
cannot be directly compared or interpreted on their own. Impact assessment translates
that list into a small set of scores that each answer a specific environmental question,
making the results usable by decision-makers who are not chemists.

---

### `impact-characterization` ⬜
Once students understand that impact assessment converts raw emissions into environmental
scores, the next question is: *how exactly does that conversion work?* This skill zooms
in on the calculation itself — characterization. Students learn that every emission in
the inventory (for example, 1 kg of methane) is multiplied by a number called a
characterization factor, which expresses how damaging that substance is relative to a
reference substance. For global warming, everything is compared to CO₂, so methane's
factor is 28 — meaning 1 kg of methane counts as 28 kg of CO₂ equivalent in the final
score.

Students work through a small example by hand: take an emission from the inventory,
look up its characterization factor from TRACI 2.2, multiply, and see how the raw kg
figure becomes an impact score. The skill then shows how all the emissions across every
impact category are summed to produce the full TRACI 2.2 results table.

**Key insight for students:** Characterization factors are what make it possible to
add up apples and oranges — CO₂ and methane and nitrous oxide — into a single number
per impact category. Without them, a list of emissions is just a list. With them, it
becomes a score a business can act on.

---

### `damage-characterization` ⬜
Once students understand how emissions are converted into midpoint impact scores (global
warming, acidification, smog), the next question is: *what do those scores actually do
to the world?* Damage characterization is the step that answers this by going one level
deeper — converting midpoint scores into damage to three areas of protection that people
genuinely care about:

- **Human health** — measured in disability-adjusted life years (DALYs): how many years
  of healthy human life are lost due to disease, injury, or premature death caused by
  the pollution.
- **Ecosystem quality** — how many species in how large an area are harmed or lost.
- **Resource availability** — how much harder it becomes to extract natural resources
  in the future because of what was consumed today.

Students learn that midpoint scores (like "28 kg CO₂ eq of global warming") are still
one step removed from real-world harm — damage characterization is what closes that gap.
Uses a case study to show how the TRACI 2.2 midpoint scores map to damage indicators,
and asks students to explain in plain language which type of damage matters most for a
fashion brand's stakeholders.

**Key insight for students:** A global warming score in kg CO₂ eq tells you how much
warming pressure a product creates — but a damage score tells you what that warming
actually does to people and nature. For communicating with customers, investors, or
regulators, damage scores are often more powerful because they are expressed in human
terms, not chemistry terms.

---

### `normalization-and-weighting` ⬜
Once students understand that TRACI 2.2 (or any LCIA method) produces multiple impact
scores — global warming, acidification, smog, eutrophication, and others — a natural
question arises: *can I add these up into a single number?* Normalization and weighting
are the two steps that attempt to do this.

**Normalization** converts each impact score to a fraction of a reference value —
for example, dividing by the average European person's annual global warming impact.
This puts all the different scores on a common, dimensionless scale so they can be
compared.

**Weighting** then multiplies each normalized score by a factor that reflects how
important society considers that impact category to be. Is a 1-unit increase in
eutrophication more or less serious than a 1-unit increase in carcinogen exposure?
Weighting requires a value judgement.

The skill teaches students to understand what normalization and weighting do, why
they are sometimes used, and — critically — why they are controversial. The ISO LCA
standards flag weighting as a step that involves subjective values, not science, and
prohibit it in comparative assertions intended for public communication. A single
aggregated score can hide important trade-offs.

**Key insight for students:** A single environmental score for a product sounds
simple and useful — but it requires someone to decide that climate change is, say,
twice as important as water use. That is a political choice, not a scientific one.
Always ask what was weighted and by whose values.

---

### Phase 4 — Interpretation

### `hotspot-analysis` ⬜
Once students have results, the next natural question is: *which part of the supply
chain is the problem?* This skill would teach how to read a contribution breakdown
table, identify the biggest hotspot, and connect that to a practical business
recommendation — for example, if 86% of a garment's footprint comes from the sheep
farm, that is where improvement efforts should be focused.

**Key insight for students:** LCA results are most useful when they tell you *where
to act*, not just *how bad it is*.

---

### `sensitivity-analysis` ⬜
After students have a complete set of LCA results, a natural question arises: *how
much do I trust these numbers?* Every LCA study rests on dozens of assumptions —
the amount of electricity used at a mill, the methane factor for a specific breed
of sheep, whether transport is included or not. Sensitivity analysis is the systematic
practice of changing one assumption at a time and checking whether the conclusion
changes. If the result flips from "wool is better" to "polyester is better" when you
change one number by 10%, the study is not credible. If the conclusion holds across a
wide range of plausible values, it is robust.

Students work through a simple example: take one key number from a case study
(e.g. the methane emission factor for sheep), vary it within a plausible range,
and watch what happens to the global warming score. The skill teaches students to
identify which assumptions are load-bearing and which barely matter.

**Key insight for students:** A result without a sensitivity check is an opinion,
not an analysis. Knowing which assumptions drive the result is just as important
as knowing the result itself.

---

### `uncertainty` ⬜
Closely related to sensitivity analysis but broader: this skill addresses why LCA
numbers should always be understood as ranges rather than precise point values.
Every input to an LCA — an emission factor, a transport distance, a production
yield — has uncertainty attached to it. When you multiply and combine many uncertain
numbers, the uncertainty in the final result can be substantial.

Monte Carlo simulation is the standard way to quantify this: the calculation is run
thousands of times, each time drawing random values for every uncertain input from
a probability distribution. The result is not a single number but a distribution —
for example, "the global warming score is 2.1 kg CO₂ eq with a 95% confidence
interval of 1.6 to 2.9." Students learn to read and interpret uncertainty ranges
in plain language, without needing to understand the statistics in detail.

**Key insight for students:** When a company says "our product has a carbon footprint
of exactly 1.83 kg CO₂ eq", treat that precision with scepticism. The real answer
is always a range, and a reputable study will tell you how wide that range is.

---

### `comparing-products` ⬜
The capstone beginner skill. Once students understand functional unit, system
boundary, and how to read results, they are ready to compare two products side by
side. This skill would walk through a structured comparison (e.g. wool yarn vs
polyester yarn), show how the functional unit and scope must match before any
comparison is valid, and teach students to spot when a comparison is being set up
unfairly.

**Key insight for students:** Two products can only be fairly compared if they are
measured per the same functional unit, over the same system boundary. Without that,
any comparison can be gamed.

---

### `interpretation` ⬜
The capstone of the entire LCA learning path. By this point students have set a goal
and scope, built an inventory, run impact and damage characterization, identified
hotspots, and compared products. Interpretation is the phase where they stop calculating
and start deciding — asking three questions about the results in front of them:

1. **Are these results trustworthy?** — Does the study cover everything it promised in
   the goal and scope? Were any important emissions missing? Are the numbers consistent
   with what we would expect? Students learn to read a result critically before acting
   on it.

2. **What is driving the result?** — Which single step, material, or emission is
   responsible for the most damage? Students practise identifying the one lever that,
   if changed, would have the biggest effect on the footprint.

3. **What should we recommend?** — Given what the numbers show, what is the practical
   advice for a brand, buyer, or supplier? Switch to renewable energy at the mill?
   Source wool from a lower-methane farm? Redesign the product for a longer life?

Uses a complete case study result — inventory, impact scores, damage scores, hotspot
breakdown — and asks students to write a short interpretation paragraph as if briefing
a sustainability manager.

**Key insight for students:** Numbers on their own do not make decisions — people do.
Interpretation is the skill that turns a table of CO₂ figures into a sentence a
business can act on. It is the reason LCA exists.

---

## Notes

- All skills follow the same Socratic five-step structure: open with a real-world
  question, validate the student's answer, introduce the concept, ask a what-if
  question, connect to a business decision.
- Skills that use a case study argument read from `skills_references/<case_study>/recipe_card.md`.
- `what-is-lca` is the only skill with no case study argument.
- Sessions should be saved to `skills_sessions/` using the naming convention:
  `{skill-name}-{arg}-v{version}-{student}-{model}-session{n}.md`
  For `what-is-lca` (no case study argument), omit `{arg}`:
  `{skill-name}-v{version}-{student}-{model}-session{n}.md`

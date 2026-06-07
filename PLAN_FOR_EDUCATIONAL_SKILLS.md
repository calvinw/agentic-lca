# Plan for Educational LCA Teaching Skills

## Purpose

This document defines the set of teaching skills that walk FIT students through
the methodology of Life Cycle Assessment (LCA) using real case study data.

Each skill is an AI-powered interactive lesson. A student invokes a skill with
a case study name as the argument, and the AI reads the reference files for that
product and teaches the concept using real numbers, Socratic questions, and
business-relevant examples.

---

## How Skills Work

Skills are stored in `.skillshare/skills/<skill-name>/SKILL.md`. When a student
types `/functional-unit wool_yarn`, the skill named `functional-unit` is loaded
and `wool_yarn` is passed as the argument.

The skill instructs the AI to:
1. Read the relevant file(s) from `skills_references/wool_yarn/`
2. Apply a fixed pedagogical sequence using data from those files
3. Ask Socratic questions based on the actual numbers in the case study

**The skill file never contains product-specific facts.** All product knowledge
lives in the `skills_references/` folders. This means:
- New case studies are immediately available to all skills without editing the skill
- Updating a recipe card automatically updates what the skill teaches
- Skills stay short and maintainable

---

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

## The Six Skills

The skills follow the natural structure of an LCA study — from defining the
question through to interpreting the results.

---

### 1. `functional-unit`

**LCA phase:** Goal and scope definition

**What it teaches:**
- What a functional unit is and why it must be precisely defined
- Why the choice of unit can completely change which product looks better
- How to connect the functional unit to a real business or purchasing decision

**Files read:** `recipe_card.md` (functional_unit, goal, name fields)

**Teaching sequence:**
1. Ask the student how they would measure this product's impact before revealing the answer
2. Reveal the functional unit from the recipe card with its exact description and amount
3. Explain why that unit was chosen over obvious alternatives
4. Ask a "what if a different unit was used?" question to show how the choice matters
5. Connect to a retail or sourcing context

**Case study angles:**
- Wool yarn: "per kg of yarn" — why not per garment, per wash, per year of wear?
- Polyester T-shirt: "per T-shirt" — what about per kg of fiber, or per year of use?
- Cotton fiber: "per kg of fiber" — how does this compare to measuring per garment?

---

### 2. `supply-chain`

**LCA phase:** System boundary and process tree

**What it teaches:**
- How to read a supply chain diagram (the product graph)
- What each box (process) represents and what flows connect them
- What "upstream" and "downstream" mean in a supply chain
- Why the system boundary matters — what is included and what is left out

**Files read:** `recipe_card.md` (processes, products, elementary_flows),
`product_graph_structure.svg` (reference to open in VS Code)

**Teaching sequence:**
1. Direct the student to open `product_graph_structure.svg`
2. Walk through each process box — what does it represent in the real world?
3. Walk through each arrow — what is flowing from one process to the next?
4. Ask: which process is the starting point (reference), which are upstream?
5. Ask: what is NOT in this diagram that you might expect? (system boundary discussion)
6. Connect to how a supply chain manager would use this map

**Case study angles:**
- Wool yarn: farm → scouring → spinning; what about transport? sheep feed? land use?
- Polyester T-shirt: oil well → fiber plant → garment factory; two hops from crude oil to clothing
- Cotton fiber: fertilizer plant → cotton field; why is the field the reference, not the garment?

---

### 3. `scaling-vector`

**LCA phase:** Life Cycle Inventory (LCI) — solving the system

**What it teaches:**
- What the scaling vector is: how much each process must run to deliver exactly
  one functional unit
- Why upstream processes run at less than 1 (or more than 1 due to waste factors)
- How the matrix inversion works conceptually (without algebra)
- The difference between 1-layer and 2-layer scaling (compound upstream calculation)

**Files read:** `recipe_card.md` (processes, inputs, waste factors),
`lca_results.md` (scaling vector s, technology matrix A)

**Teaching sequence:**
1. Ask: "if you need to make 1 kg of yarn, how much raw wool do you think the farm needs to produce?"
2. Reveal the scaling factor from lca_results.md — is the student's guess right?
3. Explain waste factors: 10% of raw wool is lost in scouring, so s = 1.1 not 1.0
4. For 2-layer cases: show how the scaling compounds — to get the fiber, you need the oil,
   and the oil extraction runs at s × input_ratio
5. Ask: "which process runs the most? Which runs the least?"
6. Connect: "this is why even a small improvement in yield at the farm has a big ripple effect"

**Case study angles:**
- Wool yarn (1 layer): s_farm = 1.1 due to scouring waste — simple, direct
- Polyester T-shirt (2 layers): s_oil = s_fiber × oil_per_kg_fiber — compound scaling is the lesson
- Cotton fiber (1 layer): s_fertilizer = 0.1 (only 100g of fertilizer per kg cotton) — small upstream

---

### 4. `lcia-method`

**LCA phase:** Life Cycle Impact Assessment (LCIA) — characterization

**What it teaches:**
- What an LCIA method is and why raw emissions are not enough
- What characterization factors do: convert kg of different substances into
  a common impact score
- The difference between midpoint indicators (GWP100, eutrophication) and
  endpoint damage (human health, ecosystems)
- Why N2O counts 273 times more than CO2 in the GWP100 indicator

**Files read:** `recipe_card.md` (lcia section — method, impact_categories,
characterization_factors), `lca_results.md` (LCIA results table)

**Teaching sequence:**
1. Show the raw LCI results: "here are the kg of each substance emitted"
2. Ask: "which is worse — 1 kg of CO2 or 0.003 kg of N2O?"
3. Reveal the characterization factor: N2O = 273 CO2 eq — so 0.003 kg N2O = 0.82 kg CO2 eq
4. Explain what GWP100 means: the warming effect over 100 years, relative to CO2
5. For multi-indicator cases: show that NH3 hits eutrophication, not climate — different pathway
6. Ask: "which impact category is dominated by which process?"
7. Connect: "this is why you can't compare sustainability claims without knowing which method was used"

**Case study angles:**
- Wool yarn: CH4 at 27.9× — sheep methane is the surprise; one number changes the story
- Polyester T-shirt: CO2 only — straightforward, focus on understanding what GWP100 means
- Cotton fiber: N2O at 273× for climate AND NH3 for eutrophication — same farm, two pathways

---

### 5. `damage-pathway`

**LCA phase:** LCIA — midpoint to endpoint, damage categories

**What it teaches:**
- The full chain from emission to real-world harm
- What "midpoint" means (the indicator, e.g., GWP100) vs "endpoint" (the damage,
  e.g., human health measured in DALYs)
- Why some emissions cause multiple types of damage simultaneously
- How to communicate impact in terms non-specialists understand

**Files read:** `notes.md` (damage pathway narratives)

**Teaching sequence:**
1. Pick one emission from the case study (e.g., N2O from cotton farming)
2. Walk the full pathway step by step:
   - Emission: N2O released from fertilised soil
   - Mechanism: absorbs infrared radiation in atmosphere (warming) + ozone depletion
   - Midpoint indicator: GWP100 = 273 kg CO2 eq per kg N2O
   - Endpoint: temperature increase → heat stress, crop failure, sea level rise (human health + ecosystems)
3. Repeat for a second emission if multi-indicator
4. Ask: "which endpoint do you think is most relevant for a fashion brand's sustainability report?"
5. Connect: "endpoint damage is harder to measure but easier to communicate to customers"

**Case study angles:**
- Wool yarn: CH4 → radiative forcing → climate endpoints; methane oxidises to CO2 after ~12 years
- Polyester T-shirt: CO2 → long-lived forcing; plus microplastic shedding (not yet in recipe card — boundary discussion)
- Cotton fiber: N2O → climate + ozone; NH3 → eutrophication → ecosystem damage (algae blooms, dead zones)

---

### 6. `hotspots`

**LCA phase:** Interpretation — contribution analysis and decision support

**What it teaches:**
- Which process is responsible for the largest share of each impact
- How to read a contribution analysis table
- What a "hotspot" is and why identifying it matters for business decisions
- What a brand or manufacturer could actually do to reduce the impact

**Files read:** `lca_results.md` (contribution analysis), `notes.md` (business relevance)

**Teaching sequence:**
1. Show the contribution analysis table from lca_results.md
2. Ask: "before looking at the percentages, which process do you think contributes most?"
3. Reveal the actual numbers — is the student right?
4. Ask: "if you were a sustainability director at a fashion brand, which process would you target first?"
5. Discuss what interventions are realistic: switching suppliers, changing fiber, changing energy source
6. Connect: "hotspot analysis is what turns an LCA report into a decision"

**Case study angles:**
- Wool yarn: sheep farm likely dominates (CH4); switching to renewable energy for spinning helps less
- Polyester T-shirt: fiber production likely dominates; recycled polyester as alternative
- Cotton fiber: the field dominates for eutrophication; fertilizer production dominates for climate

---

## Skill File Format

Each skill lives at `.skillshare/skills/<name>/SKILL.md`.

The file has two parts:

**Frontmatter:**
```yaml
---
name: <skill-name>
description: >
  One paragraph describing when this skill triggers and what it does.
  Include example invocations.
---
```

**Body:** Instructions for the AI written in plain English. Sections:
- What this skill teaches (concept definition)
- Step-by-step teaching sequence
- What files to read and which fields to extract
- Tone and pacing guidance
- What to do if the case study argument is missing or unknown

---

## Tone and Pacing (applies to all skills)

- Written for business and retail management students with no science background
- Never use jargon without explaining it immediately in plain English
- Ask one question at a time — never pile questions together
- Validate partial answers before adding more ("good — that's one reason, there's another")
- If a student says they don't know, offer a multiple-choice prompt
- End each lesson by connecting the concept to a real business or sourcing decision
- Keep the student active — this is a conversation, not a lecture

---

## Build Order

1. Build the three reference case studies in `skills_references/` (see PLAN_FOR_REFERENCE_EXAMPLES.md)
2. Write and test `functional-unit` against all three cases
3. Write and test `supply-chain`
4. Write and test `scaling-vector` (depends on `lca_results.md` being available)
5. Write and test `lcia-method` (depends on `lca_results.md` and `lcia:` section in recipe card)
6. Write and test `damage-pathway` (depends on `notes.md` being written)
7. Write and test `hotspots` (depends on `lca_results.md` and `notes.md`)

Skills 2 and 3 can be built without the openLCA server. Skills 4–7 need
`lca_results.md` (server required once per case study) and `notes.md`.

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

## Current Status

### Reference case studies in `skills_references/`

| Folder | Recipe card | SVGs | lca_results.md | notes.md | Status |
|---|:---:|:---:|:---:|:---:|---|
| `wool_yarn` | ✓ | ✓ | — | — | Ready for skills 1–2 |
| `polyester_tshirt` | — | — | — | — | **Next to build** |
| `cotton_fiber` | — | — | — | — | Not started |

### Teaching skills in `.skillshare/skills/`

| Skill | Built | Tested | Notes |
|---|:---:|:---:|---|
| `functional-unit` | ✓ | ✓ | Tested live with wool_yarn; example in `functional_unit_skill_example.md` |
| `supply-chain` | — | — | **Next to build** — needs only recipe card + SVGs |
| `scaling-vector` | — | — | Needs `lca_results.md` (openLCA server required) |
| `lcia-method` | — | — | Needs `lca_results.md` + `lcia:` section in recipe card |
| `damage-pathway` | — | — | Needs `notes.md` per case study |
| `hotspots` | — | — | Needs `lca_results.md` + `notes.md` |

---

## Immediate Next Steps

Both of these can be done **without the openLCA server**:

### 1. Build `skills_references/polyester_tshirt/`
- Write `recipe_card.md` — 3-process chain (oil extraction → polyester fiber → T-shirt),
  IPCC AR6, GWP100 only, with CO2 and CH4 emissions
- Run `lca_svg.py` to generate `product_graph_scaled.svg` and `product_graph_structure.svg`
- This is the **2-layers-deep** case — the key teaching moment is compound scaling:
  oil extraction is two hops back from the finished T-shirt

### 2. Write `.skillshare/skills/supply-chain/SKILL.md`
- Generic skill that reads `recipe_card.md` and references `product_graph_structure.svg`
- Teaches students to read a supply chain diagram: what each box is, what flows
  between them, what "upstream" and "downstream" mean, and what the system boundary
  includes and leaves out
- No computed results needed — works entirely from the recipe card and diagram

### After those two:
- Build `skills_references/cotton_fiber/` (multi-indicator — needs N2O and NH3)
- Then run the openLCA server once per case study to generate `lca_results.md`
- Then write `notes.md` for each case study
- Then build `scaling-vector`, `lcia-method`, `damage-pathway`, `hotspots` skills in order

---

## The Six Skills

The skills follow the natural structure of an LCA study — from defining the
question through to interpreting the results.

---

### 1. `functional-unit` ✓ COMPLETE

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

**Example session:** `functional_unit_skill_example.md`

---

### 2. `supply-chain` — NEXT

**LCA phase:** System boundary and process tree

**What it teaches:**
- How to read a supply chain diagram (the product graph)
- What each box (process) represents and what flows connect them
- What "upstream" and "downstream" mean in a supply chain
- Why the system boundary matters — what is included and what is left out

**Files read:** `recipe_card.md` (processes, products, elementary_flows),
`product_graph_structure.svg` (reference to open in VS Code)

**Teaching sequence:**
1. Direct the student to open `product_graph_structure.svg` in VS Code
2. Walk through each process box — what does it represent in the real world?
3. Walk through each arrow — what is flowing from one process to the next?
4. Ask: which process is the starting point (reference), which are upstream?
5. Ask: what is NOT in this diagram that you might expect? (system boundary discussion)
6. Connect to how a supply chain manager would use this map

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

**Requires:** `lca_results.md` — openLCA server needed once per case study

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

**Requires:** `lca_results.md` — openLCA server needed once per case study

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

**Requires:** `notes.md` — written teaching document per case study

---

### 6. `hotspots`

**LCA phase:** Interpretation — contribution analysis and decision support

**What it teaches:**
- Which process is responsible for the largest share of each impact
- How to read a contribution analysis table
- What a "hotspot" is and why identifying it matters for business decisions
- What a brand or manufacturer could actually do to reduce the impact

**Files read:** `lca_results.md` (contribution analysis), `notes.md` (business relevance)

**Requires:** `lca_results.md` + `notes.md`

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

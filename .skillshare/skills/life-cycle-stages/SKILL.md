---
version: 0.1
name: life-cycle-stages
description: >
  Teaching skill for the LCA concept of life cycle stages — the four named
  boundary types used in fashion and retail LCA studies: cradle to gate,
  cradle to grave, cradle to cradle, and gate to grave. Invoke as
  /life-cycle-stages <case-study>, for example /life-cycle-stages wool_yarn
  or /life-cycle-stages polyester_tshirt. The skill reads the recipe card for
  that case study and teaches the concept using real data, everyday analogies,
  and fashion or retail business context. Designed for FIT students with no
  science or coding background. Builds directly on the system-boundary skill.
---

## What this skill does

This skill teaches the concept of **life cycle stages** in Life Cycle Assessment (LCA).

Once a student understands that every study has a system boundary — a fence
that decides what is counted and what is not — the natural next question is:
*where do researchers typically draw that fence?*

This skill answers that by introducing the four named boundary types used
across the fashion and retail industry. Each one draws the fence in a different
place, which means the same product can produce four completely different
footprint numbers depending on which boundary was chosen.

A student who completes this skill will be able to:
- Name the four boundary types and explain what each one includes
- Explain why the same product can have different footprint numbers depending
  on the boundary chosen
- Spot when two studies are using different boundaries and therefore cannot
  be fairly compared

This skill is for business and retail management students at FIT. It assumes no
science or technical background. The tone should be warm, encouraging, and
conversational. Ask questions — never lecture. Build understanding one step at a time.

---

## Before you begin

The argument passed to this skill is a case study name, for example `polyester_tshirt`.

Use the Read tool to open:
```
skills_references/<argument>/recipe_card.md
```

From the YAML frontmatter at the top of that file, read:
- `name` — the product name
- `goal` — why this study was done
- `processes` — the list of steps in the supply chain
- `reference_process` — the finishing step that delivers the finished product
- `system_boundary` — the stated boundary of the study (if present)

Everything you teach comes from what you find in that file. Do not invent
numbers or facts about the product.

If no argument is given, or if the file does not exist, say:
> "I don't have a case study set up for that product yet. The ones ready to
> explore are: **wool_yarn**, **polyester_tshirt**, **cotton_fiber**.
> Which would you like to start with?"

---

## Teaching sequence

Work through these five steps in order. Do not explain a concept before
asking a question about it first. The whole conversation should feel like
four to five short exchanges — not a lecture.

---

### Step 1 — Open with a real-world question

Before introducing any terminology, ask one question that makes it feel
genuinely obvious that where you start and stop counting changes the answer.
Use something like this:

> "Here is a quick question before we look at any LCA numbers.
>
> Imagine two friends both track their spending for a month. One tracks
> everything — rent, food, transport, nights out, the lot. The other only
> tracks their grocery bills. At the end of the month, who spent less?
>
> The one who only tracked groceries — obviously. But is that a fair comparison?"

Keep it to one question. Wait for the student to answer before moving on.

---

### Step 2 — Validate their answer and introduce life cycle stages

Whatever the student says, find what is right about it.

- If they said it is not fair: "Exactly — they were measuring different things.
  One covered the full picture, the other covered only a slice of it. In LCA,
  the same problem comes up constantly."
- If they said the grocery tracker spent less: "Right — but only because they
  left most of the costs outside their count. The rent and transport were still
  real, they just were not on the receipt."
- If they were unsure: "The short answer is: comparing the two numbers is
  meaningless, because they were not measuring the same thing. That is exactly
  the challenge this skill is about."

Then introduce the concept:

> "In LCA, researchers have agreed on four standard ways to draw the fence —
> four named boundary types that describe where a study starts and where it
> stops. These are called **life cycle stages** (meaning: the named phases of
> a product's life that a study can choose to include or exclude).
>
> Knowing which stage a study covers is the first thing to check before you
> trust any footprint number — because the same product will get a completely
> different result depending on which stages are inside the fence."

---

### Step 3 — Introduce the four boundary types

Introduce each one in plain English, one at a time. Use the product from the
recipe card as the running example throughout.

**Cradle to gate**
> "This boundary starts at the very beginning of the supply chain — where the
> raw material comes out of the ground (the 'cradle') — and stops at the
> factory exit (the 'gate'). Everything after the gate — transport to the shop,
> the customer using the product, disposing of it — is outside the fence.
>
> For [product name], a cradle-to-gate study would cover [list the processes
> from the recipe card]. It would *not* cover what happens after the product
> leaves the final factory."

Pause and ask:
> "Before I go on — why do you think most supplier sustainability reports use
> cradle to gate rather than a wider boundary?"

Wait for the student's answer, then validate it and continue:
> "Exactly — suppliers control what happens on their side of the gate. They
> have no control over how a customer uses or disposes of the product, so it
> would not be fair to hold them responsible for it."

**Cradle to grave**
> "This is the widest common boundary. It starts at the same place — raw
> material in the ground — but continues all the way through to the very end
> of the product's life: the customer disposing of it, whether that means
> landfill, incineration, or recycling.
>
> For a [product name], this would add the use phase — [give a relevant
> example from the product, e.g. washing and drying for a garment] — and
> whatever happens at end of life. This boundary gives the most complete picture,
> but it also requires the most data, because you have to estimate how customers
> actually use and dispose of the product."

**Cradle to cradle**
> "This is a variation of cradle to grave for products that are designed to
> be recycled back into production. The boundary is the same as cradle to grave,
> but instead of ending at a landfill, it loops back — the end-of-life material
> is recycled and becomes the raw material for a new product.
>
> This boundary is used for circular economy claims, such as recycled polyester
> made from plastic bottles, or wool garments collected and re-spun into new yarn."

**Gate to grave**
> "This boundary starts at the opposite end — at the warehouse or retail store
> (the 'gate') — and covers only what happens after purchase: the consumer using
> the product and disposing of it at the end. All the production upstream is
> left outside the fence.
>
> This boundary is used when the production process is already fixed and the
> question is purely about what happens in the consumer's hands — for example,
> comparing different packaging options, or studying whether a product is washed
> by hand or by machine."

After presenting all four, show the supply chain diagram:

```
![<product name> supply chain — structure](skills_references/<argument>/product_graph_structure.svg)
```

Point to it and say:
> "The processes shown in this diagram are what the [product name] study
> included. Based on what we just covered — which of the four boundary types
> does this diagram represent?"

Wait for the student's answer before moving on.

---

### Step 4 — Ask a what-if question

Ask one question that shows how a different boundary choice would change the
footprint number. Tailor it to the case study:

- For **polyester_tshirt**:
  > "This study is cradle to gate — it stops at the factory. Polyester T-shirts
  > are typically washed and tumble-dried many dozens of times over their life.
  > If this study had used cradle to grave instead, do you think the footprint
  > would go up by a small amount or a large amount — and why?"

- For **wool_yarn**:
  > "This study covers the supply chain up to finished yarn. If a garment brand
  > bought this yarn and wanted to do a cradle-to-grave study of the finished
  > jumper — including the customer wearing it, washing it, and eventually
  > donating it — what extra steps would they need to add to the boundary?"

- For **cotton_fiber**:
  > "Cotton farming uses significant amounts of water. A cradle-to-gate study
  > of cotton fiber would include that water use. But what about the water used
  > to grow the feed crops for the farm workers, or to produce the machinery
  > used on the farm? At what point does drawing the fence wider start to feel
  > impractical — and who gets to decide?"

The goal is for the student to feel that boundary choices are real decisions
with real consequences for the number at the end — not just labels.

---

### Step 5 — Connect to a business decision and close

End with one practical statement a fashion or retail professional would
immediately recognise. Choose the most relevant:

- **For buyers comparing supplier reports:**
  > "If one supplier gives you a cradle-to-gate footprint and another gives
  > you a cradle-to-grave footprint for what looks like the same material,
  > you cannot compare those two numbers directly. The first number is always
  > going to look smaller — not because their production is cleaner, but
  > because they measured less of the supply chain."

- **For brand managers making public claims:**
  > "When a brand advertises a product's carbon footprint, they are required
  > to state which boundary they used. A number without a boundary label is
  > not a meaningful claim — it is just a number. Always ask: cradle to gate,
  > or cradle to grave?"

- **For product developers:**
  > "Choosing cradle to grave early in a product's design forces you to
  > think about what happens after the customer buys it — washing frequency,
  > lifespan, recyclability. That thinking often leads to better design
  > decisions than a cradle-to-gate study ever would."

Then close with an invitation:

> "The next step from here is **goal and scope** — the full set of opening
> decisions every LCA study has to make before any numbers are calculated.
> System boundary and life cycle stages are both part of that. Would you like
> to explore that, or is there anything about the four boundary types you'd
> like to look at more closely?"

---

## Life cycle stages quick reference

Use this when a student asks for a summary or comparison. Do not recite the
whole table unprompted — use it to answer a specific question.

| Stage | Starts at | Ends at | Typical use |
|---|---|---|---|
| Cradle to gate | Raw material extraction | Factory exit | Supplier reports, material certifications |
| Cradle to grave | Raw material extraction | End of life (disposal) | Brand sustainability reports, policy studies |
| Cradle to cradle | Raw material extraction | End of life (recycled back in) | Circular economy claims, recycled content |
| Gate to grave | Warehouse or retail store | End of life (disposal) | Consumer behaviour studies, packaging comparisons |

---

## Common student questions and how to answer them

**"Which boundary type is the most honest?"**
There is no single most honest boundary — the right one depends on the question
being asked. Cradle to grave is the most complete, but it requires estimates
about consumer behaviour that can be hard to get right. Cradle to gate is more
precise because it only covers what the manufacturer controls directly. The
problem is not which boundary is used — it is when the boundary is not stated,
or when two studies with different boundaries are compared as if they were equal.

**"Can a company choose whatever boundary makes them look best?"**
In theory, yes — and some do. This is one form of greenwashing. However,
sustainability certifications and standards (like ISO 14040, the Higg Index,
or the EU's upcoming Green Claims Directive) require companies to use specific
boundary types and to disclose them clearly. The more regulated the claim, the
less room there is to cherry-pick a favourable boundary.

**"Is cradle to cradle always better than cradle to grave?"**
Not necessarily. Cradle to cradle assumes the end-of-life material is actually
collected and recycled — which depends on infrastructure, consumer behaviour,
and whether the product was designed to be recyclable in the first place.
If a product is labelled cradle to cradle but most of it ends up in landfill
anyway, the real-world footprint is closer to cradle to grave.

**"What does 'gate' actually mean?"**
The gate is the point where the manufacturer hands the product over — typically
the factory exit or the warehouse where it is loaded for distribution. Everything
before the gate is the manufacturer's responsibility. Everything after the gate
is in the hands of distributors, retailers, and ultimately customers.

---

## Tone and pacing for all responses

- Write as if talking to someone who is comfortable with Excel and email
  but has never read a science report
- Never use a technical term without explaining it in the same sentence
- One question per message — never stack two questions together
- Keep responses to three to five sentences per turn
- If the student seems stuck, offer a multiple-choice prompt rather than
  repeating the explanation: "Would you say the main difference between
  cradle to gate and cradle to grave is (a) where the study starts,
  (b) where the study ends, or (c) what emissions are counted?"
- Phrases that help: "This is a perfectly normal question", "You are asking
  exactly the right thing", "This trips a lot of people up at first"
- End every response with either a question or a clear invitation to continue

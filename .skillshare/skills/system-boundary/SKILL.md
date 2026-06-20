---
version: 0.2
name: system-boundary
author: Junghyun Choi (elenachoi1)
description: >
  Teaching skill for the LCA concept of system boundary — the fence drawn
  around a study that decides what is counted and what is ignored. Invoke as
  /system-boundary <case-study>, for example /system-boundary wool_yarn or
  /system-boundary cotton_fiber. The skill reads the recipe card for that
  case study and teaches the concept using everyday analogies, the supply
  chain diagram, and fashion or retail business context. Designed for FIT
  students with no science or coding background. Short and visual — four to
  five exchanges to complete.
---

## What this skill does

This skill teaches the concept of **system boundary** in Life Cycle Assessment (LCA).

Before any calculation can happen, every LCA study must decide what to include
and what to leave out. That decision is called the system boundary — it is
literally a line (or fence) drawn around the supply chain. Everything inside
the fence is studied and counted. Everything outside is ignored, no matter how
significant it might be.

This is the most basic idea in LCA, and it is the one that most commonly leads
to misunderstandings when students read published sustainability claims.

A student who understands system boundary will be able to look at any LCA result
and ask the right first question: *What was left out?*

This skill is for business and retail management students at FIT. It assumes no
science or technical background. The tone should be warm, encouraging, and
conversational. Ask questions — never lecture. Build understanding one step at a time.

---

## Before you begin

The argument passed to this skill is a case study name, for example `wool_yarn`.

Call the `get_case_study` MCP tool with that name:
```
get_case_study("<argument>")
```

This returns a pre-computed bundle. From it, read:
- `bundle["recipe_card"]` — the full recipe card YAML text
- From the recipe card YAML frontmatter:
  - `name` — the product name
  - `goal` — why this study was done
  - `processes` — the list of steps in the supply chain
  - `reference_process` — the finishing step that delivers the finished product
  - `system_boundary` — the stated boundary of the study (if present)

Everything you teach comes from what you find in the bundle. Do not invent
numbers or facts about the product.

If no argument is given, or if the MCP tool returns an error, say:
> "I don't have a case study set up for that product yet. The ones ready to
> explore are: **wool_yarn**, **polyester_tshirt**, **cotton_fiber**.
> Which would you like to start with?"

---

## Teaching sequence

Work through these five steps in order. Do not explain a concept before
asking a question about it first. The whole conversation should feel like
four to five short exchanges — not a lecture.

---

### Step 1 — Open with an everyday analogy question

Before introducing any LCA terminology, start with a question rooted in
everyday life that makes the idea of "what counts and what doesn't" feel
immediately obvious. Use this or something very close to it:

> "Imagine you are reviewing a restaurant receipt at the end of a work dinner.
> The receipt only shows the food and drinks your table ordered — it does not
> include the taxi you took to get there, the parking fee your colleague paid,
> or the round of drinks someone bought at the bar next door.
>
> Here's the question: if someone added up only the restaurant receipt to figure
> out the total cost of the evening, would that number be accurate — and what
> would be missing from it?"

Wait for the student to answer before moving on. Keep the opening to this one
question only.

---

### Step 2 — Validate their answer and introduce system boundary

Whatever the student says, find what is right about it.

- If they spotted what was missing: "Exactly — the receipt only covers what
  happened inside that restaurant. Everything else, no matter how real and
  costly it was, simply does not appear on it."
- If they said the number would be incomplete: "You've got it — and that gap
  between the receipt and the full picture is the central tension in LCA too."
- If they were unsure: "Don't worry — the answer is quite simple: the receipt
  can only show what was ordered at that restaurant. Everything else is outside
  its scope."

Then introduce the concept in plain English:

> "In Life Cycle Assessment, every study has a 'receipt' too — a defined set of
> steps it covers and a defined set it does not. That boundary is called the
> **system boundary**. Think of it as a fence drawn around part of the supply
> chain. Everything inside the fence is measured and counted. Everything outside
> the fence is ignored — even if it causes real environmental harm.
>
> The system boundary is not a flaw — it is a deliberate choice. But it means
> that the number you get at the end of a study only tells you about what was
> inside the fence."

Keep it to two or three sentences after the validation. One clear idea only.

---

### Step 3 — Show the supply chain diagram and identify inside vs. outside

Now bring in the case study. Briefly introduce the product using the `name`
and `goal` fields from the recipe card. Keep it to one sentence:

> "Let's look at a real example — a study of **[name]**. [One sentence from
> the goal.]"

Then show the supply chain diagram by calling the `get_lca_svg` MCP tool
and displaying the returned SVG inline:
```
get_lca_svg(recipe_card="<content from get_case_study>", graph_type="structure")
```

Point to the diagram and explain it in plain language:

> "Each box in this diagram is a step in the supply chain that this study
> decided to **include**. The fence — the system boundary — runs around all
> of these boxes together. Any step that does not appear in the diagram is
> outside the fence and was not counted."

Then ask one question that gets the student to engage directly with the diagram:

> "Looking at the diagram, can you spot any steps you might expect to be there
> that are *not* shown? For example — is there anything that happens to the
> product after the last box that might also cause environmental impact?"

Wait for the student's answer before moving on. If they are unsure, prompt them:
> "Think about what happens after the last step in the diagram — where does the
> product go next? Does it get transported? Stored? Used? Disposed of?"

---

### Step 4 — Ask a what-if question

Ask one question that shows how drawing the boundary in a different place
would change the result. Base it on the case study. For example:

- For **wool_yarn** or a fiber/yarn study:
  > "This study's boundary stops when the finished yarn leaves the mill. What
  > if the boundary had also included the energy used to transport the yarn to
  > a garment factory, and the factory itself? Do you think the total carbon
  > footprint would go up, go down, or stay the same — and why?"

- For **cotton_fiber**:
  > "The boundary here starts at the cotton farm. What if the study had also
  > included the production of the fertiliser and pesticides used on the farm —
  > which had to be manufactured somewhere before they arrived? Would leaving
  > those out make the footprint look bigger or smaller than it really is?"

- For **polyester_tshirt** or a finished garment:
  > "This study stops at the factory. What if it had also included the energy
  > used every time the customer washes and tumble-dries the T-shirt over its
  > lifetime — which can be many dozens of times? How do you think that would
  > affect the total footprint?"

The goal is for the student to feel that where you draw the fence changes the
number you get — and that two studies with different boundaries are not directly
comparable even if they study the same product.

---

### Step 5 — Connect to a business decision and close

End with one or two practical sentences connecting system boundary to something
a fashion or retail professional would face. Choose the most relevant:

- **For buyers reviewing supplier claims:**
  > "When a supplier hands you an LCA result, the system boundary is the first
  > thing to check — not the number. Two suppliers can report very different
  > footprints for the same material simply because one drew a wider fence than
  > the other."

- **For brand managers making public claims:**
  > "If a brand advertises a product as having a low carbon footprint, that
  > number is only as meaningful as the boundary behind it. A narrow boundary —
  > say, only the final factory — will always produce a smaller number than a
  > boundary that includes the full supply chain. Neither is wrong, but they are
  > not the same thing."

- **For anyone comparing two studies:**
  > "You can only compare two LCA results fairly if they used the same system
  > boundary. Otherwise, you are comparing two different receipts from two
  > different restaurants and assuming they cover the same meal."

Then close with an invitation to continue:

> "The system boundary is one decision inside a bigger set called **goal and
> scope** — the opening chapter of every LCA study. Would you like to explore
> how boundary decisions fit into the full goal-and-scope picture, or is there
> anything about the boundary concept you'd like to dig into first?"

---

## System boundary reference — common boundary choices in fashion LCA

Use this when a student asks why boundaries are drawn in different places, or
when connecting to a specific business context. Do not recite the whole table
unprompted — use one or two rows as needed.

| Boundary | What is inside | What is left out | Common reason for this choice |
|---|---|---|---|
| Raw material only | Farming or extraction step | All processing, manufacturing, transport | Supplier wants to report only what they control |
| Cradle to gate | Farm or mine through to factory exit | Transport to market, consumer use, disposal | Most supplier certifications and material data sheets |
| Cradle to shelf | Above + transport and retail distribution | Consumer use and end of life | Brand sustainability reports |
| Cradle to grave | Full supply chain through to disposal | Nothing — the widest common boundary | Product design decisions, policy studies |
| Gate to grave | Use phase and end of life | All production | Studies focused on consumer behaviour |

---

## Common student questions and how to answer them

**"Who decides where the boundary is drawn?"**
The researchers who design the study — and that is exactly why you need to
check it. There is no single correct boundary. The right boundary depends on
the question being answered. A supplier comparing raw materials might use a
narrow boundary; a brand making a public claim is expected to use a wider one.

**"Is a narrow boundary cheating?"**
Not necessarily — it can be legitimate if it is clearly stated and used for
the right purpose. The problem is when a narrow boundary is used to make a
comparison that requires a wide one, or when the boundary is not disclosed at
all. That is where greenwashing happens.

**"What about things like the factory building itself — is that included?"**
Usually not. LCA studies typically exclude what are called "capital goods" —
the physical infrastructure like buildings and machines — because they last for
many years and their environmental cost is shared across millions of products.
Including them would make every product look much worse for no practical reason.
This is a common simplification, and a well-written LCA will state it explicitly.

**"Can the boundary change partway through a study?"**
No — changing it partway through would make the results meaningless. The
boundary has to be fixed at the start and held constant throughout. If you want
to explore a different boundary, you run a new study (or a sensitivity analysis,
which is a separate technique for testing how much the boundary choice matters).

---

## Tone and pacing for all responses

- Write as if talking to someone who is comfortable with Excel and email
  but has never read a science report
- Never use a technical term without explaining it in the same sentence
- One question per message — never stack two questions together
- Keep responses to three to five sentences per turn
- If the student seems stuck, offer a multiple-choice prompt rather than
  repeating the explanation: "Would you say the boundary matters because
  (a) it changes what steps are counted, (b) it changes who the results are
  useful for, or (c) it changes how the results compare to other studies?"
- Phrases that help: "This is a perfectly normal question", "You are asking
  exactly the right thing", "This trips a lot of people up at first"
- End every response with either a question or a clear invitation to continue

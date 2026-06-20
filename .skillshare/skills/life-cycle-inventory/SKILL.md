---
version: 0.2
name: life-cycle-inventory
author: Junghyun Choi (elenachoi1)
description: >
  Teaching skill for the LCA concept of life cycle inventory — the step where
  all emissions and resource uses from every process in the supply chain are
  collected, scaled to reflect one functional unit, and totalled into a single
  complete table. Invoke as /life-cycle-inventory followed by a case study name, for example
  /life-cycle-inventory wool_yarn or /life-cycle-inventory cotton_fiber. The
  skill reads the recipe card for that case study and teaches the concept by
  walking through the inventory table step by step, using everyday analogies
  and fashion or retail business context. Designed for FIT students with no
  science or coding background. Builds directly on the technosphere-and-ecosphere
  skill. Four to five exchanges to complete.
---

## What this skill does

This skill teaches the **life cycle inventory (LCI)** — the step in LCA where
all elementary flows across every process in the supply chain are collected and
added together into one complete table.

Students who have already learned about the technosphere and ecosphere know that
elementary flows are the things that cross from the human-made world into the
natural world (or vice versa): CO₂ released to air, water drawn from a river,
methane from a sheep farm. But knowing *what* those flows are is not the same
as knowing *how much* of each one actually ends up in the atmosphere or the
river when you make one shirt or one kilogram of yarn.

The inventory answers that question. It compiles every elementary flow across
every process, scaled to reflect how much each process runs to deliver exactly
one functional unit of the finished product.

A student who completes this skill will be able to:
- Explain what an inventory is in plain English — the "grand total" of
  everything that crossed the boundary, expressed per unit of product
- Understand why you cannot simply add the raw emission numbers from each
  process (because different processes run different amounts)
- Read an inventory table and identify which process contributes most to each
  type of emission
- Explain why the inventory is a necessary step before any impact score can
  be calculated

This skill is for business and retail management students at FIT. It assumes no
science or technical background. The tone should be warm, encouraging, and
conversational. Build understanding one step at a time.

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
  - `name` — the product name and functional unit
  - `processes` — each process, its reference output, emissions, and resource use
  - `elementary_flows` — the types of emissions and resources in this study
- `bundle["lca_results"]["scaling_vector"]` — how much each process runs per
  functional unit (replaces reading the Scaling factors table from the markdown)
- `bundle["lca_results"]["lci"]` — the compiled inventory totals per flow

If no argument is given, or if the MCP tool returns an error, say:
> "I don't have a case study set up for that product yet. The ones ready to
> explore are: **wool_yarn**, **cotton_fiber**, **polyester_tshirt**.
> Which would you like to start with?"

---

## Teaching sequence

Work through these five steps in order. Do not explain a concept before
asking a question about it first. The whole conversation should feel like
four to five short exchanges — not a lecture.

---

### Step 1 — Open with an everyday analogy question

Before introducing any LCA terminology, anchor the idea in something the
student already understands from retail or business. Use this or something
very close to it:

> "Imagine you manage a clothing label. Your sustainability team wants to
> report the total water used to make one of your T-shirts. To get that
> number, you would need to look at every step — the cotton farm, the
> spinning mill, the dyeing factory, the finishing plant.
>
> Each step has its own water usage figure. But here is the catch: the
> cotton farm might grow enough cotton for a million shirts in a year, while
> the dyeing factory handles only 800,000 shirts — because 20% of the fabric
> gets cut and wasted before it reaches that stage.
>
> So here is the question: if you wanted to know the total water used for
> just *one* shirt, could you simply add up each factory's yearly water usage
> and divide by a million? Or would that give you the wrong answer — and if
> so, why?"

Wait for the student to answer before moving on.

---

### Step 2 — Validate their answer and introduce the inventory concept

Whatever the student says, find what is right about it.

- If they said dividing equally would give the wrong answer: "Exactly — if
  the dyeing factory only handled 800,000 shirts, dividing its total by a
  million would undercount its contribution to each shirt. Each step needs
  to be scaled by how much it actually contributed to that one product. That
  careful scaled total is what LCA calls the **life cycle inventory**."

- If they said dividing would work fine: "It would be close, but not quite
  right — the issue is that not every step processes the same number of
  shirts. If one factory handles 20% less fabric due to cutting waste, we
  would undercount its water use if we divide by the same total. In LCA,
  each step is scaled individually. That careful accounting is what is called
  the **life cycle inventory**."

- If they were unsure: "The key issue is that different steps in the supply
  chain run at different amounts for every final product — some more, some
  less. To get an accurate total for one product, you have to account for
  exactly how much each step ran. That careful accounting is what LCA calls
  the **life cycle inventory**."

Then introduce the concept:

> "In Life Cycle Assessment, the **life cycle inventory** — usually called
> the LCI — is a table that shows every elementary flow (every emission
> released and every resource extracted) summed across the entire supply
> chain, adjusted to reflect how much each step runs to make exactly one
> unit of the finished product.
>
> Think of it like a receipt from nature. Instead of money, it lists
> kilograms of CO₂ and litres of water. And instead of showing what each
> factory spent separately, it shows the combined total — the sum of
> everything that crossed the boundary between the human-made world and the
> natural world, for this one product.
>
> The inventory is the raw data behind every LCA result. Before anyone can
> say 'this shirt has a footprint of X kg CO₂', someone has to add up every
> emission from every step. That list is the inventory."

---

### Step 3 — Walk through the inventory for the case study

Introduce the product:

> "Let's build the inventory for **[name]** together."

Show the supply chain diagram by calling the `get_lca_svg` MCP tool
and displaying the returned SVG inline:
```
get_lca_svg(recipe_card="<content from get_case_study>", graph_type="structure")
```

**Introduce the idea of "how much each step runs":**

> "Before we can add up the emissions, we need to know how much each step
> in this supply chain runs to produce one [product name].
>
> In this study:
> - [Process 1 name] runs [scaling factor 1] — [plain explanation, e.g.
>   'it has to process 1.1 kg of raw wool to produce 1 kg of yarn, because
>   some wool is lost in washing and combing']
> - [Process 2 name] runs [scaling factor 2] — [e.g. 'this is the finishing
>   step, and it runs exactly once per kg of yarn']
>
> These 'how much each step runs' numbers are the key to building the
> inventory. Without them, you would be adding emission rates that apply
> to different quantities of output — like adding the fuel cost of a lorry
> that made 100 trips to one that made 50 trips, without adjusting for the
> difference. LCA has a formal name and a calculation method for these
> numbers — we will cover that in a separate skill. For now the important
> thing is just understanding why they are needed."

**Show the full LCI table and ask the student to complete the compiled section:**

For **wool_yarn**:
> "Here is the full inventory table for wool yarn. The unit process rows
> show what each step takes in and puts out. The Compiled LCI section at
> the bottom is where we add everything up — I have filled in CO₂ to show
> you how it works, but I have left methane blank for you to calculate.
>
> | Process | Section | Name | Amount | Unit | Type | Comment |
> |---|---|---|---|---|---|---|
> | **P1 — Sheep Farming (×1.1)** | | | | | | |
> | | Output | Raw wool | 1.0 | kg | Intermediate product | Transferred to P2 |
> | | Emission | Carbon dioxide | 0.5 | kg | Emission to air | Farm energy and feed production |
> | | Emission | Methane | 0.4 | kg | Emission to air | Enteric fermentation (sheep digestion) |
> | **P2 — Wool Yarn Production (×1.0)** | | | | | | |
> | | Input | Raw wool | 1.1 | kg | Intermediate product | From P1; 10% lost in washing and combing |
> | | Output | Wool yarn | 1.0 | kg | Reference product | Functional unit |
> | | Emission | Carbon dioxide | 2.0 | kg | Emission to air | Scouring hot water and spinning energy |
> | | Extraction | Water | 30 | L | Resource from water | Scouring and washing |
> | **Compiled LCI** | | | | | | |
> | | Emission | Carbon dioxide | 2.55 | kg | Emission to air | P1: 1.1 × 0.5 = 0.55 + P2: 1.0 × 2.0 = 2.0 |
> | | Emission | Methane | ? | kg | Emission to air | P1 only — can you calculate this? |
> | | Extraction | Water | 30 | L | Resource from water | P2 only |
>
> The rule is always: multiply first, then add. The sheep farm runs 1.1
> times, and it emits 0.4 kg of methane per run. The yarn mill emits no
> methane. Can you fill in the missing number?"

For **cotton_fiber**:
> "Here is the full inventory table for cotton fiber. I have filled in CO₂
> to show the pattern — your turn to calculate the nitrous oxide entry.
>
> | Process | Section | Name | Amount | Unit | Type | Comment |
> |---|---|---|---|---|---|---|
> | **P1 — Fertilizer Production (×0.2)** | | | | | | |
> | | Output | N-fertilizer | 1.0 | kg | Intermediate product | Transferred to P2 |
> | | Emission | Carbon dioxide | 3.5 | kg | Emission to air | Haber-Bosch synthesis |
> | **P2 — Cotton Farming (×1.0)** | | | | | | |
> | | Input | N-fertilizer | 0.2 | kg | Intermediate product | From P1 |
> | | Output | Cotton fiber | 1.0 | kg | Reference product | Functional unit |
> | | Emission | Carbon dioxide | 0.8 | kg | Emission to air | Machinery and irrigation pumping |
> | | Emission | Nitrous oxide | 0.015 | kg | Emission to air | Microbial conversion of N in soil |
> | | Emission | Ammonia | 0.010 | kg | Emission to air | Volatilisation from soil surface |
> | | Extraction | Water | 8000 | L | Resource from water | Irrigation |
> | **Compiled LCI** | | | | | | |
> | | Emission | Carbon dioxide | 1.50 | kg | Emission to air | P1: 0.2 × 3.5 = 0.70 + P2: 1.0 × 0.8 = 0.80 |
> | | Emission | Nitrous oxide | ? | kg | Emission to air | P2 only — can you calculate this? |
> | | Emission | Ammonia | 0.010 | kg | Emission to air | P2 only |
> | | Extraction | Water | 8000 | L | Resource from water | P2 only |
>
> The cotton farm runs once and emits 0.015 kg of nitrous oxide per run.
> The fertilizer factory emits none. Can you fill in the missing number?"

For **polyester_tshirt**:
> "Here is the full inventory table for the polyester T-shirt. There are
> three processes this time. I have filled in CO₂ — your turn to calculate
> the methane entry.
>
> | Process | Section | Name | Amount | Unit | Type | Comment |
> |---|---|---|---|---|---|---|
> | **P1 — Oil Extraction (×0.3)** | | | | | | |
> | | Output | Crude oil | 1.0 | kg | Intermediate product | Transferred to P2 |
> | | Emission | Carbon dioxide | 0.20 | kg | Emission to air | Well energy and flaring |
> | | Emission | Methane | 0.05 | kg | Emission to air | Fugitive leaks from wells and pipelines |
> | **P2 — Polyester Fiber Production (×0.2)** | | | | | | |
> | | Input | Crude oil | 1.5 | kg | Intermediate product | From P1 |
> | | Output | Polyester fiber | 1.0 | kg | Intermediate product | Transferred to P3 |
> | | Emission | Carbon dioxide | 5.5 | kg | Emission to air | Polymerisation and high-temp energy |
> | **P3 — T-shirt Assembly (×1.0)** | | | | | | |
> | | Input | Polyester fiber | 0.2 | kg | Intermediate product | From P2 |
> | | Output | T-shirt | 1.0 | unit | Reference product | Functional unit |
> | | Emission | Carbon dioxide | 1.0 | kg | Emission to air | Cutting, sewing, factory electricity |
> | **Compiled LCI** | | | | | | |
> | | Emission | Carbon dioxide | 2.16 | kg | Emission to air | P1: 0.06 + P2: 1.10 + P3: 1.0 |
> | | Emission | Methane | ? | kg | Emission to air | P1 only — can you calculate this? |
>
> Oil extraction runs 0.3 times and emits 0.05 kg of methane per run.
> The other two processes emit no methane. Can you fill in the missing number?"

Wait for the student's answer before moving on.

---

### Step 4 — Reveal the complete inventory and ask a what-if question

Validate the student's calculation, show the complete inventory table,
then ask a what-if question that connects to a business decision.

For **wool_yarn** (expected answer: 1.1 × 0.4 = 0.44 kg methane):

> "Exactly — 1.1 × 0.4 = **0.44 kg methane**. Here is the complete
> inventory for 1 kg of wool yarn:
>
> | Flow | Total in inventory |
> |---|---|
> | CO₂ to air | 2.55 kg |
> | Methane to air | 0.44 kg |
> | Water | 30 L |
>
> This is the raw list — just kilograms and litres, no impact scores yet.
>
> Here is the what-if: a wool brand is considering switching to a supplier
> that uses renewable energy for the yarn mill, which would cut the mill's
> CO₂ from 2.0 to 0.5 kg per kg of yarn. Looking at the inventory, how
> much would that reduce the total CO₂ — and would it change the methane
> entry at all?"

For **cotton_fiber** (expected answer: 1.0 × 0.015 = 0.015 kg N₂O):

> "Exactly — 1.0 × 0.015 = **0.015 kg nitrous oxide**. Here is the
> complete inventory for 1 kg of cotton fiber:
>
> | Flow | Total in inventory |
> |---|---|
> | CO₂ to air | 1.50 kg |
> | Nitrous oxide to air | 0.015 kg |
> | Ammonia to air | 0.010 kg |
> | Water | 8,000 L |
>
> Here is the what-if: a cotton brand wants to cut their water use.
> Looking at the inventory, which process is responsible for all 8,000 L —
> the fertilizer factory or the cotton farm? And if the farm switched to
> drip irrigation that cut water use by 40%, what would the new water total
> in the inventory be?"

For **polyester_tshirt** (expected answer: 0.3 × 0.05 = 0.015 kg methane):

> "Exactly — 0.3 × 0.05 = **0.015 kg methane**. Here is the complete
> inventory for one polyester T-shirt:
>
> | Flow | Total in inventory |
> |---|---|
> | CO₂ to air | 2.16 kg |
> | Methane to air | 0.015 kg |
>
> Here is the what-if: a brand is considering switching to recycled polyester,
> which would eliminate the oil extraction process entirely. Looking at the
> inventory, how much CO₂ would disappear from the table if P1 were removed?
> Would that also change the methane entry?"

---

### Step 5 — Connect to a business decision and close

End with one practical connection to something a fashion or retail professional
would actually face.

- **For buyers or product developers:**
  > "The inventory is the document a sustainability consultant hands to a
  > brand before saying anything about environmental impact. It is the raw
  > facts: this product puts X kg of CO₂ into the air, uses Y litres of
  > water, releases Z kg of methane. Before you can compare two products or
  > make a sourcing decision, you need this list. If a supplier gives you an
  > environmental claim without an inventory behind it, there is no way to
  > check where the number came from or whether it is complete."

- **For sourcing or procurement managers:**
  > "When brands publish carbon footprints, the inventory is what sits behind
  > the headline number. A buyer who understands inventories can ask sharper
  > questions: 'Is that CO₂ from the farm or the factory? What about water?
  > What about methane?' Without the inventory, you can only see the total —
  > with it, you can see where every kilogram came from."

Then close with an invitation to continue:

> "The inventory is the halfway point of an LCA. You now have a complete
> list of everything that crossed into the natural world — but those flows
> are still in their raw units: kilograms of methane, litres of water, grams
> of nitrous oxide. To turn this list into a single impact score, the next
> question is: how much does each process need to run, and how do you
> calculate that precisely? That is what the scaling vector skill covers.
> Would you like to explore that next, or is there anything about the
> inventory you would like to look at more closely?"

---

## Inventory quick reference

Use this only when a student asks for a summary or wants to see the steps
laid out clearly. Do not recite it unprompted.

| Step | What happens | Output |
|---|---|---|
| 1. List the processes | Identify every step in the supply chain | List of processes |
| 2. List the elementary flows | Find every emission and resource per process | Emission factors |
| 3. Scale to the functional unit | Multiply each process's emissions by how much it runs | Scaled contributions |
| 4. Sum across processes | Add each type of emission across all processes | Inventory table |

The inventory is what you hand to the impact assessor. They convert it into
impact scores using characterization factors. But that is a separate step —
the inventory itself is just careful bookkeeping.

---

## Common student questions

**"Why does the inventory have different units — kg CO₂, litres of water,
kg of methane? How do you compare them?"**
Good question — and that is exactly the problem the next step in LCA is
designed to solve. The inventory is deliberately *not* a single number.
It is a list, because different emissions cause different kinds of damage that
cannot simply be added. You would not add litres of water to kilograms of CO₂
any more than you would add apples to oranges. The step after the inventory
converts each flow into a comparable unit (like "kg CO₂ equivalent") so they
can be compared and totalled. That conversion step is called characterization.

**"What if a process has no emissions in the recipe card?"**
Then it contributes nothing to those inventory entries. A process can appear
in the supply chain purely as a transformation step — taking materials from one
upstream process and passing them to the next — without releasing any direct
emissions itself. The inventory only counts what actually crosses into the
natural world.

**"Is the inventory the same as the carbon footprint?"**
Not quite. The carbon footprint is one number — total greenhouse gas emissions
expressed in kg CO₂ equivalent. To get there, you first need the inventory
(which lists all the raw emissions — CO₂, methane, nitrous oxide — in their
original units), then you convert each one using a characterization factor
(e.g. methane × 27.9 to convert to CO₂ equivalent) and add them up. The
inventory comes first; the carbon footprint is derived from it.

**"What if the supply chain has many more steps?"**
You add more rows to the inventory table. Each additional process contributes
its own emissions and resource uses. The logic is always the same: scale each
process by how much it runs, then sum across all processes for each type of
flow. Longer supply chains usually mean larger inventories — and more
opportunities to find where the biggest problems are hiding.

---

## Tone and pacing

- Write as if talking to someone comfortable with Excel and email but who has
  never read a science report
- Never use a technical term without explaining it in the same sentence
- One question per message — never stack two questions together
- Keep responses to three to five sentences per turn
- If the student seems stuck, offer a multiple-choice prompt: "Would you say
  the inventory is (a) the final impact score, (b) a list of all the raw
  emissions and resources per unit of product, or (c) just the emissions
  from one process?"
- Phrases that help: "This is a perfectly normal question", "You are asking
  exactly the right thing", "This trips a lot of people up at first"
- End every response with either a question or a clear invitation to continue

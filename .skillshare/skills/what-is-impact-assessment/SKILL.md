---
version: 0.2
name: what-is-impact-assessment
author: Junghyun Choi (elenachoi1)
description: >
  Teaching skill for the LCA concept of life cycle impact assessment (LCIA) —
  the step that converts the raw inventory of emissions and resource use
  (kg of CO2, kg of methane, kg of ammonia, litres of water) into a small set
  of comparable impact category scores, using conversion numbers called
  characterization factors. Invoke as /what-is-impact-assessment <case-study>,
  for example /what-is-impact-assessment wool_yarn or
  /what-is-impact-assessment cotton_fiber. The skill reads the recipe card and
  lca_results.md for that case study and teaches the concept using a
  currency-exchange analogy and fashion or retail business context. Designed
  for FIT students with no science or coding background. Builds directly on
  the life-cycle-inventory skill. Four to five exchanges to complete.
---

## What this skill does

This skill teaches **life cycle impact assessment (LCIA)** — the step in LCA
that turns the raw inventory into a small set of meaningful scores.

Students who have completed the inventory skill know that the inventory is a
list: so many kilograms of CO₂, so many kilograms of methane, so many litres
of water, all crossing the boundary between the human-made world and nature
to deliver one unit of product. But that list has a problem — you cannot add
litres of water to kilograms of CO₂, and you cannot say that 1 kg of methane
is "the same size" of problem as 1 kg of CO₂, because methane traps far more
heat in the atmosphere.

LCIA solves this. It uses scientifically-derived conversion numbers called
**characterization factors** to convert every flow into a common unit *within
its own type of damage* — for example, every greenhouse gas gets converted
into "kg of CO₂ equivalent" so they can be added into one climate change
score. Other factors convert flows into "kg of SO₂ equivalent" for
acidification, or "kg of PM 2.5 equivalent" for particle pollution. The result
is a short profile of scores — one number per type of environmental damage —
instead of one giant, meaningless list of mismatched units.

A student who completes this skill will be able to:
- Explain what a characterization factor is and why it is needed
- Multiply an inventory flow by its characterization factor to get its
  contribution to an impact score
- Understand why a single substance (like ammonia) can contribute to more
  than one impact category at once
- Explain why LCIA reports several separate scores rather than one combined
  "total damage" number

This skill is for business and retail management students at FIT. It assumes
no science or technical background. The tone should be warm, encouraging, and
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
- From the recipe card YAML frontmatter: `name` and `processes`
- `bundle["lca_results"]["lci"]` — the compiled inventory totals (starting point)
- `bundle["lca_results"]["lcia"]` — the TRACI 2.2 impact category scores (destination)

No separate `run_lca` call is needed — all results are pre-computed in the bundle.

Everything you teach comes from what is in these results. Do not invent
numbers. The worked examples below give you the exact characterization
factors already verified against each case study's results, so you do not
need to derive them yourself — just use the ones provided per case study.

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

> "Imagine you run a retail chain with stores in the US, the UK, and Japan.
> At the end of the month, your US stores report $40,000 in sales, your UK
> stores report £25,000, and your Japan stores report ¥3,000,000.
>
> Here is the question: can you find your total global sales just by adding
> 40,000 + 25,000 + 3,000,000? Why or why not — and what would you need to do
> first before those three numbers could be added together?"

Wait for the student to answer before moving on.

---

### Step 2 — Validate their answer and introduce impact assessment

Whatever the student says, find what is right about it.

- If they said you need to convert to one currency first: "Exactly — you'd
  use the day's exchange rate to convert pounds and yen into dollars, and
  only then could you add the three numbers together into one meaningful
  total."
- If they said the numbers can't simply be added: "You've spotted the key
  problem — dollars, pounds, and yen are different units, and adding them
  directly would produce a meaningless number."
- If they were unsure: "The issue is that $40,000, £25,000, and ¥3,000,000
  are in three different currencies. Before you can add them, you have to
  convert each one into the same currency using that day's exchange rate."

Then introduce the concept:

> "Life cycle assessment has exactly this problem. The inventory you've
> already learned about lists emissions in their own original units — kg of
> CO₂, kg of methane, kg of ammonia, litres of water. You cannot add a
> kilogram of methane to a kilogram of CO₂ any more than you can add pounds
> to yen — they cause different *kinds* of environmental damage at different
> intensities.
>
> The step that solves this is called **life cycle impact assessment**, or
> **LCIA**. It uses conversion numbers — called **characterization
> factors** — that work just like exchange rates. Each factor tells you how
> much damage one kilogram of a substance causes, *relative to* a reference
> substance, for a specific type of damage. For climate change, the
> reference substance is CO₂, so every other greenhouse gas gets converted
> into 'kg of CO₂ equivalent.' Once everything is in the same unit, you can
> finally add it up into one score."

---

### Step 3 — Walk through the worked example for the case study

Introduce the product:

> "Let's convert the inventory for **[name]** into impact scores together."

Show the supply chain diagram by calling the `get_lca_svg` MCP tool
and displaying the returned SVG inline:
```
get_lca_svg(recipe_card="<content from get_case_study>", graph_type="structure")
```

Then use the matching block below for the chosen case study.

**For wool_yarn:**

> "Here is the compiled inventory you already built in the last skill:
>
> | Flow | Inventory total |
> |---|---|
> | Carbon dioxide | 2.55 kg |
> | Methane | 0.44 kg |
> | Water | 30 L |
>
> For the **Global warming** impact category, the characterization factors
> (the 'exchange rates') are:
> - Carbon dioxide → **1** kg CO₂-eq per kg (CO₂ is the reference substance,
>   so its own factor is always 1)
> - Methane → **25** kg CO₂-eq per kg (methane traps far more heat than CO₂
>   per kilogram, which is why this factor is so much bigger than 1)
>
> I've already converted the CO₂: 2.55 kg × 1 = 2.55 kg CO₂-eq. Can you
> convert the methane the same way — multiply 0.44 kg by its factor of 25 —
> and then add the two converted numbers together to get the total Global
> warming score?"

**For cotton_fiber:**

> "Here is the compiled inventory you already built in the last skill:
>
> | Flow | Inventory total |
> |---|---|
> | Carbon dioxide | 1.5 kg |
> | Nitrous oxide | 0.015 kg |
> | Ammonia | 0.01 kg |
> | Water | 8,000 L |
>
> For the **Global warming** impact category, the characterization factors
> are:
> - Carbon dioxide → **1** kg CO₂-eq per kg
> - Nitrous oxide → **298** kg CO₂-eq per kg (nitrous oxide is an extremely
>   potent greenhouse gas — almost 300 times more powerful than CO₂, kilogram
>   for kilogram)
>
> I've already converted the CO₂: 1.5 kg × 1 = 1.5 kg CO₂-eq. Can you convert
> the nitrous oxide — multiply 0.015 kg by its factor of 298 — and then add
> the two together to get the total Global warming score?"

**For polyester_tshirt:**

> "Here is the compiled inventory you already built in the last skill:
>
> | Flow | Inventory total |
> |---|---|
> | Carbon dioxide | 2.16 kg |
> | Methane | 0.015 kg |
>
> For the **Global warming** impact category, the characterization factors
> are:
> - Carbon dioxide → **1** kg CO₂-eq per kg
> - Methane → **25** kg CO₂-eq per kg
>
> I've already converted the CO₂: 2.16 kg × 1 = 2.16 kg CO₂-eq. Can you
> convert the methane — multiply 0.015 kg by its factor of 25 — and then add
> the two together to get the total Global warming score?"

Wait for the student's answer before moving on.

---

### Step 4 — Reveal the full impact profile and ask a what-if question

Validate the student's calculation, then show the full TRACI 2.2 profile for
the case study — including the categories that scored zero — and ask a
what-if question connecting to a business decision.

**For wool_yarn** (expected answer: 0.44 × 25 = 11.0, plus 2.55 = **13.55 kg
CO₂-eq**):

> "Exactly — 0.44 × 25 = 11.0, plus the 2.55 from CO₂ = **13.55 kg CO₂-eq**.
> That matches the real openLCA result. Here is the full impact profile —
> all eight TRACI 2.2 categories for one kg of wool yarn:
>
> | Impact category | Score | Unit |
> |---|---:|---|
> | Global warming | **13.55** | kg CO₂-eq |
> | Smog formation | 0.0063 | kg O₃-eq |
> | Acidification | 0 | kg SO₂-eq |
> | Human health — particulate matter | 0 | PM 2.5-eq |
> | Eutrophication (freshwater) | 0 | kg P-eq |
> | Human health — cancer | 0 | CTUcancer |
> | Human health — non-cancer | 0 | CTUnoncancer |
> | Ozone depletion | 0 | kg CFC-11-eq |
>
> Notice that six categories are exactly zero. That's not a mistake — it
> means none of the flows in this particular supply chain (just CO₂, methane,
> and water) happen to match the substances that drive those other kinds of
> damage. A zero score never means 'no data' — it means 'nothing here causes
> this type of harm.'
>
> Here's the what-if: methane makes up only 0.44 kg out of the 2.99 kg of raw
> emissions (CO₂ + methane combined) — about 15% of the *raw* weight. But
> after characterization, it makes up 11.0 out of 13.55 kg CO₂-eq — about
> 81% of the *climate* score. Why does methane's share grow so much once you
> apply the characterization factor?"

**For cotton_fiber** (expected answer: 0.015 × 298 = 4.47, plus 1.5 = **5.97
kg CO₂-eq**):

> "Exactly — 0.015 × 298 = 4.47, plus the 1.5 from CO₂ = **5.97 kg CO₂-eq**.
> That matches the real openLCA result. Here is the full impact profile —
> all eight TRACI 2.2 categories for one kg of cotton fiber:
>
> | Impact category | Score | Unit |
> |---|---:|---|
> | Global warming | **5.97** | kg CO₂-eq |
> | Acidification | **0.0188** | kg SO₂-eq |
> | Human health — particulate matter | **0.000667** | PM 2.5-eq |
> | Smog formation | 0 | kg O₃-eq |
> | Eutrophication (freshwater) | 0 | kg P-eq |
> | Human health — cancer | 0 | CTUcancer |
> | Human health — non-cancer | 0 | CTUnoncancer |
> | Ozone depletion | 0 | kg CFC-11-eq |
>
> Notice something interesting: the 0.01 kg of ammonia from the cotton farm
> shows up in *two* categories at once — Acidification (0.01 × 1.88 = 0.0188
> kg SO₂-eq) and particulate matter (0.01 × 0.0667 = 0.000667 PM 2.5-eq).
> One substance, two completely different kinds of damage, two separate
> scores.
>
> Here's the what-if: a cotton brand is told their fertilizer use is the
> source of nearly all the acidification and particulate matter scores —
> not the climate score, which is dominated by CO₂ and N₂O instead. If a
> sustainability manager only tracked Global warming, would they have any
> idea their farms were contributing to acid rain and air-quality damage?"

**For polyester_tshirt** (expected answer: 0.015 × 25 = 0.375, plus 2.16 =
**2.535 kg CO₂-eq**):

> "Exactly — 0.015 × 25 = 0.375, plus the 2.16 from CO₂ = **2.535 kg
> CO₂-eq**. That matches the real openLCA result. Here is the full impact
> profile — all eight TRACI 2.2 categories for one polyester T-shirt:
>
> | Impact category | Score | Unit |
> |---|---:|---|
> | Global warming | **2.535** | kg CO₂-eq |
> | Smog formation | 0.000216 | kg O₃-eq |
> | Acidification | 0 | kg SO₂-eq |
> | Human health — particulate matter | 0 | PM 2.5-eq |
> | Eutrophication (freshwater) | 0 | kg P-eq |
> | Human health — cancer | 0 | CTUcancer |
> | Human health — non-cancer | 0 | CTUnoncancer |
> | Ozone depletion | 0 | kg CFC-11-eq |
>
> Here's the what-if: almost all of this shirt's Global warming score comes
> from the polyester fiber and assembly steps, not the methane leaking from
> the oil well two steps upstream. If a brand switched to recycled polyester
> and eliminated the oil extraction step entirely, would the Global warming
> score drop a lot, a little, or barely at all? (Hint: look back at how much
> of the 2.535 kg CO₂-eq came from oil extraction's methane versus the other
> two steps.)"

Wait for the student's answer before moving on.

---

### Step 5 — Connect to a business decision and close

End with one practical connection to something a fashion or retail
professional would actually face.

- **For sustainability reporting teams:**
  > "When a brand publishes 'our product has a carbon footprint of X kg
  > CO₂-eq,' that number is the output of exactly this process — every raw
  > emission converted with a characterization factor and added up. If you
  > ever see a footprint reported in 'kg of emissions' without saying
  > CO₂-equivalent, ask what they actually measured — raw kilograms of mixed
  > gases is not a real number."

- **For category managers comparing suppliers:**
  > "Two suppliers might report the same Global warming score but very
  > different Acidification or particulate matter scores, because those
  > scores come from different substances entirely. A buyer who only checks
  > one impact category can miss real differences in environmental harm
  > between two seemingly similar products."

- **For product developers:**
  > "Characterization factors are why 'natural' materials don't automatically
  > mean 'low impact.' Cotton's water and nitrogen-based emissions score high
  > on acidification and particulate matter even though no fossil fuel is
  > burned — while a synthetic fiber might score worse on climate but better
  > elsewhere. The impact profile, not a single number, tells the real
  > story."

Then close with an invitation to continue:

> "Impact assessment is the last step that turns raw inventory data into the
> scores you see in a finished LCA report. From here, the natural next
> question is: across this whole supply chain, which single process is
> responsible for most of the damage — and that is exactly what a hotspot
> analysis answers. Would you like to explore that, or is there anything
> about characterization factors or impact categories you'd like to look at
> more closely first?"

---

## LCIA quick reference

Use this only when a student asks for a summary or wants to see the steps
laid out clearly. Do not recite it unprompted.

| Step | What happens | Output |
|---|---|---|
| 1. Start with the inventory | Take the compiled list of raw flows per functional unit | Inventory table |
| 2. Pick an impact category | Choose a type of damage to measure, e.g. climate change | Category name |
| 3. Apply characterization factors | Multiply each relevant flow by its factor for that category | Converted contributions |
| 4. Sum within the category | Add the converted contributions together | One impact score |
| 5. Repeat for each category | Different flows matter for different categories | Full impact profile |

### TRACI 2.2 — the eight categories used in this project

| Category | Unit | Plain-English meaning |
|---|---|---|
| Global warming | kg CO₂-eq | Contribution to climate change |
| Acidification | kg SO₂-eq | Contribution to acid rain |
| Smog formation | kg O₃-eq | Contribution to ground-level smog |
| Human health — particulate matter | PM 2.5-eq | Fine particle health damage |
| Eutrophication (freshwater) | kg P-eq | Excess nutrients causing algal blooms |
| Human health — cancer | CTUcancer | Cancer risk from toxic substances |
| Human health — non-cancer | CTUnoncancer | Other toxic health impacts |
| Ozone depletion | kg CFC-11-eq | Damage to the stratospheric ozone layer |

---

## Common student questions

**"Why does Global warming for wool yarn add up to 13.55 when the raw
emissions only weigh 2.99 kg?"**
Because characterization factors can be much bigger than 1. Methane's factor
of 25 means each kilogram of methane counts as if it were 25 kilograms of
CO₂ for climate purposes. The "equivalent" weight goes up even though the
actual physical weight of gas released did not change — what changed is how
much climate damage that weight causes.

**"Why is acidification 0 for wool yarn but not for cotton fiber?"**
Because acidification in TRACI 2.2 is driven by substances like ammonia and
sulfur dioxide. Wool yarn's inventory only contains CO₂, methane, and water
— none of which has an acidification factor — so the category scores exactly
zero. Cotton fiber's inventory contains ammonia, which does have an
acidification factor, so it scores above zero. The zero is a real result, not
a missing one.

**"Where do characterization factors actually come from?"**
From scientific research, not from this project. They are calculated by
environmental scientists using climate models, atmospheric chemistry models,
and toxicology studies, then published as part of a standardized method —
in this project, that method is called TRACI 2.2, built by the US
Environmental Protection Agency. The numbers update over time as science
improves, which is why you'll sometimes see slightly different factors (for
example, methane's GWP factor) reported in different years or methods.

**"Why not just add all eight scores into one giant number?"**
Because they measure fundamentally different kinds of harm — climate change,
acid rain, cancer risk, ozone depletion — that cannot be meaningfully
combined any more than you could add "number of store complaints" to "number
of late deliveries" and call it one customer-service score. Keeping them
separate lets a business see exactly where its biggest problems are, rather
than hiding them inside one number.

**"Is this the final step of an LCA?"**
For getting a number, yes — this is what produces the scores reported in a
finished LCA. There is an optional further step called normalization and
weighting, which converts the eight scores into one combined index by
deciding how much each category "matters" relative to the others — but that
requires value judgments about which kinds of damage are worse, so TRACI 2.2
deliberately stops short of doing it for you.

---

## Tone and pacing

- Write as if talking to someone comfortable with Excel and email but who has
  never read a science report
- Never use a technical term without explaining it in the same sentence
- One question per message — never stack two questions together
- Keep responses to three to five sentences per turn
- If the student seems stuck, offer a multiple-choice prompt: "Would you say
  a characterization factor is (a) the raw amount of a substance released,
  (b) a conversion number showing how much damage one kilogram of a substance
  causes relative to a reference substance, or (c) the name of a chemical?"
- Phrases that help: "This is a perfectly normal question", "You are asking
  exactly the right thing", "This trips a lot of people up at first"
- End every response with either a question or a clear invitation to continue

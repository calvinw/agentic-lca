# /what-is-impact-assessment cotton_fiber
**Skill version:** 0.1
**Student:** elena
**Model:** sonnet-4-6
**Date:** 2026-06-16

**AI:** Let's get started. Before any LCA terms, here's a question to set up the big idea.

Imagine you run a retail chain with stores in the US, the UK, and Japan. At the end of the month, your US stores report $40,000 in sales, your UK stores report £25,000, and your Japan stores report ¥3,000,000.

Here's the question: can you find your total global sales just by adding 40,000 + 25,000 + 3,000,000? Why or why not — and what would you need to do first before those three numbers could be added together?

**Student:** You'd need to convert each currency to a common one first

**AI:** Exactly — you'd use the day's exchange rate to convert pounds and yen into dollars, and only then could you add the three numbers together into one meaningful total.

Life cycle assessment has exactly this problem. The inventory you've already learned about lists emissions in their own original units — kg of CO₂, kg of nitrous oxide, kg of ammonia, litres of water. You cannot add a kilogram of nitrous oxide to a kilogram of CO₂ any more than you can add pounds to yen — they cause different *kinds* of environmental damage at different intensities.

The step that solves this is called **life cycle impact assessment**, or **LCIA**. It uses conversion numbers — called **characterization factors** — that work just like exchange rates. Each factor tells you how much damage one kilogram of a substance causes, *relative to* a reference substance, for a specific type of damage. For climate change, the reference substance is CO₂, so every other greenhouse gas gets converted into "kg of CO₂ equivalent." Once everything is in the same unit, you can finally add it up into one score.

Let's convert the inventory for **Cotton Fiber** into impact scores together.

[![Cotton Fiber supply chain — structure](skills_references/cotton_fiber/product_graph_structure.svg)](skills_references/cotton_fiber/product_graph_structure.svg)
`skills_references/cotton_fiber/product_graph_structure.svg`

Here is the compiled inventory you already built in the last skill:

| Flow | Inventory total |
|---|---|
| Carbon dioxide | 1.5 kg |
| Nitrous oxide | 0.015 kg |
| Ammonia | 0.01 kg |
| Water | 8,000 L |

For the **Global warming** impact category, the characterization factors are:
- Carbon dioxide → **1** kg CO₂-eq per kg
- Nitrous oxide → **298** kg CO₂-eq per kg (nitrous oxide is an extremely potent greenhouse gas — almost 300 times more powerful than CO₂, kilogram for kilogram)

I've already converted the CO₂: 1.5 kg × 1 = 1.5 kg CO₂-eq. Can you convert the nitrous oxide — multiply 0.015 kg by its factor of 298 — and then add the two together to get the total Global warming score?

**Student:** 0.015 × 298 = 4.47, plus 1.5 = 5.97

**AI:** Exactly — 0.015 × 298 = 4.47, plus the 1.5 from CO₂ = **5.97 kg CO₂-eq**. That matches the real openLCA result. Here is the full impact profile — all eight TRACI 2.2 categories for one kg of cotton fiber:

| Impact category | Score | Unit |
|---|---:|---|
| Global warming | **5.97** | kg CO₂-eq |
| Acidification | **0.0188** | kg SO₂-eq |
| Human health — particulate matter | **0.000667** | PM 2.5-eq |
| Smog formation | 0 | kg O₃-eq |
| Eutrophication (freshwater) | 0 | kg P-eq |
| Human health — cancer | 0 | CTUcancer |
| Human health — non-cancer | 0 | CTUnoncancer |
| Ozone depletion | 0 | kg CFC-11-eq |

Notice something interesting: the 0.01 kg of ammonia from the cotton farm shows up in *two* categories at once — Acidification (0.01 × 1.88 = 0.0188 kg SO₂-eq) and particulate matter (0.01 × 0.0667 = 0.000667 PM 2.5-eq). One substance, two completely different kinds of damage, two separate scores.

Here's the what-if: a cotton brand is told their fertilizer use is the source of nearly all the acidification and particulate matter scores — not the climate score, which is dominated by CO₂ and N₂O instead. If a sustainability manager only tracked Global warming, would they have any idea their farms were contributing to acid rain and air-quality damage?

**Student:** so can you explain to me about this skill easily?

**AI:** Of course — totally normal to want a quick recap. Here's the whole idea in the simplest way I can put it:

**The problem:** When you make something (like cotton fiber), the farm and factory release several different things into the air and water — carbon dioxide, nitrous oxide, ammonia, and so on. Each one is measured in its own units, like kilograms. But you can't just add "1.5 kg of CO₂" and "0.015 kg of nitrous oxide" together and call it one number — that's like adding dollars and yen without converting first. They're different "currencies" of pollution.

**The fix:** Impact assessment is the step that converts each pollutant into a common scale, the same way an exchange rate converts yen into dollars. Scientists have already figured out, for each substance, "how much worse is this than the reference substance, kilogram for kilogram?" That conversion number is called a **characterization factor**. Once everything is converted into the same unit (like "kg of CO₂ equivalent"), you can finally add them up into one meaningful score.

**The result:** Instead of one giant combined number for "all pollution," you get a short list of separate scores — one for climate change, one for acid rain, one for air quality, and so on — because those are genuinely different kinds of harm that shouldn't be mixed together.

That's really the whole skill in one paragraph. Does that land more clearly? If so, want to go ahead and take a stab at the what-if question above, or would you like me to re-explain any one part of it first?

**Student:** so this is a skill that unify all the different units in one to calculate the impact correct?

**AI:** You're very close — just one small but important correction.

It does unify units, but not into **one single unit for everything**. It converts the raw units into a common unit **within each type of damage** — so all the greenhouse gases (CO₂, nitrous oxide, methane) get converted into "kg CO₂ equivalent" for the climate change score. But the substances that cause acid rain get converted into a *different* common unit — "kg SO₂ equivalent" — for the acidification score. And particulate matter pollution gets converted into yet another unit, "PM 2.5 equivalent."

So you end up with several small, unified totals — one per type of damage — not one giant unified number for "total impact." That's deliberate: climate change and acid rain and air quality are genuinely different kinds of harm, and squashing them into a single number would hide which one actually matters for a given business decision.

Does that distinction make sense — many small "common currencies," one per category, rather than one currency for everything?

**Student:** make it to one sentence to understand.

**AI:** Impact assessment converts each pollutant's raw amount into a common unit *within its own type of damage* — using a conversion number called a characterization factor — so you get one meaningful score per damage type (climate, acid rain, air quality, etc.), not one giant combined score for everything.

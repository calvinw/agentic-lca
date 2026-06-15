# /life-cycle-inventory wool_yarn
**Skill version:** 0.1
**Student:** elena
**Model:** sonnet-4-6
**Date:** 2026-06-15

**AI:** Imagine you manage a clothing label. Your sustainability team wants to report the total water used to make one of your T-shirts. To get that number, you would need to look at every step — the cotton farm, the spinning mill, the dyeing factory, the finishing plant.

Each step has its own water usage figure. But here is the catch: the cotton farm might grow enough cotton for a million shirts in a year, while the dyeing factory handles only 800,000 shirts — because 20% of the fabric gets cut and wasted before it reaches that stage.

So here is the question: if you wanted to know the total water used for just *one* shirt, could you simply add up each factory's yearly water usage and divide by a million? Or would that give you the wrong answer — and if so, why?

**Student:** no, it would give the wrong answer

**AI:** Exactly — if the dyeing factory only handled 800,000 shirts, dividing its total water use by a million would undercount its contribution to each shirt. Each step needs to be scaled by how much it actually contributed to that one product. That careful scaled total is what LCA calls the **life cycle inventory**.

Think of it like a receipt from nature. Instead of money, it lists kilograms of CO₂ and litres of water. And instead of showing what each factory spent separately, it shows the combined total — the sum of everything that crossed from the human-made world into the natural world to make exactly one unit of the finished product.

Let's build the inventory for **Wool Yarn — 1 kg** together.

[![Wool Yarn supply chain — structure](../../skills_references/wool_yarn/product_graph_structure.svg)](../../skills_references/wool_yarn/product_graph_structure.svg)
`../../skills_references/wool_yarn/product_graph_structure.svg`

There are two steps in this supply chain. Before we can add up the emissions, we need to know how much each step runs to produce 1 kg of finished yarn:

- **P1 — Sheep Farming** runs **1.1 times** — it has to process 1.1 kg of raw wool to produce 1 kg of yarn, because some wool is lost in washing and combing
- **P2 — Wool Yarn Production** runs **1.0 times** — this is the final step and always runs exactly once

Here is the full inventory table. The P1 and P2 sections show what each step takes in and puts out. The Compiled LCI at the bottom is where we add everything up — I have filled in CO₂ to show you how it works, but I have left methane blank for you to calculate.

| Process | Section | Name | Amount | Unit | Type | Comment |
|---|---|---|---|---|---|---|
| **P1 — Sheep Farming (×1.1)** | | | | | | |
| | Output | Raw wool | 1.0 | kg | Intermediate product | Transferred to P2 |
| | Emission | Carbon dioxide | 0.5 | kg | Emission to air | Farm energy and feed production |
| | Emission | Methane | 0.4 | kg | Emission to air | Enteric fermentation (sheep digestion) |
| **P2 — Wool Yarn Production (×1.0)** | | | | | | |
| | Input | Raw wool | 1.1 | kg | Intermediate product | From P1; 10% lost in washing and combing |
| | Output | Wool yarn | 1.0 | kg | Reference product | Functional unit |
| | Emission | Carbon dioxide | 2.0 | kg | Emission to air | Scouring hot water and spinning energy |
| | Extraction | Water | 30 | L | Resource from water | Scouring and washing |
| **Compiled LCI** | | | | | | |
| | Emission | Carbon dioxide | 2.55 | kg | Emission to air | P1: 1.1 × 0.5 = 0.55 + P2: 1.0 × 2.0 = 2.0 |
| | Emission | Methane | 0.44 | kg | Emission to air | P1 only: 1.1 × 0.4 = 0.44 |
| | Extraction | Water | 30 | L | Resource from water | P2 only |

The rule is always: **multiply first, then add.** The sheep farm runs 1.1 times and emits 0.4 kg of methane per run. The yarn mill emits no methane. Can you fill in the missing number?

**Student:** fill in all the answers

**AI:** The answer is 1.1 × 0.4 = **0.44 kg methane**. Here is the complete compiled LCI for 1 kg of wool yarn:

| Elementary flow | Compartment | Amount | Unit |
|---|---|---|---|
| Carbon dioxide | Air | 2.55 | kg |
| Methane | Air | 0.44 | kg |
| Water | Water | 30 | L |

This is the raw receipt from nature — everything that crossed into the natural world to produce 1 kg of wool yarn. Notice that the intermediate product (raw wool moving from the sheep farm to the mill) does not appear here at all, because it never left the human-made world.

The next step in LCA would be to convert these raw numbers into environmental impact scores — for example, multiplying methane by its global warming factor to find out how much it contributes to climate change compared to CO₂. That is what the scaling vector and impact assessment skills cover.

Would you like to explore that next, or is there anything about the inventory you would like to look at more closely?

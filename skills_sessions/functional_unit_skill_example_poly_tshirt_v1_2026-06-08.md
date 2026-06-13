# Example: `/functional-unit polyester_tshirt` (v1 — with structure graph and reference process)

This is a recorded example of the `functional-unit` teaching skill in action,
using the `polyester_tshirt` case study from `skills_references/polyester_tshirt/`.

This version demonstrates the updated skill flow where the structure diagram
and reference process are introduced automatically in Step 2 — without the
student having to ask for them.

---

## The conversation

---

**AI:** Two clothing brands both claim their polyester T-shirt has a lower
carbon footprint than the other's.

What is the first question you would ask before trusting either of those claims?

---

**Student:** How is this measured exactly?

---

**AI:** That's exactly the right instinct — "how is it measured?" is the
question that cuts through most sustainability marketing immediately.

The study we'll be working through in this lesson is called **Polyester T-shirt
— 1 unit**. It traces the climate impact of producing one polyester T-shirt,
following the supply chain from crude oil extraction all the way through to the
finished garment. It's a teaching example built for this course, so the numbers
are illustrative rather than from a specific brand — but they're calibrated to
be realistic.

Here's the supply chain diagram for this study:

![Polyester T-shirt supply chain — structure](../skills_references/polyester_tshirt/product_graph_structure.svg)

The rightmost box — **P3, T-shirt assembly** — has a special name in LCA: it's
called the **reference process**. That just means it's the finishing line — the
step that delivers the finished product. Everything to its left in the diagram
(the fiber factory, the oil well) exists only to supply it. The functional unit
is precisely what comes out of that box: the thing we're measuring, and the
point at which the study stops.

So back to your question — the most important part of "how is it measured?"
turns out to be: **measured per what?** That's what we're going to dig into
now. In LCA, this precise definition of what you're measuring is called the
**functional unit** — and it's the first and most important decision in any
study.

For this T-shirt study, the functional unit is: **1 polyester T-shirt, ready
for sale (approximately 200 g of fabric).**

If a competitor reports their footprint per kilogram of fabric instead of per
shirt, and their shirt happens to be heavier, could they make their product look
better than it really is just by choosing that unit?

---

**Student:** I think so but I'm not sure.

---

**AI:** That's a perfectly natural reaction — the intuition is right, the
mechanics just need a moment to click. Here's a concrete example with real
numbers.

Our shirt weighs 200 g and has a footprint of **2.58 kg CO₂ per shirt**. A
competitor's shirt weighs 300 g and has a footprint of **3.87 kg CO₂ per
shirt** — genuinely worse in total. But if they report **per kilogram of
fabric** instead, their number becomes 3.87 ÷ 0.3 = **12.9 kg CO₂ per kg**
— identical to ours at 2.58 ÷ 0.2 = **12.9 kg CO₂ per kg**. Their shirt uses
50% more material, but that fact has completely disappeared behind the unit
choice.

Flip it the other way and a heavier shirt can actually look *better* per
kilogram, because the fixed costs of running the factory get spread over more
fabric. The unit choice isn't just a technicality — it can completely reverse
a comparison.

This is why sustainability standards like the **Higg Index** — used widely
across the fashion industry — require the functional unit to be declared upfront
in any environmental claim. Without it, the number can't be verified or compared.

As a buyer or merchandiser, the habit to build is simple: whenever a supplier
hands you a carbon footprint number, the first question is always **"per what?"**
— and if they can't answer that clearly, the number isn't ready to act on.

Would you like to explore more examples of how unit choice can distort
comparisons, or shall we move on?

---

**Student:** Yes, can you give me some more examples?

---

**AI:** Here are three more from across fashion and retail, each showing a
different way the unit choice hides important information.

---

**Fast fashion vs quality**

Brand A sells a £15 T-shirt, footprint 2 kg CO₂, but it pills after 10 washes
and gets thrown away. Brand B sells a £60 T-shirt, footprint 4 kg CO₂, that
lasts 200 washes over three years.

- Measured **per garment**: Brand B looks twice as bad.
- Measured **per wear**: Brand A = 2 ÷ 10 = **0.20 kg CO₂**. Brand B = 4 ÷
  200 = **0.02 kg CO₂**. Brand B is ten times better.

The wrong unit here is per garment — it completely hides the durability
difference, which is the whole point of the comparison.

---

**Cotton tote bag vs disposable paper bag**

Measured per bag produced, a cotton tote has a footprint of ~7 kg CO₂ versus
~0.04 kg CO₂ for a paper bag — the tote looks 175 times worse. But used 200
times, the tote's per-use footprint drops to 0.035 kg CO₂ — lower than a
single paper bag.

The wrong unit here is per bag produced for a product designed to be reused.
A cradle-to-gate number always makes reusable products look worse than
disposables.

---

**Chiffon vs denim fabric**

A fabric supplier claims their chiffon (80 g per square metre) has a lower
footprint than denim (400 g per square metre), measured per square metre.
They're right — but a dress made from chiffon uses far more metres of fabric
than a pair of jeans, so the per-square-metre comparison is misleading when
the end products require very different amounts of material.

The right unit here is per kilogram for a raw material comparison, or per
finished garment if you want to compare actual products.

---

The pattern in all three cases is the same: the unit that makes a product look
good is usually the one that hides the most important fact.

---

## What this example demonstrates

- The structure diagram and reference process are now introduced automatically
  in Step 2 — the student did not need to ask for a graph; it appeared as part
  of the standard teaching sequence
- "Reference process" was introduced and defined in plain English the first time
  it appeared: "the finishing line — the step that delivers the finished product"
- The student arrived at the diagram already knowing what the reference process
  is and where the functional unit lives, before the term "functional unit" was
  even named — giving them a visual anchor that made the concept land more
  concretely
- The what-if question (per shirt vs per kg) was answered with genuine numbers
  from the recipe card (2.58 kg CO₂, 200 g), making the abstract unit-choice
  problem feel real and calculable
- The student asked for more wrong-unit examples unprompted — the reference
  table in the skill provided three clean cases (fast fashion vs quality, tote
  vs paper bag, chiffon vs denim) without the response feeling like a data dump
- Every technical term (LCA, functional unit, reference process, Higg Index,
  cradle-to-gate) was explained in plain English in the same sentence it appeared

# Example: `/functional-unit polyester_tshirt`

This is a recorded example of the `functional-unit` teaching skill in action,
using the `polyester_tshirt` case study from `skills_references/polyester_tshirt/`.

The skill reads `recipe_card.md` for that case study and teaches the concept
of functional unit using real data, Socratic questions, and fashion business context.

---

## The conversation

---

**AI:** Imagine you're a sustainability manager at a fashion brand, and two of
your T-shirt suppliers both hand you a report claiming their product has a lower
carbon footprint than the other.

What is the very first question you would ask before accepting either of those
claims?

---

**Student:** How was it measured?

---

**AI:** That's exactly the right instinct — and "how was it measured?" is the
question that separates a sustainability professional from someone who just reads
the headline number.

The most important part of "how was it measured?" is actually: **measured per
what?** Per shirt? Per kilogram of fabric? Per year of wearing? A T-shirt that
looks better per kilogram of material might look worse per finished garment if
it uses more fabric. The number is meaningless without knowing what it's attached
to.

In LCA — Life Cycle Assessment, the method used to calculate environmental impact
— this is called the **functional unit**. It's the precise definition of exactly
what is being measured, so that two products can be compared on equal footing.

For this polyester T-shirt study, the functional unit is: **1 polyester T-shirt,
ready for sale (approximately 200 g of fabric).**

Not per kilogram of polyester, not per year of wearing — per finished shirt at
the point it leaves the factory. That unit was chosen because it matches what a
buyer actually purchases and what a brand actually sells.

Here's a question to test that idea: what if one brand reports their footprint
**per shirt** and a competitor reports theirs **per kilogram of fabric** — and
the competitor's shirt happens to be heavier? Could the competitor make their
shirt look better than it really is just by choosing a different unit?

---

**Student:** Yes, but I'm not exactly sure how.

---

**AI:** That's a perfectly natural place to be — the intuition is right, the
mechanics just need a moment to click.

Here's a concrete example. Say Brand A's shirt weighs 200 g and has a footprint
of **2.58 kg CO₂ per shirt**. Brand B's shirt weighs 300 g and has a footprint
of **3.87 kg CO₂ per shirt** — actually worse in total. But if Brand B reports
**per kilogram of fabric** instead, their number becomes 3.87 ÷ 0.3 = **12.9 kg
CO₂ per kg**, while Brand A's becomes 2.58 ÷ 0.2 = **12.9 kg CO₂ per kg** too
— they look identical. Brand B hid the fact that their shirt uses 50% more
material just by switching the unit.

Flip it the other way and a heavier shirt can actually look *better* per
kilogram, because the fixed costs of running the factory get spread over more
fabric. The unit choice isn't just a technicality — it can completely reverse a
comparison.

This is why sustainability standards like the **Higg Index** (used widely in
fashion) require the functional unit to be declared upfront in any environmental
claim. Without it, the number can't be verified or compared — it's just a figure
floating in the air.

As a buyer or merchandiser, the habit to build is simple: whenever a supplier
hands you a sustainability number, the first question is always **"per what?"**
— and if they can't answer clearly, the number isn't ready to act on.

---

**Student:** So what are some other examples of functional units for fashion
business or retail clothing stores?

---

**AI:** That's a great question to sit with — and it shows you're already
thinking like someone who would design these studies, not just read them.

Here are some real examples from fashion and retail, each chosen for a different
reason:

- **Per garment** — the most common for finished products like T-shirts, jeans,
  or jackets. Matches what a customer buys and what a brand sells. Easy to
  communicate on a hangtag.
- **Per kilogram of fibre** — used when comparing raw materials like wool vs
  cotton vs polyester at the supplier level, before anyone has cut or sewn
  anything.
- **Per wear** — divides the total footprint by how many times a garment is worn
  over its lifetime. Favours durable, expensive items over cheap fast fashion.
  Used by brands like Patagonia to argue that a £300 jacket is actually lower
  impact than a £30 one.
- **Per square metre of fabric** — common in home textiles (curtains, upholstery)
  where the product is sold by area rather than by piece.
- **Per season's wardrobe** — occasionally used in academic research to compare
  the total impact of buying fast fashion vs buying less but better quality over
  a full year.

The choice always comes back to the same question: **what decision is this number
supposed to help someone make?** A sourcing manager comparing fibre suppliers
needs per kilogram. A customer choosing between two jackets needs per wear. A
brand reporting to investors might use per garment.

Would you like to try the same concept with a different product — or shall we
move on to the next part of the T-shirt study?

---

**Student:** Do you have a graph that shows this example?

---

**AI:** We have two supply chain diagrams for the polyester T-shirt — but they
show the structure of the supply chain (the three process boxes and arrows), not
a comparison between functional units. Here is the structure diagram:

![Polyester T-shirt supply chain — structure](../skills_references/polyester_tshirt/product_graph_structure.svg)

The functional unit lives at the **rightmost box — P3, T-shirt assembly**. That
is the reference process: the step that delivers exactly one finished T-shirt,
ready for sale. Everything to its left (the fiber factory, the oil well) exists
only to supply it. When the study says "1 polyester T-shirt, ready for sale," it
is pointing at the output of that box — the moment the shirt is complete and
the measurement stops.

A functional unit *comparison* chart — something that visually shows how the
same product looks different depending on which unit you choose — doesn't exist
yet in the reference materials, but it would be a useful addition.

Want to keep going with the T-shirt study and look at the supply chain in more
detail, or is there something else you'd like to explore?

---

## What this example demonstrates

- The opening question was framed as a real professional scenario (sustainability
  manager, two competing supplier claims) rather than an abstract definition —
  the student arrived at "how was it measured?" immediately, which is the right
  instinct
- The skill deepened "how was it measured?" into "per what?" before revealing
  the functional unit, so the concept landed with concrete motivation behind it
- The what-if example used real numbers from the recipe card (2.58 kg CO₂,
  200 g shirt) alongside a invented Brand B scenario — keeping the teaching
  grounded in the actual case study
- The student's follow-up question about other functional unit examples (not in
  the skill script) was answered naturally using fashion-specific contexts: per
  wear, per kg of fibre, per square metre, per season
- When the student asked for a graph, the skill was honest that the available
  diagrams show supply chain structure, not functional unit comparisons — then
  used the structure SVG to locate the functional unit within the diagram (the
  reference process box, P3) rather than deflecting the question
- Every technical term introduced (LCA, functional unit, Higg Index, reference
  process) was explained immediately in plain language without interrupting the
  flow of conversation

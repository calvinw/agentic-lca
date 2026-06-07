# Example: `/supply-chain polyester_tshirt`

This is a recorded example of the `supply-chain` teaching skill in action,
using the `polyester_tshirt` case study from `skills_references/polyester_tshirt/`.

The skill reads `recipe_card.md` for that case study and teaches students how
to read a supply chain diagram — what each box represents, what the arrows mean,
what "upstream" and "downstream" mean, and what the system boundary leaves out.

---

## The conversation

---

**AI:** Before we open any diagrams, I'd like you to think about something for a moment.

Picture a polyester T-shirt — the kind you might find in any high-street clothing
store. If you had to sketch out the journey that shirt took to exist — starting
from wherever the very first raw material comes from, all the way to the finished
garment ready on the shelf — how many steps do you think it would take, and what
would the very first step be?

There are no wrong answers here — just go with your instinct.

---

**Student:** Step getting the oil, step refining something, then a couple more
steps including transportation.

---

**AI:** That is a really strong instinct — and you nailed the most important part
straight away. Oil is exactly where this supply chain starts. Most people think
of a T-shirt and picture a fabric factory; you went all the way back to the well,
which is exactly the right place to start an LCA study.

For this teaching example we've simplified the chain down to three steps — oil
extraction, turning the oil into polyester fibre, and sewing the shirt. We've
left out refining as a separate step (it's bundled into the extraction stage)
and we've left out transport entirely for now, so we can focus on where the
emissions actually come from.

Let's look at the actual diagram. In the file panel on the left side of VS Code,
open this file:

```
skills_references/polyester_tshirt/product_graph_structure.svg
```

Click the arrow next to `skills_references`, then the arrow next to
`polyester_tshirt`, and click on `product_graph_structure.svg`. It should display
a picture with three boxes connected by arrows. Tell me when you can see it.

---

**Student:** OK I can see it — oil extraction is first, then fiber production,
then T-shirt assembly.

---

![Polyester T-shirt supply chain — structure](../skills_references/polyester_tshirt/product_graph_structure.svg)

---

**AI:** Perfect — you've read the diagram exactly right. Now let me walk you
through what each of those three boxes actually represents in the real world.

**Box 1 — Oil extraction** is an oil well. Crude oil is pumped out of the ground
here — the same oil that goes into petrol, plastic bottles, and, as we'll see,
your T-shirt. This is the very beginning of the supply chain — nothing comes
before it in this study.

**Box 2 — Polyester fiber production** is a chemical factory. It takes that crude
oil and breaks it down and reassembles it at a molecular level into a long
plastic-like thread called polyester. This is the step most people don't know
about — polyester isn't woven from a plant or an animal, it's manufactured from
petroleum.

**Box 3 — T-shirt assembly** is the garment factory — the step that probably
first comes to mind when you think of "making a T-shirt." Rolls of polyester
fabric arrive, and workers (and machines) cut and sew them into finished shirts.

Looking at the three boxes, which one do you think represents the finished product
— the thing that a customer actually buys?

---

**Student:** P3.

---

**AI:** Exactly right — P3, the T-shirt assembly step, is what we call the
**reference process**. In LCA, that just means it's the finishing line — the
step that delivers the thing we're actually measuring, which in this case is one
finished T-shirt ready for sale.

The way LCA works is that it always starts at that finishing line and works
*backwards* through the chain. So instead of asking "what does the oil well
produce?" it asks "what does the T-shirt factory need, and where does that come
from?"

Now let's look at the arrows connecting the boxes. Each arrow represents something
physically flowing from one step to the next — a material being handed off. The
arrow from P1 to P2 means the oil well sends crude oil to the chemical factory —
about 1.5 kg of crude oil is needed to make just 1 kg of polyester fibre. The
arrow from P2 to P3 means the chemical factory sends polyester fibre to the
garment factory — about 0.2 kg of fibre goes into one T-shirt.

Here's a question about direction: if you follow those arrows from left to right,
which end of the diagram is "upstream" — meaning closer to the raw materials —
and which end is "downstream" — meaning closer to the customer?

---

**Student:** Left is upstream and right to the reference process is downstream.

---

**AI:** Spot on. Left is upstream — towards the raw materials, further from the
customer — and right is downstream, towards the finished product. That language
comes up constantly in sustainability and sourcing conversations, so it's worth
knowing cold.

Now, one more thing the diagram doesn't show — and this is actually just as
important as what it does show. This study is what's called **"cradle to gate"**
— meaning it starts at the raw material (the "cradle," which here is the oil
well) and ends at the factory gate when the shirt is finished. Everything that
happens after that point is outside the boundary of this study.

What do you think happens to a T-shirt after a customer buys it that is NOT
captured in this diagram? Can you think of at least one step that's been left out?

---

**Student:** Washing and drying it, maybe throwing it away.

---

**AI:** Those are perfect examples — and they're actually two of the biggest
ones. Washing and drying a polyester T-shirt repeatedly over its lifetime can
add significantly to its total footprint, because tumble dryers use a lot of
energy. And disposal — whether it ends up in landfill, gets incinerated, or
(ideally) gets recycled — is another chapter of impact entirely. Neither of those
appears anywhere in this diagram.

This is why the scope declaration matters so much in any sustainability claim.
If a brand says "our T-shirt has a carbon footprint of 2.58 kg CO₂" — that
number is only valid *within this study's boundary*. Add in the washing, drying,
and end-of-life, and the real lifetime figure could be two or three times higher.

Here's the practical takeaway for anyone working in sourcing or buying: a
sourcing manager looking at this diagram can immediately see that two of the
three steps happen before the garment factory. That means switching to a factory
with greener electricity is only attacking one box out of three. The bigger lever
is further upstream — in how the fibre is made and where the oil comes from.
That's the kind of insight a supply chain map gives you before a single number
has been calculated.

In the next lesson we'll put numbers on this diagram — specifically, how much
each step needs to run to produce exactly one T-shirt. That's where it gets
interesting, because the oil well's contribution isn't as obvious as it looks.
Want to keep going?

---

## What this example demonstrates

- The skill opened with a guessing question before showing any diagram — the
  student arrived at the correct starting point (oil) through their own reasoning
- The student's answer included refining and transport (reasonable guesses that
  are left out of the model) — these were validated and explained rather than
  dismissed
- The structure diagram was introduced at the right moment, after the student had
  already formed a mental model of what to expect
- Each process box was explained in plain English tied to a real-world image
  (oil well, chemical factory, garment factory) — not just the technical label
- The "reference process" concept was introduced naturally at the point the
  student identified P3, rather than as an upfront definition
- Flow amounts (1.5 kg oil per kg fibre, 0.2 kg fibre per shirt) were woven into
  the arrow explanation — setting up the scaling vector lesson that follows
- The upstream/downstream vocabulary was confirmed and flagged as practically
  useful, not just academic
- The system boundary question produced two correct answers (washing/drying and
  disposal) that directly connected scope decisions to real-world impact magnitude
- The lesson closed with a business insight a sourcing manager could act on,
  before any numbers had been calculated

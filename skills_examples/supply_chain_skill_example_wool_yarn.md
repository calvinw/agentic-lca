# Example: `/supply-chain wool_yarn`

This is a recorded example of the `supply-chain` teaching skill in action,
using the `wool_yarn` case study from `skills_references/wool_yarn/`.

The skill reads `recipe_card.md` for that case study and teaches students how
to read a supply chain diagram — what each box represents, what the arrows mean,
what "upstream" and "downstream" mean, and what the system boundary leaves out.

---

## The conversation

---

**AI:** Think about a ball of wool yarn — the kind you might use to knit a
sweater or weave a scarf. Before it becomes yarn, it starts somewhere out in
the world as a raw material.

What do you think the very first step in that supply chain looks like?

---

**Student:** Sheep farm.

---

**AI:** Exactly right — and that's actually the most important step to get
right, because everything else in the chain flows from it.

This supply chain has just two steps — it's about as simple as a supply chain
gets, which makes it a great place to see how the pieces connect before we
tackle more complex ones.

Let's look at the actual diagram. In the file panel on the left side of VS Code,
open this file:

```
skills_references/wool_yarn/product_graph_structure.svg
```

Click the arrow next to `skills_references`, then the arrow next to `wool_yarn`,
and click on `product_graph_structure.svg`. It should show two boxes connected
by an arrow. Tell me when you can see it.

---

**Student:** OK I can see it.

---

![Wool yarn supply chain — structure](../skills_references/wool_yarn/product_graph_structure.svg)

---

**AI:** Great. Let me walk you through what each box represents in the real world.

**Box 1 — Sheep farming** is the farm where the sheep live. The sheep grow a
fleece over the course of a year, which is sheared off and sent away for
processing. This is the starting point — the very beginning of the wool supply
chain.

**Box 2 — Wool yarn production** is the mill. The raw fleece arrives here still
full of grease, dirt, and bits of grass. It gets washed (a process called
scouring), combed to align all the fibres (carding), and then twisted into yarn
(spinning). This is where the finished product — 1 kg of wool yarn — comes out
the other end.

Looking at those two boxes, which one do you think represents the finished
product — the thing that gets sold to a knitting brand or a textile manufacturer?

---

**Student:** Sold to knitting brand.

---

**AI:** Exactly right — the wool yarn mill (P2) is what we call the **reference
process**. That's the finishing line — the step that delivers the product we're
actually measuring, which in this study is 1 kg of yarn ready for a knitting
brand to buy.

LCA always starts at that finishing line and works backwards. So instead of
asking "what does the sheep farm produce?" it asks "what does the mill need,
and where does that come from?"

Now let's look at the arrow between the two boxes. That arrow represents raw
wool physically moving from the farm to the mill — and there's an interesting
detail in the numbers. The mill needs **1.1 kg of raw fleece to produce just
1.0 kg of finished yarn**. That extra 0.1 kg is lost during washing and combing
— dirt, grease, and short broken fibres that get removed in the process.

If you follow that arrow from left to right, which end is "upstream" — closer
to the raw material — and which end is "downstream" — closer to the customer?

---

**Student:** Left end is upstream.

---

**AI:** Spot on. The sheep farm on the left is upstream — further from the
customer — and the mill on the right is downstream, delivering the finished
product.

Now, one thing worth noticing about this diagram is what's *not* in it. This
study is what's called **"cradle to gate"** — it starts at the raw material
(the sheep farm is the "cradle") and ends at the mill gate when the yarn is
finished. Everything before the farm and everything after the sale is outside
the boundary.

Here's something to think about: sheep need to eat — and growing their feed
takes land, water, fertiliser, and energy. Why do you think the study didn't
include a "feed production" box upstream of the sheep farm?

---

**Student:** Too difficult to include maybe.

---

**AI:** That's a very reasonable answer — and you're touching on one of the
most honest challenges in LCA work. Feed production is genuinely difficult to
model: a flock of sheep grazes on pasture, eats supplementary feed from multiple
sources, and the land use varies hugely from farm to farm. Pinning down a single
reliable number is hard, and including uncertain data can actually make a study
*less* trustworthy, not more.

So yes — it's a simplification, but a deliberate one. Every LCA study has to
draw a line somewhere, and the study notes that the conclusions are only valid
within that boundary. A more detailed study of wool might include feed, land use
change, and even the energy used to make the shearing equipment — but it would
also take much longer and require far more data.

Here's the practical takeaway for a sustainability professional: a wool brand
looking at this diagram can immediately see that the sheep farm is upstream of
everything else. That means any improvement at the farm — lower-methane breeds,
better pasture management, renewable energy for farm machinery — flows through
automatically to the finished yarn's footprint. The mill can only do so much;
the real leverage is back at the farm.

In the next lesson we'll put numbers on this diagram — specifically, how much
each step needs to run to produce exactly 1 kg of yarn, and where the emissions
actually land. Want to keep going?

---

## What this example demonstrates

- The student identified the correct starting point (sheep farm) immediately and
  without prompting — the opening question was simple enough that it built
  confidence straight away
- The two-process chain (the simplest possible supply chain) let the diagram
  concepts land cleanly before introducing the more complex three-process
  polyester example
- The 1.1 kg → 1.0 kg waste detail was woven into the arrow explanation naturally,
  planting the seed for the scaling vector lesson without naming it yet
- The student answered the upstream/downstream question correctly but gave only
  half the answer ("left end") — the response confirmed it and completed the
  picture (farm = upstream, mill = downstream) without making the partial answer
  feel wrong
- The system boundary question ("why no feed production box?") produced a genuine
  and insightful student answer about data difficulty — which is exactly right,
  and was validated as such before being extended with the broader point about
  deliberate scope decisions
- The closing business insight was product-specific: farm-level improvements
  (breeds, pasture, energy) are the real lever — not the mill — because the farm
  is the only upstream node

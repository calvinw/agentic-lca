# Example: `/supply-chain polyester_tshirt` (v1 — with case study introduction)

This is a recorded example of the `supply-chain` teaching skill in action,
using the `polyester_tshirt` case study from `skills_references/polyester_tshirt/`.

This version demonstrates the updated skill flow where the case study is
introduced automatically in Step 2. It also includes a student question about
the downward "to Air" arrows on the diagram, which prompted an explanation of
emissions as elementary flows.

---

## The conversation

---

**AI:** Before we open any diagrams, think about a polyester T-shirt for a
moment.

If you had to sketch the journey of that shirt — starting from wherever the
raw materials come from, all the way to the finished garment on a shop rail
— how many steps do you think it would take, and what would the very first
step be?

---

**Student:** Well I know that polyester is basically oil before anything else.

---

**AI:** Exactly right — and that's the insight that surprises most people.
Polyester isn't a natural fibre, it's a petroleum product, so the supply chain
really does start at an oil well.

The study we'll be mapping in this lesson is called **Polyester T-shirt — 1
unit**. It traces the climate impact of producing one polyester T-shirt,
following the supply chain from crude oil extraction through to the finished
garment — and specifically shows how emissions from an oil well end up
attributed to a shirt hanging in a clothing store. It's a teaching example
built for this course, so the numbers are illustrative rather than from a
specific brand, but calibrated to be realistic.

This chain has **three processes**. Let's look at the diagram. In the file
panel on the left side of VS Code, open this file:

```
skills_references/polyester_tshirt/product_graph_structure.svg
```

Click the arrow next to `skills_references`, then `polyester_tshirt`, then
click `product_graph_structure.svg`. It should display three boxes connected
by arrows. Tell me when you can see it.

---

**Student:** OK I can see it.

---

![Polyester T-shirt supply chain — structure](../skills_references/polyester_tshirt/product_graph_structure.svg)

---

**AI:** Good. Let me walk you through what each of those three boxes represents
in the real world.

**Box 1 — Oil extraction** is an oil well. This is where crude oil is pumped
out of the ground — the very start of the supply chain. The same oil that goes
into petrol and plastic bottles is also the raw material for your T-shirt.

**Box 2 — Polyester fiber production** is a chemical factory. It takes that
crude oil and converts it at a molecular level into a long, thread-like plastic
called polyester. This is the step most people never think about — the fibre
isn't grown or spun from a natural source, it's manufactured from petroleum.

**Box 3 — T-shirt assembly** is the garment factory — the step that probably
comes to mind first when you think of making a T-shirt. Rolls of polyester
fabric arrive here and are cut and sewn into finished shirts.

Looking at those three boxes, which one do you think represents the finished
product — the thing that actually gets sold to a customer?

---

**Student:** The assembled shirt.

---

**AI:** Exactly right. P3 — T-shirt assembly — is what LCA calls the
**reference process**. That term just means it's the finishing line: the step
that delivers the finished product we're measuring. Everything to its left in
the diagram exists only to supply it — the chemical factory exists to feed the
garment factory, and the oil well exists to feed the chemical factory.

Now let's look at the arrows. Each arrow represents something physically flowing
from one step to the next — a material being handed off. There are two flows in
this diagram:

- **Oil well → Chemical factory**: the oil well sends crude oil to be converted
  into fibre. About **1.5 kg of crude oil** is needed to make just 1 kg of
  polyester fibre.
- **Chemical factory → Garment factory**: the fibre is sent on to be cut and
  sewn. About **0.2 kg of fibre** goes into one finished T-shirt.

Those two numbers are worth holding onto — they'll matter a lot in the next
lesson when we calculate how much each step has to run to produce exactly one
shirt.

Following those arrows from left to right — which direction is "upstream"
(towards the raw materials) and which is "downstream" (towards the customer)?

---

**Student:** Left is upstream, right is downstream. What are those arrows going
down "to Air"?

---

**AI:** Spot on for upstream and downstream — perfect.

Those downward arrows are a different kind of flow entirely. The arrows between
the boxes show materials moving *through* the supply chain — crude oil, polyester
fibre. But the downward arrows show things leaving the supply chain altogether
and going into the environment — specifically, gases released into the air as a
by-product of each step.

In LCA these are called **emissions** — or sometimes **elementary flows**,
meaning flows between the industrial system and the natural world. Each downward
arrow is labelled with a gas: CO₂ (carbon dioxide) and CH₄ (methane). Every
process in this supply chain releases some of these gases — the oil well from
drilling and flaring, the chemical factory from the energy-intensive
polymerisation process, and the garment factory from running its machinery.

These are the numbers that eventually get added up to calculate the carbon
footprint of the shirt. The supply chain arrows tell us *what* is made at each
step; the downward arrows tell us *what is released into the atmosphere* at each
step.

Now, one important thing the diagram doesn't show — what do you think happens
to a T-shirt after a customer buys it that is completely absent from this
picture? Can you think of at least one step that's been left out?

---

**Student:** Washing, disposing of the shirt.

---

**AI:** Both perfect examples — and two of the biggest ones. Washing and drying
a polyester T-shirt repeatedly over its life can add significantly to the total
footprint, because tumble dryers are energy-intensive. And disposal — whether
the shirt goes to landfill, gets incinerated, or is recycled — is another
chapter of impact entirely. Neither appears anywhere in this diagram.

This study is what's called **"cradle to gate"** — it starts at the raw material
(the "cradle," which here is the oil well) and ends at the factory gate when the
shirt is finished. The scope is a deliberate choice: every LCA study has to draw
a boundary somewhere, and conclusions are only valid within that boundary. A
brand claiming a low footprint based on a cradle-to-gate study hasn't said
anything about what happens when you wash or dispose of the shirt.

Here's the practical takeaway: a sourcing manager looking at this diagram can
immediately see that two of the three steps happen before the garment factory.
That means switching to a factory with greener electricity only addresses one
box out of three. The bigger lever is upstream — in how the fibre is made and
where the oil comes from. That's the kind of strategic insight a supply chain
map gives you before a single number has been calculated.

In the next lesson we'll put numbers on this diagram — specifically, how much
each step needs to run to produce exactly one T-shirt. That's where the compound
scaling comes in, and the oil well's contribution becomes surprisingly clear.
Want to keep going?

---

**Student:** So how do we figure out how much of the gases are emitted to the
air?

---

**AI:** Great question — and it's exactly what the next lesson is designed to
answer, so you're thinking ahead in exactly the right direction.

The short version: each process in the recipe card has a fixed emission rate —
for example, the oil well releases 0.20 kg of CO₂ and 0.05 kg of methane for
every kilogram of crude oil it produces. Those rates are built into the supply
chain description.

But knowing the rate per process isn't enough on its own. You also need to know
how much each process has to run to produce exactly one finished T-shirt. The
oil well doesn't run at full scale to make one shirt — it only runs a fraction
of its full cycle. Figuring out those fractions is called calculating the
**scaling vector**, and it's the subject of the next lesson.

Once you have both pieces — the emission rate and how much each process runs —
you multiply them together for every process and add everything up. That gives
you the total kg of CO₂ and methane released to produce one shirt, which is the
carbon footprint.

The supply chain map we've been looking at is the foundation for all of that —
you need to know the shape of the chain before you can do any of the maths.
That's why we started here.

Ready to move on to the scaling vector lesson?

---

## What this example demonstrates

- The student arrived at the correct starting point (oil) from their own
  knowledge before any diagram was shown — validating this immediately set
  a confident tone for the lesson
- The case study was introduced automatically in Step 2 (name, goal, teaching
  example disclaimer) before asking the student to open the diagram
- The student asked an unscripted question about the downward "to Air" arrows
  — this was answered naturally using the term "elementary flows" with an
  immediate plain-English explanation, without derailing the lesson sequence
- The distinction between supply chain arrows (materials moving between steps)
  and emission arrows (gases leaving the system into the environment) was made
  explicit and concrete
- "Reference process" was confirmed and defined when the student identified P3,
  with the explanation that everything to its left exists only to supply it
- The flow amounts (1.5 kg oil per kg fibre, 0.2 kg fibre per shirt) were
  flagged as worth remembering — planting a seed for the scaling vector lesson
- The system boundary question produced two correct answers (washing, disposal)
  and was connected directly to a sourcing insight: two of three steps happen
  before the factory, so switching factories alone won't solve the problem
- The student's closing question ("how do we figure out how much gas is emitted?")
  was answered with a preview of the scaling vector concept, bridging naturally
  to the next lesson without going off-script

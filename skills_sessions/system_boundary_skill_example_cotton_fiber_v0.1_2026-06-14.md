# System Boundary Skill Session
**Skill version:** 0.1  
**Case study:** cotton_fiber  
**Date:** 2026-06-14  

---

**Skill:** Imagine you are reviewing a restaurant receipt at the end of a work dinner. The receipt only shows the food and drinks your table ordered — it does not include the taxi you took to get there, the parking fee your colleague paid, or the round of drinks someone bought at the bar next door.

Here's the question: if someone added up only the restaurant receipt to figure out the total cost of the evening, would that number be accurate — and what would be missing from it?

**Student:** no it would not

**Skill:** You've got it — and that gap between the receipt and the full picture is the central tension in LCA too.

In Life Cycle Assessment, every study has a "receipt" — a defined set of steps it covers and a defined set it does not. That boundary is called the **system boundary**. Think of it as a fence drawn around part of the supply chain. Everything inside the fence is measured and counted. Everything outside the fence is ignored — even if it causes real environmental harm.

The system boundary is not a flaw — it is a deliberate choice. But it means the number you get at the end of a study only tells you about what was inside the fence.

Let's look at a real example — a study of **Cotton Fiber**. The goal is to calculate the environmental impact of producing 1 kg of ginned cotton fiber, tracing the supply chain from the fertilizer factory through to the cotton farm.

Here is the supply chain diagram:

![Cotton Fiber supply chain — structure](../skills_references/cotton_fiber/product_graph_structure.svg)

Each box in this diagram is a step the study decided to **include**. The fence — the system boundary — runs around both of these boxes together. Any step that does not appear is outside the fence and was not counted.

Looking at the diagram, can you spot any steps you might expect to be there that are *not* shown? For example — think about what the cotton farm needs to operate beyond fertilizer. What else goes into growing cotton that might have its own environmental footprint?

**Student:** harvesting, pesticides

**Skill:** Exactly right — and those are two really important ones.

Pesticides and herbicides have to be manufactured in a chemical factory before they ever arrive at the farm — and that manufacturing process uses energy and releases emissions. But in this study, the production of pesticides is completely **outside the fence**. The study includes the fertilizer factory but stops there — the pesticide factory is not shown in the diagram and was not counted at all.

Harvesting is similar — the diesel fuel burned by the harvesting machinery does appear indirectly (it is folded into the CO₂ figure for the cotton farm), but the manufacturing of the harvesting machine itself was left out.

Here is the what-if question: if the study had also included the production of all the pesticides and herbicides used on the farm — which had to be manufactured somewhere before they arrived — do you think the total carbon footprint would look bigger or smaller than the number this study reports?

**Student:** bigger

**Skill:** Exactly — every time you pull something from outside the fence and bring it inside, the number goes up.

And this matters in a very practical way for anyone working in fashion or retail. Cotton has a reputation as a "natural" fiber — grown in a field, not made in a chemical plant. But this study already shows that just the fertilizer factory alone adds significantly to the footprint. If you also counted the pesticide factories, the seed production, the transport to the spinning mill, and eventually the disposal of the finished garment, the number would keep climbing with every step you added.

When a cotton supplier hands you an LCA result, the system boundary is the first thing to check — not the number. Two suppliers can report very different footprints for the same cotton simply because one drew a wider fence than the other. You can only compare them fairly if they used the same boundary — otherwise you are comparing two different receipts and assuming they cover the same meal.

The system boundary is one decision inside a bigger set called **goal and scope** — the opening chapter of every LCA study, where researchers decide why the study is being done, who it is for, and exactly where the fence gets drawn. Would you like to explore how boundary decisions fit into that bigger goal-and-scope picture, or is there anything about the boundary concept you'd like to dig into first?

**Student:** can people fudge the system boundary

**Skill:** This is a really good question — and the honest answer is yes, it happens.

It is not always outright lying. The most common version is simply choosing a conveniently narrow boundary and either not mentioning it clearly, or burying it in the fine print. A cotton supplier might publish a footprint number that only covers the farm itself — leaving out the fertilizer factory entirely — because that makes the number look smaller. Nothing in the report is technically false, but the reader walks away with an incomplete picture.

This is one of the main mechanisms behind **greenwashing** — making a product look more sustainable than it really is, not by inventing data, but by carefully choosing where the fence goes. In our cotton example, the fertilizer factory alone contributes about 0.7 kg of CO₂ equivalent per kg of cotton. Leave that out, and the footprint suddenly looks much more flattering.

The defence against this — both as a buyer and as a brand manager — is always to ask the same two questions when you see an LCA number: *"What is inside the fence?"* and *"What did you leave out, and why?"* A trustworthy study will answer both questions clearly and upfront.

Would you like to explore the full **goal and scope** concept next, where these boundary decisions get formally written down — or is there anything else about system boundary you'd like to dig into?

**Student:** this is good Im done can you end the scope

# /goal-and-scope cotton_fiber
**Skill version:** 0.1
**Student:** diana
**Model:** gpt-5-5
**Date:** 2026-06-24

**AI:** A cotton supplier wants an LCA, which means a life cycle assessment: a study of the environmental impact of making a product.

Should the study include only the cotton farm, or should it also include the fertilizer factory that makes the nitrogen fertilizer used on the field?

Where would you draw the line?

**Student:** at the farm

**AI:** That is a really practical instinct. If you are the cotton grower, the farm feels like the part you directly control, so starting and stopping there can seem fair.

The case study we’ll use is called **Cotton Fiber — 1 kg**. Its goal is to calculate the climate and eutrophication impact of producing **1 kg of ginned cotton fiber, ready for spinning**, from synthetic fertilizer production through cotton farming. This is a teaching example built for this course; the numbers are illustrative but realistic.

[![Cotton Fiber — 1 kg supply chain — structure](../../skills_references/cotton_fiber/product_graph_structure.svg)](../../skills_references/cotton_fiber/product_graph_structure.svg)
`../../skills_references/cotton_fiber/product_graph_structure.svg`

Each box in this diagram is a step the study decided to include. Deciding which boxes belong in the picture is what we call the **scope**, which means “what is inside the study and what is left out.”

Would you like to continue to the next step and look at the difference between the study’s **goal** and its **scope**?

**Student:** can you give me the path to the file

**AI:** The file path is:

`skills_references/cotton_fiber/product_graph.yaml`

**Student:** can you give me the path to the product graph

**AI:** The product graph path is:

`skills_references/cotton_fiber/product_graph_structure.svg`

**Student:** explain the graph

**AI:** This graph is the supply chain picture for the cotton fiber case study.

[![Cotton Fiber — 1 kg supply chain — structure](../../skills_references/cotton_fiber/product_graph_structure.svg)](../../skills_references/cotton_fiber/product_graph_structure.svg)
`../../skills_references/cotton_fiber/product_graph_structure.svg`

Each box is one step the study includes:

**P1 — Fertilizer production**  
This is the factory step that makes synthetic nitrogen fertilizer.

**P2 — Cotton farming**  
This is the farm step that grows the cotton and produces the final product: **1 kg of ginned cotton fiber, ready for spinning**.

The arrow from **P1** to **P2** means the cotton farm uses fertilizer made by the fertilizer factory.

So even though you first said “at the farm,” this graph shows why the study includes one upstream step. “Upstream” means the earlier supplier step, like a vendor that provides ingredients to a retailer.

The study is **cradle to gate**, which means it starts with an earlier material step and stops when the cotton fiber leaves the farm gate. It does **not** include spinning, fabric-making, sewing, store transport, customer washing, or disposal.

The main goal-and-scope lesson is: the final impact number depends on where we draw the fence around the supply chain. If we only counted the farm, we would miss the fertilizer factory’s impact.

**Student:** exit the skill

**AI:** Exited the `goal-and-scope` skill.

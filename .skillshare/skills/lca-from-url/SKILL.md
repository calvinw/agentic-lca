---
version: 0.1
name: lca-from-url
author: Calvin Williamson (calvinw)
description: >
  Use this skill when the user provides a URL to an LCA study, a published
  environmental report, or a product sustainability page and wants to turn it
  into a product_graph.yaml they can run and explore. Also triggers when the user
  names a well-known LCA study by title (e.g. "Cotton Inc. cotton fiber LCA",
  "IWTO wool LCA", "thredUP secondhand clothing study") and wants to recreate
  or remix it. Builds a base-case product graph plus 3–5 scenario variants
  (just like the Levi's jeans folder), then offers to run the analysis.
  Trigger phrases: "turn this into an LCA", "build a product graph from",
  "recreate this LCA", "make scenarios for", "use this study", "remix this LCA".
---

## What this skill does

This skill takes a URL pointing to a real LCA study (or a well-known study
name) and guides the student through turning the published data into a working
`product_graph.yaml` that can be analysed with the openLCA tools already set up
in this project.

It then creates **scenario variants** — alternative versions of the product graph
where one assumption is changed at a time — so the student can answer "what if?"
questions like:
- What if the factory used renewable energy?
- What if the garment were made from recycled fibre instead of virgin?
- What if the consumer washed the item less often?
- What if the material came from an organic farm?

This mirrors exactly how the Levi's 501 jeans folder (`lca_analysis/levis/`) is
structured — a base case plus named scenario product graphs.

---

## Step-by-step workflow

### Step 1 — Fetch and read the source

Use the WebFetch tool to retrieve the URL the student provided. Read the page
carefully and extract:

1. **What product or material is being studied** — be specific (e.g. "1 kg of
   greasy wool fiber at farm gate", not just "wool").
2. **The functional unit** — exactly what is one unit of the thing being studied?
3. **The life cycle stages covered** — does the study go cradle-to-gate, gate-to-gate,
   or cradle-to-grave? What stages are included?
4. **The supply chain nodes** — what are the main production steps? Aim for 3–6
   processes that cover the most important stages.
5. **The emissions and resources** — what greenhouse gases or other substances
   are reported? Find the per-unit numbers (e.g. kg CO₂ per kg fiber).
6. **The hotspot** — which stage or substance drives the majority of the impact?
7. **The key assumptions** — what country or grid is assumed? What allocation
   method? What use-phase behaviour?

If the URL returns a PDF or a summary page without full numerical data, say so
clearly to the student and use whatever numbers are available. Make clear which
numbers come from the source and which are your best estimates to fill gaps.

Always narrate what you found in plain English before building anything.
Example:
> "I've read the study. It covers one kilogram of wool fiber, starting from
> the sheep farm and ending at the wool broker — not including spinning or
> fabric production. The biggest source of CO₂ is methane from sheep digestion,
> which accounts for about 60% of the total. The study found roughly 17 kg of
> CO₂-equivalent per kilogram of raw wool."

---

### Step 2 — Map the supply chain

Before writing any code, draw out the supply chain for the student in plain
text. Use this format:

```
[Stage 1: Farm / Raw material] → [Stage 2: Processing] → [Stage 3: ...]
         ↓ CO₂                          ↓ CO₂
     (direct emissions)          (energy use)
```

Ask the student: "Does this look right to you? Is there a stage you think we
should add or remove?"

Give the student a moment to respond before continuing. If they say it looks
right, proceed to Step 3.

---

### Step 3 — Translate into a product graph

Create the folder and product graph:

```
lca_analysis/<study_name>/product_graph.yaml
```

Use the standard product graph format (YAML frontmatter). Follow these rules:

**Units:** Always include `kg: Mass` at minimum. Add `kWh: Electrical energy`
if electricity is in the model. Add other units as needed.

**FEDEFL flow names:** Use exact EPA FEDEFL names for all elementary flows:
- Carbon dioxide (not CO2, not "CO₂ to air")
- Methane (not CH4)
- Nitrous oxide (not N2O)
- Nitrogen oxides (not NOx)
- Sulfur dioxide (not SO2)

**LCIA section:** Always include at the bottom:
```yaml
lcia:
  method_name: "TRACI 2.2"
```

**Process naming:** Name processes with a number prefix for clarity:
`P1 — Sheep farm`, `P2 — Wool scouring`, etc.

**Emissions amounts:** Use the per-unit numbers from the study. If a stage's
emissions are reported per kg of output AND the output amount differs from 1.0,
adjust accordingly.

After writing the file, narrate to the student:
> "I've created the product graph at `lca_analysis/<name>/product_graph.yaml`. Here's
> a plain-English summary of what's in it: ..."

---

## Well-known textile LCAs you can recreate

If the student does not have a URL but wants to work from a published study,
here are the best-documented ones to suggest:

| Study | What it covers | Best for teaching |
|---|---|---|
| **Levi's 501 Jeans (2015)** | Full lifecycle of denim jeans | Multi-stage supply chains, consumer use hotspot |
| **Cotton Inc. U.S. Cotton LCA (2012)** | 1 kg cotton fiber, farm gate | Farm emissions, fertilizer N₂O |
| **IWTO Wool LCA** | 1 kg greasy wool, farm gate | Animal agriculture, methane from sheep |
| **Virgin Polyester LCA** | 1 kg PET fiber | Petroleum-based fibers, energy intensity |
| **Recycled Polyester (Repreve)** | 1 kg rPET fiber vs. virgin | Recycled vs. virgin comparison |
| **Viscose/Rayon LCA (IVL)** | 1 kg viscose fiber | "Natural-origin" but chemically intensive |
| **Nylon 6 LCA** | 1 kg virgin nylon | N₂O from production, high-impact fiber |
| **thredUP Secondhand LCA (2022)** | New vs. secondhand garment | System expansion, displacement credits |

For each of these, the GWP numbers and supply chain structure are published and
documented enough to build a faithful simplified model.

---

## Tone and explanation rules

- Always explain what you found before building anything.
- Never write a product graph silently — narrate every section as you write it.
- After creating files, tell the student exactly where to find them and how to
  open them (e.g. "look in the file explorer panel on the left side of VS Code").
- If a number is your estimate rather than from the source, say so explicitly.
- Keep every explanation grounded in business and retail context — connect the
  numbers to decisions a brand, buyer, or sustainability manager would actually make.

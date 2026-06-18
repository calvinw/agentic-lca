# LCA Results: Levi's 501 Jeans LCA — cradle to grave

Generated: 2026-06-18 17:49  |  openLCA system ID: `d1180022-b679-42f4-b071-55a414a8df69`

## Step 1 — Goal and Scope

**Goal:** Calculate the total CO₂ emitted over the full lifecycle of one pair of Levi's® 501® jeans (medium stone wash), tracing the supply chain from cotton farming through fabric production, garment manufacturing, distribution, consumer washing and drying, and end-of-life disposal. Based on Levi Strauss & Co.'s 2015 LCA study (US consumer use profile).

**Functional unit:** 1.0 pair — One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave

**Reference flow vector f:**

```
  f[1] = 0.0   (Raw cotton)
  f[2] = 0.0   (Denim fabric)
  f[3] = 0.0   (Finished jeans)
  f[4] = 1.0   (Levis 501 jeans full lifecycle)
  f[5] = 0.0   (Electricity)
```

## Step 2 — Technology Matrix A

Columns = processes, rows = products.  `+` = produced, `−` = consumed.

| | P1 — Grow and harvest cotton | P2 — Spin, dye, and weave denim fabric | P3 — Cut, sew, and finish jeans | P4 — Distribute, wash, dry, and dispose of jeans | P5 — Generate electricity |
|---|---:|---:|---:|---:|---:|
| **Raw cotton** | +1.00 | -1.25 |  0   |  0   |  0   |
| **Denim fabric** |  0   | +1.00 | -0.80 |  0   |  0   |
| **Finished jeans** |  0   |  0   | +1.00 | -1.00 |  0   |
| **Levis 501 jeans full lifecycle** |  0   |  0   |  0   | +1.00 |  0   |
| **Electricity** |  0   | -22.50 | -5.20 | -25.00 | +1.00 |

## Step 3 — Scaling Vector  s = A⁻¹ · f

How many times each process must run to deliver exactly f:

| Process | Scale factor |
|---|---:|
| P1 — Grow and harvest cotton | **1.0000** |
| P2 — Spin, dye, and weave denim fabric | **0.8000** |
| P3 — Cut, sew, and finish jeans | **1.0000** |
| P4 — Distribute, wash, dry, and dispose of jeans | **1.0000** |
| P5 — Generate electricity | **48.2000** |

## Step 4 — Intervention Matrix B

Columns = processes, rows = elementary flows (biosphere).
`+` = emission (exits to environment)  `−` = resource extraction (enters from environment).

| | P1 — Grow and harvest cotton | P2 — Spin, dye, and weave denim fabric | P3 — Cut, sew, and finish jeans | P4 — Distribute, wash, dry, and dispose of jeans | P5 — Generate electricity |
|---|---:|---:|---:|---:|---:|
| **Carbon dioxide** | +2.90 |  0   |  0   | +6.40 | +0.50 |
| **Nitrogen oxides** |  0   |  0   |  0   |  0   | +0.00 |
| **Sulfur dioxide** |  0   |  0   |  0   |  0   | +0.00 |

## Step 5 — LCI Results  B · s

**Emissions to environment:**

| Flow | Numpy result | openLCA result | Unit | Match |
|---|---:|---:|---|:---:|
| **Carbon dioxide** | 33.4000 | 33.4000 | kg | ✓ |
| **Nitrogen oxides** | 0.0434 | 0.0434 | kg | ✓ |
| **Sulfur dioxide** | 0.0289 | 0.0289 | kg | ✓ |

## Step 6 — Scaled Emissions by Process  (B · diag(s))

Each cell = emission rate × scaling factor.  Columns sum to the LCI totals in Step 5.

| Process | s | Carbon dioxide | Nitrogen oxides | Sulfur dioxide |
|---|---:|---:|---:|---:|
| P1 — Grow and harvest cotton | 1.0000 | 2.9000 | 0 | 0 |
| P2 — Spin, dye, and weave denim fabric | 0.8000 | 0 | 0 | 0 |
| P3 — Cut, sew, and finish jeans | 1.0000 | 0 | 0 | 0 |
| P4 — Distribute, wash, dry, and dispose of jeans | 1.0000 | 6.4000 | 0 | 0 |
| P5 — Generate electricity | 48.2000 | 24.1000 | 0.0434 | 0.0289 |
| **Total** | | **33.4000** | **0.0434** | **0.0289** |

## Step 7 — LCIA Results  (TRACI 2.2)

Characterization factors from the database. Each impact category score is the sum of all elementary flow contributions as computed by the openLCA engine.

| Impact Category | Score | Unit |
|---|---:|---|
| Ozone depletion | **0.000000** | kg CFC-11 eq |
| Ecotoxicity | **0.000000** | CTUe |
| Respiratory effects (Particulate) | **0.002081** | kg PM2.5 eq |
| Acidification | **0.059286** | kg SO2 eq |
| Carcinogenics | **0.000000** | CTUh |
| Global warming | **33.400000** | kg CO2 eq |
| Smog (Photochemical Oxidation Formation) | **1.075390** | kg O3 eq |
| Non carcinogenics | **0.000000** | CTUh |
| Eutrophication: freshwater | **0.000000** | kg P eq |
| Eutrophication: marine | **0.000222** | kg N eq |

## Summary

**LCIA Method:** TRACI 2.2

> **Ozone depletion: 0.000000 kg CFC-11 eq** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Ecotoxicity: 0.000000 CTUe** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Respiratory effects (Particulate): 0.002081 kg PM2.5 eq** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Acidification: 0.059286 kg SO2 eq** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Carcinogenics: 0.000000 CTUh** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Global warming: 33.400000 kg CO2 eq** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Smog (Photochemical Oxidation Formation): 1.075390 kg O3 eq** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Non carcinogenics: 0.000000 CTUh** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Eutrophication: freshwater: 0.000000 kg P eq** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
> **Eutrophication: marine: 0.000222 kg N eq** per 1.0 pair of One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave

## Product System Graphs

### Scaled (with amounts)

![Scaled](product_graph_scaled.svg)

### Structure (flow names only)

![Structure](product_graph_structure.svg)

---
*Generated by `lca_scripts/lca_analysis.py` using openLCA gdt-server v2*
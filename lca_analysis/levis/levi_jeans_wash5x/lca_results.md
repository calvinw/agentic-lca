# LCA Results: Levi's 501 Jeans — wash every 5 wears (Group 1, Scenario C)

Generated: 2026-06-14 02:12  |  openLCA system ID: `d21a2916-0a2e-4104-a795-c7e0925a8711`

## Step 1 — Goal and Scope

**Goal:** Reproduce the Levi's 2015 LCA consumer care scenario where the consumer washes their jeans once every 5 times they wear them — roughly twice as infrequently as the US average. US consumer, conventional washing machine, average mix of cold/warm water and tumble dry. Based on Levi Strauss & Co.'s 2015 LCA study.

**Functional unit:** 1.0 pair — One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears

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
| **Electricity** |  0   | -22.50 | -5.20 | -12.30 | +1.00 |

## Step 3 — Scaling Vector  s = A⁻¹ · f

How many times each process must run to deliver exactly f:

| Process | Scale factor |
|---|---:|
| P1 — Grow and harvest cotton | **1.0000** |
| P2 — Spin, dye, and weave denim fabric | **0.8000** |
| P3 — Cut, sew, and finish jeans | **1.0000** |
| P4 — Distribute, wash, dry, and dispose of jeans | **1.0000** |
| P5 — Generate electricity | **35.5000** |

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
| **Carbon dioxide** | 27.0500 | 27.0500 | kg | ✓ |
| **Nitrogen oxides** | 0.0320 | 0.0319 | kg | ✓ |
| **Sulfur dioxide** | 0.0213 | 0.0213 | kg | ✓ |

## Step 6 — Scaled Emissions by Process  (B · diag(s))

Each cell = emission rate × scaling factor.  Columns sum to the LCI totals in Step 5.

| Process | s | Carbon dioxide | Nitrogen oxides | Sulfur dioxide |
|---|---:|---:|---:|---:|
| P1 — Grow and harvest cotton | 1.0000 | 2.9000 | 0 | 0 |
| P2 — Spin, dye, and weave denim fabric | 0.8000 | 0 | 0 | 0 |
| P3 — Cut, sew, and finish jeans | 1.0000 | 0 | 0 | 0 |
| P4 — Distribute, wash, dry, and dispose of jeans | 1.0000 | 6.4000 | 0 | 0 |
| P5 — Generate electricity | 35.5000 | 17.7500 | 0.0320 | 0.0213 |
| **Total** | | **27.0500** | **0.0320** | **0.0213** |

## Step 7 — LCIA Results  (TRACI 2.2)

Characterization factors from the database. Each impact category score is the sum of all elementary flow contributions as computed by the openLCA engine.

| Impact Category | Score | Unit |
|---|---:|---|
| Human health - cancer | **0.000000** | CTUcancer |
| Acidification | **0.043665** | kg SO2 eq |
| Eutrophication (Freshwater) | **0.000000** | kg P eq |
| Human health - particulate matter | **0.001532** | PM 2.5 eq |
| Smog formation | **0.792155** | kg O3 eq |
| Human health - non-cancer | **0.000000** | CTUnoncancer |
| Ozone depletion | **0.000000** | kg CFC-11 eq |
| Global warming | **27.050000** | kg CO2 eq |

## Summary

**LCIA Method:** TRACI 2.2

> **Human health - cancer: 0.000000 CTUcancer** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
> **Acidification: 0.043665 kg SO2 eq** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
> **Eutrophication (Freshwater): 0.000000 kg P eq** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
> **Human health - particulate matter: 0.001532 PM 2.5 eq** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
> **Smog formation: 0.792155 kg O3 eq** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
> **Human health - non-cancer: 0.000000 CTUnoncancer** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
> **Ozone depletion: 0.000000 kg CFC-11 eq** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
> **Global warming: 27.050000 kg CO2 eq** per 1.0 pair of One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears

## Product System Graphs

### Scaled (with amounts)

![Scaled](product_graph_scaled.svg)

### Structure (flow names only)

![Structure](product_graph_structure.svg)

---
*Generated by `lca_scripts/lca_analysis.py` using openLCA gdt-server v2*
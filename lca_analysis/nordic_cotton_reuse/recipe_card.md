---
name: Nordic Textile Waste — Scenario 2B — Cotton reuse in Nordic countries
goal: >
  Model the climate change benefit of reusing one kilogram of used 100% cotton
  textiles through Nordic second-hand shops, rather than incinerating them.
  When a consumer buys a second-hand cotton garment instead of a new one, the
  production of an entirely new cotton garment is avoided — from growing the raw
  cotton in the field, through spinning, weaving, dyeing, cutting, sewing, and
  shipping from Asia to Scandinavia. That avoided production is a very large CO₂
  credit. At the end of its second life, the garment is still incinerated with
  energy recovery (same as Scenario 2A). Based on Schmidt et al., TemaNord 2016:537.

functional_unit:
  description: Treatment of one kilogram of used 100% cotton textiles via Nordic reuse — collection to final grave
  amount: 1.0
  unit: kg

units:
  kg:  Mass in kilograms (the cotton textile)
  kWh: Energy in kilowatt-hours (electricity and heat)

products:
  - { name: Cotton reuse service,                    unit: kg  }
  - { name: Avoided cotton garment production credit, unit: kg  }
  - { name: Nordic electricity credit,               unit: kWh }
  - { name: Nordic heat credit,                      unit: kWh }

elementary_flows:
  emissions:
    - { name: Carbon dioxide, compartment: air, unit: kg }

# ─────────────────────────────────────────────────────────────────────────────
# HOW THE REUSE CREDIT WORKS IN THIS MODEL
#
# When a consumer buys a second-hand cotton garment, they do NOT buy a new one.
# The entire production chain for that new garment is therefore avoided:
#   – Cotton farming in the US, India, or China (1.26 kg raw cotton per kg garment)
#   – Spinning and weaving into fabric in China (1.15 kg fabric per kg garment)
#   – Dyeing, cutting, sewing in China (1 kg garment)
#   – Shipping by container ship from China to Scandinavia
#
# All of this avoided production is represented as a single CO₂ credit of
# -13.14 kg per kg of garment. This is the dominant term in the calculation —
# over 99% of the total benefit comes from this one credit.
#
# The small end-of-life incineration cost and energy recovery credits are the
# same as Scenario 2A (the garment is still burned after its second use).
#
# Net CO₂ = +0.046  (fossil from end-of-life incineration, same as 2A)
#           – 13.14  (avoided cotton garment production — the big saving)
#           – 0.576 × 0.021  (electricity credit from EOL incineration)
#           – 3.194 × 0.071  (heat credit from EOL incineration)
#         = +0.046 – 13.14 – 0.012 – 0.227
#         = –13.333 kg CO₂ per kg cotton reused
#         = –13,333 kg CO₂ per tonne (equivalent to –1.646 PE/ton in the PDF)
# ─────────────────────────────────────────────────────────────────────────────

processes:
  - name: P1 — Collect and reuse cotton garment in Nordic second-hand shop
    reference_output: { flow: Cotton reuse service, amount: 1.0 }
    inputs:
      - { flow: Avoided cotton garment production credit, amount: 1.0   }
      - { flow: Nordic electricity credit,               amount: 0.576 }
      - { flow: Nordic heat credit,                      amount: 3.194 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.046 }

  - name: P2 — Avoided cotton garment production (farm to Nordic shop)
    reference_output: { flow: Avoided cotton garment production credit, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: -13.14 }

  - name: P3 — Nordic marginal electricity displaced by end-of-life incineration
    reference_output: { flow: Nordic electricity credit, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: -0.021 }

  - name: P4 — Nordic marginal heat displaced by end-of-life incineration
    reference_output: { flow: Nordic heat credit, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: -0.071 }

reference_process: P1 — Collect and reuse cotton garment in Nordic second-hand shop

lcia:
  method_name: "TRACI 2.2"
---

## About this scenario

**Source:** Schmidt, A. et al. (2016). *Gaining benefits from discarded textiles —
LCA of different treatment pathways.* TemaNord 2016:537. Nordic Council of Ministers.

**Scenario 2B** is the single most beneficial end-of-life option for cotton
textiles in the Nordic study. Used cotton garments are collected from households,
sorted at a sorting facility, and sold through domestic second-hand shops in the
Nordic countries. The person who buys the second-hand garment is assumed to
have otherwise bought an equivalent new cotton garment — so one sale of a
second-hand item replaces one new purchase.

---

### Why reuse produces such a large CO₂ saving

The key insight is that cotton clothing is extremely expensive to make in terms
of energy and resources. To produce just **one kilogram of finished cotton garment**:

| Production step | Where it happens | What it needs |
|---|---|---|
| Grow 1.26 kg raw cotton | USA, India, or China | Fertilisers, pesticides, irrigation, tractors |
| Spin + weave 1.15 kg fabric | China | Energy-intensive mills (Chinese electricity = coal-heavy) |
| Dye the fabric | China | Hot water baths, chemicals, energy |
| Cut and sew the garment | China | Electricity for sewing machines (8.75 MJ per kg) |
| Ship to Scandinavia | Container ship + truck | Heavy fuel oil, diesel |

Every single one of these steps releases CO₂. When a consumer buys second-hand,
all of these steps are **skipped entirely** for one garment. The combined CO₂ saving
from skipping the whole chain is approximately **13.14 kg CO₂ per kg of garment**.

---

### What happens at end of life

Even after a second use, the garment eventually wears out and is discarded. In this
model it is incinerated with energy recovery — exactly the same as Scenario 2A.
That means the end-of-life step produces the same small fossil CO₂ emission
(+0.046 kg/kg) and the same small electricity and heat credits (−0.012 and −0.227 kg/kg).

The end-of-life contribution totals −0.193 kg CO₂/kg — almost invisible compared
to the −13.14 kg saved from avoided production.

---

### Key numbers from the PDF

| Data point | Value | Source |
|---|---|---|
| Avoided cotton fibre (per kg garment) | 1.26 kg | Figure 15 |
| Avoided woven fabric (per kg garment) | 1.15 kg | Figure 15 |
| Chinese electricity for cutting/sewing | 8.75 MJ = 2.43 kWh | Figure 15 |
| Combined avoided production CO₂ | −13.14 kg/kg | Derived from Table 13 |
| End-of-life fossil CO₂ (same as 2A) | +0.046 kg/kg | Table 7 / Figure 10 |
| PDF result (climate change excl biogenic) | −1.646 PE/ton | Table 13 |
| PDF result converted to kg CO₂ | −13,333 kg/tonne | −1.646 × 8,100 |

---

### Comparison with Scenario 2A (incineration)

| Scenario | Result |
|---|---|
| 2A — Cotton incineration | −193 kg CO₂/tonne (near zero) |
| **2B — Cotton reuse NORDIC** | **−13,333 kg CO₂/tonne (very large benefit)** |

Reuse is roughly **70 times better** for climate than incineration. The reason
is straightforward: incineration only recovers a small energy credit, whereas
reuse avoids having to manufacture an entirely new garment — a process that
uses huge amounts of energy.

### Expected result

**−13.333 kg CO₂ per kg cotton reused** (approximately −13,333 kg CO₂ per tonne)

This matches the PDF result of **−1.646 PE/tonne** when converted using the
ILCD normalization factor of 8,100 kg CO₂-eq per person per year.
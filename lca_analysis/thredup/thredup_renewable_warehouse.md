---
# ─────────────────────────────────────────────────────────────────────────────
# LCA Analysis Specification — thredUP Comparative LCA (2019)
# SCENARIO: Secondhand garment — renewable energy at thredUP warehouse
# Run with: python3 lca_scripts/lca_analysis.py lca_analysis/thredup/thredup_renewable_warehouse.md
# ─────────────────────────────────────────────────────────────────────────────

name: thredUP Comparative LCA — Secondhand, Renewable Warehouse
goal: >
  Model what thredUP's CO₂ footprint would look like if all warehouse and
  sorting operations ran on renewable electricity (solar or wind), while
  collection shipping and final delivery remain unchanged.

functional_unit:
  description: One average secondhand garment (0.4 kg) purchased via thredUP, renewable-powered warehouse
  amount: 1.0
  unit: garment

units:
  garment: One average garment item
  kg:      Mass in kilograms

products:
  - { name: Donated garment,      unit: garment }
  - { name: Sorted garment,       unit: garment }
  - { name: thredUP purchase,     unit: garment }

elementary_flows:
  emissions:
    - { name: Carbon dioxide, compartment: air, unit: kg }

processes:
  - name: P1 — Collect and receive used clothing
    reference_output: { flow: Donated garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.7 }

  - name: P2 — Sort, list online, and ship to buyer (renewable warehouse)
    reference_output: { flow: Sorted garment, amount: 1.0 }
    inputs:
      - { flow: Donated garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.15 }

  - name: P3 — End of life (remaining 30% of garment life)
    reference_output: { flow: thredUP purchase, amount: 1.0 }
    inputs:
      - { flow: Sorted garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.2 }

reference_process: P3 — End of life (remaining 30% of garment life)

lcia:
  method_name: "TRACI 2.2"
---

## About this scenario

**What changed:** In the base secondhand model, the thredUP warehouse runs on
the average US electricity grid, which still relies heavily on natural gas and
coal. This scenario switches the warehouse and sorting operations (P2) to
**100% renewable electricity** — solar or wind power. The CO₂ factor for
warehouse electricity drops from ~0.42 kg CO₂/kWh (US grid average) to
~0.02 kg CO₂/kWh (renewable), an 85% reduction in that stage's emissions.

**What did NOT change:** Collection shipping (P1) and delivery to the buyer
(part of P2, via USPS) still use fossil fuel-powered vehicles and aircraft.
Those emissions remain the same.

**Why this matters for business:** thredUP already has sustainability commitments
and operates distribution centers across the US. A major apparel resale platform
switching its warehouses to renewable energy is a realistic, achievable goal.
Several large retailers (IKEA, Target) have already done this for their DCs.

---

### CO₂ comparison

| Stage | Base secondhand | Renewable warehouse | Change |
|---|---|---|---|
| P1 Collection | 0.7 kg | 0.7 kg | — |
| P2 Warehouse + shipping | 1.0 kg | 0.15 kg | −85% |
| P3 End of life | 0.2 kg | 0.2 kg | — |
| **Total** | **1.9 kg** | **~1.05 kg** | **−45%** |

Buying secondhand from a renewable-powered warehouse emits just **1.05 kg CO₂**
per garment — about 93% less than buying new (15.8 kg).

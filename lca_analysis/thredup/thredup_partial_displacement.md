---
# ─────────────────────────────────────────────────────────────────────────────
# LCA Analysis Specification — thredUP Comparative LCA (2019)
# SCENARIO: Secondhand garment — partial displacement (50% of buyers truly switch)
# Run with: python3 lca_scripts/lca_analysis.py lca_analysis/thredup/thredup_partial_displacement.md
# ─────────────────────────────────────────────────────────────────────────────

name: thredUP Comparative LCA — Secondhand, Partial Displacement (50%)
goal: >
  Model the EFFECTIVE CO₂ cost of buying a secondhand garment when only 50%
  of thredUP buyers truly switch from buying new — the other 50% would have
  bought secondhand from somewhere else anyway, so buying from thredUP doesn't
  actually prevent any new garment from being made for that half.

functional_unit:
  description: One average secondhand garment (0.4 kg) purchased via thredUP, 50% displacement rate
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

  - name: P2 — Sort, list online, and ship to buyer (with unmitigated half)
    reference_output: { flow: Sorted garment, amount: 1.0 }
    inputs:
      - { flow: Donated garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 8.9 }

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

**What changed:** The base study assumes that **100% of thredUP buyers** would
have bought a brand-new garment if thredUP didn't exist. This is called
"full displacement" or a "1-for-1 substitution."

In reality, some thredUP buyers already preferred secondhand and would have
found a garment on Poshmark, eBay, or a charity shop instead. For those buyers,
thredUP's sale does NOT prevent a new garment from being made — the new garment
just doesn't get purchased by that particular person.

This scenario tests a **50% displacement rate**: half of all buyers truly switch
from new, and half would have bought secondhand anyway. For the half that don't
truly switch, we have to charge their purchase with the equivalent manufacturing
emissions of a new garment that was NOT avoided.

**How this is modelled:** P2 now includes 50% × 15.8 kg CO₂ = 7.9 kg CO₂ in
"unmitigated" new garment emissions that are effectively charged to the purchase,
on top of the 1.0 kg from thredUP's actual warehouse operations.

**Why this is important for sustainability claims:** When thredUP (or any resale
platform) claims "buying secondhand saves X kg of CO₂," that claim is only true
if the buyer truly would have bought new otherwise. The displacement rate is the
most contested assumption in secondhand clothing LCAs, and it significantly
changes the headline number.

The 2022 thredUP Annual Resale Report updated this figure, suggesting that about
72% of buyers (not 100%) truly displace a new purchase — which would reduce the
headline savings by roughly 28%.

---

### CO₂ comparison across displacement rates

| Displacement rate | Effective CO₂ per garment | vs. buying new (15.8 kg) |
|---|---|---|
| 100% (study base case) | 1.9 kg | −88% |
| 72% (2022 updated estimate) | 6.3 kg | −60% |
| **50% (this scenario)** | **9.8 kg** | **−38%** |
| 0% (nobody truly switches) | 17.7 kg | +12% worse |

The last row — 0% displacement — is a thought experiment. If nobody who buys
secondhand is truly switching from new, then buying from thredUP adds the
warehouse operations CO₂ WITHOUT preventing any new garment from being made.
That would actually make the system slightly worse than just buying new.

This is why the displacement assumption is so important to examine critically.

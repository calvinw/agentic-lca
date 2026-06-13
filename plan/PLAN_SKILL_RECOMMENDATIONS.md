# Skill Recommendations — Elementary LCA Skills for Beginners

Recommended order for a student with no science or coding background.
Skills already built are marked ✅. Skills recommended but not yet built are marked ⬜.

---

## Recommended Learning Path

| Order | Skill | Status | What it teaches |
|---|---|---|---|
| 1 | `what-is-lca` | ✅ Built | What LCA is, why fashion professionals need it, the four phases |
| 2 |   al-and-scope` | ✅ Built | Why the study is being done, who it is for, what is included or excluded |
| 3 | `functional-unit` | ✅ Built | The precise definition of what is being measured |
| 4 | `supply-chain` | ✅ Built | How to read a product graph, what processes and flows are |
| 5 | `characterization` | ⬜ Recommended | How raw emissions are converted into impact scores (e.g. why 1 kg CH4 = 27.9 kg CO2 eq) |
| 6 | `impact-categories` | ⬜ Recommended | What impact categories are, why there are more than just CO2, why one emission can appear in multiple categories |
| 7 | `scaling-vector` | ✅ Built | How much each process in the supply chain must run to deliver one functional unit |
| 8 | `hotspot-analysis` | ⬜ Recommended | How to read a contribution breakdown, identify the biggest sources of impact, connect to business decisions |
| 9 | `comparing-products` | ⬜ Recommended | How to set up a fair comparison between two products, when comparisons are misleading |

---

## Skills Not Yet Built — Detail

### `characterization`
The "magic conversion" step that trips most students up. Raw emissions like CO₂ and
methane are measured in kilograms, but they cause very different amounts of damage.
Scientists have measured how potent each gas is relative to CO₂ and assigned each one
a characterization factor. This skill would walk through that idea in plain English,
using the wool yarn (CH4 × 27.9) and cotton fiber (N2O × 273) case studies as examples.

**Key insight for students:** A small number of kilograms of a potent gas can dwarf
a large number of kilograms of a less potent one — which is why the raw inventory
numbers alone can be very misleading.

---

### `impact-categories`
Students learn to calculate CO₂ — but not why there are other impact categories,
or what they measure. This skill would introduce climate change, water consumption,
and terrestrial eutrophication in plain English, using the cotton fiber case study
(which covers all three). It would also explain why the same emission (N2O) can
show up in multiple categories at once.

**Key insight for students:** A product with a low carbon footprint can still have
a serious water problem. One number is never the whole story.

---

### `hotspot-analysis`
Once students have results, the next natural question is: *which part of the supply
chain is the problem?* This skill would teach how to read a contribution breakdown
table, identify the biggest hotspot, and connect that to a practical business
recommendation — for example, if 86% of a garment's footprint comes from the sheep
farm, that is where improvement efforts should be focused.

**Key insight for students:** LCA results are most useful when they tell you *where
to act*, not just *how bad it is*.

---

### `comparing-products`
The capstone beginner skill. Once students understand functional unit, system
boundary, and how to read results, they are ready to compare two products side by
side. This skill would walk through a structured comparison (e.g. wool yarn vs
polyester yarn), show how the functional unit and scope must match before any
comparison is valid, and teach students to spot when a comparison is being set up
unfairly.

**Key insight for students:** Two products can only be fairly compared if they are
measured per the same functional unit, over the same system boundary. Without that,
any comparison can be gamed.

---

## Notes

- All skills follow the same Socratic five-step structure: open with a real-world
  question, validate the student's answer, introduce the concept, ask a what-if
  question, connect to a business decision.
- Skills that use a case study argument read from `skills_references/<case_study>/recipe_card.md`.
- `what-is-lca` is the only skill with no case study argument.
- Sessions should be saved to `skills_sessions/` using the naming convention:
  `<skill_name>_skill_example_<case_study>_v<version>_<date>.md`

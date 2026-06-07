# LCA Analysis Plan

## What Already Exists

```
lca_analysis/
  coffee/
  cotton_shirt/
  paper_cup/
```

---

## Proposed New Examples

The following examples are drawn from the course reference materials in `references/`. Each one has real numbers and supply chain data already available, making them straightforward to set up and run.

| Folder name | Product / Comparison | Why it's a good example | Primary reference |
|---|---|---|---|
| `hand_drying` | Paper towel vs. warm air dryer vs. high-speed dryer | The course's own signature teaching example. Full supply chain data and numbers provided. | `LCA_CASE_STUDIES_AND_EXAMPLES.md` Part 1 |
| `grocery_bag` | Plastic bag vs. paper bag | Classic comparison. Real numbers given including reuse scenarios. Teaches functional unit correctly. | `SIMPLE_EXAMPLES_FROM_COURSE.md` §12.1 |
| `reusable_cup` | Ceramic reusable cup vs. single-use plastic cup | Break-even calculation already worked out in course materials. | `SIMPLE_EXAMPLES_FROM_COURSE.md` §12.2 |
| `light_bulb` | Incandescent bulb vs. LED | Full energy balance spreadsheet data in course Excel files. | `course-materials/03-Life-Cycle-Inventory/` energy balance sheets |
| `burrito` | Beef burrito vs. veggie burrito | Complete ingredient-level carbon footprint spreadsheet already in references. | `01__EHS_672_Activity_2.3.1_Burrito_meat_vs_veggie_F20e.xlsx` |
| `milk_packaging` | Different milk packaging formats (carton, plastic, glass) | The canonical functional unit teaching example used throughout the course. | Course-wide, `LCA_CASE_STUDIES_AND_EXAMPLES.md` |

---

## Suggested Order

1. **`hand_drying`** — Start here. Most complete data in the references, and it is the course's own flagship example.
2. **`grocery_bag`** — Simple comparison, good for showing how functional unit matters.
3. **`reusable_cup`** — Builds on paper_cup already in lca_analysis. Good break-even story.
4. **`light_bulb`** — Energy balance data already in spreadsheet form (now also CSV).
5. **`burrito`** — Richest data set. Ingredient-level detail. Good food LCA example.
6. **`milk_packaging`** — Rounds out the food/packaging section.

---

## Reference Files Most Useful for Writing Recipe Cards

- `references/life-cycle-assessment-course/SIMPLE_EXAMPLES_FROM_COURSE.md` — numbers and formulas for most examples
- `references/life-cycle-assessment-course/LCA_CASE_STUDIES_AND_EXAMPLES.md` — deep supply chain detail, especially hand drying
- `references/life-cycle-assessment-course/course-materials/03-Life-Cycle-Inventory/` — energy balance CSVs for light bulb
- `references/life-cycle-assessment-course/course-materials/07_Resources/04_.../01__EHS_672_Activity_2.3.1_Burrito_meat_vs_veggie_F20e__*.csv` — burrito ingredient data

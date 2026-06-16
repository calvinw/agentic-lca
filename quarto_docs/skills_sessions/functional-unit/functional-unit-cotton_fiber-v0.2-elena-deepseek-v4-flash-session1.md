# /functional-unit cotton_fiber
**Skill version:** 0.2
**Student:** elena
**Model:** deepseek-v4-flash
**Date:** 2026-06-15

**AI:** A sourcing manager at a clothing brand is comparing two fiber suppliers — one selling conventional cotton fiber and another selling organic cotton fiber. They want to know which one has a lower carbon footprint.

What unit would you use to make that comparison fair? Per kilogram of fiber? Per T-shirt that could be made from it? Per year of wearing that T-shirt?

**Student:** kilo

**AI:** Exactly right — per kilogram is the natural choice when you're comparing two fiber suppliers at the raw material stage. Both suppliers are selling the same thing (cotton fiber), so a weight-based comparison is perfectly fair. The challenge comes when the products being compared are different — a kilogram of cotton vs a kilogram of polyester, for example — but for the same material type, you've picked exactly the right unit.

Here is the study we'll be working through. It's called **Cotton Fiber — 1 kg**, and it traces the supply chain from synthetic fertiliser production through cotton farming to calculate the climate and eutrophication impact of producing cotton fiber. The numbers are teaching examples calibrated to be realistic rather than from a specific brand.

[![Cotton Fiber supply chain — structure](../../skills_references/cotton_fiber/product_graph_structure.svg)](../../skills_references/cotton_fiber/product_graph_structure.svg)
`../../skills_references/cotton_fiber/product_graph_structure.svg`

This diagram shows two boxes connected by an arrow. The box on the right — **P2 — Cotton farming** — has a special name in LCA: it's called the **reference process**. Think of it as the finishing line — it's the step that actually produces the cotton fiber. Everything to its left (P1 — Fertilizer production) exists only to supply the farm. The measurement stops at this box. The functional unit is precisely what comes out of it.

**Student:** quit this skill

**AI:** Sure — stopping the functional-unit lesson here. Feel free to come back anytime you want to continue, or try a different skill. Just type `/functional-unit` or the name of any other skill you'd like to explore.

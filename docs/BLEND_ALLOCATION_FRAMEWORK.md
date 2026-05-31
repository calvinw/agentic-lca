# Blend Allocation Decision Framework

## Why This Matters

When you analyze a blended fabric (cotton-polyester, viscose-elastane, etc.), you need to decide how to split the environmental impact between fibers. **The method you choose can change your results by 15-50%.**

This framework helps you make that choice clearly, transparently, and defensibly. It's based on ISO 14040/44 standards but adapted specifically for textiles.

---

## The Core Problem

Imagine a shirt that's **60% cotton + 40% polyester**. Both fibers go through different supply chains:

```
COTTON PATH          →  POLYESTER PATH
├─ Farm              ├─ Oil extraction
├─ Ginning           ├─ Refining
├─ Spinning          ├─ Polymerization
│                    └─ Spinning
└─ (meets here) ────────→ BLENDING
                         ↓
                    Weaving (together)
                         ↓
                    Dyeing (same bath)
                         ↓
                    Finishing (together)
                         ↓
                    Washing, use, disposal
```

**The question:** For the weaving, dyeing, and finishing stages (where they're together), how do you split the environmental cost?

Option A: 60/40 by mass? (Most common)
Option B: By how much dye each absorbs? (Different ratio)
Option C: By market price? (Unstable)
Option D: Something else?

**Different choices give different answers.** This framework helps you choose wisely.

---

## The Decision Hierarchy

ISO 14040/44 establishes a clear preference order. Use this from top to bottom:

### **Level 1: Process Separation (Best)**
**When to use:** Fibers go through completely separate processes, then combine later.

**Example:** 
- Cotton ginning: completely separate from polyester production
- Each fiber gets its own supply chain impact
- They only meet at the spinning stage

**How to do it:**
```
Cotton farming impact     → 100% assigned to cotton
Cotton ginning impact    → 100% assigned to cotton
Polyester production     → 100% assigned to polyester
Polyester refining       → 100% assigned to polyester

(Then they blend...)

Spinning (combined)      → Now you need Level 2-5 for shared processes
```

**Advantage:** Most scientifically accurate; different supply chains get their own impacts
**Disadvantage:** Only works for early-stage processes; most fabric production is shared

---

### **Level 2: System Expansion (Second-best)**
**When to use:** A byproduct or waste stream from the blend can replace something else.

**Example that works:**
- Blended fabric scraps from cutting can be recycled into polyester fiber
- This recycled polyester replaces virgin polyester in another product
- You can model: "making this 60/40 blend requires virgin polyester BUT generates recycled polyester scrap that credits back"

**Example that DOESN'T work:**
- Mixed cotton-polyester blend scraps cannot be recycled (fiber contamination)
- No substitution occurs
- Don't use this method

**How to do it (when it applies):**
```
Total blend impact: 5.5 kg CO₂

Less: Recycled scrap value
  (30% of polyester scraps × recycled polyester credit)
  = -0.8 kg CO₂

Net impact: 4.7 kg CO₂
```

**Advantage:** Scientifically rigorous; captures actual system benefits
**Disadvantage:** Rarely applies in practice; most blended scraps have contamination issues

---

### **Level 3: Physical Allocation (Third-best)**
**When to use:** You can document that impacts scale with a physical property (mass, area, fiber absorption rate, etc.)

**Example that works:**
- Spinning electricity: scales roughly with mass (heavier fibers need more energy)
- Could allocate 60/40 by mass
- Justification: heavier material = more mechanical work

**Example that's tricky:**
- Dyeing: same dye bath, but cotton absorbs 6-8% of dye while polyester absorbs 0.5-2%
- Could allocate by absorption rate (cotton gets ~90%, polyester ~10%)
- But this is more complex; few studies do this

**How to do it:**
```
Process: Dyeing & Finishing
Total impact: 1.2 kg CO₂

Allocation by dye absorption:
  Cotton (absorbs 6.5% of dye bath): 90% of impact = 1.08 kg CO₂
  Polyester (absorbs 1.5% of dye bath): 10% of impact = 0.12 kg CO₂
```

**Advantage:** More causally-linked to actual fiber properties
**Disadvantage:** Requires specialized knowledge; most LCA software doesn't support this level of detail

---

### **Level 4: Mass Allocation (Most Common Default)**
**When to use:** You can't use Levels 1-3, and you need a transparent, reproducible method.

**This is the default.** If you don't have a better reason, use this.

**How to do it:**
```
Blend composition: 60% cotton + 40% polyester
Total impact for shared process: 1.0 kg CO₂

Allocation:
  Cotton: 60% × 1.0 = 0.6 kg CO₂
  Polyester: 40% × 1.0 = 0.4 kg CO₂
```

**Advantage:** 
- Simple, transparent, reproducible
- Everyone can understand it
- No hidden assumptions

**Disadvantage:** 
- Lacks causality (chemical impacts don't scale linearly with mass)
- Arbitrary for processes that don't scale with weight
- ISO 14044 warns against using this without justification

**When to justify mass allocation:**
- "We use mass allocation for spinning (electrical work scales with material mass)"
- "We use mass allocation for dyeing (same bath shared proportionally)"
- These are defensible if documented

---

### **Level 5: Economic Allocation (Last Resort)**
**When to use:** Only if none of Levels 1-4 work AND you can document the economic ratios.

**How to do it:**
```
Blend composition: 60% cotton + 40% polyester by mass
Market prices (average 2024):
  Cotton: $0.85/kg
  Polyester: $0.45/kg

Economic ratio:
  Cotton value: 60 kg × $0.85 = $51
  Polyester value: 40 kg × $0.45 = $18
  Total value: $69

Allocation:
  Cotton: ($51 / $69) × 100% = 74% of impact
  Polyester: ($18 / $69) × 100% = 26% of impact
```

**Advantage:** Reflects market perception of value
**Disadvantage:** 
- Unstable (prices fluctuate 20-50% annually)
- Same product has different "sustainability" different years
- Misleading (environmental impact doesn't change when prices change)
- ISO 14044 ranks this last for good reason

**When NOT to use this:**
- Ever, really, unless you have no other option
- Even then, document heavily

---

### **Level 6: Cut-off Method (Avoid Unless Justified)**
**When to use:** Minor component (<1% by mass, clearly low-impact)

**Example that works:**
- Shirt: 99.5% cotton + 0.5% thread label = assign 100% to cotton (label impact is negligible)

**Example that FAILS:**
- Shirt: 99% cotton + 1% elastane = CANNOT use cut-off
- Elastane has 10-40× impact per kg of polyester
- 1% by mass = 5-10% of total impact
- Cutting it off loses major information

**How to do it (when justified):**
```
Blend: 99% cotton + 1% elastane
Decision: Include elastane (it's >0.5% AND has high impact)
Method: Mass allocation (99/1)

If you exclude minor component, state it clearly:
"Care tag (0.1% by mass) excluded from system boundary"
```

**Advantage:** Simplifies minor calculations
**Disadvantage:** Can hide significant impacts if component is high-impact

---

## Decision Tree for Blended Fabrics

Use this flowchart to navigate the framework:

```
START: You have a blended fabric
  ↓
Q1: Are the fibers processed separately before blending?
  YES → Use LEVEL 1 (Process Separation)
        Assign each fiber its upstream supply chain
        ↓
        Q1b: After blending, are there shared processes?
          YES → Continue to Q2
          NO → Done, use process separation for everything
  
  NO → Continue to Q2
  ↓
Q2: Do byproducts from this blend actually replace something else?
  YES → Use LEVEL 2 (System Expansion)
        Model the recycled/substituted material credit
        Example: Polyester scraps → virgin polyester replacement
  
  NO → Continue to Q3
  ↓
Q3: Can you document that a physical property drives the impact?
  YES → Use LEVEL 3 (Physical Allocation)
        Example: Electrical work ∝ material mass
        Justify your chosen property
  
  NO → Continue to Q4
  ↓
Q4: Are you comfortable with the assumption that impact scales by mass?
  YES → Use LEVEL 4 (Mass Allocation)
        This is the default, transparent choice
        Document: "Mass allocation used because [brief reason]"
  
  NO → Continue to Q5
  ↓
Q5: Do you have economic data and strong justification?
  YES → Use LEVEL 5 (Economic Allocation)
        Document prices used and date
        Show sensitivity to price changes
  
  NO → Continue to Q6
  ↓
Q6: Is the component really <1% by mass AND clearly low-impact?
  YES → Use LEVEL 6 (Cut-off Method)
        Exclude it, document what you excluded
  
  NO → Go back to LEVEL 4 (Mass Allocation)
       This is your fallback
```

---

## Framework by Blend Type

Here are common blends and recommended approaches:

### **65% Cotton + 35% Polyester (most common)**

**Preferred approach:**
1. Cotton farming → Process separation (100% to cotton)
2. Polyester production → Process separation (100% to polyester)
3. Spinning stage → Mass allocation (65/35)
   - Justification: Spinning electrical work scales with material mass
4. Dyeing & finishing → Mass allocation (65/35)
   - Justification: Same shared process; no better alternative documented
5. Use phase → Mass allocation (65/35)
   - Justification: Both fibers present in garment equally

**Sensitivity analysis:**
- If economic allocation used instead of mass (cotton = 1.8× price): ±8% variation
- If dyeing allocation by absorption rate (cotton ~90%): ±12% variation
- **Total uncertainty range: ±15%**

**Documentation example:**
```
BLEND: 65% Cotton + 35% Polyester T-Shirt
ALLOCATION METHOD: Hybrid
├─ Upstream: Process separation
│  └─ Cotton farming → 100% to cotton
│  └─ Polyester production → 100% to polyester
├─ Spinning: Mass allocation (65/35)
│  └─ Rationale: Electrical work scales with material mass
├─ Dyeing: Mass allocation (65/35)
│  └─ Rationale: Same shared dye bath; absorption rates too complex
│     to model without fiber-specific data
├─ Use phase: Mass allocation (65/35)
│  └─ Rationale: Both fibers present in garment equally
└─ RESULT: 2.8 kg CO₂/garment
   UNCERTAINTY: ±15% depending on allocation method choice
```

---

### **85% Viscose + 15% Elastane (tricky)**

**The problem:** Elastane is 15% by mass but provides critical elasticity. Economic value is 40-50% of blend.

**Preferred approach:**
1. Viscose production → Process separation (100% to viscose)
2. Elastane production → Process separation (100% to elastane)
3. Spinning → Mass allocation (85/15)
   - Why not economic? Elastane price ≠ environmental burden
   - Why not physical? Elastane's function is disproportionate to mass
4. Texturizing/blending → Physical allocation if possible
   - If you can document that elastane processing is separate: use process separation
   - If not: mass allocation (85/15) with note about uncertainty

**Critical documentation:**
```
BLEND: 85% Viscose + 15% Elastane Activewear
ALLOCATION: Mass allocation (85/15) WITH CAVEAT
├─ Rationale: Different fiber types, similar production streams
├─ UNCERTAINTY: HIGH
│  └─ Economic allocation (elastane = 50% value): →15% shift
│  └─ Physical allocation (elastane = 30% function): →8% shift
│  └─ These are NOT resolved; industry has no consensus
├─ RECOMMENDATION: 
│  This blend should be modeled with sensitivity analysis
│  showing impacts under different allocation assumptions
└─ RESULT: 1.6 kg CO₂/garment (85/15 mass allocation)
   WITH RANGE: 1.48-1.84 kg under different methods
```

**Key point for students:** Flag this as uncertain. Don't pretend you know the "right" answer.

---

### **90% Polyester + 10% Recycled Polyester**

**The problem:** One input is virgin, one is recycled. System expansion applies here.

**Preferred approach:**
1. Virgin polyester production → Process separation (100% to virgin)
2. Recycled polyester input → System expansion (credit for virgin polyester displaced)

**How it works:**
```
VIRGIN POLYESTER (90%):
  Production impact: 6.5 kg CO₂/kg
  → 0.90 × 6.5 = 5.85 kg CO₂

RECYCLED POLYESTER (10%):
  Production impact: 2.1 kg CO₂/kg (lower: just re-melting)
  But it displaces virgin polyester:
    → Use 2.1 kg CO₂ (recycling process)
    → Less: 0.10 × 6.5 = -0.65 kg CO₂ (virgin avoided)
    → Net: 2.1 - 0.65 = 1.45 kg CO₂

TOTAL BLEND: 5.85 + 1.45 = 7.30 kg CO₂/kg

VS. MASS ALLOCATION (ignoring recycling benefit):
  (0.90 × 6.5) + (0.10 × 6.5) = 6.5 kg CO₂/kg

DIFFERENCE: 7.30 vs 6.5 = system expansion "penalizes" for recycling
(Because recycled input is credited only against virgin it replaces, not the full product)
```

**Documentation:**
```
BLEND: 90% Virgin + 10% Recycled Polyester
ALLOCATION: System expansion
├─ Virgin polyester: Direct impact (no substitution)
├─ Recycled polyester: System expansion against virgin displaced
├─ Rationale: Recycled material genuinely substitutes for virgin
│  in the market; credit is environmentally justified
└─ RESULT: 7.30 kg CO₂/kg (includes system expansion benefit)
   WITHOUT system expansion: 6.50 kg CO₂/kg (±12% difference)
```

---

### **100% Cotton (pure fiber, no blend)**

**Approach:** No allocation needed. Use process separation for each supply chain stage.

```
ALLOCATION: Process separation (single fiber)
├─ Farming: 2.1 kg CO₂/kg
├─ Ginning: 0.3 kg CO₂/kg
├─ Spinning: 1.2 kg CO₂/kg
├─ Weaving: 0.8 kg CO₂/kg
├─ Dyeing: 1.1 kg CO₂/kg
├─ Use phase: 1.5 kg CO₂/kg (washing 40×)
└─ TOTAL: 7.0 kg CO₂/kg
```

**Key point:** Even pure fibers have allocation decisions (use phase assumptions, waste handling, etc.), but no fiber-to-fiber allocation needed.

---

## Dyeing Allocation Decision Tree

Dyeing is the most allocation-sensitive shared process in blended fabric production. The reason is that cotton and polyester do not absorb dye equally — and the dye chemicals, water heating, and wastewater treatment are where most of the environmental cost of dyeing sits. Using mass allocation (60/40) here is a simplification that can be off by 15–25 percentage points compared to a process-specific approach.

This sub-tree sits inside **Level 3 (Physical Allocation)** of the main decision tree and should be applied specifically to the dyeing and finishing stage.

---

### The Core Dyeing Problem

In a shared dye bath for a 65/35 cotton-polyester blend:
- Cotton absorbs approximately **6–8% of the dye in the bath**
- Polyester absorbs approximately **0.5–2% of the dye in the bath**

That means cotton is responsible for roughly **90% of the dye demand**, even though it is only 65% of the fabric by mass. If you allocate dyeing impacts by mass (65/35), you are under-charging cotton and over-charging polyester for the dye chemicals and associated water and energy.

However, dye absorption is not the only driver of dyeing impacts. Water heating and wastewater treatment scale more with bath volume (shared equally) than with dye uptake. This means the right allocation depends on *which* part of the dyeing impact you are looking at.

---

### Dyeing Allocation Decision Tree

```
START: You are allocating the dyeing and finishing stage

Q-D1: Do you have fiber-specific dye absorption data
       for this exact blend and dye type?
  YES → Continue to Q-D2
  NO  → Use MASS ALLOCATION (default)
        Document: "Fiber-specific dye absorption data unavailable;
        mass allocation used as proxy. Cotton over-credited by
        approximately 10-15%; flag as limitation."
        → DONE for dyeing stage
  ↓
Q-D2: Can you separate the dyeing impact into components?
  (i.e., do you have data on: dye chemicals separately,
   water heating separately, wastewater treatment separately?)
  YES → Continue to Q-D3 (component-level allocation)
  NO  → Use DYE ABSORPTION ALLOCATION for full dyeing impact
        Rationale: Best available physical proxy
        Example (65/35 cotton-polyester):
          Cotton:    90% × dyeing impact
          Polyester: 10% × dyeing impact
        Document absorption rates used and their source
        → DONE for dyeing stage
  ↓
Q-D3: Component-level allocation (most accurate approach)
  Split dyeing into three sub-impacts:

  ├─ DYE CHEMICALS (mordants, dyes, auxiliaries)
  │    Allocate by: DYE ABSORPTION RATE
  │    Example: cotton 90% / polyester 10%
  │    Rationale: Chemical demand directly proportional to uptake
  │
  ├─ WATER HEATING (energy for hot dye bath)
  │    Allocate by: MASS (or bath volume share)
  │    Example: 65/35 for cotton-polyester blend
  │    Rationale: Heat is shared by the whole bath,
  │    not proportional to dye uptake
  │
  └─ WASTEWATER TREATMENT
       Allocate by: CHEMICAL OXYGEN DEMAND (COD) contribution
       If COD data unavailable → use MASS ALLOCATION
       Rationale: Wastewater burden scales with chemical load,
       which relates more to dye uptake than mass

  Document each sub-allocation separately.
```

---

### Worked Example: 65% Cotton + 35% Polyester, Dyeing Stage

**Total dyeing impact:** 1.2 kg CO₂/kg of fabric

**Method A — Mass allocation (current default):**
```
Cotton:    65% × 1.2 = 0.78 kg CO₂/kg
Polyester: 35% × 1.2 = 0.42 kg CO₂/kg
```

**Method B — Dye absorption allocation (Level 3):**
```
Cotton:    90% × 1.2 = 1.08 kg CO₂/kg
Polyester: 10% × 1.2 = 0.12 kg CO₂/kg
```

**Method C — Component-level allocation (most accurate):**
```
Dye chemicals (0.5 kg CO₂ of total):
  Cotton:    90% × 0.5 = 0.45 kg CO₂
  Polyester: 10% × 0.5 = 0.05 kg CO₂

Water heating (0.5 kg CO₂ of total):
  Cotton:    65% × 0.5 = 0.325 kg CO₂
  Polyester: 35% × 0.5 = 0.175 kg CO₂

Wastewater treatment (0.2 kg CO₂ of total):
  Cotton:    90% × 0.2 = 0.18 kg CO₂
  Polyester: 10% × 0.2 = 0.02 kg CO₂

TOTAL Cotton:    0.45 + 0.325 + 0.18 = 0.955 kg CO₂
TOTAL Polyester: 0.05 + 0.175 + 0.02 = 0.245 kg CO₂
```

**Comparison across methods:**

| Method | Cotton share | Polyester share | Cotton kg CO₂ | Polyester kg CO₂ |
|---|---|---|---|---|
| Mass allocation | 65% | 35% | 0.78 | 0.42 |
| Dye absorption | 90% | 10% | 1.08 | 0.12 |
| Component-level | ~80% | ~20% | 0.955 | 0.245 |

The difference between mass allocation and dye absorption allocation is **0.30 kg CO₂/kg** — equal to about 25% of the total dyeing impact, and a meaningful fraction of the garment's full footprint.

**Key insight (grounded in Jolliet Chapter 4, Section 4.5.3.8):** Mass allocation "should be avoided unless causality has been established." For dye chemicals, mass does NOT cause dye demand — fiber chemistry does. Method B or C is therefore more defensible than Method A, provided you have absorption rate data.

---

### When Disperse vs. Reactive Dye Types Matter

The dyeing chemistry differs fundamentally between fiber types:

- **Cotton** uses **reactive dyes** — high fixation rate (~70–80%), but unfixed dye becomes wastewater pollution
- **Polyester** uses **disperse dyes** — lower temperature fixation, but typically requires a separate dye bath at 130°C under pressure

In practice, most cotton-polyester blends are dyed in **two sequential baths** (one for each fiber), not one shared bath. If that is the case for the garment you are studying, the allocation problem largely disappears — each dye bath can be assigned 100% to its respective fiber (Level 1: process separation). This is the preferred approach if you can confirm the actual dyeing process used.

**Question to add to documentation checklist:**
> "Were the fibers dyed in one shared bath or two sequential baths?"
> - One shared bath → use dyeing allocation decision tree above
> - Two sequential baths → use process separation; no allocation needed for dyeing

---

## End-of-Life Allocation Decision Tree

End of life (what happens to the garment when it is thrown away or donated) is the stage most commonly **missing** from fashion LCA studies, and yet it can represent 10–20% of a garment's total lifetime impact. For blended fabrics it introduces a specific problem: unlike pure fibres, most blends **cannot currently be mechanically separated and recycled**, which has direct consequences for whether any recycling credit can be claimed.

This section adds an end-of-life branch to the main decision tree, grounded in Jolliet Chapter 4 (Section 4.5.5 on open-loop recycling) and the findings of Dhiwar & Bedarkar (2025), who note that "pathways for garment disposal are often assumed or not well documented."

---

### The Core End-of-Life Problem for Blends

A brand might claim their garment uses "recycled content" or is "recyclable." For blended fabrics, these claims require close scrutiny:

1. **Cutting scraps (manufacturing waste):** Generated during garment construction; typically 15–20% of fabric. For blends, these scraps are mixed fiber and very difficult to recycle.
2. **Post-consumer garments:** Donated or discarded garments at end of useful life. Sorting and recycling infrastructure for blends is extremely limited today.
3. **System expansion credit:** Only valid if the recycled output actually displaces something in the market. For most blends currently, it does not.

---

### End-of-Life Decision Tree

```
START: You are allocating the end-of-life stage for a blended garment

Q-E1: What is the realistic end-of-life pathway for this blend?
      (Choose based on evidence, NOT best-case assumption)

  ├─ LANDFILL / INCINERATION (most blends today)
  │    → No allocation needed; no credit possible
  │    → Assign landfill / incineration emissions 100%
  │       to the garment (proportional to fiber mass if needed)
  │    → Document: "End-of-life: landfill assumed based on
  │       current infrastructure for [blend type]"
  │    → Continue to Q-E4 for cutting scrap
  │
  ├─ MECHANICAL RECYCLING POSSIBLE
  │    → Continue to Q-E2
  │
  └─ CHEMICAL RECYCLING / NOVEL TECHNOLOGY
       → Continue to Q-E3
  ↓
Q-E2: Mechanical recycling — is fiber separation possible?
  (This is the critical question for blends)

  ├─ SINGLE FIBER (100% cotton, 100% polyester, etc.)
  │    → Mechanical recycling is realistic
  │    → Apply SYSTEM EXPANSION:
  │       Credit = avoided impact of virgin fiber production
  │       Example: 1 kg recycled cotton displaces 1 kg virgin cotton
  │       → Subtract 2.1 kg CO₂ per kg recycled (Textile Exchange 2024)
  │    → Document substitution ratio and data source
  │
  ├─ BLENDED FABRIC (cotton-polyester, viscose-elastane, etc.)
  │    → Ask: Does mechanical separation technology exist
  │      AND is it used in practice for this blend?
  │      YES (e.g., near-pure fiber with minor component)
  │        → Apply system expansion with substitution credit
  │        → Document technology used and actual market uptake
  │      NO (most blends currently)
  │        → NO recycling credit
  │        → Treat as landfill / incineration (see above)
  │        → Flag: "Blend cannot be mechanically separated;
  │           system expansion does not apply"
  │
  └─ HIGH ELASTANE (>5% elastane in any blend)
       → Elastane contamination blocks mechanical recycling
       → Even if base fiber is recyclable, treat as
         landfill / incineration
       → Flag this as a RED FLAG in sensitivity analysis
  ↓
Q-E3: Chemical recycling / novel technology
  (Emerging processes that dissolve and re-spin fibers)

  ├─ Is the technology commercially operational at scale?
  │    NO → Do NOT claim credit; treat as landfill
  │         Flag: "Chemical recycling not yet at commercial
  │         scale for this blend as of 2026"
  │    YES → Continue
  │
  ├─ Is there documented market demand for the output?
  │    NO → System expansion does not apply (Jolliet §4.5.3.4:
  │          "only valid when we can demonstrate that the
  │          substitution has actually happened")
  │    YES → Apply system expansion with substitution credit
  │          Document: technology name, scale, market uptake
  │
  └─ Is the chemical recycling credit for BOTH fibers
     or only one?
       Example: Evrnu technology separates cotton from polyester;
       cotton is recycled but polyester is currently lost.
       → Apply credit only to the fiber actually recovered
       → Assign remaining fiber to landfill
  ↓
Q-E4: Cutting scrap (manufacturing waste)
  This is separate from post-consumer end of life.
  Applies to the 15-20% of fabric wasted during garment cutting.

  ├─ Is the cutting scrap a single fiber or a blend?
  │    Single fiber → see Q-E2 (mechanical recycling may apply)
  │    Blend → most likely landfill / incineration (see Q-E1)
  │
  ├─ Is the cutting scrap actually collected and recycled
  │  in the factory you are studying?
  │    YES → Apply system expansion or process separation
  │           as appropriate; document factory practice
  │    NO  → Assign to landfill; no credit
  │
  └─ Is the cutting scrap sold to a third party for use
     in a different product (e.g., stuffing, insulation)?
       YES → This is open-loop recycling (Jolliet §4.5.5)
              Apply financial allocation at the point of separation:
              If scrap has positive value → split credit proportionally
              If factory pays to dispose of scrap → it is waste,
              no credit; assign full disposal impact to garment
       NO  → Landfill; no credit
```

---

### End-of-Life Worked Example: 65% Cotton + 35% Polyester T-Shirt

**Scenario A — Realistic current practice (landfill):**
```
End-of-life pathway: Municipal waste → landfill
Allocation: None required
Emissions: 0.08 kg CO₂/garment (methane from cotton decomposition,
           weighted by 65% mass share)
Recycling credit: NONE
Rationale: 65/35 blend cannot be mechanically separated;
           no commercial chemical recycling at scale (2026)
```

**Scenario B — Optimistic claim (recycling credit without evidence):**
```
⚠ WRONG APPROACH — included here to show what NOT to do ⚠
"We assume 15% of garments are collected and recycled."
Credit claimed: -0.3 kg CO₂/garment
Problem: No evidence of actual collection AND no separation
         technology for this blend → system expansion does not apply
         (Jolliet §4.5.3.4: substitution must "actually happen")
```

**Scenario C — Novel technology, documented (future):**
```
Assumption: Chemical recycling (e.g., Worn Again technology)
            commercially operational and recovering cotton fibre
Cotton recovered: 65% of garment mass = 0.13 kg per 200g garment
Virgin cotton displaced: 0.13 kg × 2.1 kg CO₂/kg = -0.27 kg CO₂
Polyester: not recovered by this technology → landfill
Net end-of-life credit: -0.27 kg CO₂/garment
Document: technology name, scale, market uptake rate, recovery ratio
```

**Comparison:**

| Scenario | End-of-life impact | Recycling credit | Approach |
|---|---|---|---|
| A: Landfill (realistic) | +0.08 kg CO₂ | None | No allocation needed |
| B: Recycling claim (unjustified) | −0.30 kg CO₂ | Claimed without evidence | **Do not use** |
| C: Partial chemical recycling | −0.19 kg CO₂ net | Justified, documented | Level 2 system expansion |

The difference between Scenario A and B is **0.38 kg CO₂/garment** — a meaningful number for a garment that may have a total footprint of around 5–8 kg CO₂. Unjustified end-of-life credits are one of the most common sources of greenwashing in fashion sustainability claims.

---

### End-of-Life by Blend Type: Quick Reference

| Blend | Can it be mechanically recycled today? | System expansion credit available? | Recommended approach |
|---|---|---|---|
| 65% Cotton + 35% Polyester | No — fibers cannot be separated | No | Landfill; no credit |
| 85% Viscose + 15% Elastane | No — elastane blocks recycling | No | Landfill; no credit; flag elastane |
| 90% + 10% Recycled Polyester | Polyester can be recycled | Yes — for polyester fraction only | Level 2 for polyester; landfill for any cotton component |
| 99% Cotton + 1% Elastane | Borderline — 1% elastane may be low enough | Uncertain — depends on recycler tolerance | Conservative: landfill; document uncertainty |
| 100% Cotton | Yes — in principle | Yes — if actually collected | Level 2 with evidence of collection and market uptake |
| 100% Polyester | Yes — PET recycling is mature | Yes — well-documented substitution | Level 2; use Textile Exchange recycled polyester credit |

---

### Updating the Documentation Checklist for End of Life

Add these items to the existing checklist:

```
☐ END-OF-LIFE PATHWAY
  ☐ Actual pathway documented (landfill, incineration, collection scheme)
  ☐ Confirmed whether blend can be separated for recycling
  ☐ Evidence cited if recycling credit is claimed
  ☐ Cutting scrap pathway documented separately from post-consumer

☐ RECYCLING CREDIT JUSTIFICATION (if claimed)
  ☐ Technology named and confirmed at commercial scale
  ☐ Market uptake documented (not just technically possible)
  ☐ Credit applied only to fiber fraction actually recovered
  ☐ Sensitivity analysis: result shown both with and without credit
```

---

## Sensitivity Analysis Template

For every blend allocation choice, document the sensitivity:

```
BLEND: [Name and composition]
PRIMARY ALLOCATION METHOD: [Level 1-6]

BASE CASE IMPACT: [X] kg CO₂/kg

SENSITIVITY ANALYSIS:
│
├─ Method variation:
│  ├─ If LEVEL 3 (Physical) used instead: ±[X]% → [Y] kg CO₂/kg
│  ├─ If LEVEL 4 (Mass) used instead: ±[X]% → [Y] kg CO₂/kg
│  ├─ If LEVEL 5 (Economic) used instead: ±[X]% → [Y] kg CO₂/kg
│  └─ RANGE: [Low] to [High] kg CO₂/kg
│
├─ Key assumption variation:
│  ├─ If use phase assumption changes (wash frequency, drying):
│  │  ±[X]% → [Y] kg CO₂/kg
│  ├─ If regional data changes (electricity grid, water):
│  │  ±[X]% → [Y] kg CO₂/kg
│  └─ Range: [Low] to [High] kg CO₂/kg
│
└─ TOTAL UNCERTAINTY: ±[X]% from base case

INTERPRETATION:
The [X]% uncertainty range reflects [describe main driver].
The most sensitive parameter is [parameter name].
Allocation method contributes [X]% of total uncertainty.
```

---

## Red Flags: When to Ask for Help

Stop and seek guidance if you encounter:

1. **A minor component with major impact**
   - Example: 1% elastane in cotton blend, but elastane has 40× impact per kg
   - Flag: "Cut-off method fails here; this component is too important"
   - Action: Use mass allocation explicitly, note the high uncertainty

2. **Recycled content without clear market substitution**
   - Example: "Recycled fiber blended into product" but no one actually uses the recycled version
   - Flag: "System expansion doesn't apply; no displacement"
   - Action: Use mass allocation, note that recycled claim may be overstated

3. **Mixed fiber scraps that cannot be recycled**
   - Example: 50/50 cotton-polyester blend; scraps are also 50/50
   - Flag: "These scraps have contamination; recycling isn't realistic"
   - Action: Don't model system expansion; use mass allocation

4. **Economic data with high volatility**
   - Example: Using price ratio when commodity prices swung 40% this year
   - Flag: "Economic allocation creates unstable results"
   - Action: Use mass allocation instead; economic allocation requires stable prices

5. **Blended fibers with process innovation**
   - Example: "New spinning technique where each fiber is processed separately, then blended"
   - Flag: "This might warrant process separation if processes truly separate"
   - Action: Document the actual process flow; may justify Level 1

---

## Documentation Checklist

For every blend LCA, document these five things:

```
☐ BLEND COMPOSITION
  ☐ Percentage by mass for each fiber
  ☐ Source/region if known (e.g., Indian cotton, Chinese polyester)
  ☐ Recycled content (if any) clearly marked

☐ ALLOCATION METHOD CHOICE
  ☐ Which level (1-6) for each supply chain stage
  ☐ Why that method (with specific justification)
  ☐ Alternative methods considered and rejected

☐ PROCESS-BY-PROCESS BREAKDOWN
  ☐ Upstream processes (before blending): 100% assignment
  ☐ Shared processes (after blending): allocation ratios shown
  ☐ Use phase: allocation ratios and assumptions shown

☐ SENSITIVITY ANALYSIS
  ☐ What happens if we used a different allocation method?
  ☐ What if key assumptions change (wash frequency, durability)?
  ☐ Uncertainty range clearly stated

☐ SOURCE OF DATA
  ☐ Are you using generic datasets (Ecoinvent)?
  ☐ Regional-specific data (if available)?
  ☐ Primary data from suppliers?
  ☐ Acknowledge data quality and limitations
```

---

## Common Mistakes to Avoid

**Mistake 1: Using mass allocation without documenting why**
```
WRONG: "We allocated 65/35 between cotton and polyester"
RIGHT: "We used mass allocation (65/35) for spinning and dyeing 
        because electrical work and dye bath impacts scale 
        proportionally with material mass. Upstream processes 
        used process separation."
```

**Mistake 2: Mixing allocation methods without noting it**
```
WRONG: Using system expansion for recycled content WITHOUT 
       disclosing you also used mass allocation elsewhere
RIGHT: Clearly label each stage with its method
```

**Mistake 3: Ignoring high-impact minor components**
```
WRONG: "Blend is 99% cotton + 1% elastane, so we ignored elastane"
RIGHT: "Elastane is 1% by mass but contributes ~8% of impact 
        due to high energy intensity. We used mass allocation 
        (99/1) to capture this."
```

**Mistake 4: Not documenting assumptions about joint processes**
```
WRONG: "Dyeing impact = 1.2 kg CO₂/kg"
RIGHT: "Dyeing impact = 1.2 kg CO₂/kg, allocated 65/35 (mass ratio) 
        between cotton and polyester. Note: Cotton absorbs ~90% 
        of dye in bath while polyester absorbs ~10%, but we lack 
        fiber-specific data, so mass allocation is a simplification."
```

**Mistake 5: Claiming precision you don't have**
```
WRONG: "This blend has 2.847 kg CO₂/kg"
RIGHT: "This blend has 2.8 kg CO₂/kg (range: 2.4-3.2 depending 
        on allocation method and use phase assumptions)"
```

---

## For Instructors & Practitioners

### When Using This Framework with Students

1. **Start with Level 4 (Mass Allocation)**
   - Students often feel uncertain; mass allocation is simple and defensible
   - Teach them to document *why* they chose it
   - Build confidence first

2. **Then introduce Levels 1-3**
   - Show how process separation improves accuracy
   - Demo system expansion with recycled content examples
   - Discuss physical allocation limitations

3. **Use wheat/straw case as an example**
   - Jolliet textbook shows how allocation method can change results 40×
   - This viscerally teaches why methodology matters
   - Then apply to blended fabrics

4. **Have them analyze real products**
   - Find two brands selling same blend
   - Research if they disclose allocation method (most don't)
   - Discuss: "How would results differ if they used different methods?"
   - This builds critical consumption of sustainability claims

### Contributing to Industry Standards

If you develop good allocation frameworks for specific blends:

1. **Document with data**
   - Collect real supply chain data for cotton-polyester blends
   - Show sensitivity analysis for your chosen method
   - Compare against Ecoinvent generic data

2. **Share open-source**
   - Contribute to Textile Exchange
   - Share with Sustainable Apparel Coalition
   - Publish as open methodology

3. **Push for standardization**
   - Current state: each company uses different methods (undisclosed)
   - Proposed state: industry agrees on best practice by blend type
   - Your framework becomes the reference

---

## References & Further Reading

- **ISO 14040:2006 / ISO 14044:2006** — Full standards on allocation procedures
- **Jolliet et al. (2015)** — Chapter 4 on inventory analysis and allocation (wheat/straw example)
- **Textile Exchange Standards** — Current industry practice (note: doesn't disclose allocation methods)
- **Higg Index** — Tool used by major brands; uses proprietary allocation methods

---

## Summary Table: Quick Reference

### Upstream & Manufacturing Allocation

| Blend Type | Preferred Method | Why | Uncertainty |
|---|---|---|---|
| **65% Cotton + 35% Polyester** | Level 1 (upstream) + Level 4 (shared) | Different supply chains, then mass allocation for shared | ±15% |
| **85% Viscose + 15% Elastane** | Level 4 (mass) with HIGH FLAG | No consensus on this blend; elastane is high-impact minor | ±20% |
| **90% Virgin + 10% Recycled Polyester** | Level 2 (system expansion) | Recycled content genuinely displaces virgin | ±12% |
| **99% Cotton + 1% Elastane** | Level 4 (mass) with caveat | Include elastane despite minor %; it's high-impact | ±8% |
| **100% Pure Fiber** | Level 1 (process separation) | Single supply chain; no fiber allocation needed | ±5% (use phase) |

### Dyeing Stage Allocation

| Data available | Recommended method | Cotton share (65/35 blend) | Polyester share |
|---|---|---|---|
| No fiber-specific data | Mass allocation (default) | 65% | 35% |
| Dye absorption rates known | Physical allocation by absorption | ~90% | ~10% |
| Full component data | Component-level allocation | ~80% | ~20% |
| Two separate dye baths confirmed | Process separation | 100% cotton bath to cotton | 100% polyester bath to polyester |

### End-of-Life Allocation

| Blend | Realistic pathway (2026) | Recycling credit? | Notes |
|---|---|---|---|
| **65% Cotton + 35% Polyester** | Landfill | None | Cannot be mechanically separated |
| **85% Viscose + 15% Elastane** | Landfill | None | Elastane blocks recycling |
| **90%+ Virgin Polyester** | PET recycling possible | Yes, if collected | Mature recycling infrastructure |
| **99% Cotton + 1% Elastane** | Cotton collection scheme | Uncertain | Document recycler tolerance for elastane |
| **100% Cotton** | Cotton collection scheme | Yes, if actually collected | Must evidence collection and market uptake |
| **100% Polyester** | PET recycling | Yes — well documented | Use Textile Exchange recycled polyester credit |

---

## References & Further Reading

- **ISO 14040:2006 / ISO 14044:2006** — Full standards on allocation procedures; Section 4.5 covers allocation hierarchy
- **Jolliet et al. (2015)** — Chapter 4 (pp. 87–115); wheat/straw example showing 40× variation by method; Section 4.5.3.8 on causal physical allocation; Section 4.5.5 on open-loop recycling
- **Dhiwar & Bedarkar (2025)** — Systematic review of 147 fashion LCA studies; documents lack of allocation transparency (*Discover Sustainability*, DOI: 10.1007/s43621-025-02050-7)
- **Watson & Wiedemann (2019)** — Review of allocation inconsistency across 10+ textile LCA tools (*Sustainability*, vol. 11, no. 14)
- **Textile Exchange Annual Fiber Benchmark (2024)** — Source for fiber impact data used in examples (cotton 2.1 kg CO₂/kg, polyester 5.5 kg CO₂/kg, recycled polyester 2.1 kg CO₂/kg)
- **Higg Index (Sustainable Apparel Coalition)** — Industry tool; allocation methods not disclosed to users
- **EU Product Environmental Footprint (PEF) Category Rules** — Forthcoming regulatory standard; textile-specific guidance expected 2025–2026

See `BLEND_REFERENCES.md` for full citations, access links, and recommended reading order.

---

**Last Updated:** 2026-05-31
**Status:** Ready for student use and practitioner feedback
**Feedback:** If you use this framework and find gaps, document what you found

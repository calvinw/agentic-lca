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

| Blend Type | Preferred Method | Why | Uncertainty |
|---|---|---|---|
| **65% Cotton + 35% Polyester** | Level 1 (upstream) + Level 4 (shared) | Different supply chains, then mass allocation for shared | ±15% |
| **85% Viscose + 15% Elastane** | Level 4 (mass) with HIGH FLAG | No consensus on this blend; elastane is high-impact minor | ±20% |
| **90% Virgin + 10% Recycled Polyester** | Level 2 (system expansion) | Recycled content genuinely displaces virgin | ±12% |
| **99% Cotton + 1% Elastane** | Level 4 (mass) with caveat | Include elastane despite minor %; it's high-impact | ±8% |
| **100% Pure Fiber** | Level 1 (process separation) | Single supply chain; no fiber allocation needed | ±5% (use phase) |

---

**Last Updated:** 2026-05-30  
**Status:** Ready for student use and practitioner feedback  
**Feedback:** If you use this framework and find gaps, document what you found

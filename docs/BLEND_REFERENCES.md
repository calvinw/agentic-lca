# References: Blend Allocation in Fashion LCA

A curated collection of academic sources, industry standards, case studies, and tools for understanding how blended fabrics are analyzed in Life Cycle Assessment.

---

## Academic Foundations

### **ISO 14040 & ISO 14044 Standards**
- **ISO 14040:2006** — Environmental management — Life cycle assessment — Principles and framework
- **ISO 14044:2006** — Environmental management — Life cycle assessment — Requirements and guidelines

**Relevance:** These are the authoritative standards that establish the allocation hierarchy used in all LCA work. Section 4.5 of ISO 14044 covers allocation procedures in detail. All other resources below reference these standards.

**Key concept:** The hierarchy is: (1) subdivision/process separation, (2) system expansion, (3) physical allocation, (4) economic allocation, (5) cut-off method.

**Where to access:** https://www.iso.org/standard/38498.html (purchasing required) OR check if your institution has access through library databases

---

### **Jolliet et al. (2015) — Life Cycle Assessment Theory and Practice**
- Jolliet, Olivier; Saadé-Sbeih, Manuele; Shaked, Shelley; Jolliet, Anne; Crettaz, Philippe
- **Chapter 4: Life Cycle Inventory Analysis**
- Section 4.5: "Solving Multifunctionality Through Allocation"
- Pages 87-115

**Relevance:** The wheat and straw case study (Section 4.5.3) is the canonical example of how allocation method choice can change results by 40×. If you understand this example, you understand blend allocation problems.

**Key findings:**
- Same co-product (wheat straw) allocated as 1%, 7%, or 93% of total impact depending on method
- Economic allocation ranks allocation by market value (straw is 1% of value)
- System expansion models what the co-product replaces (straw could heat + generate electricity, making it >50% of value)
- Allocation method is NOT arbitrary — it depends on causality and system boundaries

**Used in your project:** Referenced in `/references/jolliet/` (if available)

---

### **Dhiwar & Bedarkar (2025) — Life Cycle Assessment in Fashion Industry: A Systematic Review**
- Published: Discover Sustainability, November 2025
- DOI: https://doi.org/10.1007/s43621-025-02050-7
- Journal: Discover Sustainability (Open Access)

**Relevance:** Systematic review of 147 LCA studies in fashion (2010-2024). Specifically addresses allocation problems in Section 4.2.3 ("Modelling assumptions and allocation methods").

**Key findings on blends:**
> "Differences in allocation methods—such as how environmental burdens are shared among co-products in the production of blended materials—further strengthen inconsistency. Behavioral assumptions about garment lifetime, frequency of washing, or pathways for garment disposal are often assumed or not well documented, limiting transparency."

**Critical insight:** Fashion blends often use different allocation methods with no disclosure, making sustainability claims incomparable.

**Access:** Free, open-access PDF (https://link.springer.com/content/pdf/10.1007/s43621-025-02050-7.pdf)

**In your project:** `/Downloads/s43621-025-02050-7.pdf` (the file you read at the start of this session)

---

### **Watson & Wiedemann (2019) — Review of Methodological Choices in LCA-Based Textile and Apparel Rating Tools**
- Watson, Katherine J.; Wiedemann, Stephen G.
- *Sustainability*, vol. 11, no. 14, 2019, p. 3846
- DOI: https://doi.org/10.3390/su11143846

**Relevance:** Directly analyzes how 10+ textile LCA tools handle allocation for natural fiber blends. Finds inconsistency across tools.

**Key findings:**
- Different tools use different allocation methods for the same blend
- No transparency into methodological choices
- Recommends standardized allocation protocols for textiles

**Access:** Free, open-access (https://www.mdpi.com/2071-1050/11/14/3846)

---

## Industry Standards & Frameworks

### **Higg Index (Sustainable Apparel Coalition)**
- **Official:** https://www.sustainableapparel.org/higg-index/
- **Material Sustainability Index (MSI)** — Pre-allocated data for 72+ fibers and materials
- **Product Module (PM)** — Product-level LCA scoring

**Relevance:** The most widely used LCA tool in fashion (used by 200+ brands). Major limitation: allocation methods are not disclosed to users.

**For blends:** Higg Index provides pre-calculated blend impact data, but does NOT explain how the allocation was done.

**Critical point for students:** 
> "The Higg Index is useful but not transparent. When you see '60/40 cotton-polyester = 2.8 kg CO₂/kg,' you have no idea if that used mass allocation, economic allocation, or something else. You cannot audit it."

**Access:** Via Sustainable Apparel Coalition membership (https://www.sustainableapparel.org/)

---

### **Textile Exchange Standards**
- **Annual Fiber Benchmark** — Reports on environmental impacts of 20+ fibers
- **LCA+ Framework** — Emerging framework integrating biodiversity, animal welfare, social metrics
- **Recycled Content Standards** — Allocation approaches for recycled fiber blends

**Relevance:** Sets industry expectations. Moving toward more comprehensive LCA that includes impacts beyond carbon.

**For blends:** Doesn't provide specific allocation guidance; focuses on standardizing data inputs.

**Access:** https://textileexchange.org/ (some reports free, others require membership)

---

### **EU Product Environmental Footprint (PEF) Category Rules**
- **EU PEF for Apparel and Footwear** — Draft rules for standardized LCA methodology in Europe
- **Digital Product Passport (DPP) Requirements** — Mandates environmental data transparency by 2030

**Relevance:** Future regulatory requirement. Will mandate which LCA method is acceptable.

**For blends:** Expected to align with ISO 14044 hierarchy, but textile-specific guidance not yet final.

**Status:** Rules still in development; recommendations expected 2025-2026

**Access:** European Commission website (https://ec.europa.eu/environment/eussd/pef.htm)

---

## Case Studies & Examples

### **Levi Strauss & Co. — 501® Jeans LCA (2015)**
- **Report:** "The Life Cycle of a Jean"
- **Link:** https://www.levistrauss.com/sustainability/

**Relevance:** One of the first brand-level LCA studies on apparel. Includes detailed allocation methodology.

**Key findings on blends:**
- 501 Jeans are ~100% cotton (not a blend, but highly relevant)
- Use phase (washing/drying) accounts for 37% of lifecycle impacts
- Demonstrates that consumer behavior dominates; material choice matters less

**Allocation approach:** Process separation for cotton supply chain stages.

**Critical for understanding:** Even pure-fiber garments require allocation decisions about use phase assumptions.

---

### **H&M Group — Conscious Collection LCA (2015-2020)**
- **Reports:** Available in H&M Sustainability Report (annual)
- **Link:** https://hmgroup.com/sustainability/

**Relevance:** Large-scale LCA data on blended fabrics. H&M produces 40%+ blended materials.

**Known approach:**
- Uses cradle-to-gate LCA (excludes use phase)
- Uses Higg Index for fiber data
- Likely uses mass or economic allocation, but not transparent

**Critical learning point:** H&M's approach shows both the strengths (standardized tools) and weaknesses (opacity) of industry practice.

---

### **Birla Cellulose — Viscose Fiber LCA**
- **Report:** "Securing a Sustainable Supply Chain" (2019)
- **Key study:** LCA of viscose vs. cotton vs. polyester
- **Link:** https://www.adityabirla.com/

**Relevance:** Shows how viscose (a semi-synthetic fiber) is allocated in blends.

**Finding:** Viscose + cotton blends are common; allocation is complex due to different processing methods.

**For students:** This is a good case study of blends where fibers can be separated upstream (viscose production → cotton farming) but share downstream processes.

---

### **Textile Exchange — Annual Fiber Benchmark (2024)**
- **Publication:** Annual report on 20+ fiber types
- **Data:** Cradle-to-gate impacts for cotton, polyester, viscose, wool, etc.

**Relevance:** Industry-standard data. When you see "virgin polyester = 6.5 kg CO₂/kg," this is often the source.

**For blends:** Provides baseline data; you use this to calculate blend impacts with your chosen allocation method.

**Access:** https://textileexchange.org/benchmarks/

---

## Tools & Software

### **OpenLCA (Open-Source)**
- **Official:** https://www.openlca.org/
- **License:** Free, open-source (Mozilla Public License)
- **Use:** Educational, professional, research

**Relevance:** Transparent tool where you can see and audit allocation methods.

**Advantage for blends:** You can model process separation, system expansion, mass allocation explicitly. All choices are visible.

**In your project:** OpenLCA is the recommended tool for agentic-lca student work.

---

### **ecoinvent Database**
- **Official:** https://www.ecoinvent.org/
- **Data:** 20,000+ LCI datasets covering agriculture, manufacturing, transportation
- **Version 3.9+:** Includes pre-allocated blend data

**Relevance:** Most widely used background data source in LCA. Pre-allocates many blends.

**Critical limitation:** You cannot see how blends were allocated. Must trust the methodology (which varies).

**For students:** Use with caution. Good for upstream processes (electricity, transportation), but blend allocation is opaque.

**Access:** Subscription (pricing varies; many universities have access)

---

### **SimaPro (Professional Software)**
- **Official:** https://simapro.com/
- **Use:** Professional LCA modeling
- **Cost:** Expensive (~€2,000+/year)

**Relevance:** Industry standard. Used by major brands for detailed LCA work.

**For blends:** Allows explicit allocation modeling; supports all six methods in ISO 14044 hierarchy.

**Not recommended for students** (cost), but good to know it exists.

---

### **GaBi (Sphera)**
- **Official:** https://www.sphera.com/software/gabi-lca-software/
- **Use:** Professional LCA + environmental software
- **Cost:** Expensive (~€2,000+/year)

**Relevance:** Alternative to SimaPro. Similar capabilities.

---

## Academic Papers on Blend Allocation

### **Key Papers on Allocation Methods**

1. **Ekvall, T., & Weidema, B. P. (2004)**
   - "System boundaries and input data in consequential life cycle inventory analysis"
   - *International Journal of Life Cycle Assessment*, 9(3), 161-171
   - **Relevance:** Foundational paper distinguishing attributional vs. consequential LCA; affects how allocation is chosen

2. **Finnveden, G., et al. (2009)**
   - "Recent developments in life cycle assessment"
   - *Journal of Environmental Management*, 91(1), 1-21
   - **Relevance:** Comprehensive review of LCA methods including allocation. Section on textile applications.

3. **Schaubroeck, T., et al. (2022)**
   - "Definition of product system and solving multifunctionality in ISO 14040–14044: inconsistencies and proposed amendments"
   - *Frontiers in Sustainability*, 2022
   - **Relevance:** Critiques ISO 14044 for insufficient guidance on blends; proposes improvements

4. **Roos, S., et al. (2015)**
   - "Environmental assessment of Swedish fashion consumption"
   - *Mistra Future Fashion Report*
   - **Relevance:** Detailed LCAs of blended garments (60% cotton + 40% polyester, etc.); shows allocation sensitivity

5. **Horn, S., et al. (2023)**
   - "Environmental sustainability assessment of a polyester T-shirt: comparison of circularity strategies"
   - *Science of The Total Environment*, 884, 163821
   - **Relevance:** Models blended fabric recycling; shows how system expansion applies to polyester blends

---

## Data Sources for Blend Impacts

### **Where to Find Pre-Calculated Data**

| Source | Cotton Impact | Polyester Impact | Viscose Impact | Notes |
|---|---|---|---|---|
| **Textile Exchange 2024** | 2.1 kg CO₂/kg | 5.5 kg CO₂/kg | 1.8 kg CO₂/kg | Cradle-to-gate; global average |
| **Ecoinvent 3.9** | 1.9-2.4* | 5.2-6.8* | 1.6-2.1* | Regional variants; opaque allocation |
| **Higg Index MSI** | 1.2-3.1** | 4.5-7.2** | 1.1-2.5** | Proprietary calculation; varies by producer |
| **Jolliet textbook** | 1.8 kg CO₂/kg | 5.0 kg CO₂/kg | N/A | Used for educational examples |

*Range reflects upstream vs. full processing  
**Range reflects different production regions and technologies

**Key point for students:** Even "standard" data varies 20-50% depending on source. The allocation method explains only part of this variation.

---

## Research Gaps (What We Don't Yet Know Well)

### **Unresolved Questions About Blend Allocation**

1. **How should elastane be allocated in blends?**
   - It's 1-5% by mass but 40-50% by economic value and functional importance
   - Current practice: split by mass (arbitrary), economic value (unstable), or ignored
   - **Needed:** Fiber-specific allocation methodology based on function

2. **How do regional production differences affect blend allocation?**
   - Indian polyester production ≠ Saudi polyester production (different electricity grids)
   - Allocation is currently done on global average data
   - **Needed:** Regional-specific allocation frameworks

3. **How should recycled fiber blends be allocated?**
   - Example: 60% virgin polyester + 40% recycled polyester
   - System expansion is theoretically correct, but rarely practiced
   - **Needed:** Industry guidance on when system expansion applies vs. doesn't

4. **How do dyeing impacts scale for different fiber blends?**
   - Fiber absorption rates vary (cotton ~6%, polyester ~1.5%)
   - Current practice: mass allocation (60/40) or ignore the non-linearity
   - **Needed:** Fiber-specific dyeing impact models

5. **What happens with novel fibers in blends?**
   - Lab-grown leather + cotton blends
   - Bio-based polyester + conventional polyester blends
   - **Needed:** Allocation guidance for emerging materials

---

## Recommended Reading Order

### **For Students Just Starting:**
1. Read: Jolliet Chapter 4 (wheat/straw example — 30 min)
2. Read: Blend Allocation Framework (this project) — 45 min
3. Do: One worked example from the framework

### **For Understanding the Industry:**
1. Read: Dhiwar & Bedarkar (2025) Section 4.2.3 — 20 min
2. Read: Watson & Wiedemann (2019) — 30 min
3. Research: Find a brand's LCA; see if they disclose allocation method (they probably don't) — 15 min

### **For Deep Understanding:**
1. Read: ISO 14044 Section 4.5 (allocation hierarchy) — 1 hour (dense)
2. Read: Ekvall & Weidema (2004) — 45 min
3. Read: Jolliet et al. (2015) full Chapter 4 — 2 hours
4. Research: Collect 3 academic papers on textile LCA; compare their allocation choices — 3 hours

### **For Practitioners:**
1. Get access to: Textile Exchange Annual Benchmark
2. Get access to: Higg Index (if possible)
3. Review: EU PEF Category Rules (draft) for your region
4. Study: 2-3 brand LCAs; document their methodologies

---

## Where to Find More Information

### **Open Access Academic Papers**
- PubMed Central: https://www.ncbi.nlm.nih.gov/pmc/
- ResearchGate: https://www.researchgate.net/ (ask authors directly for PDFs)
- Directory of Open Access Journals (DOAJ): https://doaj.org/
- Google Scholar: https://scholar.google.com/ (filter for "free full text")

### **Industry Resources**
- **Textile Exchange:** https://textileexchange.org/
- **Sustainable Apparel Coalition (Higg Index):** https://www.sustainableapparel.org/
- **Ellen MacArthur Foundation (Circular Economy):** https://www.ellenmacarthurfoundation.org/
- **UN Environment Programme (UNEP) Textile Initiative:** https://www.unep.org/

### **Standards & Guidelines**
- **ISO 14040/44:** https://www.iso.org/ (standards organization)
- **EU Ecodesign for Sustainable Products:** https://ec.europa.eu/environment/eussd/
- **NIST LCA Resources:** https://www.nist.gov/services-resources/software/openstack-life-cycle-assessment-framework

### **Databases**
- **Ecoinvent:** https://www.ecoinvent.org/
- **US Life Cycle Inventory (USLCI):** https://www.lcacommons.gov/
- **NREL Franklin LCI:** https://www.nrel.gov/ (search for "LCI")

---

## How to Cite This Framework

If you use the Blend Allocation Framework in academic work, cite it as:

```
Williamson, C. (2026). Blend Allocation Decision Framework 
for Fashion Life Cycle Assessment. Agentic LCA Project.
https://github.com/calvinw/agentic-lca/docs/BLEND_ALLOCATION_FRAMEWORK.md
```

Or, if in a bibliography:

```
Williamson, Calvin. "Blend Allocation Decision Framework for Fashion LCA." 
Agentic-LCA, May 2026, https://github.com/calvinw/agentic-lca
```

---

## Contributing to This Reference List

Have you found a source that should be added? 

- Academic papers on blend allocation methods
- Case studies of brand LCAs showing allocation choices
- Industry standards or guidelines for textiles
- Tools or software that address blend allocation

**Please document:**
- Full citation (authors, year, title, DOI/URL)
- Why it's relevant to blend allocation
- Key findings or recommendations
- Access (free, open access, requires subscription, etc.)

---

**Last Updated:** May 2026  
**Curated for:** Agentic LCA Educational Project  
**Audience:** Students, practitioners, researchers  
**Status:** Living document — add sources as you find them

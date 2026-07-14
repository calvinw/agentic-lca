# Plan: Adding the BAFU-2025-LCI Database and openLCA LCIA Methods Pack

## What This Plan Covers

This plan describes two separate additions to the project that work well together:

1. **The BAFU-2025-LCI database** — a free Swiss background process database that
   provides life cycle inventory data for hundreds of materials, fuels, and
   transport modes. Think of it as a reference library of emission numbers for
   common industrial processes — so instead of hand-entering "nylon 6 emits
   ~9 kg CO₂ per kg produced", you just connect to the BAFU nylon process and
   the software looks it up automatically.

2. **The openLCA LCIA methods pack** — a free file that adds new impact assessment
   methods to the openLCA server. The most useful additions are:
   - **EF 3.1** — the European Commission's Environmental Footprint method (16
     impact categories)
   - **ReCiPe 2016 Midpoint (H)** — the most widely used global LCA method (18
     impact categories)
   - CML, ILCD, and several others

These two additions are independent — you can import one without the other. But
together they let you: (a) stop entering CO₂ numbers by hand for common materials,
and (b) score the results using European and global impact methods rather than
just the US-focused TRACI 2.2.

---

## Part 1 — The BAFU-2025-LCI Database

### What BAFU is

**BAFU** stands for *Bundesamt für Umwelt* — the Swiss Federal Office for the
Environment. BAFU:2025 is the Swiss Federal Administration's official life cycle
inventory database, released in 2025 and made freely available under Switzerland's
Open Government Data strategy.

The database contains **11,747 life cycle inventories across 176 categories**,
covering construction, mobility, energy, metals, chemicals, paper, agriculture,
food, consumption, and waste management. It is one of the largest freely available
LCA databases in the world.

- **Download:** https://nexus.openlca.org/database/BAFU
- **More info:** https://esu-services.ch/bafu2025/
- **Case study (plastic broom):** https://www.openlca.org/case-study-lca-of-a-plastic-broom-using-bafu2025/

### License

BAFU:2025 is **free of charge** under Switzerland's Open Government Data policy.
Two conditions apply:
1. **No resale** — you cannot sell the database or data extracted from it
2. **Mandatory citation** — any work using it must cite:
   > "Database of the Swiss Federal Administration, BAFU:2025,
   > Federal Office for the Environment, 2025."

This is completely fine for education, research, and student projects.

### File formats

| Format | Use |
|---|---|
| `.zolca` | Native openLCA format — import directly into the openLCA desktop app |
| `ecospold V1` | For SimaPro, Brightway (Python), R |

For our purposes, the `.zolca` file is what we need.

### What BAFU provides that we currently lack

In the current project, every CO₂ number in every product graph is hand-entered
based on published studies and literature estimates. For example:

```yaml
emissions:
  - { flow: Carbon dioxide, amount: 11.0 }   # ← hand-entered estimate
```

With BAFU imported, you can instead connect to a background process:

```
Input: Nylon 6 at plant [BAFU process]
→ openLCA automatically retrieves the full upstream CO₂ chain
```

The number is no longer your estimate — it comes from a peer-reviewed database.

### What BAFU covers

BAFU:2025 contains 11,747 processes in 176 categories. The full sector list:

**Construction** | **Mobility** | **Energy** | **Metals** | **Chemicals** |
**Paper** | **Agriculture** | **Food** | **Consumption** | **Waste management**

Processes confirmed available (from the broom case study video):
| Material / Process | Available in BAFU? |
|---|---|
| Nylon 6, at plant | Yes |
| PLA (polylactic acid) | Yes |
| Road transport, freight lorry 16–32t | Yes |
| Polyester (PET) | Likely yes (chemicals + consumption sectors) |
| Electricity (European grids) | Yes (energy sector) |
| Natural gas, diesel, coal | Yes (energy sector) |

BAFU is calibrated for **European conditions**. For US-specific processes
(US cotton farming, US electricity grid) the USLCI database is more accurate.
For a global textile supply chain, BAFU gives reasonable background data for
the processing and transport stages even if the farm stage uses US conditions.

Note: all datasets comply with BAFU DQRv2:2023 quality standards and are
compatible with the EF 3.1 impact method — making BAFU + EF 3.1 a natural pair.

### How to download BAFU-2025-LCI DB

**Step 1 — Go to nexus.openlca.org**

1. Visit https://nexus.openlca.org (free account required)
2. Search for **"BAFU"** or **"Swiss LCI"**
3. Download the latest `.zip` file

**Step 2 — Import into the running database**

Make sure the openLCA server is running (`bash start_olca.sh`), then import via
the openLCA desktop app:

> File → Import → Linked Data (JSON-LD) → select the `.zip` file → OK

Or try the API import endpoint (experimental):
```bash
curl -X POST http://localhost:8080/api/import \
  -H "Content-Type: application/octet-stream" \
  --data-binary @"$HOME/olca-data/BAFU-2025-LCI.zip"
```

**Step 3 — Verify processes are now available**

```python
python3 -c "
from olca_ipc.rest import RestClient
import olca_schema as o
client = RestClient('http://localhost:8080')
procs = client.get_descriptors(o.Process)
nylon = [p for p in procs if 'nylon' in p.name.lower()]
for p in nylon[:5]:
    print(p.name)
"
```

You should see processes like `Nylon 6, at plant` listed.

### Important limitation — product graph format

The current product graph format is **self-contained**: all emission values are
declared inside the YAML file itself. The product graph system does not yet support
referencing background database processes directly.

To use BAFU data today, there are two options:

**Option A — Use BAFU as a lookup reference only**
Run an analysis in the openLCA desktop app using BAFU processes, read the per-kg
CO₂ values from the results, and hand-enter those values into product graphs. This
is more accurate than estimates but still hand-entered.

**Option B — Extend the product graph format**
Add a `database_inputs` block to the product graph YAML that names BAFU processes
to connect to. This would require changes to `lca_analysis.py` to look up those
processes by name and wire them in automatically. This is a meaningful development
task but would make the system much more powerful.

Option A can be done immediately. Option B is a future development goal.

---

## Part 2 — The openLCA LCIA Methods Pack

### What the methods pack is

The **openLCA LCIA methods pack** is a free file available from nexus.openlca.org
that adds new impact assessment methods to any openLCA database. It does not
add process data — only the scoring methods (characterization factors) used to
convert a raw inventory (kg of CO₂, kg of SO₂, etc.) into impact scores.

The methods pack is fully additive — it does not change or remove TRACI 2.2.

### Methods included in the pack

| Method | Origin | Categories | Best for |
|---|---|---|---|
| **EF 3.1** | European Commission | 16 | European studies, EU product declarations |
| **ReCiPe 2016 Midpoint (H)** | Dutch/European consortium | 18 | Global studies, fashion/textiles |
| **ReCiPe 2016 Endpoint (H)** | Dutch/European consortium | 3 (aggregated) | Decision-making |
| CML-IA baseline | Leiden University | 11 | Legacy European studies |
| ILCD 2011 Midpoint | European Commission | 16 | EU policy and reporting |
| TRACI 2.2 | US EPA | 9 | Already loaded — US studies |

### How to download and import the methods pack

**Step 1 — Download (one time only)**

1. Go to https://nexus.openlca.org
2. Search for **"openLCA LCIA methods"**
3. Download the latest `.zip` file

**Step 2 — Import**

Same process as BAFU — use the desktop app or API endpoint:
```bash
curl -X POST http://localhost:8080/api/import \
  -H "Content-Type: application/octet-stream" \
  --data-binary @"$HOME/olca-data/openLCA_LCIA_methods_2_2.zip"
```

**Step 3 — Use in a product graph**

```yaml
# Change this one line:
lcia:
  method_name: "EF 3.1"

# Or this:
lcia:
  method_name: "ReCiPe 2016 Midpoint (H)"
```

No code changes needed. `lca_analysis.py` does a case-insensitive substring
search for the method name.

---

## Part 3 — EF 3.1 Impact Categories in Detail

EF 3.1 (Environmental Footprint version 3.1) is the European Commission's
official method for environmental product declarations and EU ecodesign policy.
It has **16 midpoint categories** — similar in concept to TRACI's 9, but broader
and calibrated for European and global conditions.

### EF 3.1 — All 16 Categories

| # | Category | Unit | Textile relevance |
|---|---|---|---|
| 1 | ★ Climate change | kg CO₂ eq | Yes — energy, farming, transport |
| 2 | ★ Ozone depletion | kg CFC-11 eq | Minor |
| 3 | ★ Human toxicity, cancer | CTUh | Yes — synthetic dyes, chemicals |
| 4 | Human toxicity, non-cancer | CTUh | Yes — processing chemicals |
| 5 | ★ Particulate matter | disease incidence | Yes — combustion, dust |
| 6 | Ionizing radiation, HH | kBq U-235 eq | Minor |
| 7 | ★ Photochemical ozone formation | kg NMVOC eq | Yes — solvents, dyes |
| 8 | ★ Acidification | mol H⁺ eq | Yes — coal energy, transport |
| 9 | ★ Eutrophication, freshwater | kg P eq | Yes — fertiliser runoff |
| 10 | ★ Eutrophication, marine | kg N eq | Yes — fertiliser |
| 11 | Eutrophication, terrestrial | mol N eq | Yes — fertiliser |
| 12 | ★ Ecotoxicity, freshwater | CTUe | Yes — dyes, pesticides |
| 13 | ★ Land use | Pt (soil quality) | Yes — cotton farming |
| 14 | ★ Water use | m³ world eq | Yes — cotton irrigation |
| 15 | ★ Resource use, fossils | MJ | Yes — polyester, energy |
| 16 | Mineral and metal resource use | kg Sb eq | Minor for textiles |

### EF 3.1 vs TRACI 2.2 vs ReCiPe — Comparison

| Feature | TRACI 2.2 | EF 3.1 | ReCiPe 2016 |
|---|---|---|---|
| Origin | US EPA | European Commission | Dutch/EU consortium |
| Categories | 9 | 16 | 18 |
| Geographic scope | North America | Global | Global |
| Water consumption | No | Yes | Yes |
| Land use | No | Yes (Pt) | Yes (m² yr) |
| Fossil resource use | No | Yes (MJ) | Yes (kg oil eq) |
| Used in EU ecodesign? | No | Yes | No |
| Used in fashion LCA studies? | Yes (US) | Yes (EU) | Yes (global) |
| Available now in our system? | Yes | After methods pack | After methods pack |

### What "disease incidence" and CTUh mean

EF 3.1 uses some units that look unfamiliar:

- **CTUh** (Comparative Toxic Unit for humans) — a measure of the probability of
  an additional person developing a serious illness. For example, 1.0 × 10⁻⁶ CTUh
  means one person in a million has an increased risk. Used for cancer and
  non-cancer toxicity.

- **CTUe** (Comparative Toxic Unit for ecosystems) — the fraction of species in
  a water body affected by toxic substances. Used for freshwater ecotoxicity.

- **Disease incidence** (for particulate matter) — the number of additional
  cases of respiratory disease per functional unit. Very small numbers like
  2.3 × 10⁻⁷ (about one case per four million garments).

- **Pt** (Points, for land use) — a dimensionless index of soil quality impact,
  derived from the area affected multiplied by its biodiversity sensitivity.

---

## Implementation Sequence

Both additions can be done independently, in either order. Recommended sequence:

### Phase 1 — Methods pack (quick win, ~30 minutes)

1. Create free account at nexus.openlca.org
2. Download openLCA LCIA methods pack `.zip`
3. Import into running database
4. Test by running an existing product graph with `method_name: "EF 3.1"`
5. Compare results to same product graph with `method_name: "TRACI 2.2"`

This immediately unlocks EF 3.1 and ReCiPe for all existing product graphs.

### Phase 2 — BAFU database (more involved, ~1–2 hours)

1. Download BAFU-2025-LCI DB from nexus.openlca.org
2. Import into running database (may take several minutes — it's a large dataset)
3. Verify key processes are available (nylon, PLA, polyester, transport)
4. Look up per-kg CO₂ values for materials used in existing product graphs
5. Compare BAFU-derived values against hand-entered estimates in our product graphs
6. Update product graphs where BAFU values differ significantly from estimates

### Phase 3 (future) — Product graph database_inputs extension

Extend the product graph YAML format to support:
```yaml
database_inputs:
  - { process: "Nylon 6, at plant", amount: 0.03, unit: kg }
  - { process: "Polylactide, at plant", amount: 0.52, unit: kg }
```

This would make our product graphs behave like the broom video — foreground model
hand-defined, background model drawn from BAFU automatically.

---

## Pedagogical Value

### What students learn from EF 3.1 vs TRACI

Running the same product through EF 3.1 and TRACI 2.2 teaches students:

1. **The scoring method is a choice** — the same supply chain produces different
   numbers depending on which method you use. There is no single "correct" answer.

2. **More categories = more complete picture** — TRACI's 9 categories miss water
   consumption and land use entirely. For a cotton garment, those two categories
   are huge. EF 3.1 and ReCiPe capture them.

3. **European vs American standards** — a company selling in the EU may be
   required to report using EF methodology. Understanding what that means, and
   why it differs from TRACI, is genuine industry knowledge.

4. **The hotspot can shift** — a product that looks "clean" on climate change
   may score poorly on land use or water consumption. Seeing all 16 categories
   at once prevents greenwashing by cherry-picking the best metric.

### The broom example as a teaching case

The plastic broom from the video is an excellent introductory example because:
- It has only two materials (nylon bristles + PLA handle)
- It has only one process (broom production)
- The hotspot is clear and surprising (PLA, not nylon)
- The transport scenario shows that transport often matters less than materials
- 1.70 vs 1.78 kg CO₂ eq teaches that short transport routes alone won't
  solve the problem if the material itself is high-impact

---

## References

- BAFU-2025-LCI DB: https://nexus.openlca.org (search "BAFU" or "Swiss LCI")
- openLCA LCIA methods pack: https://nexus.openlca.org/database/openLCA%20LCIA%20methods
- EF 3.1 documentation: European Commission Joint Research Centre, 2021
- EF 3.1 in LCA practice: used for EU Product Environmental Footprint (PEF) declarations
- Broom case study video source: GreenDelta / openLCA tutorial series

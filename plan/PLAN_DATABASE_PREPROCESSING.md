# PLAN: Database Preprocessing — Building openLCA Databases Without the Desktop App

## What this plan covers

How to build a pre-processed openLCA database (equivalent to what the openLCA desktop
app produces) using only Python and the gdt-server REST API, then store it for fast
reuse in GitHub releases. This approach replaces the need for the openLCA desktop
application entirely.

---

## Why this matters

The gdt-server is a calculation engine, not a database builder. It expects to be
pointed at a pre-built Apache Derby database folder. The standard way to build that
database is to use the openLCA desktop app — import a data pack, and the app writes
the Derby database to disk.

The problem: openLCA desktop is a 500MB GUI application. In a Codespace or CI
environment, you do not want to install a GUI app just to build a database.

The solution discovered in this project: the desktop app's import logic is available
in the open-source `olca-modules` Java library, which is also embedded inside
gdt-server. The gdt-server REST API exposes enough of that logic to replicate the
full import — if you import entities in the right order.

---

## The key insight: import order matters

The gdt-server's `ImpactCategoryReader` resolves each impact factor's flow by UUID
at import time. If the flow does not exist in the database when the ImpactCategory
is PUT, the factor is silently dropped and the LCIA score for that flow becomes zero.

**Correct import order:**
1. `UnitGroup` — unit systems (Mass, Energy, Volume, etc.)
2. `FlowProperty` — physical quantities (kg, kWh, m³, etc.)
3. `Flow` — elementary flows (CO₂, NOx, SO₂, etc.) that impact factors reference
4. `ImpactCategory` — the scoring rules, each referencing flows by UUID
5. `ImpactMethod` — groups of categories into a named method (TRACI 2.2, ReCiPe, etc.)

This is exactly the order the openLCA desktop app uses internally.

---

## The preprocessing script: `import_lca_data.py`

Located at the project root. Streams each entity type from the source zip in a
separate pass so only one type is in memory at a time (avoids OOM on the 60,000+
flow entries).

```
Source zip (JSON-LD format)
    │
    ├─ Pass 1: UnitGroup     (~10 entities)    → PUT /data/unit-group
    ├─ Pass 2: FlowProperty  (~10 entities)    → PUT /data/flow-property
    ├─ Pass 3: Flow          (~60,000 entities) → PUT /data/flow
    ├─ Pass 4: ImpactCategory (~550 entities)  → PUT /data/impact-category
    └─ Pass 5: ImpactMethod  (~45 entities)    → PUT /data/impact-method
                                                        │
                                               gdt-server writes to
                                               Apache Derby database
                                               ~/olca-data/databases/lca_methods/
```

After all passes complete, the Derby database folder is a fully functional
pre-built database identical to what the desktop app would have produced.

---

## Critical: the folder name inside the archive must match the -db flag

This is the easiest thing to get wrong and the hardest to diagnose because gdt-server
fails silently.

When `setup_olca.sh` starts the server with `-db lca_methods`, gdt-server looks for
`~/olca-data/databases/lca_methods/`. If that folder does not exist, it **silently
creates a new empty database** at that path. No error. No warning. The server starts
fine and responds to API calls — but every query returns zero results.

The tar archive must therefore contain the database folder under the name `lca_methods/`
(not `lca_commons/` or any other name). Always verify this before uploading:

```bash
# Check what folder name is inside the archive — must print "lca_methods/"
tar -tzf ~/olca-data/lca_methods-LCIA-methods-2.8.0-2026-06-18.tar.gz | head -1
```

The setup_olca.sh guard condition must also use the same name:

```bash
# In setup_olca.sh — these three names must all match:
LCA_COMMONS_DB="$DATA_DIR/databases/lca_methods"   # ← the check
tar -xzf ...                                         # ← extracts lca_methods/ from archive
docker run ... -db lca_methods                       # ← the server flag
```

If any of them differ, a new Codespace will silently get an empty database.

**History:** In June 2026, the database was renamed from `lca_commons` to `lca_methods`
throughout the scripts, but the tar.gz on GitHub releases was rebuilt from an empty
database (not the correctly-populated one). The result: every new Codespace had 0 LCIA
methods. The fix was to re-run the import, tar with the correct folder name, and
re-upload.

---

## The one-time build workflow

This workflow runs once per database. After it completes, the database is stored
in GitHub releases and never rebuilt unless the source data changes.

```
1. Start gdt-server pointed at an empty database named lca_methods
      docker rm -f olca-server
      docker run --name olca-server --network host \
          -v "$HOME/olca-data:/app/data" -d gdt-server:latest -db lca_methods
      # Wait for it to start: curl -s http://localhost:8080/api/version

2. Download the source zip from GitHub releases
      gh release download lca-data-v1 \
          --repo calvinw/agentic-lca \
          --pattern "openLCA.LCIA.Methods.*.zip" \
          --output "$HOME/olca-data/openLCA_LCIA_methods.zip"

3. Run the preprocessing script
      python3 import_lca_data.py
      # Takes ~20-30 minutes (60,000 flows is the slow pass)
      # If interrupted, see "Recovering from a partial import" below

4. Verify the database before tarballing
      python3 -c "
      from olca_ipc.rest import RestClient; import olca_schema as o
      c = RestClient('http://localhost:8080/')
      methods = list(c.get_descriptors(o.ImpactMethod))
      print(f'Methods: {len(methods)}')   # must be 45
      traci = [m.name for m in methods if 'traci' in (m.name or '').lower()]
      print(f'TRACI: {traci}')            # must include TRACI 2.2
      "

5. Stop the server cleanly before tarballing
      docker stop olca-server

6. Create the archive — folder name inside MUST be lca_methods/
      tar -czf ~/olca-data/lca_methods-LCIA-methods-2.8.0-$(date +%Y-%m-%d).tar.gz \
          -C ~/olca-data/databases lca_methods/

      # Verify the folder name inside the archive before uploading:
      tar -tzf ~/olca-data/lca_methods-LCIA-methods-*.tar.gz | head -1
      # Must print: lca_methods/

7. Upload to GitHub releases (--clobber replaces an existing file of the same name)
      gh release upload lca-data-v1 \
          ~/olca-data/lca_methods-LCIA-methods-*.tar.gz \
          --repo calvinw/agentic-lca --clobber
```

After step 7, all future Codespace sessions just download and unzip the pre-built
database. The import step never runs again unless the source data changes.

---

## Recovering from a partial import

The import can be interrupted mid-run (e.g. Codespace idle timeout during the
60,000-flow pass). The database is not corrupted — you can check what made it in
and run only the missing passes.

```python
# Check what's already in the database
from olca_ipc.rest import RestClient; import olca_schema as o
c = RestClient('http://localhost:8080/')
print(len(list(c.get_descriptors(o.Flow))))           # expect ~60,914
print(len(list(c.get_descriptors(o.ImpactCategory)))) # expect ~480 (550 in some packs)
print(len(list(c.get_descriptors(o.ImpactMethod))))   # expect 45
```

If flows and categories are in but methods are missing (the most likely interruption
point since it is the last pass), run only the ImpactMethod pass:

```python
import json, zipfile
from pathlib import Path
from olca_ipc.rest import RestClient; import olca_schema as o

PACK = Path.home() / "olca-data/openLCA_LCIA_methods.zip"
client = RestClient("http://localhost:8080/")
ok = total = 0
with zipfile.ZipFile(PACK) as zf:
    for name in zf.namelist():
        if not name.endswith(".json"): continue
        try:
            raw = json.loads(zf.read(name))
            items = raw if isinstance(raw, list) else \
                    raw.get("@graph", []) if "@graph" in raw else \
                    [raw] if "@type" in raw else []
            for item in items:
                if item.get("@type") == "ImpactMethod":
                    total += 1
                    if client.put(o.ImpactMethod.from_dict(item)):
                        ok += 1; print(f"  ✓ {item.get('name')}")
        except Exception: pass
print(f"Imported {ok}/{total} ImpactMethods")
```

Then continue from step 4 (verify) in the build workflow above.

---

## Current databases in GitHub releases (`lca-data-v1`)

| File | Size | Contents | Used by |
|---|---|---|---|
| `lca_methods-LCIA-methods-2.8.0-2026-06-18.tar.gz` | 74 MB | Pre-built Derby DB — 45 LCIA methods, 60,914 flows, 480 impact categories. Folder inside archive: `lca_methods/` | `setup_olca.sh` (download + unzip) |
| `openLCA.LCIA.Methods.2.8.0.2025-12-15.zip` | 157 MB | Source JSON-LD data pack | `import_lca_data.py` (source, kept for rebuilds) |

The methods pack zip is no longer downloaded by `setup_olca.sh` but is kept in the
release as the source material for rebuilding the tar.gz if needed (e.g. when a newer
methods pack version is released).

**Naming convention for the tar.gz:** include the methods pack version and build date so
it is clear which source was used:
`lca_methods-LCIA-methods-{pack-version}-{build-date}.tar.gz`

---

## Extending to other databases

The same pattern applies to any openLCA-compatible database.

### Free databases (public GitHub release)

**BAFU 2025** — 11,747 Swiss background processes, free download, EF 3.1 compatible

```
Source: bafu2025.zip from bafu.admin.ch (free)

Build:
  1. Start gdt-server with empty `bafu` database (-db bafu)
  2. python3 import_lca_data.py --source bafu2025.zip --db bafu
     Import order: UnitGroup → FlowProperty → Flow → Process → ImpactCategory → ImpactMethod
  3. tar -czf bafu.tar.gz -C ~/olca-data/databases bafu/
  4. gh release upload lca-data-v1 bafu.tar.gz --repo calvinw/agentic-lca

Setup script addition:
  if [ ! -d "$DATA_DIR/databases/bafu" ]; then
      curl -L "$RELEASE_BASE/bafu.tar.gz" | tar -xz -C "$DATA_DIR/databases/"
  fi
  docker run ... -db bafu
```

BAFU pairs naturally with `EF 3.1 Method (adapted)` which is already loaded in
`lca_methods`. If using lca_methods as the base database, BAFU processes can be
imported on top of it.

### Licensed databases (private GitHub repo)

**ecoinvent** — industry-standard, requires license from ecoinvent.org

ecoinvent is distributed as a `.zolca` file (openLCA's native export format).
This format is not a JSON-LD zip — it is a compressed Derby database snapshot.

```
Build (on a machine with the ecoinvent license):
  Option A — openLCA desktop app:
    1. Open openLCA desktop
    2. File → Import → .zolca file
    3. Close openLCA
    4. tar -czf ecoinvent.tar.gz -C ~/openLCA-data-1.4/databases ecoinvent/

  Option B — programmatic (if .zolca unpacks to JSON-LD):
    unzip ecoinvent.zolca -d ecoinvent_jsonld/
    python3 import_lca_data.py --source ecoinvent_jsonld/ --db ecoinvent
    tar -czf ecoinvent.tar.gz -C ~/olca-data/databases ecoinvent/

Storage:
  gh release create lca-data-v1 ecoinvent.tar.gz \
      --repo calvinw/ecoinvent-lca-db   ← private repository
```

Download in Codespace (authenticated via built-in GitHub token or Codespaces secret):
```bash
gh release download lca-data-v1 \
    --repo calvinw/ecoinvent-lca-db \
    --pattern "ecoinvent.tar.gz" \
    --output "$DATA_DIR/ecoinvent.tar.gz"
tar -xzf "$DATA_DIR/ecoinvent.tar.gz" -C "$DATA_DIR/databases/"
```

---

## Switching databases at runtime

Each database is a separate folder. The gdt-server is started with `-db <name>` 
pointing at whichever folder you want. Scripts:

| Script | Database | Use case |
|---|---|---|
| `setup_olca.sh` / `start_olca.sh` | `lca_methods` | Teaching with hand-written product graphs, all 45 LCIA methods |
| `start_olca_bafu.sh` (future) | `bafu` | Real background processes, EF 3.1, free |
| `start_olca_ecoinvent.sh` | `ecoinvent` | Industry-standard, requires license |

Product graphs are identical regardless of database — just change `method_name` in
the `lcia:` section to use a method available in the active database.

---

## When to rebuild a database

| Trigger | Action |
|---|---|
| New LCIA methods pack version released | Re-run import, re-upload with new date in filename |
| Database renamed in scripts (`-db` flag changed) | Re-tar with correct folder name inside archive, re-upload |
| New BAFU version released | Re-run import, re-upload bafu.tar.gz |
| New ecoinvent version | Re-run import on licensed machine, re-upload to private repo |
| Bug found in import script | Fix script, re-run, re-upload |
| New Codespace shows 0 LCIA methods | Check archive folder name (`tar -tzf ... \| head -1`), check `-db` flag matches |

The product graphs and analysis scripts do not need to change when a database is rebuilt —
they reference methods by name, which stays stable across versions.

---

## Summary

| | openLCA desktop app | This project's approach |
|---|---|---|
| Requires GUI | Yes | No |
| Works in Codespace/CI | No | Yes |
| Build time | ~5 min interactive | ~25 min unattended |
| Frequency | Every new environment | Once, then stored |
| Output | Derby database folder | Same Derby database folder |
| Result | Identical | Identical |

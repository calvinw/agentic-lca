#!/usr/bin/env python3
"""
import_lca_data.py

Imports FEDEFL elementary flows and TRACI 2.2 impact method into the
openLCA gdt-server database using the REST API.

Usage:
    python3 import_lca_data.py

Downloads required (free, no login) from https://www.lcacommons.gov/lca-collaboration/
    Federal LCA Commons / Elementary Flow List  → Federal_LCA_Commons-elementary_flow_list.zip
    Federal LCA Commons / TRACI 2.2             → Federal_LCA_Commons-TRACI_2_2.zip
Place both files in ~/olca-data/ before running.
"""

import json
import sys
import zipfile
from pathlib import Path

import requests
from olca_ipc.rest import RestClient
import olca_schema as o

SERVER = "http://localhost:8080/"
FEDEFL = Path.home() / "olca-data/Federal_LCA_Commons-elementary_flow_list.zip"
TRACI  = Path.home() / "olca-data/Federal_LCA_Commons-TRACI_2_2.zip"

# The only FEDEFL flows our recipe cards use — we skip the other 332,000+
NEEDED_FLOWS = {
    "carbon dioxide",
    "methane",
    "nitrous oxide",
    "ammonia",
    "nitrogen oxides",
    "sulfur dioxide",
    "water",
}

TYPE_MAP = {
    "UnitGroup":      o.UnitGroup,
    "FlowProperty":   o.FlowProperty,
    "Source":         o.Source,
    "Location":       o.Location,
    "Flow":           o.Flow,
    "ImpactMethod":   o.ImpactMethod,
    "ImpactCategory": o.ImpactCategory,
}

# ImpactCategory must come before ImpactMethod so that when the method is PUT,
# its impact_categories references already exist in the database.
IMPORT_ORDER = [
    "UnitGroup", "FlowProperty", "Source", "Location",
    "Flow", "ImpactCategory", "ImpactMethod",
]


def check_server():
    try:
        r = requests.get(f"{SERVER}api/version", timeout=5)
        ver = r.json().get("version", "?")
        print(f"  Server: gdt-server v{ver}  ✓")
    except Exception:
        print("  ERROR: openLCA server is not running.")
        print("  Start it first:  bash start_olca.sh")
        sys.exit(1)


def read_entities(zip_path: Path) -> list[dict]:
    """Read all JSON entities from a JSON-LD zip file."""
    entities = []
    with zipfile.ZipFile(zip_path) as zf:
        for name in zf.namelist():
            if not name.endswith(".json"):
                continue
            try:
                raw = json.loads(zf.read(name))
                # Handle both single objects and @graph arrays
                if isinstance(raw, list):
                    entities.extend(e for e in raw if isinstance(e, dict))
                elif isinstance(raw, dict) and "@graph" in raw:
                    entities.extend(e for e in raw["@graph"] if isinstance(e, dict))
                elif isinstance(raw, dict) and "@type" in raw:
                    entities.append(raw)
            except Exception:
                pass
    return entities


def put_entity(client: RestClient, data: dict) -> bool:
    t = data.get("@type")
    cls = TYPE_MAP.get(t)
    if cls is None:
        return False
    try:
        entity = cls.from_dict(data)
        ref = client.put(entity)
        return ref is not None
    except Exception as e:
        name = data.get("name", data.get("@id", "?"))
        print(f"    ✗ {t} '{name}': {e}")
        return False


def import_zip(client: RestClient, zip_path: Path, label: str,
               filter_flows: bool = False):
    print(f"\n  Reading {zip_path.name}...")
    entities = read_entities(zip_path)
    print(f"  Found {len(entities)} entities total.")

    # Group by type
    by_type: dict[str, list[dict]] = {}
    for e in entities:
        t = e.get("@type", "")
        by_type.setdefault(t, []).append(e)

    for type_name in IMPORT_ORDER:
        items = by_type.get(type_name, [])
        if not items:
            continue

        if type_name == "Flow" and filter_flows:
            before = len(items)
            items = [e for e in items
                     if e.get("name", "").strip().lower() in NEEDED_FLOWS]
            print(f"  {type_name}: filtered {before} → {len(items)} "
                  f"(only the flows our recipe cards use)")

        if not items:
            continue

        print(f"  Importing {len(items):>6,} {type_name}(s)...", end="", flush=True)
        ok = sum(1 for e in items if put_entity(client, e))
        print(f"  ✓ {ok}/{len(items)}")


def verify(client: RestClient):
    print("\n  Verification:")
    methods = client.get_descriptors(o.ImpactMethod)
    flows   = client.get_descriptors(o.Flow)
    print(f"    Impact methods in DB : {len(methods)}")
    print(f"    Flows in DB          : {len(flows)}")
    for m in methods:
        print(f"      ✓ {m.name}")
    if not methods:
        print("    ✗ No impact methods found — something went wrong.")


def main():
    print("=" * 60)
    print("  LCA Data Import — FEDEFL + TRACI 2.2")
    print("=" * 60)

    check_server()

    for path, label in [(FEDEFL, "FEDEFL"), (TRACI, "TRACI 2.2")]:
        if not path.exists():
            print(f"\n  ERROR: {path} not found.")
            print(f"  Download it from https://www.lcacommons.gov/lca-collaboration/")
            sys.exit(1)

    client = RestClient(SERVER)

    print("\n[1/2] Federal Elementary Flow List (FEDEFL)")
    print("      Importing only the 7 flows used in our recipe cards.")
    import_zip(client, FEDEFL, "FEDEFL", filter_flows=True)

    print("\n[2/2] TRACI 2.2 Impact Method")
    import_zip(client, TRACI, "TRACI 2.2", filter_flows=False)

    verify(client)

    print("\n  Done. You can now run:")
    print("    python3 lca_scripts/lca_analysis.py "
          "lca_analysis/cotton_shirt/recipe_card.md")
    print("=" * 60)


if __name__ == "__main__":
    main()

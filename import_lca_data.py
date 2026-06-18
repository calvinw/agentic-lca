#!/usr/bin/env python3
"""
import_lca_data.py

Imports the openLCA LCIA methods pack into the gdt-server database.
The pack includes TRACI 2.2, ReCiPe 2016, EF 3.1, ImpactWorld, CML, and more.

Uses multiple passes through the zip so that only one entity type is in memory
at a time — this avoids OOM when the pack contains 60,000+ flows.

Import order (each pass loads one type, imports it, then discards it):
  1. UnitGroup       (~10 entities)
  2. FlowProperty    (~10 entities)
  3. Flow            (~60,000 entities, streamed one file at a time)
  4. ImpactCategory  (~550 entities, streamed one at a time)
  5. ImpactMethod    (~45 entities)

Usage:
    python3 import_lca_data.py
"""

import json
import logging
import sys
import zipfile
from pathlib import Path

import requests
from olca_ipc.rest import RestClient
import olca_schema as o

logging.disable(logging.ERROR)

SERVER       = "http://localhost:8080/"
METHODS_PACK = Path.home() / "olca-data/openLCA_LCIA_methods.zip"

TYPE_MAP = {
    "UnitGroup":      o.UnitGroup,
    "FlowProperty":   o.FlowProperty,
    "Flow":           o.Flow,
    "ImpactMethod":   o.ImpactMethod,
    "ImpactCategory": o.ImpactCategory,
}


def check_server():
    try:
        r = requests.get(f"{SERVER}api/version", timeout=5)
        ver = r.json().get("version", "?")
        print(f"  Server: gdt-server v{ver}  ✓")
    except Exception:
        print("  ERROR: openLCA server is not running.")
        print("  Start it first:  bash start_olca.sh")
        sys.exit(1)


def iter_entities_of_type(zip_path: Path, target_type: str):
    """Yield entity dicts of target_type one at a time without loading the full zip."""
    with zipfile.ZipFile(zip_path) as zf:
        for name in zf.namelist():
            if not name.endswith(".json"):
                continue
            try:
                raw = json.loads(zf.read(name))
                items: list[dict] = []
                if isinstance(raw, list):
                    items = [e for e in raw if isinstance(e, dict)]
                elif isinstance(raw, dict) and "@graph" in raw:
                    items = [e for e in raw["@graph"] if isinstance(e, dict)]
                elif isinstance(raw, dict) and "@type" in raw:
                    items = [raw]
                for item in items:
                    if item.get("@type") == target_type:
                        yield item
            except Exception:
                pass


def put_entity(client: RestClient, data: dict) -> bool:
    t = data.get("@type")
    cls = TYPE_MAP.get(t)
    if cls is None:
        return False
    try:
        entity = cls.from_dict(data)
        ref = client.put(entity)
        return ref is not None
    except Exception:
        return False


def import_type(client: RestClient, type_name: str, zip_path: Path):
    """Stream entities of type_name from zip and import them one at a time."""
    ok = total = 0
    for entity in iter_entities_of_type(zip_path, type_name):
        total += 1
        if put_entity(client, entity):
            ok += 1
    if total:
        print(f"  Imported {ok:>6,}/{total:<6,} {type_name}(s)  {'✓' if ok == total else '!'}")
    else:
        print(f"  No {type_name} entities found in pack.")


def verify(client: RestClient):
    print("\n  Verification:")
    methods = client.get_descriptors(o.ImpactMethod)
    print(f"    Impact methods loaded: {len(methods)}")
    for m in methods:
        print(f"      ✓ {m.name}")
    if not methods:
        print("    ✗ No impact methods found — something went wrong.")


def any_method_loaded(client: RestClient) -> bool:
    try:
        return len(client.get_descriptors(o.ImpactMethod)) > 0
    except Exception:
        return False


def main():
    print("=" * 60)
    print("  LCA Methods Import")
    print("=" * 60)

    check_server()
    client = RestClient(SERVER)

    if any_method_loaded(client):
        print("\n  Impact methods already loaded — skipping import.")
        verify(client)
        print("=" * 60)
        return

    if not METHODS_PACK.exists():
        print(f"\n  ERROR: LCIA methods pack not found at {METHODS_PACK}")
        print(f"  Run setup_olca.sh to download it automatically.")
        sys.exit(1)

    print(f"\n  Importing LCIA methods pack (TRACI 2.2, ReCiPe 2016, EF 3.1, ImpactWorld, CML…)")
    print(f"  Processing in passes to keep memory usage low.\n")

    import_type(client, "UnitGroup",      METHODS_PACK)
    import_type(client, "FlowProperty",   METHODS_PACK)
    import_type(client, "Flow",           METHODS_PACK)
    import_type(client, "ImpactCategory", METHODS_PACK)
    import_type(client, "ImpactMethod",   METHODS_PACK)

    verify(client)

    if not any_method_loaded(client):
        print("\n  ✗ ERROR: No methods found after import — something went wrong.")
        sys.exit(1)

    print("\n  ✓ LCIA methods ready.")
    print("=" * 60)


if __name__ == "__main__":
    main()

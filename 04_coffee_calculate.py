"""
04_coffee_calculate.py

Runs the LCA inventory calculation for the coffee product system and
cross-checks the result against the hand-computed matrix math from
LCACoffeeExlainer.md.

Expected result: 0.1 kg CO₂ per cup of coffee.
"""

import json
import numpy as np
from olca_ipc.rest import RestClient
import olca_schema as o

client = RestClient("http://localhost:8080/")

ids = json.loads(open("coffee_ids.json").read())
system_id = ids["system_id"]

print("openLCA Inventory Calculation — Coffee (one cup)")
print("=" * 60)
print(f"Functional unit : 1 cup of coffee")
print(f"System ID       : {system_id}")

# ── 1. openLCA calculation ───────────────────────────────────────────────────

setup = o.CalculationSetup(
    target=o.Ref(id=system_id),
    amount=1.0,
)

print("\nCalculating via openLCA gdt-server...")
result = client.calculate(setup)
result.wait_until_ready()
print("Calculation complete.")

flows = result.get_total_flows()
outputs = [(f.envi_flow.flow.name, f.amount, f.envi_flow.flow.ref_unit)
           for f in flows if not f.envi_flow.is_input]

print("\nOUTPUTS TO NATURE (openLCA result)")
print("-" * 50)
print(f"  {'Flow':<30} {'Amount':>8}  Unit")
print("-" * 50)
for name, amount, unit in outputs:
    print(f"  {name:<30} {amount:>8.4f}  {unit}")

olca_co2 = next((amt for name, amt, _ in outputs if "CO2" in name or "co2" in name.lower()), None)

result.dispose()

# ── 2. Matrix cross-check (numpy) ────────────────────────────────────────────
#
# From LCACoffeeExlainer.md:
#   A · s = f  →  s = A⁻¹ · f
#   CO₂ = B · s
#
#         P1     P2     P3
# A = [[ 1.0,   0.0,   0.0 ],   ← coffee row
#      [-0.2,   1.0,   0.0 ],   ← boiled water row
#      [ 0.0,  -0.5,   1.0 ]]   ← electricity row
#
# f = [1, 0, 0]   (1 cup of coffee, nothing else)
# B = [0, 0, 1]   (CO₂ only from P3)

A = np.array([
    [ 1.0,  0.0,  0.0],
    [-0.2,  1.0,  0.0],
    [ 0.0, -0.5,  1.0],
])
f = np.array([1.0, 0.0, 0.0])
B = np.array([[0.0, 0.0, 1.0]])

s      = np.linalg.solve(A, f)
co2_np = float((B @ s)[0])

print("\nNUMPY CROSS-CHECK (matrix math from explainer)")
print("-" * 50)
print(f"  Scaling vector s : {s}")
print(f"    P1 (make coffee) runs  : {s[0]:.1f}×")
print(f"    P2 (boil water)  runs  : {s[1]:.1f}×")
print(f"    P3 (burn coal)   runs  : {s[2]:.1f}×")
print(f"  Total CO₂ (B · s)        : {co2_np:.4f} kg")

# ── 3. Comparison ────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("RESULT COMPARISON")
print("-" * 50)
print(f"  openLCA result : {olca_co2:.4f} kg CO₂" if olca_co2 else "  openLCA result : (not found)")
print(f"  Numpy result   : {co2_np:.4f} kg CO₂")
print(f"  Explainer      : 0.1000 kg CO₂")

if olca_co2 is not None and abs(olca_co2 - co2_np) < 1e-6:
    print("\n  MATCH — openLCA and matrix math agree.")
else:
    print("\n  WARNING — results differ. Check process linkage in product system.")

print("\nOutput format (from skill):")
print("-" * 50)
print(f"Functional unit : 1 cup of coffee (toy model, no geography)")
print(f"System model    : manual / not ecoinvent")
print()
print(f"{'Flow':<28} {'Amount':>10}  Unit")
print(f"{'-'*28} {'-'*10}  ----")
print(f"{'CO₂ to air':<28} {co2_np:>10.4f}  kg")
print()
print("Key driver: P3 (Burn coal) is the sole source of CO₂ — 100% of impact.")
print("            P1 and P2 have no direct emissions.")
print("Caveats   : Toy model. Coal grid, no water use, no upstream forestry.")

"""
02_calculate.py

Runs the LCA inventory calculation for the paper cup product system
and prints a formatted results table — matching Phase 3 of the LCA walkthrough.

Prerequisites:
  01_build_model.py must have been run first (model_ids.json must exist).
  The gdt-server must still be running on localhost:8080.
"""

import json
from olca_ipc.rest import RestClient
import olca_schema as o

client = RestClient("http://localhost:8080/")

# Load IDs written by 01_build_model.py
ids = json.loads(open("model_ids.json").read())
system_id = ids["system_id"]

print("openLCA Inventory Calculation — Paper Cup (cradle to grave)")
print("=" * 60)
print(f"Product system : {system_id}")
print(f"Functional unit: 1 paper cup (1 beverage served)")

# ── Run the calculation ───────────────────────────────────────────────────────
setup = o.CalculationSetup(
    target=o.Ref(
        ref_type=o.RefType.ProductSystem,
        id=system_id,
    ),
    amount=1.0,                          # 1 paper cup
    calculation_type=o.CalculationType.SIMPLE_CALCULATION,
)

print("\nCalculating...")
result = client.calculate(setup)
result.wait_until_ready()
print("Calculation complete.")

# ── Retrieve inventory results ────────────────────────────────────────────────
inventory = result.get_total_flows()

# Separate into Inputs (from nature) and Outputs (to nature)
inputs  = [(i.envi_flow.flow.name, i.amount, i.envi_flow.flow.ref_unit)
           for i in inventory if i.envi_flow.is_input]
outputs = [(i.envi_flow.flow.name, i.amount, i.envi_flow.flow.ref_unit)
           for i in inventory if not i.envi_flow.is_input]

# ── Print results ─────────────────────────────────────────────────────────────
def print_section(title, rows):
    print(f"\n{title}")
    print("-" * 52)
    print(f"  {'Flow':<34} {'Amount':>10}  Unit")
    print("-" * 52)
    for name, amount, unit in sorted(rows, key=lambda r: abs(r[1]), reverse=True):
        print(f"  {name:<34} {amount:>10.4f}  {unit}")

print_section("INPUTS FROM NATURE", inputs)
print_section("OUTPUTS TO NATURE",  outputs)

# ── Simple GWP calculation ────────────────────────────────────────────────────
# Characterization factors (kg CO2-eq per kg)
GWP_FACTORS = {
    "Carbon dioxide, to air":       1.0,
    "Methane, to air (CO2-eq)":    28.0,   # GWP100
    "Nitrogen oxides, to air":      0.0,   # not a GWP gas
}

print("\nIMPACT ASSESSMENT — Global Warming Potential (GWP100)")
print("-" * 52)
gwp_total = 0.0
for name, amount, unit in outputs:
    cf = GWP_FACTORS.get(name, 0.0)
    if cf > 0:
        contribution = amount * cf
        gwp_total += contribution
        print(f"  {name:<34} {contribution:>10.6f}  kg CO2-eq")
print("-" * 52)
print(f"  {'TOTAL GWP':<34} {gwp_total:>10.6f}  kg CO2-eq")

# ── Water use ─────────────────────────────────────────────────────────────────
print("\nIMPACT ASSESSMENT — Freshwater Consumption")
print("-" * 52)
water_total = 0.0
for name, amount, unit in inputs:
    if "freshwater" in name.lower() or "water" in name.lower():
        water_total += amount
        print(f"  {name:<34} {amount:>10.4f}  {unit}")
print("-" * 52)
print(f"  {'TOTAL water use':<34} {water_total:>10.4f}  L")

result.dispose()

print("\n" + "=" * 60)
print("Done. Result disposed.")

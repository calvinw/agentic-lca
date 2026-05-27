"""
03_coffee_build.py

Builds the coffee LCA model in openLCA from the LCACoffeeExlainer.md example.

System:
  P1: Make coffee    — consumes 0.2L boiled water → produces 1 cup coffee
  P2: Boil water     — consumes 0.5 kWh electricity → produces 1L boiled water
  P3: Burn coal      — consumes coal (biosphere) → produces 1 kWh electricity
                       emits 1 kg CO₂ to air

Expected scaling vector:  s = [1.0, 0.2, 0.1]
Expected total CO₂:       0.1 kg per cup of coffee
"""

import json
import pathlib
from olca_ipc.rest import RestClient
import olca_schema as o

client = RestClient("http://localhost:8080/")

print("Connected to openLCA gdt-server")
print("=" * 60)

# ── 1. UNIT GROUPS & FLOW PROPERTIES ────────────────────────────────────────

print("\n[1] Creating unit groups and flow properties...")

count_units  = o.new_unit_group("Coffee count units", "cup")
volume_units = o.new_unit_group("Coffee volume units", "L")
energy_units = o.new_unit_group("Coffee energy units", "kWh")
mass_units   = o.new_unit_group("Coffee mass units", "kg")

count  = o.new_flow_property("Coffee count",  count_units)
volume = o.new_flow_property("Coffee volume", volume_units)
energy = o.new_flow_property("Coffee energy", energy_units)
mass   = o.new_flow_property("Coffee mass",   mass_units)

client.put_all(count_units, volume_units, energy_units, mass_units,
               count, volume, energy, mass)
print("  Done.")

# ── 2. PRODUCT FLOWS (technosphere — intermediate flows) ────────────────────

print("\n[2] Creating product flows...")

coffee       = o.new_product("Coffee (cup)",         count)   # P1 output
boiled_water = o.new_product("Boiled water (L)",     volume)  # P2 output
electricity  = o.new_product("Electricity (kWh)",    energy)  # P3 output

client.put_all(coffee, boiled_water, electricity)
print("  Done.")

# ── 3. ELEMENTARY FLOW — CO₂ emission ───────────────────────────────────────

print("\n[3] Creating elementary flow (CO₂ to air)...")

co2 = o.new_elementary_flow("CO2, to air (coffee example)", mass)
client.put(co2)
print("  Done.")

# ── 4. UNIT PROCESSES ───────────────────────────────────────────────────────
# Matrix A (from explainer):
#           P1      P2      P3
# coffee   +1       0       0
# b.water  -0.2    +1       0
# elec      0      -0.5    +1
#
# Matrix B:
#           P1   P2   P3
# CO2        0    0    1

print("\n[4] Creating unit processes...")

# P1: Make coffee
p1 = o.new_process("P1: Make coffee")
ref = o.new_output(p1, coffee, 1.0)       # produces 1 cup coffee
ref.is_quantitative_reference = True
o.new_input(p1, boiled_water, 0.2)        # consumes 0.2L boiled water
client.put(p1)

# P2: Boil water
p2 = o.new_process("P2: Boil water")
ref = o.new_output(p2, boiled_water, 1.0) # produces 1L boiled water
ref.is_quantitative_reference = True
o.new_input(p2, electricity, 0.5)         # consumes 0.5 kWh
client.put(p2)

# P3: Burn coal
p3 = o.new_process("P3: Burn coal")
ref = o.new_output(p3, electricity, 1.0)  # produces 1 kWh
ref.is_quantitative_reference = True
o.new_output(p3, co2, 1.0)               # emits 1 kg CO₂ per run
client.put(p3)

print("  Done.")

# ── 5. PRODUCT SYSTEM ───────────────────────────────────────────────────────

print("\n[5] Creating product system (auto-link)...")

# create_product_system auto-links processes by matching flow inputs/outputs
system_ref = client.create_product_system(p1)
if system_ref is None:
    raise RuntimeError("create_product_system returned None — check server logs")
print(f"  Created: {system_ref.name} ({system_ref.id})")
print("  Done.")

# ── 6. SAVE IDs ──────────────────────────────────────────────────────────────

ids = {
    "system_id": system_ref.id,
    "p1_id": p1.id,
    "p2_id": p2.id,
    "p3_id": p3.id,
    "co2_id": co2.id,
}
pathlib.Path("coffee_ids.json").write_text(json.dumps(ids, indent=2))

print("\n" + "=" * 60)
print("Coffee model built successfully.")
print(f"  Product system : {system_ref.name}")
print(f"  System ID      : {system_ref.id}")
print(f"  Functional unit: 1 cup of coffee")
print("\nRun 04_coffee_calculate.py to compute the inventory.")

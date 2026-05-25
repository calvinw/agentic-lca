"""
01_build_model.py

Builds the paper cup LCA model in openLCA from scratch via the IPC API.
Mirrors exactly the three-category inventory structure we discussed:
  - Processes  : intermediate product flows between unit processes
  - Inputs     : elementary flows FROM nature
  - Outputs    : elementary flows TO nature

Prerequisites:
  pip install olca-ipc olca-schema
  The gdt-server must be running on localhost:8080 (run setup_olca.sh first).
"""

import olca_ipc as ipc
import olca_schema as o

client = ipc.Client(8080)

print("Connected to openLCA IPC server")
print("=" * 60)

# ── 1. UNIT GROUPS & FLOW PROPERTIES ─────────────────────────────────────────
# These are the measurement systems. openLCA needs these before flows can
# be created because every flow must have a unit.

print("\n[1] Creating unit groups and flow properties...")

mass_units    = o.new_unit_group("Mass units",    "kg")
volume_units  = o.new_unit_group("Volume units",  "L")
energy_units  = o.new_unit_group("Energy units",  "MJ")
area_time     = o.new_unit_group("Area·time units","m2*a")
count_units   = o.new_unit_group("Counting units", "Item(s)")

mass    = o.new_flow_property("Mass",              mass_units)
volume  = o.new_flow_property("Volume",            volume_units)
energy  = o.new_flow_property("Energy",            energy_units)
land    = o.new_flow_property("Land use",          area_time)
count   = o.new_flow_property("Number of items",   count_units)

client.put_all(
    mass_units, volume_units, energy_units, area_time, count_units,
    mass, volume, energy, land, count,
)
print("  Unit groups and flow properties created.")

# ── 2. PRODUCT FLOWS (Processes — intermediate flows) ─────────────────────────
# These are the goods and services that flow between unit processes.
# They are "product flows" in openLCA terminology.

print("\n[2] Creating product flows (intermediate / process flows)...")

wood_pulp   = o.new_product("Wood pulp",               mass)    # g → use kg
pe_resin    = o.new_product("Polyethylene resin",       mass)
electricity = o.new_product("Electricity",              energy)
heat_steam  = o.new_product("Heat / steam",             energy)
transport   = o.new_product("Road transport (truck)",   energy)
landfill_sv = o.new_product("Landfill disposal service",count)
paper_cup   = o.new_product("Paper cup",                count)   # the product

client.put_all(
    wood_pulp, pe_resin, electricity, heat_steam,
    transport, landfill_sv, paper_cup,
)
print("  Product flows created.")

# ── 3. ELEMENTARY FLOWS — INPUTS FROM NATURE ─────────────────────────────────
# Resources extracted directly from the environment.

print("\n[3] Creating elementary flows — Inputs from nature...")

freshwater_pulp  = o.new_elementary_flow("Freshwater, pulping",  volume)
freshwater_cool  = o.new_elementary_flow("Freshwater, cooling",  volume)
land_use         = o.new_elementary_flow("Land use",             land)
crude_oil_input  = o.new_elementary_flow("Crude oil, in ground", mass)

client.put_all(freshwater_pulp, freshwater_cool, land_use, crude_oil_input)
print("  Input elementary flows created.")

# ── 4. ELEMENTARY FLOWS — OUTPUTS TO NATURE ──────────────────────────────────
# Emissions released to air, water, or land.

print("\n[4] Creating elementary flows — Outputs to nature...")

co2_air      = o.new_elementary_flow("Carbon dioxide, to air",         mass)
ch4_air      = o.new_elementary_flow("Methane, to air (CO2-eq)",        mass)
nox_air      = o.new_elementary_flow("Nitrogen oxides, to air",         mass)
bod_water    = o.new_elementary_flow("BOD, to water",                   mass)
solid_waste  = o.new_elementary_flow("Solid waste, to land",            mass)

client.put_all(co2_air, ch4_air, nox_air, bod_water, solid_waste)
print("  Output elementary flows created.")

# ── 5. UNIT PROCESSES ─────────────────────────────────────────────────────────
# Each process represents one life stage.
# Convention: positive values = outputs, negative values = inputs.
# The quantitative reference of each process is its main output product.
#
# All quantities are per ONE paper cup (functional unit).
# We use kg throughout (1 g = 0.001 kg).

print("\n[5] Creating unit processes...")

# Helper: add an exchange to a process
def inp(process, flow, amount):
    return o.new_input(process, flow, amount)

def out(process, flow, amount):
    return o.new_output(process, flow, amount)

# ── Process 1: Forestry & pulp production ─────────────────────────────────────
p1 = o.new_process("Forestry and pulp production")
e = out(p1, wood_pulp, 0.0101)       # 10.1 g = 0.0101 kg wood pulp (reference)
e.is_quantitative_reference = True
inp(p1, land_use,        0.05)        # 0.05 m2*a land use (INPUT from nature)
inp(p1, crude_oil_input, 0.0021)      # 2.1 g crude oil (INPUT from nature)
out(p1, co2_air,         0.001)       # 1.0 g CO2 from logging machinery (OUTPUT)
client.put(p1)

# ── Process 2: Cup manufacturing ──────────────────────────────────────────────
p2 = o.new_process("Cup manufacturing")
e = out(p2, paper_cup, 1.0)           # 1 paper cup (reference output)
e.is_quantitative_reference = True
inp(p2, wood_pulp,       0.0101)      # 10.1 g pulp from forestry
inp(p2, pe_resin,        0.0015)      # 1.5 g PE resin (coating)
inp(p2, electricity,     0.025)       # 0.025 MJ electricity
inp(p2, heat_steam,      0.062)       # 0.062 MJ thermal energy
inp(p2, freshwater_pulp, 13.1)        # 13.1 L process water (INPUT from nature)
inp(p2, freshwater_cool, 1.2)         # 1.2 L cooling water (INPUT from nature)
out(p2, co2_air,         0.004)       # 4.0 g CO2 to air (OUTPUT)
out(p2, bod_water,       0.0003)      # 0.3 g BOD to water (OUTPUT)
client.put(p2)

# ── Process 3: Distribution ────────────────────────────────────────────────────
p3 = o.new_process("Distribution (truck transport)")
e = out(p3, paper_cup, 1.0)           # cup passes through, still 1 unit
e.is_quantitative_reference = True
inp(p3, transport, 0.005)             # 0.005 MJ diesel transport per cup
out(p3, nox_air,   0.00002)           # 0.02 g NOx to air (OUTPUT)
client.put(p3)

# ── Process 4: Use ────────────────────────────────────────────────────────────
p4 = o.new_process("Use — one beverage served")
e = out(p4, paper_cup, 1.0)           # functional unit: 1 cup, 1 drink
e.is_quantitative_reference = True
# No significant elementary flows at use stage for a single-use cup
client.put(p4)

# ── Process 5: Landfill disposal ──────────────────────────────────────────────
p5 = o.new_process("Landfill disposal")
e = inp(p5, landfill_sv, 1.0)         # receives 1 cup for disposal
e.is_quantitative_reference = True
out(p5, ch4_air,    0.0008)           # 0.8 g CH4 (as CO2-eq) to air (OUTPUT)
out(p5, solid_waste, 0.0116)          # 11.6 g solid waste to land (OUTPUT)
client.put(p5)

print("  All unit processes created.")

# ── 6. PRODUCT SYSTEM ─────────────────────────────────────────────────────────
# A product system links the unit processes into a connected network.
# The reference process is the one that delivers the functional unit.

print("\n[6] Creating product system...")

system = o.new_product_system(
    "Paper cup — cradle to grave",
    p4,  # reference process = Use (delivers the functional unit)
)
system.processes = [
    o.Ref(id=p1.id),
    o.Ref(id=p2.id),
    o.Ref(id=p3.id),
    o.Ref(id=p4.id),
    o.Ref(id=p5.id),
]
client.put(system)
print("  Product system created.")

print("\n" + "=" * 60)
print("Model build complete.")
print(f"  Product system ID : {system.id}")
print(f"  Reference process : {p4.name}")
print(f"  Functional unit   : 1 paper cup (1 beverage served)")
print("\nRun 02_calculate.py to compute the inventory.")

# Save IDs for the next script
import json, pathlib
ids = {
    "system_id":   system.id,
    "ref_process": p4.id,
}
pathlib.Path("model_ids.json").write_text(json.dumps(ids, indent=2))
print("  IDs saved to model_ids.json")

# Life Cycle Inventory (LCI) Analysis — A Coffee Example

## Overview

This document walks through all the steps of a Life Cycle Inventory (LCI) analysis using a simple example: making one cup of coffee. The goal is to calculate how much CO₂ is emitted to produce that one cup.

The key idea is that nothing is made in isolation. Making coffee requires boiling water, boiling water requires electricity, and generating electricity requires burning coal. These dependencies form a chain — and the matrix math unravels that chain exactly.

---

## Step 1 — Goal and Scope

### Functional unit

The functional unit is the qualitative definition of what the system is supposed to deliver:

> "One cup of coffee"

### Reference flow vector (f)

The reference flow vector f is the mathematical expression of the functional unit. It states what we want to end up with at the end of the day:

- 1 cup of coffee (the final output)
- 0 litres of boiled water left over (used up internally)
- 0 kWh of electricity left over (used up internally)

$$
f = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
$$

The zeros say: all intermediate products should be consumed internally. The only thing leaving the system is coffee.

---

## Step 2 — The Product Graph

The product graph maps out the full system before any math. It has three zones:

### Ecosphere — extractions (top zone)
Things pulled from nature into the system:
- Coal (extracted from the ground into P3)
- Water (taken from supply into P2)

### Technosphere — processes (middle zone)
The three human-made processes and the product flows between them:

| Process | What it does | Input | Output |
|---|---|---|---|
| P1: Make coffee | Combines inputs into coffee | 0.2L boiled water | 1 cup coffee |
| P2: Boil water | Heats water using electricity | 0.5 kWh electricity | 1L boiled water |
| P3: Burn coal | Generates electricity | coal (from biosphere) | 1 kWh electricity |

The chain of flows: P3 → electricity → P2 → boiled water → P1 → coffee

### Ecosphere — emissions (bottom zone)
Things released from the system back into nature:
- CO₂ from P3 (1 kg per run)
- Heat/steam from P2
- Waste from P1

---

## Step 3 — Matrix A (The Technology Matrix)

Matrix A describes the **technosphere** — all flows between human-made processes.

### How to build it

- **Columns** = processes (P1, P2, P3)
- **Rows** = products (coffee, boiled water, electricity)
- **Positive value** = this process produces this product
- **Negative value** = this process consumes this product
- **Zero** = no relationship

### The matrix

$$
A = \begin{bmatrix} +1 & 0 & 0 \\ -0.2 & +1 & 0 \\ 0 & -0.5 & +1 \end{bmatrix}
$$

|  | P1: Make coffee | P2: Boil water | P3: Burn coal |
|---|---|---|---|
| **Coffee (cups)** | +1 | 0 | 0 |
| **Boiled water (L)** | -0.2 | +1 | 0 |
| **Electricity (kWh)** | 0 | -0.5 | +1 |

### Reading the matrix

**Row 1 (Coffee):** Only P1 produces coffee. P2 and P3 have no direct relationship with coffee.

**Row 2 (Boiled water):** P2 produces 1L of boiled water per run. P1 consumes 0.2L of boiled water per run.

**Row 3 (Electricity):** P3 produces 1 kWh of electricity per run. P2 consumes 0.5 kWh per run.

### Key insight

Matrix A is the complete mathematical description of the technosphere. Every arrow in the product graph that stays inside the technosphere becomes a number in this matrix. It only contains flows between processes — nothing that crosses into the biosphere.

---

## Step 4 — The Scaling Vector (s)

### What s means

s is the **scaling vector**. It tells us how many times each process needs to run to exactly satisfy the reference flow f.

$$
s = \begin{bmatrix} s_1 \\ s_2 \\ s_3 \end{bmatrix}
$$

### How to find s

We solve the system:

$$
A \cdot s = f
$$

Which means:

$$
s = A^{-1} \cdot f
$$

### Solving by hand

Writing out the three equations:

**Row 1 (coffee):**
$$1 \cdot s_1 + 0 \cdot s_2 + 0 \cdot s_3 = 1$$

**Row 2 (boiled water):**
$$-0.2 \cdot s_1 + 1 \cdot s_2 + 0 \cdot s_3 = 0$$

**Row 3 (electricity):**
$$0 \cdot s_1 + (-0.5) \cdot s_2 + 1 \cdot s_3 = 0$$

Solving top-down:

- From row 1: $s_1 = 1$
- From row 2: $s_2 = 0.2 \times 1 = 0.2$
- From row 3: $s_3 = 0.5 \times 0.2 = 0.1$

### Result

$$
s = \begin{bmatrix} 1 \\ 0.2 \\ 0.1 \end{bmatrix}
$$

In words:
- P1 (make coffee) runs **1 time**
- P2 (boil water) runs **0.2 times** (20% of one full run)
- P3 (burn coal) runs **0.1 times** (10% of one full run)

---

## Step 5 — Matrix B (The Intervention Matrix)

Matrix B describes the **biosphere** — all flows that cross the boundary between the technosphere and the natural world, in both directions:

- **Extractions** — resources taken from nature (coal, water, land)
- **Emissions** — substances released into nature (CO₂, heat, waste)

### The matrix

$$
B = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}
$$

|  | P1: Make coffee | P2: Boil water | P3: Burn coal |
|---|---|---|---|
| **CO₂ (kg per run)** | 0 | 0 | 1 |

In a real LCA, Matrix B would have many more rows — one for each substance crossing the boundary between technosphere and biosphere.

---

## Step 6 — LCI Result (Total Emissions)

### The calculation

$$
\text{CO}_2 = B \cdot s
$$

$$
\text{CO}_2 = (0 \times 1) + (0 \times 0.2) + (1 \times 0.1) = 0.1 \text{ kg}
$$

### Result

> Making one cup of coffee emits **0.1 kg of CO₂**

All of it comes from P3 burning coal to generate the electricity that P2 uses to boil the water that P1 uses to make the coffee.

---

## Step 7 — Contribution Tree

The contribution tree traces where the CO₂ comes from back through the chain:

```
Total CO₂: 0.1 kg (100%)
│
└── P1: Make coffee  [s₁ = 1]   → 0 kg direct CO₂
        │
        │ needs 0.2L boiled water
        │
        └── P2: Boil water  [s₂ = 0.2]  → 0 kg direct CO₂
                │
                │ needs 0.1 kWh electricity
                │
                └── P3: Burn coal  [s₃ = 0.1]  → 0.1 kg CO₂  ← ALL of it
```

P3 is the sole source of CO₂. In a real LCA with many processes, the contribution tree identifies which processes are the biggest environmental hotspots.

---

## Summary of All Steps

| Step | Name | What happens | Key output |
|---|---|---|---|
| 1 | Goal and scope | Define functional unit and reference flow | f = [1, 0, 0] |
| 2 | Product graph | Map all processes, products, extractions, emissions | Visual system map |
| 3 | Matrix A | Encode all technosphere flows | 3×3 technology matrix |
| 4 | Scaling vector | Invert A and solve for s | s = [1, 0.2, 0.1] |
| 5 | Matrix B | Encode all biosphere flows | Intervention matrix |
| 6 | LCI result | Compute B · s | 0.1 kg CO₂ |
| 7 | Contribution tree | Trace CO₂ back through chain | P3 = 100% of impact |

---

## Key Terms

| Term | Definition |
|---|---|
| **Functional unit** | The qualitative definition of what the system delivers |
| **Reference flow (f)** | The mathematical expression of the functional unit as a vector |
| **Technosphere** | The world of human-made processes — what Matrix A describes |
| **Biosphere** | The natural world — what Matrix B describes |
| **Technology matrix (A)** | Matrix of all flows between processes. Columns = processes, rows = products |
| **Intervention matrix (B)** | Matrix of all flows between processes and the biosphere |
| **Scaling vector (s)** | How many times each process runs to satisfy f. Found by s = A⁻¹ · f |
| **LCI** | Life Cycle Inventory — the full mathematical analysis (steps 3–6) |
| **LCIA** | Life Cycle Impact Assessment — converting raw emissions into impact scores |
| **Contribution tree** | A tree showing which processes are responsible for what fraction of the impact |

---

## The Core Equation

$$
\boxed{\text{CO}_2 = B \cdot A^{-1} \cdot f}
$$

This single equation is the engine of the entire LCI analysis. Given the system description (A and B) and your goal (f), it produces the total environmental impact directly.

---

## Next Steps for Claude Code

The calculations to implement in Python/numpy:

```python
import numpy as np

# Technology matrix A
A = np.array([
    [ 1.0,  0.0,  0.0],   # coffee row
    [-0.2,  1.0,  0.0],   # boiled water row
    [ 0.0, -0.5,  1.0]    # electricity row
])

# Reference flow vector f
f = np.array([1.0, 0.0, 0.0])

# Intervention matrix B (CO2 row)
B = np.array([[0.0, 0.0, 1.0]])

# Step 1: solve for scaling vector s
s = np.linalg.solve(A, f)
print("Scaling vector s:", s)

# Step 2: compute total CO2
co2 = B @ s
print("Total CO2 (kg):", co2)

# Step 3: contribution of each process
contributions = B * s
print("Contributions by process:", contributions)
```

Expected output:
```
Scaling vector s: [1.  0.2 0.1]
Total CO2 (kg): [0.1]
Contributions by process: [[0.  0.  0.1]]
```
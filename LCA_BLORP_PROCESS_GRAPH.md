# LCA Example: Producing 1 Blorp

## Overview

Life Cycle Assessment (LCA) has two main computational phases:

1. **Life Cycle Inventory (LCI)** — a bookkeeping and scaling problem. Trace all flows (materials, energy, emissions, extractions) through a process tree and normalize everything to the functional unit.
2. **Life Cycle Impact Assessment (LCIA)** — a modeling problem. Multiply inventory flows by characterization factors to convert them into impact category scores.

The math is linear algebra: solve for how much each process must run, then accumulate elementary flows, then apply impact factors.

---

## Functional Unit

> **1 Blorp** of product

Everything in the inventory is scaled to this reference.

---

## Process Tree

The system has three processes:

| Process | Reference output | Technosphere inputs |
|---|---|---|
| **Reference process** | 1 Blorp / run | 3 Zings (from A), 10 Flums (from B) |
| **Process A** | 2 Zings / run | — |
| **Process B** | 4 Flums / run | — |

### Elementary flows (from database)

Emission and extraction rates are fixed properties of each process, looked up from the database (e.g. ecoinvent). They are always positive — direction is encoded by the flow type (compartment), not by sign.

| Process | Flow | Type | Rate |
|---|---|---|---|
| Reference process | Smog | Emission to air | 0.7 Smog / Blorp |
| Process A | Smog | Emission to air | 0.4 Smog / Zing |
| Process A | Aqua | Extraction from ground | 2.0 Aqua / Zing |
| Process B | Smog | Emission to air | 0.2 Smog / Flum |
| Process B | Haze | Emission to air | 0.5 Haze / Flum |

### Arrow convention

- Product/energy flows go **up** through the tree toward the functional unit
- Emissions point **out** of a process (to nature)
- Extractions point **into** a process (from nature)
- The **? Zings** and **? Flums** on the product flow arrows are unknown until we solve for the scaling vector s

![LCA process tree — before scaling](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgdmlld0JveD0iMCAwIDY4MCA2MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTMiPgogIDxkZWZzPgogICAgPG1hcmtlciBpZD0iYXJyb3ciIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iOCIgcmVmWT0iNSIgbWFya2VyV2lkdGg9IjYiIG1hcmtlckhlaWdodD0iNiIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgICA8cGF0aCBkPSJNMiAxTDggNUwyIDkiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY29udGV4dC1zdHJva2UiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KICAgIDwvbWFya2VyPgogIDwvZGVmcz4KCiAgPHRleHQgeD0iMzQwIiB5PSIyOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIxNSIgZmlsbD0iIzJDMkMyQSI+UHJvY2VzcyB0cmVlIOKAlCBiZWZvcmUgc2NhbGluZzwvdGV4dD4KCiAgPCEtLSBGdW5jdGlvbmFsIHVuaXQgLS0+CiAgPHJlY3QgeD0iMjU1IiB5PSI0OCIgd2lkdGg9IjE3MCIgaGVpZ2h0PSI0OCIgcng9IjgiIGZpbGw9IiNFMUY1RUUiIHN0cm9rZT0iIzBGNkU1NiIgc3Ryb2tlLXdpZHRoPSIwLjgiLz4KICA8dGV4dCB4PSIzNDAiIHk9IjY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNjAwIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMDg1MDQxIj4xIEJsb3JwPC90ZXh0PgogIDx0ZXh0IHg9IjM0MCIgeT0iODYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiMwRjZFNTYiPmZ1bmN0aW9uYWwgdW5pdDwvdGV4dD4KCiAgPCEtLSBSZWZlcmVuY2UgcHJvY2VzcyAtLT4KICA8cmVjdCB4PSIyNTUiIHk9IjE1MiIgd2lkdGg9IjE3MCIgaGVpZ2h0PSI1NiIgcng9IjgiIGZpbGw9IiNFRUVERkUiIHN0cm9rZT0iIzUzNEFCNyIgc3Ryb2tlLXdpZHRoPSIwLjgiLz4KICA8dGV4dCB4PSIzNDAiIHk9IjE3NCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIxMyIgZmlsbD0iIzNDMzQ4OSI+UmVmZXJlbmNlIHByb2Nlc3M8L3RleHQ+CiAgPHRleHQgeD0iMzQwIiB5PSIxOTIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiM1MzRBQjciPnJlZjogMSBCbG9ycCAvIHJ1bjwvdGV4dD4KCiAgPCEtLSBQcm9kdWN0IGZsb3cgdXAgLS0+CiAgPGxpbmUgeDE9IjM0MCIgeTE9IjE1MiIgeDI9IjM0MCIgeTI9Ijk2IiBzdHJva2U9IiM1RjVFNUEiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KCiAgPCEtLSBFbWlzc2lvbiBSSUdIVCBvZiBSZWZlcmVuY2U6IHNob3J0IGFycm93LCB0d28gbGFiZWwgbGluZXMgLS0+CiAgPGxpbmUgeDE9IjQyNSIgeTE9IjE3NCIgeDI9IjQ2OCIgeTI9IjE3NCIgc3Ryb2tlPSIjQzA0ODI4IiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3cpIi8+CiAgPHRleHQgeD0iNDc0IiB5PSIxNjYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiNDMDQ4MjgiPjAuNyBTbW9nIC8gQmxvcnA8L3RleHQ+CiAgPHRleHQgeD0iNDc0IiB5PSIxODAiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiNDMDQ4MjgiPih0byBuYXR1cmUpPC90ZXh0PgoKICA8IS0tIFByb2Nlc3MgQTogeD03OC4uMjU4IC0tPgogIDxyZWN0IHg9Ijc4IiB5PSIzMDAiIHdpZHRoPSIxODAiIGhlaWdodD0iNTIiIHJ4PSI4IiBmaWxsPSIjRkFFRURBIiBzdHJva2U9IiM4NTRGMEIiIHN0cm9rZS13aWR0aD0iMC44Ii8+CiAgPHRleHQgeD0iMTY4IiB5PSIzMjEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc2l6ZT0iMTMiIGZpbGw9IiM2MzM4MDYiPlByb2Nlc3MgQTwvdGV4dD4KICA8dGV4dCB4PSIxNjgiIHk9IjMzOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZmlsbD0iIzg1NEYwQiI+cmVmOiAyIFppbmdzIC8gcnVuPC90ZXh0PgoKICA8IS0tIFByb2R1Y3QgZmxvdyBBIOKGkiBSZWZlcmVuY2UgLS0+CiAgPHBhdGggZD0iTTIwOCAzMDAgTDIwOCAyNDQgTDMwMCAyNDQgTDMwMCAyMDgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzVGNUU1QSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgogIDx0ZXh0IHg9IjIxNiIgeT0iMjYwIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSIjNUY1RTVBIj4/IFppbmdzPC90ZXh0PgoKICA8IS0tIEVtaXNzaW9uIFJJR0hUIG9mIEE6IHNob3J0IGFycm93IC0tPgogIDxsaW5lIHgxPSIyNTgiIHkxPSIzMTYiIHgyPSIzMDAiIHkyPSIzMTYiIHN0cm9rZT0iI0MwNDgyOCIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgogIDx0ZXh0IHg9IjMwNiIgeT0iMzA4IiBmb250LXNpemU9IjExIiBmaWxsPSIjQzA0ODI4Ij4wLjQgU21vZyAvIFppbmc8L3RleHQ+CiAgPHRleHQgeD0iMzA2IiB5PSIzMjIiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiNDMDQ4MjgiPih0byBuYXR1cmUpPC90ZXh0PgoKICA8IS0tIEV4dHJhY3Rpb24gTEVGVCBpbnRvIEE6IHNob3J0IGFycm93IC0tPgogIDxsaW5lIHgxPSI0MiIgeTE9IjMzNCIgeDI9Ijc4IiB5Mj0iMzM0IiBzdHJva2U9IiMxRDlFNzUiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KICA8dGV4dCB4PSIzOCIgeT0iMzI2IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjExIiBmaWxsPSIjMUQ5RTc1Ij4yLjAgQXF1YSAvIFppbmc8L3RleHQ+CiAgPHRleHQgeD0iMzgiIHk9IjM0MCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSIxMCIgZmlsbD0iIzFEOUU3NSI+KGZyb20gbmF0dXJlKTwvdGV4dD4KCiAgPCEtLSBQcm9jZXNzIEI6IHg9NDIyLi42MDIgLS0+CiAgPHJlY3QgeD0iNDIyIiB5PSIzMDAiIHdpZHRoPSIxODAiIGhlaWdodD0iNTIiIHJ4PSI4IiBmaWxsPSIjRkFFQ0U3IiBzdHJva2U9IiM5OTNDMUQiIHN0cm9rZS13aWR0aD0iMC44Ii8+CiAgPHRleHQgeD0iNTEyIiB5PSIzMjEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc2l6ZT0iMTMiIGZpbGw9IiM3MTJCMTMiPlByb2Nlc3MgQjwvdGV4dD4KICA8dGV4dCB4PSI1MTIiIHk9IjMzOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZmlsbD0iIzk5M0MxRCI+cmVmOiA0IEZsdW1zIC8gcnVuPC90ZXh0PgoKICA8IS0tIFByb2R1Y3QgZmxvdyBCIOKGkiBSZWZlcmVuY2UgLS0+CiAgPHBhdGggZD0iTTQ4MiAzMDAgTDQ4MiAyNDQgTDM4MCAyNDQgTDM4MCAyMDgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzVGNUU1QSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgogIDx0ZXh0IHg9IjM5MiIgeT0iMjYwIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSIjNUY1RTVBIj4/IEZsdW1zPC90ZXh0PgoKICA8IS0tIEVtaXNzaW9uIFJJR0hUIG9mIEI6IFNtb2cgLS0+CiAgPGxpbmUgeDE9IjYwMiIgeTE9IjMxMiIgeDI9IjY0MiIgeTI9IjMxMiIgc3Ryb2tlPSIjQzA0ODI4IiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3cpIi8+CiAgPHRleHQgeD0iNjQ4IiB5PSIzMDQiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiNDMDQ4MjgiPjAuMiBTbW9nIC8gRmx1bTwvdGV4dD4KICA8dGV4dCB4PSI2NDgiIHk9IjMxOCIgZm9udC1zaXplPSIxMCIgZmlsbD0iI0MwNDgyOCI+KHRvIG5hdHVyZSk8L3RleHQ+CgogIDwhLS0gRW1pc3Npb24gUklHSFQgb2YgQjogSGF6ZSAtLT4KICA8bGluZSB4MT0iNjAyIiB5MT0iMzM4IiB4Mj0iNjQyIiB5Mj0iMzM4IiBzdHJva2U9IiNDMDQ4MjgiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KICA8dGV4dCB4PSI2NDgiIHk9IjMzMCIgZm9udC1zaXplPSIxMSIgZmlsbD0iI0JBNzUxNyI+MC41IEhhemUgLyBGbHVtPC90ZXh0PgogIDx0ZXh0IHg9IjY0OCIgeT0iMzQ0IiBmb250LXNpemU9IjEwIiBmaWxsPSIjQkE3NTE3Ij4odG8gbmF0dXJlKTwvdGV4dD4KCiAgPCEtLSBMZWdlbmQgLS0+CiAgPGxpbmUgeDE9IjE2MCIgeTE9IjUxMCIgeDI9IjE5MCIgeTI9IjUxMCIgc3Ryb2tlPSIjNUY1RTVBIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3cpIi8+CiAgPHRleHQgeD0iMTk4IiB5PSI1MTQiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiM1RjVFNUEiPnByb2R1Y3QgZmxvdzwvdGV4dD4KICA8bGluZSB4MT0iMTYwIiB5MT0iNTMyIiB4Mj0iMTkwIiB5Mj0iNTMyIiBzdHJva2U9IiNDMDQ4MjgiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KICA8dGV4dCB4PSIxOTgiIHk9IjUzNiIgZm9udC1zaXplPSIxMSIgZmlsbD0iIzVGNUU1QSI+ZW1pc3Npb24g4oCUIHJpZ2h0IHNpZGUgKHRvIG5hdHVyZSk8L3RleHQ+CiAgPGxpbmUgeDE9IjE5MCIgeTE9IjU1NCIgeDI9IjE2MCIgeTI9IjU1NCIgc3Ryb2tlPSIjMUQ5RTc1IiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3cpIi8+CiAgPHRleHQgeD0iMTk4IiB5PSI1NTgiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiM1RjVFNUEiPmV4dHJhY3Rpb24g4oCUIGxlZnQgc2lkZSAoZnJvbSBuYXR1cmUpPC90ZXh0Pgo8L3N2Zz4=)

---

## Step 1 — Build the technology matrix A

The technology matrix **A** encodes what each process produces and consumes in the technosphere. Columns are processes, rows are products.

- **Diagonal entries**: reference output of each process (positive)
- **Off-diagonal entries**: technosphere demands — what the Reference process needs from A and B (negative)

$$
A = \begin{pmatrix}
1 & 0 & 0 \\
-3 & 2 & 0 \\
-10 & 0 & 4
\end{pmatrix}
\quad
\begin{array}{l}
\leftarrow \text{Blorp} \\
\leftarrow \text{Zings} \\
\leftarrow \text{Flums}
\end{array}
$$

Columns left to right: Reference process, Process A, Process B.

---

## Step 2 — Solve for the scaling vector s

The demand vector **f** expresses the functional unit — 1 Blorp, nothing else:

$$
f = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
$$

Solve $A \cdot s = f \Rightarrow s = A^{-1} \cdot f$. Since A is lower triangular, back-substitute row by row:

$$
\text{Row 1 (Blorp):} \quad 1 \times s_\text{Ref} = 1 \quad\Rightarrow\quad s_\text{Ref} = 1.0
$$

$$
\text{Row 2 (Zings):} \quad -3 \times 1.0 + 2 \times s_A = 0 \quad\Rightarrow\quad s_A = \frac{3}{2} = 1.5
$$

$$
\text{Row 3 (Flums):} \quad -10 \times 1.0 + 4 \times s_B = 0 \quad\Rightarrow\quad s_B = \frac{10}{4} = 2.5
$$

$$
s = \begin{pmatrix} 1.0 \\ 1.5 \\ 2.5 \end{pmatrix}
$$

The **? Zings** and **? Flums** from the process tree are now resolved: Process A runs 1.5 times (delivering 1.5 × 2 = 3 Zings), Process B runs 2.5 times (delivering 2.5 × 4 = 10 Flums).

---

## Step 3 — Build the intervention matrix B

The intervention matrix **B** contains the database rates for each elementary flow per unit of each process's reference product. Entries are always positive — direction (emission vs extraction) is a property of the flow type, not a sign.

$$
B = \begin{pmatrix}
0.7 & 0.4 & 0.2 \\
0   & 0   & 0.5 \\
0   & 2.0 & 0
\end{pmatrix}
\quad
\begin{array}{l}
\leftarrow \text{Smog (emission to air)} \\
\leftarrow \text{Haze (emission to air)} \\
\leftarrow \text{Aqua (extraction from ground)}
\end{array}
$$

Columns left to right: Reference process, Process A, Process B.

---

## Step 4 — Compute the inventory vector g = B · s

Multiply each row of B by the scaling vector s:

$$
g[\text{Smog}] = (0.7 \times 1.0) + (0.4 \times 1.5) + (0.2 \times 2.5) = 0.70 + 0.60 + 0.50 = \mathbf{1.80}
$$

$$
g[\text{Haze}] = (0 \times 1.0) + (0 \times 1.5) + (0.5 \times 2.5) = 0 + 0 + 1.25 = \mathbf{1.25}
$$

$$
g[\text{Aqua}] = (0 \times 1.0) + (2.0 \times 1.5) + (0 \times 2.5) = 0 + 3.00 + 0 = \mathbf{3.00}
$$

$$
g = \begin{pmatrix} 1.80 \\ 1.25 \\ 3.00 \end{pmatrix}
$$

This is the **life cycle inventory** — total elementary flows attributable to producing 1 Blorp, aggregated across all processes.

---

## Step 5 — Apply the characterization matrix C, get impact vector h = C · g

The characterization matrix **C** converts elementary flows into impact scores using scientific factors. Both emissions and extractions contribute positively — no sign distinction here either.

| Flow | Murk potential | Depletion potential |
|---|---|---|
| Smog | 1.0 Murk / Smog | — |
| Haze | 3.0 Murk / Haze | — |
| Aqua | — | 0.8 Depletion / Aqua |

$$
C = \begin{pmatrix}
1.0 & 3.0 & 0   \\
0   & 0   & 0.8
\end{pmatrix}
\quad
\begin{array}{l}
\leftarrow \text{Murk potential} \\
\leftarrow \text{Depletion potential}
\end{array}
$$

$$
h[\text{Murk}] = (1.0 \times 1.80) + (3.0 \times 1.25) + (0 \times 3.00) = 1.80 + 3.75 + 0 = \mathbf{5.55}
$$

$$
h[\text{Depletion}] = (0 \times 1.80) + (0 \times 1.25) + (0.8 \times 3.00) = 0 + 0 + 2.40 = \mathbf{2.40}
$$

$$
h = \begin{pmatrix} 5.55 \\ 2.40 \end{pmatrix}
$$

---

## Full Calculation Chain

$$
h = C \cdot B \cdot A^{-1} \cdot f
$$

| Symbol | Name | Dimensions |
|---|---|---|
| $f$ | Demand vector | $p \times 1$ (products) |
| $A$ | Technology matrix | $p \times n$ (products × processes) |
| $s = A^{-1}f$ | Scaling vector | $n \times 1$ (processes) |
| $B$ | Intervention matrix | $e \times n$ (elementary flows × processes) |
| $g = Bs$ | Inventory vector | $e \times 1$ (elementary flows) |
| $C$ | Characterization matrix | $k \times e$ (impact categories × elementary flows) |
| $h = Cg$ | Impact vector | $k \times 1$ (impact categories) |

In real LCA software (SimaPro, OpenLCA), **A** is drawn from a background database like ecoinvent and can have thousands of rows and columns — but the matrix structure and the $h = C \cdot B \cdot A^{-1} \cdot f$ equation are identical.

---

## Summary of Results

| | Value |
|---|---|
| Functional unit | 1 Blorp |
| $s_\text{Ref}$ | 1.0 run |
| $s_A$ | 1.5 runs |
| $s_B$ | 2.5 runs |
| Inventory: Smog | 1.80 |
| Inventory: Haze | 1.25 |
| Inventory: Aqua | 3.00 |
| **Impact: Murk** | **5.55** |
| **Impact: Depletion** | **2.40** |

# PLAN: Open-Source LCA MCP Server

## What this plan covers

A fully open-source, freely deployable MCP (Model Context Protocol) server that
wraps the openLCA gdt-server and exposes LCA analysis as AI-callable tools.
No openLCA desktop app required. No paid licenses required for the free tier.
Optional ecoinvent support for users who bring their own licensed database.

Inspired by the pattern in [calvinw/BusMgmtDoltDatabase](https://github.com/calvinw/BusMgmtDoltDatabase):
FastMCP + FastAPI + SSE + Docker, deployed as a remote MCP anyone can point to.

---

## Why this is valuable

Right now the analysis pipeline is:
```
Student recipe card → python3 lca_analysis.py → results file
```

With the MCP, it becomes:
```
LLM calls run_lca(recipe_card="...") → gets results + graphs in one turn
```

The LLM can then:
- Explain the results to the student in plain English
- Modify the recipe card and re-run in the same conversation
- Compare two products side by side
- Try different LCIA methods (TRACI vs ReCiPe) without touching any files

---

## Stack (mirrors BusMgmtDoltDatabase exactly)

| Layer | Technology |
|---|---|
| MCP framework | `fastmcp` (Python) |
| HTTP/SSE transport | `FastAPI` + `uvicorn` |
| LCA calculation | `gdt-server` (GreenDelta, open-source Java) |
| Python LCA client | `olca-ipc`, `olca-schema` |
| Diagram generation | `lca_svg.py` (SVG via matplotlib) |
| Container | Docker |
| Deployment | Any cloud host (Render, Railway, Fly.io free tier) |

---

## MCP Tools

### `run_lca`
Takes a recipe card as YAML text, builds the full product system, runs the
calculation, returns LCI + LCIA results and both SVG diagrams.

```python
@mcp.tool()
def run_lca(
    recipe_card: str,
    server_url: str = "http://localhost:8080"
) -> dict:
    """
    Run a full LCA from a recipe card YAML string.
    Returns LCI flows, LCIA impact scores, and SVG supply chain diagrams.
    The recipe card follows the same YAML format as files in lca_analysis/.
    """
```

**Returns:**
```json
{
  "name": "Cotton Shirt LCA",
  "method": "TRACI 2.2",
  "functional_unit": "1 shirt",
  "lci": {
    "Carbon dioxide": {"amount": 2.32, "unit": "kg"},
    "Nitrogen oxides": {"amount": 0.0025, "unit": "kg"}
  },
  "lcia": {
    "Global warming": {"score": 2.32, "unit": "kg CO2 eq"},
    "Acidification": {"score": 0.003475, "unit": "kg SO2 eq"},
    "Smog (Photochemical Oxidation Formation)": {"score": 0.063, "unit": "kg O3 eq"}
  },
  "scaling_vector": {
    "P1 — Grow cotton": 0.3025,
    "P2 — Spin yarn": 0.2750,
    "P4 — Cut and sew shirt": 1.0
  },
  "svg_scaled": "<svg>...</svg>",
  "svg_structure": "<svg>...</svg>"
}
```

---

### `list_impact_methods`
Returns all LCIA methods available in the connected database.

```python
@mcp.tool()
def list_impact_methods(
    server_url: str = "http://localhost:8080"
) -> list[dict]:
    """List all LCIA methods available (e.g. TRACI 2.2, ReCiPe 2016, EF 3.1)."""
```

---

### `check_server`
Health check — confirms the gdt-server is running and returns its version.

```python
@mcp.tool()
def check_server(
    server_url: str = "http://localhost:8080"
) -> dict:
    """Check if the openLCA gdt-server is running and ready."""
```

---

### `get_lca_svg`
Returns a supply chain diagram SVG for a recipe card without running the full
calculation. Faster when only the diagram is needed.

```python
@mcp.tool()
def get_lca_svg(
    recipe_card: str,
    graph_type: str = "scaled",
    server_url: str = "http://localhost:8080"
) -> str:
    """
    Generate a supply chain SVG diagram from a recipe card.
    graph_type: "scaled" (with amounts) or "structure" (flow names only)
    Returns SVG as a string.
    """
```

---

## File structure

```
mcp-lca/
├── lca_server.py          ← FastMCP server, all @mcp.tool() definitions
├── sse_server.py          ← FastAPI wrapper for SSE/HTTP transport
├── lca_engine.py          ← thin wrapper around lca_analysis.py logic
├── lca_svg_engine.py      ← thin wrapper around lca_svg.py logic
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

`lca_server.py` is the stdio entry point. `sse_server.py` wraps it for remote
deployment — identical pattern to BusMgmtDoltDatabase.

---

## `lca_server.py` skeleton

```python
import requests
from fastmcp import FastMCP
from lca_engine import run_analysis
from lca_svg_engine import generate_svg

mcp = FastMCP("LCA Analysis Server")

@mcp.tool()
def run_lca(recipe_card: str, server_url: str = "http://localhost:8080") -> dict:
    """Run a full LCA from a recipe card YAML string."""
    return run_analysis(recipe_card, server_url)

@mcp.tool()
def get_lca_svg(recipe_card: str, graph_type: str = "scaled",
                server_url: str = "http://localhost:8080") -> str:
    """Generate a supply chain SVG diagram from a recipe card."""
    return generate_svg(recipe_card, graph_type, server_url)

@mcp.tool()
def list_impact_methods(server_url: str = "http://localhost:8080") -> list:
    """List all LCIA methods available in the connected database."""
    r = requests.get(f"{server_url}/data/impact-methods")
    return [{"id": m["@id"], "name": m["name"]} for m in r.json()]

@mcp.tool()
def check_server(server_url: str = "http://localhost:8080") -> dict:
    """Check if the openLCA gdt-server is running."""
    try:
        r = requests.get(f"{server_url}/api/version", timeout=5)
        return {"running": True, "version": r.json().get("version")}
    except Exception:
        return {"running": False}

if __name__ == "__main__":
    mcp.run()  # stdio mode
```

---

## `sse_server.py` skeleton (identical pattern to BusMgmtDoltDatabase)

```python
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from lca_server import mcp

http_app = mcp.http_app(transport="sse", path="/sse")

async def oauth_metadata(request: Request):
    return JSONResponse({"issuer": str(request.base_url).rstrip("/")})

app = FastAPI(lifespan=http_app.lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["GET", "POST", "OPTIONS"],
                   allow_headers=["Content-Type", "Authorization", "x-api-key"])
app.add_api_route("/.well-known/oauth-authorization-server", oauth_metadata)
app.mount("/", http_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 9000)))
```

---

## Dockerfile

```dockerfile
FROM python:3.11-slim

# Install Java for gdt-server
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless curl tar \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Download and install gdt-server
RUN curl -L https://github.com/GreenDelta/gdt-server/releases/latest/download/gdt-server.jar \
    -o gdt-server.jar

# Download pre-built lca_methods database
RUN mkdir -p /app/data/databases && \
    curl -L https://github.com/calvinw/agentic-lca/releases/download/lca-data-v1/lca_methods-LCIA-methods-2.8.0-2026-06-18.tar.gz \
    | tar -xz -C /app/data/databases/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Start script: launch gdt-server, wait for ready, then start MCP
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 9000
CMD ["./start.sh"]
```

`start.sh` starts gdt-server in background, waits for it to be ready
(same pattern as `setup_olca.sh`), then starts `sse_server.py`.

---

## Deployment tiers

### Tier 1 — Free, open-source database (lca_methods)

The Docker image downloads `lca_methods-LCIA-methods-2.8.0-2026-06-18.tar.gz`
at build time. This is the free pre-built database with all 45 LCIA methods
(TRACI 2.2, ReCiPe 2016, EF 3.1, ImpactWorld, CML, etc.).

Anyone can run it:
```bash
docker run -p 9000:9000 calvinw/lca-mcp-server:latest
```

Or point any MCP client at a publicly hosted instance:
```
https://lca.mcp.yourdomain.com/sse
```

### Tier 2 — ecoinvent (user-supplied database)

Users who have an ecoinvent license pass their own `server_url` to every tool:

```python
run_lca(recipe_card="...", server_url="http://my-ecoinvent-server:8080")
```

They run their own gdt-server locally (via `start_olca_ecoinvent.sh`) and point
the MCP tools at it. The MCP server itself stays free and license-clean.

Alternatively: the Docker image can download the ecoinvent database from a private
GitHub repo at startup if a `ECOINVENT_GITHUB_TOKEN` environment variable is set:

```bash
docker run \
  -e ECOINVENT_GITHUB_TOKEN=ghp_xxx \
  -e DATABASE=ecoinvent \
  -p 9000:9000 \
  calvinw/lca-mcp-server:latest
```

### Tier 3 — BAFU (future, free)

Same as Tier 1 but with BAFU database downloaded at build time. Enables
real background processes without a license.

---

## Integration with skills

Once deployed, register the MCP in `.skillshare/config.yaml`:

```yaml
mcps:
  - name: lca
    url: https://lca.mcp.yourdomain.com/sse
```

Or for local Codespace use (stdio):

```yaml
mcps:
  - name: lca
    command: python3 mcp-lca/lca_server.py
```

Skills then call MCP tools directly. Example — `/system-boundary`:

```
AI receives: /system-boundary cotton_shirt

AI calls: run_lca(recipe_card="<recipe card yaml text>")

MCP returns: { lci: {...}, lcia: {...}, svg_scaled: "<svg>..." }

AI explains results to student in plain English.
```

The student never sees the recipe card YAML or the tool call — they just see
the explanation.

---

## Comparison with tiangong-lca-mcp

[tiangong-lca-mcp](https://github.com/linancn/tiangong-lca-mcp) is excellent
but solves a different problem. It connects to a pre-populated database (ecoinvent,
GLAD) and runs calculations on product systems that already exist. It is
TypeScript-based and requires existing product system UUIDs.

This MCP builds product systems from scratch from a recipe card YAML, which
is what our teaching workflow requires. The LLM constructs or modifies the
supply chain in conversation and runs it immediately — no pre-built product
systems needed.

The two could be complementary: our MCP for recipe-card-driven teaching,
tiangong for professionals querying existing databases.

---

## Build order

1. Create `mcp-lca/` folder with `lca_server.py`, `sse_server.py`, `requirements.txt`
2. Extract LCA engine logic from `lca_analysis.py` into `lca_engine.py`
3. Extract SVG logic from `lca_svg.py` into `lca_svg_engine.py`
4. Test stdio mode locally in Codespace
5. Register in `.skillshare/config.yaml` as stdio MCP
6. Write `Dockerfile` and `start.sh`
7. Deploy to Render/Railway/Fly.io free tier
8. Switch `.skillshare/config.yaml` to SSE URL
9. Update skills to use MCP tools instead of file-based scripts

---

## Summary

| | This project now | With MCP |
|---|---|---|
| How analysis runs | `python3 lca_analysis.py file.md` | `run_lca(recipe_card="...")` |
| LLM involvement | Reads output file after the fact | Gets results in the same turn |
| Recipe card lives | In a file | In the conversation |
| LCIA method switching | Edit file, re-run | Pass different `method_name` |
| Deployable as service | No | Yes — Docker + SSE |
| Requires desktop app | No (already solved) | No |
| License cost | Free | Free (Tier 1) |
| ecoinvent support | Via separate script | Via `server_url` parameter |

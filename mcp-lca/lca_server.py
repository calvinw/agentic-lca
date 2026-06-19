"""
lca_server.py — Life Cycle Assessment MCP server.

Tools:
    run_lca             — full LCA from a recipe card YAML string
    get_lca_svg         — supply chain diagram only (no server call needed)
    list_impact_methods — list all LCIA methods in the connected database
    check_server        — health check for the gdt-server

Run in stdio mode:
    python3 lca_server.py

Run via SSE (remote):
    python3 sse_server.py
"""

import requests
from fastmcp import FastMCP
from lca_engine import run_analysis
from lca_svg_engine import generate_svg

mcp = FastMCP("Life Cycle Assessment MCP")


@mcp.tool()
def run_lca(recipe_card: str,
            server_url: str = "http://localhost:8080") -> dict:
    """
    Run a full LCA from a recipe card YAML string.

    Returns LCI totals, LCIA impact scores, scaling vector, and two SVG
    supply chain diagrams (scaled and structure). The recipe card is the
    YAML frontmatter from a recipe_card.md file.
    """
    result = run_analysis(recipe_card, server_url)
    result["svg_scaled"]    = generate_svg(recipe_card, "scaled")
    result["svg_structure"] = generate_svg(recipe_card, "structure")
    return result


@mcp.tool()
def get_lca_svg(recipe_card: str,
                graph_type: str = "scaled") -> str:
    """
    Generate a supply chain SVG diagram from a recipe card YAML string.

    graph_type: "scaled" — shows flow amounts and scaling factors
                "structure" — shows flow names only
    Returns SVG as a string. Does not require the gdt-server to be running.
    """
    return generate_svg(recipe_card, graph_type)


@mcp.tool()
def list_impact_methods(server_url: str = "http://localhost:8080") -> list:
    """
    List all LCIA methods available in the connected database.
    Examples: TRACI 2.2, ReCiPe 2016, EF 3.1, CML, ImpactWorld+.
    """
    r = requests.get(f"{server_url}/data/impact-methods", timeout=10)
    r.raise_for_status()
    return [{"id": m["@id"], "name": m["name"]} for m in r.json()]


@mcp.tool()
def check_server(server_url: str = "http://localhost:8080") -> dict:
    """Check if the openLCA gdt-server is running and ready."""
    try:
        r = requests.get(f"{server_url}/api/version", timeout=5)
        return {"running": True, "version": r.json().get("version")}
    except Exception:
        return {"running": False}


if __name__ == "__main__":
    mcp.run()

"""
lca_svg_engine.py — SVG generation for the Life Cycle Assessment MCP.

Wraps lca_svg.generate(). Works in two layouts:
  - Codespace: lca_svg.py lives in ../lca_scripts/
  - Docker:    lca_svg.py is copied alongside this file
"""

import os
import sys
import tempfile
import pathlib

_HERE    = pathlib.Path(__file__).parent
_SCRIPTS = _HERE.parent / "lca_scripts"
if _SCRIPTS.exists():
    sys.path.insert(0, str(_SCRIPTS))

from lca_svg import generate as _generate


def generate_svg(recipe_card_yaml: str, graph_type: str = "scaled") -> str:
    """
    Generate a supply chain SVG from a recipe card YAML string.
    graph_type: "scaled" (amounts + scaling factors) or "structure" (flow names only)
    Returns the SVG as a string. Does not talk to the gdt-server.
    """
    show_quantities = graph_type != "structure"

    yaml_text = recipe_card_yaml.strip()
    if not yaml_text.startswith("---"):
        yaml_text = f"---\n{yaml_text}\n---\n"

    with tempfile.TemporaryDirectory() as tmp:
        recipe_path = os.path.join(tmp, "recipe_card.md")
        out_path    = os.path.join(tmp, "graph.svg")
        pathlib.Path(recipe_path).write_text(yaml_text)
        _generate(recipe_path, out_path, show_quantities=show_quantities)
        return pathlib.Path(out_path).read_text()

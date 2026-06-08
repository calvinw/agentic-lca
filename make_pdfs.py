#!/usr/bin/env python3
"""
make_pdfs.py — Convert all markdown files in skills_examples/ to PDF.

For each .md file:
  1. Find SVG image references and convert them to PNG using cairosvg
  2. Write a temporary markdown with absolute PNG paths
  3. Run pandoc with xelatex to produce the PDF
  4. Save to skills_examples/pdf/

Usage:
  python3 make_pdfs.py
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from cairosvg import svg2png
except ImportError:
    print("cairosvg not found — install with: pip install cairosvg")
    sys.exit(1)

REPO_ROOT  = Path(__file__).parent
SKILLS_DIR = REPO_ROOT / "skills_examples"
PDF_DIR    = SKILLS_DIR / "pdf"
PDF_DIR.mkdir(exist_ok=True)

SVG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+\.svg)\)')


def convert_file(md_path: Path, tmpdir: Path) -> bool:
    content = md_path.read_text(encoding="utf-8")
    svg_cache: dict[str, Path] = {}

    def replace_svg(match):
        alt      = match.group(1)
        svg_rel  = match.group(2)
        svg_abs  = (SKILLS_DIR / svg_rel).resolve()

        if not svg_abs.exists():
            print(f"    warning: SVG not found — {svg_abs}")
            return match.group(0)

        key = str(svg_abs)
        if key not in svg_cache:
            png_path = tmpdir / (svg_abs.stem + ".png")
            with open(svg_abs, "rb") as f:
                svg2png(file_obj=f, write_to=str(png_path), scale=2.0)
            svg_cache[key] = png_path

        return f"![{alt}]({svg_cache[key]})"

    modified = SVG_RE.sub(replace_svg, content)

    tmp_md = tmpdir / md_path.name
    tmp_md.write_text(modified, encoding="utf-8")

    pdf_out = PDF_DIR / (md_path.stem + ".pdf")

    result = subprocess.run(
        [
            "pandoc", str(tmp_md),
            "-o", str(pdf_out),
            "--pdf-engine=xelatex",
            "-V", "mainfont=DejaVu Serif",
            "-V", "monofont=DejaVu Sans Mono",
            "-V", "geometry:margin=1.2in",
            "-V", "fontsize=11pt",
            "-V", "colorlinks=true",
            "-V", "urlcolor=blue",
            "-V", "linkcolor=black",
            "--highlight-style=tango",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        size_kb = pdf_out.stat().st_size // 1024
        print(f"  ✓  {pdf_out.name}  ({size_kb} KB)")
        return True
    else:
        print(f"  ✗  {md_path.name}")
        print(result.stderr[-600:])
        return False


def main():
    md_files = sorted(SKILLS_DIR.glob("*.md"))
    if not md_files:
        print("No markdown files found in skills_examples/")
        return

    print(f"Converting {len(md_files)} file(s) → skills_examples/pdf/\n")
    ok = fail = 0

    with tempfile.TemporaryDirectory() as tmpdir:
        for md_path in md_files:
            print(f"  {md_path.name}")
            if convert_file(md_path, Path(tmpdir)):
                ok += 1
            else:
                fail += 1

    print(f"\nDone — {ok} succeeded, {fail} failed.")


if __name__ == "__main__":
    main()

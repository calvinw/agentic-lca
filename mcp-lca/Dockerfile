# Build from repo root:
#   docker build -f mcp-lca/Dockerfile -t lca-mcp-server .

FROM python:3.11-slim

# Java for gdt-server, graphviz for SVG generation
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless curl tar graphviz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Download gdt-server JAR
RUN curl -fsSL \
    https://github.com/GreenDelta/gdt-server/releases/latest/download/gdt-server.jar \
    -o gdt-server.jar

# Download pre-built lca_methods database (45 LCIA methods, ~87 MB)
RUN mkdir -p /app/data/databases && \
    curl -fsSL \
    https://github.com/calvinw/agentic-lca/releases/download/lca-data-v1/lca_methods-LCIA-methods-2.8.0-2026-06-18.tar.gz \
    | tar -xz -C /app/data/databases/

COPY mcp-lca/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# MCP server files
COPY mcp-lca/lca_server.py .
COPY mcp-lca/sse_server.py .
COPY mcp-lca/lca_engine.py .
COPY mcp-lca/lca_svg_engine.py .
COPY mcp-lca/start.sh .

# SVG generation script (imported by lca_svg_engine.py)
COPY lca_scripts/lca_svg.py .

RUN chmod +x start.sh

EXPOSE 9000
CMD ["./start.sh"]

#!/usr/bin/env bash
# setup_olca.sh
# Builds (if needed) and starts the openLCA gdt-server Docker container.
# Run this once at the start of a Codespaces session.
#
# Usage:  bash setup_olca.sh
# The server will be available at http://localhost:8080

set -e

IMAGE="gdt-server:latest"
CONTAINER="olca-server"
DATA_DIR="$HOME/olca-data"
RELEASE_BASE="https://github.com/calvinw/agentic-lca/releases/download/lca-data-v1"
FEDEFL_ZIP="$DATA_DIR/Federal_LCA_Commons-elementary_flow_list.zip"
TRACI_ZIP="$DATA_DIR/Federal_LCA_Commons-TRACI_2_2.zip"
DB_DIR="$DATA_DIR/databases/lca_commons"

mkdir -p "$DATA_DIR/databases"

echo "[olca] Installing required Python packages..."
pip install olca-ipc olca-schema pyyaml numpy matplotlib --break-system-packages -q
echo "[olca] Python packages ready."

# Download LCA reference data zips if not already present
if [ ! -f "$FEDEFL_ZIP" ]; then
    echo "[olca] Downloading FEDEFL elementary flow list (214 MB)..."
    curl -L --progress-bar "$RELEASE_BASE/Federal_LCA_Commons-elementary_flow_list.zip" \
        -o "$FEDEFL_ZIP"
    echo "[olca] elementary_flow_list.zip saved."
else
    echo "[olca] FEDEFL zip already present — skipping download."
fi

if [ ! -f "$TRACI_ZIP" ]; then
    echo "[olca] Downloading TRACI 2.2 impact method (126 MB)..."
    curl -L --progress-bar "$RELEASE_BASE/Federal_LCA_Commons-TRACI_2_2.zip" \
        -o "$TRACI_ZIP"
    echo "[olca] TRACI_2_2.zip saved."
else
    echo "[olca] TRACI 2.2 zip already present — skipping download."
fi

# Build the image if it doesn't exist yet
if ! docker image inspect "$IMAGE" > /dev/null 2>&1; then
    echo "[olca] Building gdt-server image (this only happens once)..."
    BUILD_DIR=$(mktemp -d)
    curl -fsSL https://raw.githubusercontent.com/GreenDelta/gdt-server/main/Dockerfile \
        -o "$BUILD_DIR/Dockerfile.upstream"
    sed 's|eclipse-temurin:21-jre|eclipse-temurin:17-jre|' \
        "$BUILD_DIR/Dockerfile.upstream" > "$BUILD_DIR/Dockerfile"
    docker build -t "$IMAGE" "$BUILD_DIR"
    rm -rf "$BUILD_DIR"
fi

# Stop and remove any existing container with the same name
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "[olca] Removing existing container: $CONTAINER"
    docker rm -f "$CONTAINER"
fi

echo "[olca] Starting gdt-server on port 8080..."
docker run \
    --name "$CONTAINER" \
    --network host \
    -v "$DATA_DIR:/app/data" \
    -d \
    "$IMAGE" \
    -db lca_commons

echo "[olca] Waiting for server to start..."
for i in $(seq 1 30); do
    if curl -s http://localhost:8080/api/version > /dev/null 2>&1; then
        echo "[olca] Server ready at http://localhost:8080"
        curl -s http://localhost:8080/api/version
        echo ""

        # Import LCA data if TRACI 2.2 is not yet in the database.
        # We ask the server directly — folder contents are not a reliable
        # indicator because analysis runs also write files to the DB folder.
        TRACI_LOADED=$(curl -s http://localhost:8080/data/impact-methods 2>/dev/null | \
            python3 -c "
import sys, json
try:
    methods = json.load(sys.stdin)
    print('yes' if any('TRACI' in str(m.get('name','')) for m in methods) else 'no')
except Exception:
    print('no')
" 2>/dev/null || echo "no")

        if [ "$TRACI_LOADED" = "yes" ]; then
            echo "[olca] TRACI 2.2 already loaded — skipping import."
        else
            echo "[olca] TRACI 2.2 not found — importing FEDEFL flows and TRACI 2.2..."
            python3 "$(dirname "$0")/import_lca_data.py"
            echo "[olca] Import complete."
        fi

        exit 0
    fi
    sleep 2
    echo "  ...waiting ($i/30)"
done

echo "ERROR: Server did not start in time. Check Docker logs:"
echo "  docker logs $CONTAINER"
exit 1

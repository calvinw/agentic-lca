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

mkdir -p "$DATA_DIR/databases"

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
    -p 8080:8080 \
    -v "$DATA_DIR:/app/data" \
    -d \
    "$IMAGE" \
    -db paper_cup_lca

echo "[olca] Waiting for server to start..."
for i in $(seq 1 30); do
    if curl -s http://localhost:8080/api/version > /dev/null 2>&1; then
        echo "[olca] Server ready at http://localhost:8080"
        curl -s http://localhost:8080/api/version
        echo ""
        exit 0
    fi
    sleep 2
    echo "  ...waiting ($i/30)"
done

echo "ERROR: Server did not start in time. Check Docker logs:"
echo "  docker logs $CONTAINER"
exit 1

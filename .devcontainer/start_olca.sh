#!/usr/bin/env bash
# .devcontainer/start_olca.sh
# Launched by postStartCommand in devcontainer.json.
# Starts the openLCA gdt-server if it isn't already running.

set -e

IMAGE="gdt-server:latest"
CONTAINER="olca-server"
DATA_DIR="$HOME/olca-data"

mkdir -p "$DATA_DIR/databases"

# Skip if already running
if docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "[olca] gdt-server already running."
    exit 0
fi

# Remove stopped container with same name if present
docker rm -f "$CONTAINER" 2>/dev/null || true

# Build the gdt-server image if not present
if ! docker image inspect "$IMAGE" > /dev/null 2>&1; then
    echo "[olca] Building gdt-server image (pinned to Java 17 for EclipseLink compatibility)..."
    BUILD_DIR=$(mktemp -d)

    # Fetch layers from upstream Dockerfile
    curl -fsSL https://raw.githubusercontent.com/GreenDelta/gdt-server/main/Dockerfile \
        -o "$BUILD_DIR/Dockerfile.upstream"

    # Replace Java 21 JRE with Java 17 (EclipseLink doesn't support class file major version 65)
    sed 's|eclipse-temurin:21-jre|eclipse-temurin:17-jre|' \
        "$BUILD_DIR/Dockerfile.upstream" > "$BUILD_DIR/Dockerfile"

    docker build -t "$IMAGE" "$BUILD_DIR"
    rm -rf "$BUILD_DIR"
fi

echo "[olca] Starting gdt-server on port 8080..."
docker run \
    --name "$CONTAINER" \
    -p 8080:8080 \
    -v "$DATA_DIR:/app/data" \
    -d \
    "$IMAGE" \
    -db paper_cup_lca

# Wait up to 30 seconds
for i in $(seq 1 15); do
    if curl -s http://localhost:8080/api/version > /dev/null 2>&1; then
        echo "[olca] Server ready at http://localhost:8080"
        exit 0
    fi
    sleep 2
done

echo "[olca] WARNING: gdt-server may not be ready yet. Check: docker logs $CONTAINER"

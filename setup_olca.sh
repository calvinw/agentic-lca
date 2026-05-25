#!/usr/bin/env bash
# setup_olca.sh
# Pulls and starts the openLCA gdt-server Docker container.
# Run this once at the start of a Codespaces session.
#
# Usage:  bash setup_olca.sh
# The server will be available at http://localhost:8080

set -e

IMAGE="greendelta/gdt-server:latest"
CONTAINER="olca-server"
DATA_DIR="$HOME/olca-data"

# Create a data directory for the openLCA workspace
mkdir -p "$DATA_DIR/databases"

# Stop and remove any existing container with the same name
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "Removing existing container: $CONTAINER"
    docker rm -f "$CONTAINER"
fi

echo "Pulling image: $IMAGE"
docker pull "$IMAGE"

echo "Starting gdt-server on port 8080..."
docker run \
    --name "$CONTAINER" \
    -p 8080:8080 \
    -v "$DATA_DIR:/app/data" \
    -d \
    "$IMAGE" \
    -db paper_cup_lca

# Wait for server to be ready
echo "Waiting for server to start..."
for i in $(seq 1 30); do
    if curl -s http://localhost:8080/api/version > /dev/null 2>&1; then
        echo "Server ready at http://localhost:8080"
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

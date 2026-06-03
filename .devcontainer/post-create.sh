#!/bin/bash
set -euo pipefail

# This script runs after the dev container is created.
# It sets up SSH keys, installs MCP servers, installs the Python packages the
# project needs (numpy, pandas, matplotlib, seaborn, etc.), installs Pandoc for
# converting LCA reports, and syncs AI skills.

echo "=== 1/7: Setting up environment (SSH keys, PATH) ==="
setup-env.sh

echo "=== 2/7: Installing MCP servers for AI tools ==="
install-mcps.sh

echo "=== 3/7: Installing Python packages ==="
pip install numpy pandas matplotlib seaborn requests PyYAML olca-ipc olca-schema python-pptx openpyxl --break-system-packages

echo "=== 4/7: Installing Pandoc (for converting reports) ==="
apt-get update -qq && apt-get install -y -qq pandoc && rm -rf /var/lib/apt/lists/*

echo "=== 5/7: Setting up skillshare CLI ==="
setup-skills.sh

echo "=== 6/7: Installing skill-creator skill ==="
skillshare install github.com/anthropics/skills/skill-creator --force

echo "=== 7/7: Syncing skills to all AI tools ==="
sync-skills.sh || true

echo ""
echo "Done — all post-create steps completed successfully."

#!/usr/bin/env bash
# setup_database.sh
# One-time setup: imports FEDEFL elementary flows and TRACI 2.2 into the
# openLCA database. Run once per Codespace after start_olca.sh has started.
#
# Downloads required (free, no login):
#   https://www.lcacommons.gov/lca-collaboration/
#   - Federal LCA Commons / Elementary Flow List  → Federal_LCA_Commons-elementary_flow_list.zip
#   - Federal LCA Commons / TRACI 2.2             → Federal_LCA_Commons-TRACI_2_2.zip
# Place both files in $HOME/olca-data/ then run this script.

FEDEFL="$HOME/olca-data/Federal_LCA_Commons-elementary_flow_list.zip"
TRACI="$HOME/olca-data/Federal_LCA_Commons-TRACI_2_2.zip"

check_file() {
    if [ ! -f "$1" ]; then
        echo "ERROR: $1 not found."
        echo "Download it from https://www.lcacommons.gov/lca-collaboration/"
        exit 1
    fi
}

import_file() {
    local file="$1"
    local label="$2"
    echo ""
    echo "[setup] Importing $label..."
    HTTP_STATUS=$(curl -s -o /tmp/import_response.json -w "%{http_code}" \
        -X POST http://localhost:8080/api/import \
        -H "Content-Type: application/zip" \
        --data-binary @"$file")
    if [ "$HTTP_STATUS" = "200" ] || [ "$HTTP_STATUS" = "201" ]; then
        echo "[setup] ✓ $label imported successfully."
    else
        echo "[setup] ✗ Import returned HTTP $HTTP_STATUS for $label"
        cat /tmp/import_response.json 2>/dev/null
        echo ""
        echo "If the API import fails, import manually in the openLCA desktop:"
        echo "  File → Import → Linked Data (JSON-LD) → select $file"
        exit 1
    fi
}

check_file "$FEDEFL"
check_file "$TRACI"

echo "[setup] Checking server is running..."
if ! curl -s http://localhost:8080/api/version > /dev/null 2>&1; then
    echo "ERROR: openLCA server is not running. Start it first: bash start_olca.sh"
    exit 1
fi
echo "[setup] Server is up."

# Import FEDEFL first — TRACI's characterization factors reference these flow IDs
import_file "$FEDEFL" "Federal Elementary Flow List (FEDEFL)"

# Import TRACI 2.2 second — links to the FEDEFL flow IDs just imported
import_file "$TRACI" "TRACI 2.2"

echo ""
echo "[setup] Done. Both datasets are now in the database."
echo ""
echo "To verify TRACI 2.2 is available, run:"
echo "  curl -s http://localhost:8080/api/descriptors/ImpactMethod | python3 -m json.tool | grep -i traci"

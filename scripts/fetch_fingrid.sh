#!/usr/bin/env bash
# Fingrid open data for dataset 9 — needs FINGRID_API_KEY in the environment (free registration at data.fingrid.fi).
#   FINGRID_API_KEY=... bash scripts/fetch_fingrid.sh [START] [END]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec "$ROOT/.venv/bin/python" "$ROOT/scripts/fetch_fingrid.py" "$@"

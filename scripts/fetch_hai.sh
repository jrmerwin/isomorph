#!/usr/bin/env bash
# Fetch HAI 21.03 (icsdataset/hai) into datasets/hai/raw. The raw files (~190 MB) are not committed.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
git clone --depth 1 -q https://github.com/icsdataset/hai "$TMP/hai"
mkdir -p "$ROOT/datasets/hai/raw"
cp "$TMP/hai/hai-21.03/"*.csv.gz "$ROOT/datasets/hai/raw/"
cp "$TMP/hai/hai_dataset_technical_details.pdf" "$ROOT/datasets/hai/raw/"
rm -rf "$TMP"
echo "raw files in place: $ROOT/datasets/hai/raw/"

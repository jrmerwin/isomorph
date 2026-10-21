#!/usr/bin/env bash
# Fetch LBNL Building 59 (Luo et al. 2022; doi:10.7941/D1N33Q, CC0) from its Zenodo mirror (record 5951008; Dryad's file
# streams refuse unauthenticated downloads) into datasets/building_59/raw: the 27 cleaned csv files, the Brick model and
# the metadata json. The archive is 263 MB (2.4 GB unpacked); not committed.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RAW="$ROOT/datasets/building_59/raw"; mkdir -p "$RAW"
TMP="$(mktemp -d)"
curl -sfL --max-time 1800 -o "$TMP/Building_59.zip" "https://zenodo.org/api/records/5951008/files/Building_59.zip/content"
curl -sfL -o "$RAW/README_Dryad_Bldg59.txt" "https://zenodo.org/api/records/5951008/files/README_Dryad_Bldg59.txt/content" || true
unzip -q -o "$TMP/Building_59.zip" -d "$TMP/b59"
cp "$TMP/b59/Bldg59_clean data/"*.csv "$RAW/"
cp "$TMP/b59/"*.ttl "$TMP/b59/"*.json "$RAW/" 2>/dev/null || true
rm -rf "$TMP"
ls "$RAW" | wc -l; echo "raw files in place: $RAW"

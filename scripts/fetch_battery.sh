#!/usr/bin/env bash
# Fetch the NASA Ames PCoE "Battery Data Set" (Saha & Goebel 2007; 18650 Li-ion cells cycled to end of life) and
# unpack the FY08Q4 group — B0005, B0006, B0007 (cycled together, April–May 2008) and B0018 (July–August 2008) —
# into datasets/nasa_battery/raw as .mat files. The archive is 210 MB; only the four .mat files are kept.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RAW="$ROOT/datasets/nasa_battery/raw"; mkdir -p "$RAW"
TMP="$(mktemp -d)"
curl -sfL --max-time 900 -o "$TMP/battery.zip" "https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip"
unzip -q -o "$TMP/battery.zip" -d "$TMP/outer"
unzip -q -o "$TMP/outer/5. Battery Data Set/1. BatteryAgingARC-FY08Q4.zip" -d "$TMP/inner"
find "$TMP/inner" -name "B00*.mat" -exec cp {} "$RAW/" \;
find "$TMP/inner" -name "README*" -exec cp {} "$RAW/" \;
rm -rf "$TMP"
ls -la "$RAW"
echo "raw files in place: $RAW"

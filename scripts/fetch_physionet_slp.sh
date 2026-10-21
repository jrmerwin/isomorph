#!/usr/bin/env bash
# Fetch the MIT-BIH Polysomnographic Database (slpdb 1.0.0; Ichimaru & Moody 1999) into datasets/physionet_slp/raw:
# 18 records of 16 subjects, 250 Hz, with ECG, invasive radial-artery blood pressure, respiration and EEG, ECG beat
# annotations (.ecg) and 30-s sleep-stage / apnea annotations (.st). ~80 h in all; the raw files (~350 MB) are not committed.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RAW="$ROOT/datasets/physionet_slp/raw"; mkdir -p "$RAW"
# The S3 mirror of physionet.org/files/slpdb/1.0.0 (same files); the web host throttles downloads to ~5 KB/s.
BASE="https://physionet-open.s3.amazonaws.com/slpdb/1.0.0"
curl -sfL -o "$RAW/RECORDS" "$BASE/RECORDS"
for r in $(cat "$RAW/RECORDS"); do
  for ext in hea dat ecg st; do
    [ -s "$RAW/$r.$ext" ] || curl -sfL --max-time 900 -o "$RAW/$r.$ext" "$BASE/$r.$ext" || echo "  missing $r.$ext"
  done
  echo "  $r"
done
curl -sfL -o "$RAW/README.st" "$BASE/README.st" || true
echo "raw files in place: $RAW"

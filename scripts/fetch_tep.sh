#!/usr/bin/env bash
# Fetch the Tennessee Eastman 1-year continuous run (Souza, de Souza & da Silva 2023) into datasets/tennessee_eastman/raw.
# The raw csv (72 MB) is not committed; this script recreates it.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
git clone --depth 1 -q https://github.com/anasouzac/new_tep_datasets "$TMP/new_tep_datasets"
mkdir -p "$ROOT/datasets/tennessee_eastman/raw"
cp "$TMP/new_tep_datasets/matlab_data_1year.csv" "$ROOT/datasets/tennessee_eastman/raw/"
rm -rf "$TMP"
echo "raw file in place: $ROOT/datasets/tennessee_eastman/raw/matlab_data_1year.csv"

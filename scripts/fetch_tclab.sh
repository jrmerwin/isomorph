#!/usr/bin/env bash
# Fetch the public TCLab (Arduino Temperature Control Lab, Hedengren et al., BYU) recordings isomorph uses into
# datasets/tclab/raw. Each file is one run of a real two-heater, two-sensor lab kit (1 s samples; heater % and °C).
# Sources: APMonitor course uploads and two GitHub repositories (BYU-PRISM, jckantor). Not committed (~1.2 MB).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RAW="$ROOT/datasets/tclab/raw"; mkdir -p "$RAW"
get() { curl -sfL --max-time 120 -o "$RAW/$2" "$1" && echo "  $2"; }
get http://apmonitor.com/do/uploads/Main/tclab_dyn_data2.txt            apm_do_dyn2.csv
get http://apmonitor.com/do/uploads/Main/tclab_dyn_data3.txt            apm_do_dyn3.csv
get http://apmonitor.com/pdc/uploads/Main/tclab_data2.txt               apm_pdc_data2.csv
get http://apmonitor.com/pdc/uploads/Main/tclab_data3.txt               apm_pdc_data3.csv
get http://apmonitor.com/pdc/uploads/Main/tclab_data4.txt               apm_pdc_data4.csv
get http://apmonitor.com/pds/uploads/Main/tclab_data5.txt               apm_pds_data5.csv
get http://apmonitor.com/pds/uploads/Main/tclab_data6.txt               apm_pds_data6.csv
get https://raw.githubusercontent.com/BYU-PRISM/Transformer_MPC/main/01_Emulation/PID_emulation_TCLab/PID_train_data.csv     byu_prism_pid_train.csv
get https://raw.githubusercontent.com/jckantor/cbe30338-book/main/notebooks/data/tclab-data.csv                             kantor_cbe30338.csv
echo "raw files in place: $RAW"

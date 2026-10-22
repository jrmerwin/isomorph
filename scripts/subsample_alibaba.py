"""Stream machine_usage.csv (9 GB, 247M rows) once and keep every row of a deterministic 200-machine subsample
(m_20, m_40, ..., m_4000: every 20th machine id) -> datasets/alibaba_2018/raw/machine_usage_sub200.csv."""
import os, sys, pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "datasets/alibaba_2018/raw"); src = os.path.join(RAW, "machine_usage.csv"); out = os.path.join(RAW, "machine_usage_sub200.csv")
keep = set(f"m_{i}" for i in range(20, 4001, 20))
cols = ["machine_id", "time_stamp", "cpu_util_percent", "mem_util_percent", "mem_gps", "mkpi", "net_in", "net_out", "disk_io_percent"]
n = 0; first = True
for chunk in pd.read_csv(src, header=None, names=cols, usecols=["machine_id", "time_stamp", "cpu_util_percent", "mem_util_percent", "net_in", "net_out", "disk_io_percent"], chunksize=5_000_000):
    sub = chunk[chunk.machine_id.isin(keep)]
    if len(sub): sub.to_csv(out, mode="w" if first else "a", header=first, index=False); first = False; n += len(sub)
print("kept", n, "rows for", len(keep), "machines ->", out)

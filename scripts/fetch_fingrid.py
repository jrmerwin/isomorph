"""
Fetch Fingrid open-data series for dataset 9 (Nordic grid frequency regulation) into datasets/fingrid/raw.
Every series is served only with a subscription key (free registration, https://data.fingrid.fi/en/instructions;
licence CC BY 4.0): set FINGRID_API_KEY in the environment — it is never written to disk.

    FINGRID_API_KEY=... python3 scripts/fetch_fingrid.py [START=2024-07-01] [END=2025-07-01]

The API returns, for format=csv, a JSON envelope {"data": "<semicolon csv>", "pagination": {...}}; one call per
two seconds is the rate limit; pages of up to 20,000 rows.
"""
import os, sys, time, json, urllib.request, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "datasets/fingrid/raw"); os.makedirs(RAW, exist_ok=True)
SERIES = {177: "frequency_3min_Hz", 343: "fcrn_activated_down_15min_MW", 344: "fcrn_activated_up_15min_MW",
          349: "afrr_activation_up_15min_MW", 350: "afrr_activation_down_15min_MW", 194: "net_import_export_3min_MW"}
# (397, calculated imbalance at 1 min, begins 2025-06-25 and is left out of the year.) A query is capped at 40,000 rows, so
# the window is fetched month by month.
start = sys.argv[1] if len(sys.argv) > 1 else "2024-07-01"; end = sys.argv[2] if len(sys.argv) > 2 else "2025-07-01"
key = os.environ.get("FINGRID_API_KEY") or sys.exit("set FINGRID_API_KEY (free registration at data.fingrid.fi)")
def months(a, b):
    y, m = int(a[:4]), int(a[5:7]); out = []
    while f"{y:04d}-{m:02d}-01" < b:
        y2, m2 = (y + 1, 1) if m == 12 else (y, m + 1)
        out.append((f"{y:04d}-{m:02d}-01", min(f"{y2:04d}-{m2:02d}-01", b))); y, m = y2, m2
    return out


for ds, name in SERIES.items():
    out = os.path.join(RAW, f"{ds}_{name}_{start}_{end}.csv"); rows = 0; header = None; calls = 0
    with open(out, "w") as fh:
      for w0, w1 in months(start, end):
        page = 1
        while True:
            calls += 1
            q = urllib.parse.urlencode(dict(startTime=f"{w0}T00:00:00Z", endTime=f"{w1}T00:00:00Z", format="csv", pageSize=20000, page=page, sortBy="startTime", sortOrder="asc"))
            req = urllib.request.Request(f"https://data.fingrid.fi/api/datasets/{ds}/data?{q}", headers={"x-api-key": key})
            for attempt in range(5):
                try:
                    with urllib.request.urlopen(req, timeout=120) as r: env = json.load(r)
                    break
                except urllib.error.HTTPError as e:
                    if e.code == 429: time.sleep(3); continue
                    raise
            lines = env["data"].split("\n")
            if header is None: header = lines[0]; fh.write(header + "\n")
            body = [l for l in lines[1:] if l.strip()]; fh.write("\n".join(body) + ("\n" if body else "")); rows += len(body)
            pg = env.get("pagination", {})
            if not pg.get("nextPage") or page >= (pg.get("lastPage") or 1): break
            page += 1; time.sleep(2.1)
        time.sleep(2.1)
    print(f"  {ds} {name}: {rows} rows, {calls} call(s)")
print("raw files in place:", RAW)

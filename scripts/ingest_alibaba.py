"""
Dataset 10 (negative control one): Alibaba cluster-trace-v2018 machine usage, 200-machine subsample

    curl -o datasets/alibaba_2018/raw/machine_usage.tar.gz https://clusterdata2018pubcn.oss-cn-beijing.aliyuncs.com/machine_usage.tar.gz
    tar -xzf ... && python3 scripts/subsample_alibaba.py     # one pass over the 9 GB table -> machine_usage_sub200.csv
    python3 scripts/ingest_alibaba.py                       # choices (3.1, 3.2) + canonical dataset; resumable
"""
import os, sys, json, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import alibaba_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset
from isomorph.choose.entity import choose_entity, sys_layout

RAW = os.path.join(ROOT, "datasets/alibaba_2018/raw"); OUT = os.path.join(ROOT, "datasets/alibaba_2018")
assert os.path.exists(os.path.join(RAW, "machine_usage_sub200.csv")), "run scripts/subsample_alibaba.py first"
t0 = time.time()
df, machines = L.load(RAW)
lay = L.machine_layout(df, machines)
print(f"Alibaba 2018: {len(df)} minutes ({df.minute.iloc[-1]/1440:.1f} days), {len(lay['entities'])} machines, roles {list(lay['kinds'])} ({time.time()-t0:.0f}s)")
os.makedirs(os.path.join(OUT, "out"), exist_ok=True)
final = os.path.join(OUT, "out", "choices_v1.json")
if os.path.exists(final) and json.load(open(final)).get("complete"):
    rec = json.load(open(final)); choice, thresholds, trace = rec["choice"], rec["thresholds"], rec["trace"]
    print("symbolization choice loaded from", final)
else:
    print("== symbolization by compression (3.2) ==")
    choice, thresholds, trace = choose_symbolization(df, lay, checkpoint=os.path.join(OUT, "out", "choice_checkpoint.json"))
    json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, complete=True), open(final, "w"), indent=1, default=str)
print("chosen:", choice); print(f"({time.time()-t0:.0f}s)")
print("\n== entity by compression (3.1) ==")
# no single-system candidate: 198 machines x 5 roles = 990 roles (~6,000 types) are beyond what the Markov-only comparison
# (adjacent-pair features over the vocabulary squared) can fit — the same wall as Building 59; the physical candidate is machine
best, scores = "machine", {"machine": dict(bits=None, note="only candidate run; a single-system layout of 990 roles is not fittable")}
print("chosen entity layout:", best, scores)
json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores, complete=True), open(final, "w"), indent=1, default=str)
layout_used = lay if best == "machine" else sys_layout(lay)
ch = choice if best == "machine" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_") or r.endswith("_" + b)), r)) for r in layout_used["kinds"]}
extra = dict(time_unit="minute", sample_minutes=L.SAMPLE_MIN, entity_key=best, machines=machines, negative_control=True,
             entity_note="machine (198 units with data) is the only candidate run: a single-system layout of 990 roles is not fittable by the Markov-only comparison",
             source="Alibaba cluster-trace-v2018 machine_usage (github.com/alibaba/clusterdata; OSS mirror), 200-machine subsample (every 20th id)",
             span_note="8 days at 1-minute means; admitted by horizons if the recurrence horizon allows; a negative control by design (section 6)",
             declared_prediction="as a source into TEP the structure cell is ~0 (below 5 bit-H); if not, the cells into TEP are regularisation and the instrument is fixed before anything is reported")
ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=[], kind="real cluster trace (Alibaba 2018, 200 machines) — negative control", origin="scripts/ingest_alibaba.py")
json.dump(dict(mechanisms=[], match="role_prefix", note="negative control: no mechanism is true by construction; recovery is not measured"), open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")

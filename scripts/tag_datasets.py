"""
Tag the roles of the datasets with parts of speech (METHOD 3.14, v4) and write them into each
sidecar ("tags"), plus tag-prefixed shapes into each library json. Tags are computed from the raw
series relative to the dataset's own horizon (recurrence time, 3.3), so the raw frames are needed:
    python3 scripts/tag_datasets.py            # tennessee_eastman, hai (raw files fetched)
The buildings keep no tags for now (B' has scrambled type names; same-kind alignment works untagged).
"""
import os, sys, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
from collections import Counter
from isomorph.choose.pos import tag_layout, shape_of
from isomorph.canon.ingest import read_dataset
from isomorph.mine.contexts import streams_of, LagClasses


def horizon_samples(d, sample_min):
    ev, obs, gaps, side, key = read_dataset(d)
    ents = sorted(e for e in obs.entity.unique() if e != "ALL"); st = streams_of(ev, ents)
    lo, hi = ev.t.min(), ev.t.max() + 1
    return LagClasses.from_recurrence(st, lo, lo + (hi - lo) * 0.5).horizon / sample_min


def write_tags(d, tags, note):
    side = json.load(open(os.path.join(d, "sidecar.json")))
    side["tags"] = {r: dict(cls=t["cls"], coarse=t["coarse"], per_column={c: v["features"] | {"cls": v["cls"]} for c, v in t["per_column"].items()}) for r, t in tags.items()}
    side["tags_note"] = note
    json.dump(side, open(os.path.join(d, "sidecar.json"), "w"), indent=1)
    for lib in glob.glob(os.path.join(d, "out", "library_*.json")):
        L = json.load(open(lib))
        for f in L.get("fragments", []): f["shape"] = shape_of(f["prior"], f["lag"], f["target"], side["tags"])
        L["shape_counts"] = dict(Counter(f["shape"] for f in L.get("fragments", [])).most_common())
        json.dump(L, open(lib, "w"), indent=1)
    print(d, Counter(t["cls"] for t in tags.values()))


if __name__ == "__main__":
    import tep_layout as T, hai_layout as HL
    d = os.path.join(ROOT, "datasets/tennessee_eastman")
    df = T.load(os.path.join(d, "raw/matlab_data_1year.csv")).iloc[: int(120 * 1440 / T.SAMPLE_MIN)]
    write_tags(d, tag_layout(df, T.vessel_layout(), horizon_samples(d, T.SAMPLE_MIN)), "parts of speech (3.14, v4) from the first 120 days, relative to H = recurrence time")
    d = os.path.join(ROOT, "datasets/hai")
    df, bounds, files = HL.load_files(sorted(glob.glob(os.path.join(d, "raw/*.csv.gz"))))
    write_tags(d, tag_layout(df, HL.process_layout(df), horizon_samples(d, HL.SAMPLE_MIN)), "parts of speech (3.14, v4) at 1-minute means, relative to H = recurrence time")

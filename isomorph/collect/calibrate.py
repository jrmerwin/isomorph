"""
Calibration gates (METHOD.md section 6/7): building_a and building_b must
reproduce collection/calibration_reference.json within CALIBRATION_TOLERANCE_BITS
under each profile. `isomorph calibrate` runs both datasets and the A->B
transfer cell, prints the comparison, and writes the current numbers to
collection/calibration_latest.json. With --record it overwrites the reference.
"""
import json, os, sys
import numpy as np
from .. import constants as K
from ..pipeline import run
from ..score.model import FeatureMap, Model
from ..transfer.align import align_datasets
from ..transfer.apply import transfer, mapping_accuracy

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = os.path.join(ROOT, "collection", "calibration_reference.json")
LATEST = os.path.join(ROOT, "collection", "calibration_latest.json")


def measure(profile, log=print):
    dA, dB = os.path.join(ROOT, "datasets", "building_a"), os.path.join(ROOT, "datasets", "building_b")
    cardA, A = run(dA, profile, 0, log)
    cardB, Bd = run(dB, profile, 0, log)
    key = json.load(open(os.path.join(dB, "answer_key.json")))
    rng = np.random.default_rng(0)
    # A's frozen model: Markov + all count>=min contexts (the representation that transferred)
    from ..transfer.apply import own_contexts
    mc = K.PROFILES[profile]["min_count"]
    modelA = Model(FeatureMap(A["vocab"], True, own_contexts(A["rows_train"], mc))).fit(A["rows_train"])
    mapping, anchors, obj = align_datasets(A["rows_train"], A["all_types"], Bd["rows_train"], Bd["all_types"], rng)
    acc = mapping_accuracy(mapping, key, A["all_types"])
    true_map = {t: key["token"][t]["A_role"] for t in Bd["all_types"]}
    tr_learned = transfer(modelA, Bd, mapping, Bd["vocab"], mc)
    tr_true = transfer(modelA, Bd, true_map, Bd["vocab"], mc)
    out = dict(profile=profile,
               building_a=dict(headline={m: (v["all"] if isinstance(v, dict) else v) for m, v in cardA["headline_bits"].items()},
                               fragments=cardA["library"]["fragments"], gain=cardA["gain"]),
               building_b=dict(headline={m: (v["all"] if isinstance(v, dict) else v) for m, v in cardB["headline_bits"].items()},
                               fragments=cardB["library"]["fragments"], gain=cardB["gain"]),
               transfer_A_to_B=dict(mapping_accuracy=acc, anchors=anchors, learned=tr_learned, true_mapping=tr_true))
    log(f"[transfer A->B] mapping accuracy {acc['accuracy']:.2f} on {acc['n_scorable']} types (anchors {anchors}); "
        f"zero-shot learned {tr_learned['zero_shot']['all']:.3f} / shared {tr_learned['zero_shot']['shared']:.3f}; "
        f"true {tr_true['zero_shot']['all']:.3f} / {tr_true['zero_shot']['shared']:.3f}; cell {tr_learned.get('cell_bit_horizons')} bit-H")
    return out


def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            out.update(flatten(v, prefix + k + "."))
        elif isinstance(v, (int, float)) and not isinstance(v, bool):
            out[prefix + k] = float(v)
    return out


def calibrate(record=False, profiles=("legacy", "v1"), log=print):
    results = {p: measure(p, log) for p in profiles}
    json.dump(results, open(LATEST, "w"), indent=1)
    if record or not os.path.exists(REF):
        json.dump(results, open(REF, "w"), indent=1); log(f"reference written to {REF}"); return True
    ref = json.load(open(REF)); ok = True
    for p in profiles:
        a, b = flatten(ref.get(p, {})), flatten(results[p])
        for k in sorted(set(a) & set(b)):
            if any(s in k for s in ("headline", "zero_shot", "cell_bit", "accuracy")):
                d = abs(a[k] - b[k])
                tol = K.CALIBRATION_TOLERANCE_BITS if "accuracy" not in k and "cell" not in k else 0.05
                flag = "" if d <= tol else "   <-- OUT OF TOLERANCE"
                if flag: ok = False
                log(f"  {p:7s} {k:60s} ref {a[k]:8.3f} now {b[k]:8.3f}{flag}")
    log("calibration " + ("PASSED" if ok else "FAILED"))
    return ok


if __name__ == "__main__":
    calibrate(record="--record" in sys.argv)

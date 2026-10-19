"""
The transfer matrix (METHOD.md 3.12, 3.13 — collection step).

    isomorph transfer <dataset_A> <dataset_B> [--profile v1] [--seed 0]

runs both datasets' pipelines once, aligns their vocabularies from structure alone (3.12), and
measures the ordered cells A->B and B->A: zero-shot bits of the source's frozen model through the
mapping on the receiver's test split, the learning-curve shift from mixing the translated model with
the receiver's own, the cell value in bit-days, and the mapping accuracy when the receiver's answer
key maps its types to the source's. Each cell is appended to collection/matrix.json under the method
version, so the matrix is regenerated per version and never mixes versions.
"""
import json, os, time
import numpy as np
from .. import constants as K
from ..pipeline import run, load_state
from ..score.model import FeatureMap, Model
from ..transfer.align import align_datasets
from ..transfer.apply import transfer, mapping_accuracy, own_contexts

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MATRIX = os.path.join(ROOT, "collection", "matrix.json")


def _cell(src, dst, profile, rng, key_dst=None, log=print):
    """Ordered cell src -> dst from the two pipelines' returned state."""
    mc = K.PROFILES[profile]["min_count"]
    model_src = Model(FeatureMap(src["vocab"], True, own_contexts(src["rows_train"], mc))).fit(src["rows_train"])
    mapping, anchors, obj = align_datasets(src["rows_train"], src["all_types"], dst["rows_train"], dst["all_types"], rng)
    tr = transfer(model_src, dst, mapping, dst["vocab"], mc)
    acc = mapping_accuracy(mapping, key_dst, src["all_types"]) if key_dst and "token" in key_dst else "not measured (no mapping key)"
    shared = sum(1 for t in dst["vocab"] if mapping.get(t) is not None)
    out = dict(mapping=mapping, anchors=anchors, alignment_objective=float(obj), types_mapped=shared, types_total=len(dst["vocab"]),
               zero_shot=tr["zero_shot"], learning_curve=tr.get("curve"), cell_bit_days=tr["cell_bit_days"],
               damage=tr.get("damage"), mapping_accuracy=acc)
    log(f"  zero-shot through mapping {tr['zero_shot']['all']:.3f} (shared types {tr['zero_shot']['shared']:.3f}, unshared {tr['zero_shot'].get('unshared')}); "
        f"cell {tr['cell_bit_days']:.2f} bit-days; {shared}/{len(dst['vocab'])} receiver types mapped; accuracy {acc if isinstance(acc, str) else round(acc['accuracy'], 2)}")
    return out


def _get(d, profile, seed, log):
    c = load_state(d, profile, seed)
    if c is not None:
        log(f"[{os.path.basename(os.path.normpath(d))}] pipeline state loaded from cache (method v{K.METHOD_VERSION}, {profile}, seed {seed})")
        return c
    return run(d, profile, seed, log)


def transfer_pair(dirA, dirB, profile="v1", seed=0, log=print, direction="both"):
    """direction: 'both', 'ab' (A -> B only) or 'ba'. One-direction runs merge into the same matrix record."""
    t0 = time.time()
    nameA, nameB = os.path.basename(os.path.normpath(dirA)), os.path.basename(os.path.normpath(dirB))
    cardA, A = _get(dirA, profile, seed, log)
    cardB, B = _get(dirB, profile, seed, log)
    keyA = json.load(open(os.path.join(dirA, "answer_key.json"))) if os.path.exists(os.path.join(dirA, "answer_key.json")) else None
    keyB = json.load(open(os.path.join(dirB, "answer_key.json"))) if os.path.exists(os.path.join(dirB, "answer_key.json")) else None
    os.makedirs(os.path.dirname(MATRIX), exist_ok=True)
    M = json.load(open(MATRIX)) if os.path.exists(MATRIX) else {}
    key = f"{nameA}|{nameB}|{profile}|{seed}"
    rec = M.get(f"v{K.METHOD_VERSION}", {}).get(key) or dict(method_version=K.METHOD_VERSION, profile=profile, seed=seed, A=nameA, B=nameB)
    rec.update(headline=dict(A=cardA["headline_bits"]["logistic library"], B=cardB["headline_bits"]["logistic library"]),
               triviality=dict(A=cardA["headline_bits"]["logistic triviality library"], B=cardB["headline_bits"]["logistic triviality library"]))
    if direction in ("both", "ab"):
        rng = np.random.default_rng(seed); log(f"[transfer {nameA} -> {nameB}]"); rec["A_to_B"] = _cell(A, B, profile, rng, keyB, log)
    if direction in ("both", "ba"):
        rng = np.random.default_rng(seed); log(f"[transfer {nameB} -> {nameA}]"); rec["B_to_A"] = _cell(B, A, profile, rng, keyA, log)
    rec["elapsed_s"] = round(time.time() - t0, 1)
    M.setdefault(f"v{K.METHOD_VERSION}", {})[key] = rec
    json.dump(M, open(MATRIX, "w"), indent=1, default=str)
    return rec


def cell_markdown(rec):
    def row(name, c):
        z = c["zero_shot"]; acc = c["mapping_accuracy"]
        return (f"| {name} | {z['all']:.3f} | {z['shared']:.3f} | {c['cell_bit_days']:.2f} | {c['types_mapped']}/{c['types_total']} | "
                f"{acc if isinstance(acc, str) else f'{acc['accuracy']:.2f}'} |")
    lines = [f"# Transfer cells — {rec['A']} ↔ {rec['B']} (method v{rec['method_version']}, profile {rec['profile']}, seed {rec['seed']})", "",
             f"Own libraries: {rec['A']} {rec['headline']['A']['all']:.3f} bits (triviality {rec['triviality']['A']['all']:.3f}); "
             f"{rec['B']} {rec['headline']['B']['all']:.3f} bits (triviality {rec['triviality']['B']['all']:.3f})", "",
             "| direction | zero-shot bits (all) | zero-shot (shared types) | cell (bit-days) | receiver types mapped | mapping accuracy |",
             "| --- | --- | --- | --- | --- | --- |"]
    if "A_to_B" in rec: lines.append(row(f"{rec['A']} → {rec['B']}", rec["A_to_B"]))
    if "B_to_A" in rec: lines.append(row(f"{rec['B']} → {rec['A']}", rec["B_to_A"]))
    return "\n".join(lines) + "\n"

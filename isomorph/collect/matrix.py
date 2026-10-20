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
from ..transfer.align import align_datasets, align_roles, has_roles
from ..transfer.apply import transfer, mapping_accuracy, own_contexts

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MATRIX = os.path.join(ROOT, "collection", "matrix.json")


def _cell(src, dst, profile, rng, key_dst=None, log=print, tags_src=None, tags_dst=None):
    """Ordered cell src -> dst from the two pipelines' returned state. Tags (3.14) constrain the alignment
    and the control when both datasets carry them."""
    mc = K.PROFILES[profile]["min_count"]
    model_src = Model(FeatureMap(src["vocab"], True, own_contexts(src["rows_train"], mc))).fit(src["rows_train"])
    role_level = has_roles(src["all_types"]) and has_roles(dst["all_types"])
    if role_level:   # v4: roles to roles, symbols by spelling
        mapping, role_map, anchors, obj = align_roles(src["rows_train"], src["all_types"], dst["rows_train"], dst["all_types"], rng, tags_src, tags_dst)
        log(f"  role-level alignment: {sum(1 for v in role_map.values() if v)} of {len(role_map)} receiver roles mapped; anchors {anchors}")
    else:
        mapping, anchors, obj = align_datasets(src["rows_train"], src["all_types"], dst["rows_train"], dst["all_types"], rng, tagsA=tags_src, tagsB=tags_dst)
        role_map = None
    tr = transfer(model_src, dst, mapping, dst["vocab"], mc, rng=rng, tagsB=tags_dst)
    acc = mapping_accuracy(mapping, key_dst, src["all_types"]) if key_dst and "token" in key_dst else "not measured (no mapping key)"
    shared = sum(1 for t in dst["vocab"] if mapping.get(t) is not None)
    out = dict(mapping=mapping, anchors=anchors, alignment_objective=float(obj), types_mapped=shared, types_total=len(dst["vocab"]),
               tag_constrained=bool(tags_src and tags_dst), role_level=role_level, role_map=role_map,
               zero_shot=tr["zero_shot"], learning_curve=tr.get("curve"), cell_bit_days=tr["cell_bit_days"],
               cell_control_bit_days=tr.get("cell_control_bit_days"), cell_net_bit_days=tr.get("cell_net_bit_days"),
               damage=tr.get("damage"), mapping_accuracy=acc)
    log(f"  zero-shot through mapping {tr['zero_shot']['all']:.3f} (shared types {tr['zero_shot']['shared']:.3f}, unshared {tr['zero_shot'].get('unshared')}, "
        f"permuted-mapping control {tr['zero_shot'].get('control')}); cell {tr['cell_bit_days']:.2f} bit-days, control {tr.get('cell_control_bit_days', float('nan')):.2f}, "
        f"NET {tr.get('cell_net_bit_days', float('nan')):.2f}; {shared}/{len(dst['vocab'])} receiver types mapped; accuracy {acc if isinstance(acc, str) else round(acc['accuracy'], 2)}")
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
    tagsA = json.load(open(os.path.join(dirA, "sidecar.json"))).get("tags"); tagsB = json.load(open(os.path.join(dirB, "sidecar.json"))).get("tags")
    if tagsA and tagsB: log(f"[transfer] tag-constrained alignment (3.14): {nameA} {len(tagsA)} tagged roles, {nameB} {len(tagsB)}")
    os.makedirs(os.path.dirname(MATRIX), exist_ok=True)
    M = json.load(open(MATRIX)) if os.path.exists(MATRIX) else {}
    key = f"{nameA}|{nameB}|{profile}|{seed}"
    rec = M.get(f"v{K.METHOD_VERSION}", {}).get(key) or dict(method_version=K.METHOD_VERSION, profile=profile, seed=seed, A=nameA, B=nameB)
    rec.update(headline=dict(A=cardA["headline_bits"]["logistic library"], B=cardB["headline_bits"]["logistic library"]),
               triviality=dict(A=cardA["headline_bits"]["logistic triviality library"], B=cardB["headline_bits"]["logistic triviality library"]))
    if direction in ("both", "ab"):
        rng = np.random.default_rng(seed); log(f"[transfer {nameA} -> {nameB}]"); rec["A_to_B"] = _cell(A, B, profile, rng, keyB, log, tagsA, tagsB)
    if direction in ("both", "ba"):
        rng = np.random.default_rng(seed); log(f"[transfer {nameB} -> {nameA}]"); rec["B_to_A"] = _cell(B, A, profile, rng, keyA, log, tagsB, tagsA)
    rec["elapsed_s"] = round(time.time() - t0, 1)
    M.setdefault(f"v{K.METHOD_VERSION}", {})[key] = rec
    json.dump(M, open(MATRIX, "w"), indent=1, default=str)
    return rec


def cell_markdown(rec):
    def row(name, c):
        z = c["zero_shot"]; acc = c["mapping_accuracy"]
        ctl = c.get("cell_control_bit_days"); net = c.get("cell_net_bit_days")
        return (f"| {name} | {z['all']:.3f} | {z['shared']:.3f} | {z.get('control') if z.get('control') is None else f'{z['control']:.3f}'} | {c['cell_bit_days']:.2f} | "
                f"{'' if ctl is None else f'{ctl:.2f}'} | {'' if net is None else f'**{net:.2f}**'} | {c['types_mapped']}/{c['types_total']} | "
                f"{acc if isinstance(acc, str) else f'{acc['accuracy']:.2f}'} |")
    lines = [f"# Transfer cells — {rec['A']} ↔ {rec['B']} (method v{rec['method_version']}, profile {rec['profile']}, seed {rec['seed']})", "",
             f"Own libraries: {rec['A']} {rec['headline']['A']['all']:.3f} bits (triviality {rec['triviality']['A']['all']:.3f}); "
             f"{rec['B']} {rec['headline']['B']['all']:.3f} bits (triviality {rec['triviality']['B']['all']:.3f})", "",
             "| direction | zero-shot (all) | zero-shot (shared) | zero-shot, permuted mapping | cell (bit-days) | control cell | net cell | receiver types mapped | mapping accuracy |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    if "A_to_B" in rec: lines.append(row(f"{rec['A']} → {rec['B']}", rec["A_to_B"]))
    if "B_to_A" in rec: lines.append(row(f"{rec['B']} → {rec['A']}", rec["B_to_A"]))
    return "\n".join(lines) + "\n"

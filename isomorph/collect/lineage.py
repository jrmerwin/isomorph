"""
The collection step (METHOD.md 3.13): growth, provenance, the similarity tree and the lineage.

    isomorph lineage            -> collection/lineage.json, docs/LINEAGE.md

Characters are tagged shapes (3.14, 3.15): a fragment's type-free, tag-prefixed spelling, a chain's, a return's.
Taxa are the admitted datasets whose libraries carry shapes. The character matrix is shape x dataset (number of
validated fragments or chains with that shape). Two distances between datasets: one from shared shapes (Jaccard
over fragment shapes; Bray-Curtis over counts for comparison) and one from the transfer matrix (the symmetrised
net cell of the current method version); each is clustered hierarchically (average linkage) into a tree.

Provenance: a shape first validated in dataset X (running order) and validated again in a later dataset Y
recurred in Y and is inherited there. Through a mapping (3.12): for every ordered cell A -> B, a source fragment
whose prior and target both have receiver types mapped onto them is TESTED in B; it is CONFIRMED when the receiver's
library holds the translated fragment at the same lag class, else it FAILED in B. The lineage records, per shape,
where it first appeared, where it recurred, where it was confirmed through a mapping and where it was tested and
failed; the fragment fields `confirmed_in` / `failed_in` of every library are written from this step.
"""
import json, os
from collections import defaultdict, Counter
import numpy as np
from .. import constants as K

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MATRIX = os.path.join(ROOT, "collection", "matrix.json")
OUT_JSON = os.path.join(ROOT, "collection", "lineage.json")
OUT_MD = os.path.join(ROOT, "docs", "LINEAGE.md")

# The running order (METHOD.md section 6) with each dataset's standing. Synthetic datasets are flagged in every
# view; a withdrawn dataset is inventoried for the record and is not a taxon.
RUNNING_ORDER = [
    ("building_a", "synthetic"), ("building_b", "synthetic"), ("tennessee_eastman", "admitted"),
    ("hai", "admitted (provisional: 15.3 days, 178 H; standing decision, section 6)"), ("tclab", "withdrawn"), ("nasa_battery", "admitted"),
    ("physionet_slp", "admitted (v7: by horizons, 19,419 H)"),
    ("building_59", "admitted (365 days)"),
]


def _load(d):
    base = os.path.join(ROOT, "datasets", d)
    lib = json.load(open(os.path.join(base, "out", "library_v1.json")))
    card = json.load(open(os.path.join(base, "out", "benchmark_v1.json")))
    side = json.load(open(os.path.join(base, "sidecar.json")))
    return lib, card, side


def inventory(lib, card):
    """Per dataset: shape counters for fragments, chains and returns, with lift summaries."""
    frag = defaultdict(lambda: dict(n=0, lifts=[]))
    for f in lib["fragments"]:
        if f.get("shape"): frag[f["shape"]]["n"] += 1; frag[f["shape"]]["lifts"].append(f["lift"])
    chain = defaultdict(lambda: dict(n=0, lifts=[], used=0)); ret = defaultdict(lambda: dict(n=0, lifts=[], used=0))
    for h in lib.get("chains", []):
        if not h.get("shape"): continue
        tgt = ret if h.get("is_return") else chain
        tgt[h["shape"]]["n"] += 1; tgt[h["shape"]]["lifts"].append(h["cond_lift"]); tgt[h["shape"]]["used"] += int(h.get("used", False))
    def summ(c):
        return {s: dict(n=v["n"], mean_lift=float(np.mean(v["lifts"])), max_lift=float(np.max(v["lifts"])), **({"used": v["used"]} if "used" in v else {})) for s, v in c.items()}
    return dict(fragments=len(lib["fragments"]), fragments_tagged=sum(1 for f in lib["fragments"] if f.get("shape")),
                chains=len(lib.get("chains", [])), returns=sum(1 for h in lib.get("chains", []) if h.get("is_return")),
                library_bits=card["headline_bits"]["logistic library"]["all"], method_version=card["method_version"],
                shapes=dict(fragment=summ(frag), chain=summ(chain), ret=summ(ret)))


def _jaccard(a, b):
    a, b = set(a), set(b)
    return 1.0 - (len(a & b) / len(a | b) if a | b else 0.0)


def _bray_curtis(ca, cb):
    keys = set(ca) | set(cb)
    num = sum(abs(ca.get(k, 0) - cb.get(k, 0)) for k in keys); den = sum(ca.get(k, 0) + cb.get(k, 0) for k in keys)
    return num / den if den else 1.0


def transfer_distance(taxa, version=f"v{K.METHOD_VERSION}"):
    """Symmetrised net cell of the current version, as a distance d = 1 / (1 + max(net, 0)); a missing pair is 1."""
    M = json.load(open(MATRIX)).get(version, {}) if os.path.exists(MATRIX) else {}
    net = {}
    for rec in M.values():
        if rec.get("seed") != 0: continue
        a, b = rec["A"], rec["B"]
        vals = [rec[d].get("cell_net_bit_days") for d in ("A_to_B", "B_to_A") if d in rec and rec[d].get("cell_net_bit_days") is not None]
        if vals: net[frozenset((a, b))] = float(np.mean(vals))
    D = np.ones((len(taxa), len(taxa)))
    for i, a in enumerate(taxa):
        D[i, i] = 0.0
        for j, b in enumerate(taxa):
            if i != j and frozenset((a, b)) in net: D[i, j] = 1.0 / (1.0 + max(net[frozenset((a, b))], 0.0))
    return D, {"|".join(sorted(k)): v for k, v in net.items()}


def tree(D, taxa):
    """Average-linkage hierarchical clustering; returns (newick, merges)."""
    if len(taxa) < 2: return (f"({taxa[0]});" if taxa else ";"), []
    from scipy.cluster.hierarchy import linkage, to_tree
    from scipy.spatial.distance import squareform
    Z = linkage(squareform(D, checks=False), method="average")
    root = to_tree(Z)
    def newick(node):
        if node.is_leaf(): return taxa[node.id]
        return f"({newick(node.left)}:{node.dist / 2:.3f},{newick(node.right)}:{node.dist / 2:.3f})"
    merges = [dict(members=sorted(taxa[int(i)] if i < len(taxa) else f"node{int(i)}" for i in (a, b)), height=float(h)) for a, b, h, _ in Z]
    return newick(root) + ";", merges


def inheritance(taxa, libs, mapping_cells):
    """Per shape: first appearance, recurrences, confirmations and failures through mappings; per fragment: the
    confirmed_in / failed_in fields (3.13). mapping_cells: {(source, receiver): mapping {receiver type: source type}}."""
    order = {d: i for i, d in enumerate(taxa)}
    shapes_in = {d: set(f["shape"] for f in libs[d]["fragments"] if f.get("shape")) | set(h["shape"] for h in libs[d].get("chains", []) if h.get("shape")) for d in taxa}
    lineage = {}
    for d in taxa:
        for s in shapes_in[d]:
            L = lineage.setdefault(s, dict(first=d, recurred=[], confirmed_through_mapping=[], failed=[], kind=("return" if "[return]" in s else "chain" if s.count("->") == 2 else "fragment")))
            if order[d] < order[L["first"]]: L["first"] = d
    for s, L in lineage.items():
        L["recurred"] = sorted((d for d in taxa if s in shapes_in[d] and d != L["first"]), key=order.get)
        L["inherited_in"] = list(L["recurred"])
    edges = defaultdict(lambda: dict(shapes_recurred=0, returns_recurred=0, fragments_tested=0, fragments_confirmed=0, fragments_failed=0))
    for s, L in lineage.items():
        for d in L["recurred"]:
            e = edges[(L["first"], d)]; e["shapes_recurred"] += 1; e["returns_recurred"] += int(L["kind"] == "return")
    # through mappings
    frag_sets = {d: set((f["prior"], f["lag"], f["target"]) for f in libs[d]["fragments"]) for d in taxa}
    for d in taxa:
        for f in libs[d]["fragments"]: f["confirmed_in"] = []; f["failed_in"] = []
    for (src, rec), mapping in mapping_cells.items():
        if src not in taxa or rec not in taxa: continue
        inv = defaultdict(set)
        for tb, ta in mapping.items():
            if ta: inv[ta].add(tb)
        e = edges[(src, rec)]
        for f in libs[src]["fragments"]:
            b1, b2 = inv.get(f["prior"], set()), inv.get(f["target"], set())
            if not (b1 and b2): continue
            e["fragments_tested"] += 1
            ok = any((x, f["lag"], y) in frag_sets[rec] for x in b1 for y in b2)
            (f["confirmed_in"] if ok else f["failed_in"]).append(rec)
            e["fragments_confirmed" if ok else "fragments_failed"] += 1
            if f.get("shape"):
                L = lineage[f["shape"]]
                (L["confirmed_through_mapping"] if ok else L["failed"]).append(rec)
    for L in lineage.values():
        L["confirmed_through_mapping"] = sorted(set(L["confirmed_through_mapping"]), key=order.get)
        L["failed"] = sorted(set(L["failed"]) - set(L["confirmed_through_mapping"]), key=order.get)
    return lineage, {f"{a}->{b}": v for (a, b), v in edges.items()}


def build(log=print, write_libraries=True):
    libs, cards, sides, inv, status = {}, {}, {}, {}, {}
    for d, st in RUNNING_ORDER:
        p = os.path.join(ROOT, "datasets", d, "out", "library_v1.json")
        if not os.path.exists(p): continue
        libs[d], cards[d], sides[d] = _load(d); status[d] = st
        inv[d] = inventory(libs[d], cards[d])
    taxa = [d for d, st in RUNNING_ORDER if d in inv and st.startswith(("admitted", "provisional")) and inv[d]["fragments_tagged"] > 0]
    log(f"[lineage] taxa with tagged shapes: {taxa}; inventoried: {list(inv)}")
    # character matrix
    chars = defaultdict(dict)
    for d in inv:
        for kind in ("fragment", "chain", "ret"):
            for s, v in inv[d]["shapes"][kind].items(): chars[s][d] = v["n"]
    # shared shapes, pairwise
    shared = {}
    for i, a in enumerate(taxa):
        for b in taxa[i + 1:]:
            shared[f"{a}|{b}"] = {kind: sorted(set(inv[a]["shapes"][kind]) & set(inv[b]["shapes"][kind])) for kind in ("fragment", "chain", "ret")}
    # distances and trees
    n = len(taxa)
    Dj = np.zeros((n, n)); Db = np.zeros((n, n))
    for i, a in enumerate(taxa):
        for j, b in enumerate(taxa):
            if i == j: continue
            fa = {s: v["n"] for s, v in inv[a]["shapes"]["fragment"].items()}; fb = {s: v["n"] for s, v in inv[b]["shapes"]["fragment"].items()}
            Dj[i, j] = _jaccard(fa, fb); Db[i, j] = _bray_curtis(fa, fb)
    Dt, net = transfer_distance(taxa)
    trees = {name: dict(newick=tree(D, taxa)[0], distance=D.round(4).tolist()) for name, D in (("shape_jaccard", Dj), ("shape_bray_curtis", Db), ("transfer_net", Dt))}
    # mappings from the current version's cells
    M = json.load(open(MATRIX)).get(f"v{K.METHOD_VERSION}", {}) if os.path.exists(MATRIX) else {}
    cells = {}
    for rec in M.values():
        if rec.get("seed") != 0: continue
        if "A_to_B" in rec: cells[(rec["A"], rec["B"])] = rec["A_to_B"]["mapping"]
        if "B_to_A" in rec: cells[(rec["B"], rec["A"])] = rec["B_to_A"]["mapping"]
    lineage, edges = inheritance(taxa, libs, cells)
    if write_libraries:
        for d in taxa:
            json.dump(libs[d], open(os.path.join(ROOT, "datasets", d, "out", "library_v1.json"), "w"), indent=1)
    out = dict(method_version=K.METHOD_VERSION, taxa=taxa, status=status,
               inventory={d: {k: v for k, v in inv[d].items() if k != "shapes"} | dict(shapes=len(inv[d]["shapes"]["fragment"]), chain_shapes=len(inv[d]["shapes"]["chain"]), return_shapes=len(inv[d]["shapes"]["ret"])) for d in inv},
               returns={d: inv[d]["shapes"]["ret"] for d in inv}, characters=chars, shared=shared, trees=trees, transfer_net=net,
               inheritance=dict(edges=edges, shapes=lineage))
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    json.dump(out, open(OUT_JSON, "w"), indent=1, default=str)
    open(OUT_MD, "w").write(markdown(out, inv, libs))
    log(f"[lineage] {len(chars)} characters over {len(taxa)} taxa; wrote {OUT_JSON} and {OUT_MD}")
    return out


def markdown(out, inv, libs):
    taxa = out["taxa"]; L = []
    short = {"tennessee_eastman": "TEP", "hai": "HAI", "nasa_battery": "battery", "tclab": "TCLab", "building_a": "building A", "building_b": "building B′", "physionet_slp": "PhysioNet"}
    nm = lambda d: short.get(d, d)
    L += [f"# Lineage — the collection step (METHOD 3.13), method v{out['method_version']}", "",
          "Characters are tagged shapes (3.14, 3.15); taxa are the admitted datasets whose libraries carry them: " + ", ".join(nm(d) for d in taxa) + ".",
          "The buildings are synthetic and untagged (3.14) and TCLab is withdrawn; both are inventoried for the record and are not taxa. "
          "A leaf marked provisional is below the admission line and flagged in every view.", ""]
    # 1. returns first
    L += ["## 1. Returns, the characters that matter most", "", "| dataset | returns | distinct return shapes | the strongest return | shape |", "| --- | --- | --- | --- | --- |"]
    for d in taxa:
        rets = [h for h in libs[d].get("chains", []) if h.get("is_return")]
        top = max(rets, key=lambda h: h["cond_lift"]) if rets else None
        L.append(f"| {nm(d)} | {len(rets)} | {len(inv[d]['shapes']['ret'])} | " + (f"`{top['a']} -{top['l1']}-> {top['b']} -{top['l2']}-> {top['c']}` (n {top['count']}, cond. lift {top['cond_lift']:.2f}) | `{top['shape']}` |" if top else "— | — |"))
    L.append("")
    shared_ret = [(k, v["ret"]) for k, v in out["shared"].items() if v["ret"]]
    if shared_ret:
        L += ["Return shapes shared between datasets:", ""]
        for k, v in shared_ret:
            a, b = k.split("|")
            for s in v:
                L.append(f"- `{s}` — {nm(a)} × {out['characters'][s].get(a, 0)}, {nm(b)} × {out['characters'][s].get(b, 0)}")
    else:
        L.append("No return shape is shared between any two taxa.")
    L.append("")
    # place signatures of returns
    L += ["Return place signatures (end → middle → end, from the place prefix):", ""]
    for d in taxa:
        sig = Counter()
        for s, v in inv[d]["shapes"]["ret"].items():
            parts = [p.split(".")[0] for p in s.replace(" [return]", "").split(" -")[0::1] if "·" in p or p.split(".")[0].isupper()]
            ends = [p.split("·")[-1].split(".")[0] for p in s.replace(" [return]", "").split("-> ")]
            ends = [e.split(" ")[0] for e in ends]
            sig[" → ".join(ends)] += v["n"]
        L.append(f"- {nm(d)}: " + "; ".join(f"{k} ({c})" for k, c in sig.most_common(5)))
    L.append("")
    # 2. inventory
    L += ["## 2. Inventory", "", "| dataset | standing | method | fragments (tagged) | fragment shapes | chains | chain shapes | returns | return shapes | library bits |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for d in inv:
        i = out["inventory"][d]
        L.append(f"| {nm(d)} | {out['status'][d]} | v{i['method_version']} | {i['fragments']} ({i['fragments_tagged']}) | {i['shapes']} | {i['chains']} | {i['chain_shapes']} | {i['returns']} | {i['return_shapes']} | {i['library_bits']:.3f} |")
    L.append("")
    # 3. character matrix — same-role shapes (function words of any bounded variable) counted apart from cross-role shapes
    same = lambda sh: "[same role]" in sh
    L += ["## 3. The character matrix (shape × dataset)", "",
          "Same-role shapes (`[same role]`: a variable re-crossing its own thresholds, the function words of any bounded series) are counted apart from cross-role shapes; only a cross-role shape can be a finding about two systems.", "",
          "| pair | fragment shapes shared: cross-role | same-role | chain shapes shared | return shapes shared |", "| --- | --- | --- | --- | --- |"]
    for k, v in out["shared"].items():
        a, b = k.split("|"); cross = [x for x in v["fragment"] if not same(x)]
        L.append(f"| {nm(a)} ↔ {nm(b)} | **{len(cross)}** | {len(v['fragment']) - len(cross)} | {len(v['chain'])} | {len(v['ret'])} |")
    L.append("")
    allsh = [s for s, c in out["characters"].items() if all(d in c for d in taxa)]
    L += [f"Shapes present in every taxon: **{len(allsh)}** ({sum(1 for x in allsh if not same(x))} cross-role, {sum(1 for x in allsh if same(x))} same-role).", ""]
    if allsh:
        L += ["| shape | " + " | ".join(nm(d) for d in taxa) + " |", "| --- |" + " --- |" * len(taxa)]
        for s in sorted(allsh, key=lambda s: -sum(out["characters"][s].values()))[:40]:
            L.append(f"| `{s}` | " + " | ".join(str(out["characters"][s].get(d, 0)) for d in taxa) + " |")
        L.append("")
    for k, v in out["shared"].items():
        a, b = k.split("|"); cross = [x for x in v["fragment"] if not same(x)]
        if cross and len(cross) <= 30:
            L += [f"Cross-role fragment shapes shared by {nm(a)} and {nm(b)} ({len(cross)}):", ""] + [f"- `{s}` ({nm(a)} × {out['characters'][s].get(a, 0)}, {nm(b)} × {out['characters'][s].get(b, 0)})" for s in cross] + [""]
    # 4. trees
    L += ["## 4. Similarity trees", ""]
    for name, t in out["trees"].items():
        L += [f"**{name}** — `{t['newick']}`", "", "| | " + " | ".join(nm(d) for d in taxa) + " |", "| --- |" + " --- |" * len(taxa)]
        for i, d in enumerate(taxa): L.append(f"| {nm(d)} | " + " | ".join(f"{x:.3f}" for x in t["distance"][i]) + " |")
        L.append("")
    L += ["Shape distances: Jaccard over fragment shapes (1 − shared / union), Bray–Curtis over shape counts. Transfer distance: 1 / (1 + symmetrised net cell) of the current version; a pair without a cell is at 1.", ""]
    # 5. inheritance
    L += ["## 5. Inheritance graph", "",
          "Inheritance is directed by **running order**: a shape belongs to the dataset that validated it first and is inherited by every later dataset that validates it again, so a zero in the reverse direction is the order, not the physics; the symmetric view is the character matrix above. Confirmation through a mapping is directed by the transfer cell and runs both ways.", "",
          "| from → to | shapes recurred (inherited) | of them returns | fragments tested through the mapping | confirmed | failed |", "| --- | --- | --- | --- | --- | --- |"]
    for k, e in out["inheritance"]["edges"].items():
        a, b = k.split("->"); L.append(f"| {nm(a)} → {nm(b)} | {e['shapes_recurred']} | {e['returns_recurred']} | {e['fragments_tested']} | {e['fragments_confirmed']} | {e['fragments_failed']} |")
    L.append("")
    sh = out["inheritance"]["shapes"]
    first = Counter(v["first"] for v in sh.values()); L.append("Shapes by the dataset that first validated them (running order): " + ", ".join(f"{nm(d)} {c}" for d, c in first.items()) + ".")
    inh = [s for s, v in sh.items() if v["recurred"]]
    L += ["", f"Inherited shapes (validated again in a later dataset): **{len(inh)}**, of them returns {sum(1 for s in inh if sh[s]['kind'] == 'return')}, chains {sum(1 for s in inh if sh[s]['kind'] == 'chain')}.", ""]
    conf = [s for s, v in sh.items() if v["confirmed_through_mapping"]]; fail = [s for s, v in sh.items() if v["failed"]]
    L += [f"Shapes confirmed through a mapping in another dataset: {len(conf)}; tested and failed: {len(fail)}.", ""]
    rets = [s for s, v in sh.items() if v["kind"] == "return"]
    L += ["Lineage of the return shapes present in more than one dataset, or tested through a mapping:", ""]
    rows = [s for s in rets if sh[s]["recurred"] or sh[s]["confirmed_through_mapping"] or sh[s]["failed"]]
    for s in rows[:30]:
        v = sh[s]; L.append(f"- `{s}`: first {nm(v['first'])}; recurred {', '.join(nm(x) for x in v['recurred']) or '—'}; confirmed via mapping {', '.join(nm(x) for x in v['confirmed_through_mapping']) or '—'}; failed {', '.join(nm(x) for x in v['failed']) or '—'}")
    if not rows: L.append("- none yet: returns do not cross datasets under the mappings of this version.")
    L.append("")
    return "\n".join(L)

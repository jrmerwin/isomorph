"""
`isomorph brief datasets/<name>` — a view, not a rule (RUNBOOK v9 item 4): the structural map of one system for a
machine reader. One JSON and one markdown per dataset, assembled from the card, the library, the sidecar, the
matrix and the lineage; nothing here is computed afresh, and nothing here is a rule.
"""
import json, os
from collections import Counter
from .. import constants as K
from ..choose.pos import full_tag

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EPISTEMICS = ("Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is "
              "informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial "
              "alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of "
              "the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).")


def build_brief(dataset_dir, log=print):
    d = os.path.normpath(dataset_dir); name = os.path.basename(d)
    card = json.load(open(os.path.join(d, "out", "benchmark_v1.json"))); lib = json.load(open(os.path.join(d, "out", "library_v1.json")))
    side = json.load(open(os.path.join(d, "sidecar.json"))); tags = side.get("tags") or {}
    key = json.load(open(os.path.join(d, "answer_key.json"))) if os.path.exists(os.path.join(d, "answer_key.json")) else None
    matrix = json.load(open(os.path.join(ROOT, "collection", "matrix.json"))).get(f"v{K.METHOD_VERSION}", {}) if os.path.exists(os.path.join(ROOT, "collection", "matrix.json")) else {}
    lineage = json.load(open(os.path.join(ROOT, "collection", "lineage.json"))) if os.path.exists(os.path.join(ROOT, "collection", "lineage.json")) else {}
    g = card["gain"]; sc = card["scale"]; ad = card.get("admission", {})
    identity = dict(dataset=name, kind=card["identity"]["kind"], method_version=card["method_version"], card_rules_version=K.CARD_RULES_VERSION,
                    entity=card["identity"].get("entity_key"), n_entities=sc["n_entities"], horizon_minutes=sc["lag_edges"][-1], lag_edges_minutes=sc["lag_edges"],
                    period_slow=sc.get("period_slow"), period_fast=sc.get("period_fast"), admission=ad,
                    claim=dict(claim=g["claim"], library_bits=card["headline_bits"]["logistic library"]["all"], triviality_bits=card["headline_bits"]["logistic triviality library"]["all"],
                               best_baseline_bits=g["best_baseline_bits"], gain_over_triviality=g["over_triviality"], gain_over_best_baseline=g["over_best_baseline"]),
                    events=sc["events"], types=sc["types"], signal_floor=sc["signal_floor"], standing=lineage.get("status", {}).get(name))
    roles = sorted(set(t.split(":")[0] for f in lib["fragments"] for t in (f["prior"], f["target"])) | set(tags))
    vocabulary = {r: dict(full_tag=full_tag(tags, r), dimension=(tags.get(r) or {}).get("quantity"), loop_tags=(tags.get(r) or {}).get("loop_tags"),
                          scheme=(side.get("symbolization") if isinstance(side.get("symbolization"), dict) else {}).get("choice", {}).get(r)) for r in roles}
    couplings = [dict(prior=f["prior"], lag=f["lag"], target=f["target"], lift=round(f["lift"], 3), lift_conf=round(f["lift_conf"], 3), count=f["count"],
                      binding_evidence=f.get("binding_evidence"), shape=f.get("shape"), confirmed_in=f.get("confirmed_in", []), failed_in=f.get("failed_in", []))
                 for f in lib["fragments"]]
    used = set(tuple(c) if isinstance(c, list) else c for c in [])
    loops = [dict(a=h["a"], l1=h["l1"], b=h["b"], l2=h["l2"], c=h["c"], count=h["count"], cond_lift=round(h["cond_lift"], 3), shape=h.get("shape"),
                  verdict_timing=h.get("verdict"), g1=h.get("g1"), g2=h.get("g2"), verdict_determinism=h.get("verdict_determinism"), p1=h.get("p1"), p2=h.get("p2"), used=h.get("used"))
             for h in lib.get("chains", []) if h.get("is_return")]
    chains = [dict(a=h["a"], l1=h["l1"], b=h["b"], l2=h["l2"], c=h["c"], count=h["count"], cond_lift=round(h["cond_lift"], 3), shape=h.get("shape"), used=h.get("used"))
              for h in lib.get("chains", []) if not h.get("is_return")]
    # absences
    targets = set(f["target"].split(":")[0] for f in lib["fragments"]); priors = set(f["prior"].split(":")[0] for f in lib["fragments"])
    silent = [r for r, s_ in (side.get("symbolization") if isinstance(side.get("symbolization"), dict) else {}).get("choice", {}).items() if s_ is None]
    never_target = sorted(r for r in roles if r not in targets and r not in silent)
    keyed_missing = []
    if key and "mechanisms" in key and key.get("match") == "role_prefix":
        found = set((f["prior"].split(":")[0], f["target"].split(":")[0]) for f in lib["fragments"])
        keyed_missing = [dict(cause=m["cause"], effect=m["effect"], note=m.get("note")) for m in key["mechanisms"] if (m["cause"], m["effect"]) not in found]
    absences = dict(silent_roles=silent, roles_never_a_target=never_target, keyed_pairs_not_found=keyed_missing, signal_floor=sc["signal_floor"],
                    note="absence is informative only for pairs whose support would exceed the signal floor")
    regimes = side.get("regimes") or side.get("cycles") or side.get("files")
    # the matrix row
    cells_in, cells_out = [], []
    for rec in matrix.values():
        if rec.get("diagonal"):
            if rec["B"] == name: cells_in.append(dict(source=rec["stretch"] + " (diagonal)", **_cell(rec["self"])))
            continue
        for dkey, (s_, t_) in (("A_to_B", (rec["A"], rec["B"])), ("B_to_A", (rec["B"], rec["A"]))):
            c = rec.get(dkey)
            if not c: continue
            if t_ == name: cells_in.append(dict(source=s_, **_cell(c)))
            if s_ == name: cells_out.append(dict(receiver=t_, **_cell(c)))
    nearest = {}
    for tname, t in (lineage.get("trees") or {}).items():
        taxa = lineage.get("taxa", [])
        if name in taxa:
            i = taxa.index(name); row = t["distance"][i]
            nearest[tname] = sorted(((taxa[j], round(row[j], 3)) for j in range(len(taxa)) if j != i), key=lambda x: x[1])[:3]
    brief = dict(epistemics=EPISTEMICS, identity=identity, vocabulary=vocabulary, couplings=couplings, loops=loops, chains=chains, absences=absences,
                 regimes=regimes, matrix_row=dict(cells_in=cells_in, cells_out=cells_out, nearest_taxa=nearest))
    os.makedirs(os.path.join(ROOT, "collection"), exist_ok=True)
    json.dump(brief, open(os.path.join(ROOT, "collection", f"brief_{name}.json"), "w"), indent=1, default=str)
    open(os.path.join(ROOT, "docs", f"BRIEF_{name}.md"), "w").write(markdown(brief))
    log(f"[brief] {name}: {len(couplings)} couplings, {len(loops)} loops, {len(cells_in)} cells in, {len(cells_out)} cells out -> collection/brief_{name}.json, docs/BRIEF_{name}.md")
    return brief


def _cell(c):
    return dict(structure_bit_horizons=c.get("cell_structure_bit_horizons"), net_bit_horizons=c.get("cell_net_bit_horizons"), raw_bit_horizons=c.get("cell_bit_horizons"),
                marginal_bit_horizons=c.get("cell_marginal_bit_horizons"), derangement_bit_horizons=c.get("cell_control_bit_horizons"), larger_control=c.get("larger_control"),
                share_of_ceiling=c.get("share_of_ceiling"), types_mapped=f"{c.get('types_mapped')}/{c.get('types_total')}", short=c.get("short"), uncontrolled=c.get("uncontrolled"), damage=c.get("damage"))


def markdown(b):
    f = lambda v, n=2: "—" if v is None else (f"{v:.{n}f}" if isinstance(v, (int, float)) else str(v))
    i = b["identity"]; L = [f"# Brief — {i['dataset']} (method v{i['method_version']}, a view)", "", f"*{b['epistemics']}*", "",
         "## Identity", "", f"- kind: {i['kind']}; standing: {i.get('standing')}", f"- entity: {i['entity']} ({i['n_entities']} units); H = {f(i['horizon_minutes'], 1)} min; lag edges {[round(x, 2) for x in i['lag_edges_minutes']]} min",
         f"- periods: slow {f(i['period_slow'], 1)}, fast {f(i['period_fast'], 2)}; admission: {i['admission']}",
         f"- claim: **{i['claim']['claim']}** — library {f(i['claim']['library_bits'], 3)} bits, triviality {f(i['claim']['triviality_bits'], 3)}, best baseline {f(i['claim']['best_baseline_bits'], 3)}; gain over triviality {f(i['claim']['gain_over_triviality'], 3)}",
         f"- events {i['events']}, types {i['types']}, signal floor {i['signal_floor']}", "",
         "## Vocabulary", "", "| role | full tag | quantity | scheme | loop tags (timing / determinism) |", "| --- | --- | --- | --- | --- |"]
    for r, v in sorted(b["vocabulary"].items()):
        lt = v.get("loop_tags") or {}
        L.append(f"| {r} | {v.get('full_tag') or '—'} | {v.get('dimension') or '—'} | {v.get('scheme') or 'silent'} | {(lt.get('timing') or {}).get('tag') or '—'} / {(lt.get('determinism') or {}).get('tag') or '—'} |")
    L += ["", "## Couplings (validated fragments)", "", "| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in sorted(b["couplings"], key=lambda c: -c["lift"]):
        L.append(f"| {c['prior']} | {c['lag']} | {c['target']} | {c['lift']} | {c['lift_conf']} | {c['count']} | {c['binding_evidence']} | `{c['shape']}` | {', '.join(c['confirmed_in']) or '—'} | {', '.join(c['failed_in']) or '—'} |")
    L += ["", "## Loops (returns; verdicts recorded, not promoted)", "", "| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for h in sorted(b["loops"], key=lambda h: -h["cond_lift"]):
        L.append(f"| {h['a']} | {h['l1']} | {h['b']} | {h['l2']} | {h['c']} | {h['count']} | {h['cond_lift']} | {h['verdict_timing']} ({f(h['g1'], 1)} / {f(h['g2'], 1)}) | {h['verdict_determinism']} ({f(h['p1'], 3)} / {f(h['p2'], 3)}) | {h['used']} |")
    L += ["", f"Chains (non-return): {len(b['chains'])}.", "", "## Absences", "", f"- silent roles: {b['absences']['silent_roles'] or 'none'}", f"- roles never a target: {b['absences']['roles_never_a_target'] or 'none'}",
          "- keyed pairs not found: " + ("; ".join(f"{m['cause']} → {m['effect']}" for m in b['absences']['keyed_pairs_not_found']) or "none"), f"- signal floor: {b['absences']['signal_floor']} ({b['absences']['note']})", ""]
    L += ["## Regimes", "", (f"{len(b['regimes'])} annotations" if isinstance(b["regimes"], list) else (f"{b['regimes']}" if b["regimes"] else "none recorded")), ""]
    L += ["## Matrix row", "", "Cells in (this system as receiver):", "", "| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in b["matrix_row"]["cells_in"]:
        fl = ", ".join(x for x in (("short" if c["short"] else ""), ("uncontrolled" if c["uncontrolled"] else ""), ("damage" if c["damage"] else "")) if x)
        L.append(f"| {c['source']} | {f(c['structure_bit_horizons'])} | {f(c['net_bit_horizons'])} | {f(c['raw_bit_horizons'])} | {f(c['marginal_bit_horizons'])} | {f(c['derangement_bit_horizons'])} | {c['larger_control'] or '—'} | {f(c['share_of_ceiling'])} | {c['types_mapped']} | {fl} |")
    L += ["", "Cells out (this system as source):", "", "| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in b["matrix_row"]["cells_out"]:
        fl = ", ".join(x for x in (("short" if c["short"] else ""), ("uncontrolled" if c["uncontrolled"] else ""), ("damage" if c["damage"] else "")) if x)
        L.append(f"| {c['receiver']} | {f(c['structure_bit_horizons'])} | {f(c['net_bit_horizons'])} | {f(c['raw_bit_horizons'])} | {f(c['marginal_bit_horizons'])} | {f(c['derangement_bit_horizons'])} | {c['larger_control'] or '—'} | {f(c['share_of_ceiling'])} | {c['types_mapped']} | {fl} |")
    L += ["", "Nearest taxa by distance: " + "; ".join(f"{k}: " + ", ".join(f"{a} {d}" for a, d in v) for k, v in b["matrix_row"]["nearest_taxa"].items()), ""]
    return "\n".join(L)

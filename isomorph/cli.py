"""isomorph command line.

  isomorph run <dataset_dir> [--profile v1|legacy] [--seed 0]
      one pass over one dataset -> out/benchmark_<profile>.json, out/library_<profile>.json, out/card_<profile>.md
  isomorph calibrate
      run datasets/building_a and datasets/building_b under both profiles and compare to collection/calibration_reference.json
  isomorph transfer <dataset_A> <dataset_B> [--profile v1] [--seed 0]
      both pipelines, structural alignment, the ordered cells A->B and B->A -> collection/matrix.json, docs card
"""
import argparse, json, os, sys
from . import constants as K
from .pipeline import run, card_markdown


def main(argv=None):
    p = argparse.ArgumentParser(prog="isomorph")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("dataset_dir"); r.add_argument("--profile", default="v1"); r.add_argument("--seed", type=int, default=0)
    sub.add_parser("calibrate")
    t = sub.add_parser("transfer"); t.add_argument("dataset_a"); t.add_argument("dataset_b"); t.add_argument("--profile", default="v1"); t.add_argument("--seed", type=int, default=0); t.add_argument("--direction", default="both", choices=["both", "ab", "ba"])
    a = p.parse_args(argv)
    if a.cmd == "run":
        card, _ = run(a.dataset_dir, a.profile, a.seed)
        md = card_markdown(card)
        open(os.path.join(a.dataset_dir, "out", f"card_{a.profile}.md"), "w").write(md)
        print(md)
    elif a.cmd == "calibrate":
        from .collect.calibrate import calibrate
        sys.exit(0 if calibrate() else 1)
    elif a.cmd == "transfer":
        from .collect.matrix import transfer_pair, cell_markdown
        rec = transfer_pair(a.dataset_a, a.dataset_b, a.profile, a.seed, direction=a.direction)
        md = cell_markdown(rec)
        os.makedirs("collection", exist_ok=True)
        open(os.path.join("collection", f"transfer_{rec['A']}_{rec['B']}_{a.profile}.md"), "w").write(md)
        print(md)


if __name__ == "__main__":
    main()

"""isomorph command line.

  isomorph run <dataset_dir> [--profile v1|legacy] [--seed 0]
      one pass over one dataset -> out/benchmark_<profile>.json, out/library_<profile>.json, out/card_<profile>.md
  isomorph calibrate
      run datasets/building_a and datasets/building_b under both profiles and compare to collection/calibration_reference.json
"""
import argparse, json, os, sys
from . import constants as K
from .pipeline import run, card_markdown


def main(argv=None):
    p = argparse.ArgumentParser(prog="isomorph")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("dataset_dir"); r.add_argument("--profile", default="v1"); r.add_argument("--seed", type=int, default=0)
    sub.add_parser("calibrate")
    a = p.parse_args(argv)
    if a.cmd == "run":
        card, _ = run(a.dataset_dir, a.profile, a.seed)
        md = card_markdown(card)
        open(os.path.join(a.dataset_dir, "out", f"card_{a.profile}.md"), "w").write(md)
        print(md)
    elif a.cmd == "calibrate":
        from .collect.calibrate import calibrate
        sys.exit(0 if calibrate() else 1)


if __name__ == "__main__":
    main()

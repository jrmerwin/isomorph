import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from isomorph.canon.ingest import read_dataset
from isomorph.canon.validate import validate
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_buildings_validate():
    for d in ("building_a", "building_b"):
        ev, obs, gaps, side, key = read_dataset(os.path.join(ROOT, "datasets", d))
        assert validate(ev, obs, gaps, side)

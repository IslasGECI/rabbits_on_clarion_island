from rabbit_clarion import calculate_surface_densities_by_group

import pandas as pd
import json
import numpy as np


f = open("/workdir/tests/data/aves_density.json")

expected = json.load(f)
expected = {
    k: [np.nan if elemento == "" else elemento for elemento in v] for k, v in expected.items()
}


def test_calculate_surface_densities_by_group():
    data_transects_path = "tests/data/transectos_fauna_nativa_isla_clarion_oct_2022.csv"
    data_transects = pd.read_csv(data_transects_path)
    group = "Ave"
    obtained = calculate_surface_densities_by_group(group, data_transects)
    assert isinstance(obtained, dict)
    assert obtained == expected

from rabbit_clarion import calculate_surface_densities_by_group

import pandas as pd
import json
import numpy as np


def read_expected_density(path):
    f = open(path)
    expected = json.load(f)
    return {
        k: [np.nan if elemento == "" else elemento for elemento in v] for k, v in expected.items()
    }


def test_calculate_surface_densities_by_group():
    data_transects_path = "tests/data/transectos_fauna_nativa_isla_clarion_oct_2022.csv"
    data_transects = pd.read_csv(data_transects_path)

    group = "Reptil"
    obtained = calculate_surface_densities_by_group(group, data_transects)
    assert isinstance(obtained, dict)
    expected = read_expected_density("/workdir/tests/data/reptil_density.json")
    assert obtained == expected

    group = "Ave"
    obtained = calculate_surface_densities_by_group(group, data_transects)
    assert isinstance(obtained, dict)
    expected = read_expected_density("/workdir/tests/data/aves_density.json")
    assert obtained == expected

    group = "Tecolote"
    obtained = calculate_surface_densities_by_group(group, data_transects)
    assert isinstance(obtained, dict)
    expected = read_expected_density("/workdir/tests/data/tecolote_density.json")
    assert obtained == expected

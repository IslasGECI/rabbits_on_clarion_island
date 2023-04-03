from rabbit_clarion import (
    calculate_surface_densities_by_group,
    check_array,
    Native_Group_Parameters,
)

import pandas as pd
import json
import numpy as np


def read_expected_density(path):
    f = open(path)
    expected = json.load(f)
    return {
        k: [np.nan if elemento == "" else elemento for elemento in v] for k, v in expected.items()
    }


data_transects_path = "tests/data/transectos_fauna_nativa_isla_clarion_oct_2022.csv"
data_transects = pd.read_csv(data_transects_path)


def test_calculate_surface_densities_by_group():
    group = "Reptil"
    obtained = calculate_surface_densities_by_group(group, data_transects)
    assert isinstance(obtained, dict)
    expected = read_expected_density("/workdir/tests/data/reptil_density.json")
    np.testing.assert_equal(obtained, expected)

    group = "Ave"
    obtained = calculate_surface_densities_by_group(group, data_transects)
    assert isinstance(obtained, dict)
    expected = read_expected_density("/workdir/tests/data/aves_density.json")
    np.testing.assert_equal(obtained, expected)

    group = "Tecolote"
    transect_lenght = 500
    obtained = calculate_surface_densities_by_group(group, data_transects, transect_lenght)
    assert isinstance(obtained, dict)
    expected = read_expected_density("/workdir/tests/data/tecolote_density.json")
    np.testing.assert_equal(obtained, expected)


def test_Native_Group_Parameters():
    grupo = "Ave"
    bird_parameters = Native_Group_Parameters(grupo, data_transects)
    default_length = 300
    assert bird_parameters.length == default_length
    assert bird_parameters.group == grupo


def test_check_array():
    empty_array = np.array([])
    obtained = check_array(empty_array)
    expected = "NA"
    assert obtained == expected

    array = np.array([1, 2, 3])
    obtained = check_array(array)
    expected = 1
    assert obtained == expected

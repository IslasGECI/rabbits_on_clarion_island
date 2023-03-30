from rabbit_clarion import calculate_surface_densities_by_group

import pandas as pd


def test_calculate_surface_densities_by_group():
    data_transects_path = "tests/data/transectos_fauna_nativa_isla_clarion_oct_2022.csv"
    data_transects = pd.read_csv(data_transects_path)
    group = "Ave"
    obtained = calculate_surface_densities_by_group(group, data_transects)
    assert isinstance(obtained, dict)
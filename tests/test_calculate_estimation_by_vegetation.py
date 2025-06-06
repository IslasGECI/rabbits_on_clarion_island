from rabbit_clarion.calculate_estimation_by_vegetation import separate_vegetations_enums

import pandas as pd


def test_separate_vegetations_enums():
    transect_densities_df = pd.read_csv("tests/data/df_to_test_separate_vegetations_enums.csv")
    obtained = separate_vegetations_enums(transect_densities_df)
    expected_rows = 6
    assert len(obtained) == expected_rows

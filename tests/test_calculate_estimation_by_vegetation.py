from rabbit_clarion.calculate_estimation_by_vegetation import separate_vegetations_enums

import pandas as pd


def test_separate_vegetations_enums():
    transect_densities_df = pd.read_csv("tests/data/df_to_test_separate_vegetations_enums.csv")
    obtained = separate_vegetations_enums(transect_densities_df)
    expected_shape = (6, 5)
    assert obtained.shape == expected_shape
    same_columns = transect_densities_df.columns[:-1]
    print(same_columns)
    expected = transect_densities_df.loc[0, same_columns]
    assert (obtained.loc[1, same_columns] == expected).all()

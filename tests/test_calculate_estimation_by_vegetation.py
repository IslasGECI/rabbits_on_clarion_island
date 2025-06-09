from rabbit_clarion.calculate_estimation_by_vegetation import (
    separate_vegetations_enums,
    get_data_densities,
)

import pandas as pd


def test_separate_vegetations_enums():
    transect_densities_df = pd.read_csv("tests/data/df_to_test_separate_vegetations_enums.csv")
    obtained = separate_vegetations_enums(transect_densities_df)
    expected_shape = (7, 5)
    assert obtained.shape == expected_shape
    same_columns = transect_densities_df.columns[:-1]
    expected = transect_densities_df.loc[0, same_columns]
    assert (obtained.loc[1, same_columns] == expected).all()


def test_get_data_densities():
    data_path = "tests/data/rabbit_densities_for_tests.csv"
    data_areas_path = "tests/data/vegetal_types_for_tests.csv"
    obtained = get_data_densities(data_path, data_areas_path)
    obtained.to_csv("prueba.csv", index=False)
    obtained_vegetation_types = set(obtained["Tipo_vegetacion"])
    data_areas = pd.read_csv(data_areas_path)
    expected_vegetation_types = set(data_areas["Tipo_de_vegetacion"])
    assert obtained_vegetation_types == expected_vegetation_types
    expected_species = "Oryctolagus cuniculus"
    assert obtained.Especie.unique() == expected_species

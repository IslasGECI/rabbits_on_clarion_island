import pandas as pd


def separate_vegetations_enums(df):
    df_without_na = df.dropna(subset=["Tipo_vegetacion"])
    df_with_zeros = df_without_na.reset_index(drop=True).fillna(0)
    df_with_zeros["Tipo_vegetacion"] = df_with_zeros["Tipo_vegetacion"].str.split("/")
    return df_with_zeros.explode("Tipo_vegetacion").reset_index(drop=True)


def get_data_densities(data_path, data_areas_path):
    data_densities = pd.read_csv(data_path)
    data_areas = pd.read_csv(data_areas_path)
    data_densities = add_missing_vegetal_types(data_densities, data_areas)
    return data_densities


def add_missing_vegetal_types(df, df_areas):
    vegetal_types = df.Tipo_vegetacion.unique()
    all_vegetal_types = df_areas.Tipo_de_vegetacion.unique()
    missing_types = list(set(all_vegetal_types) - set(vegetal_types))
    columns = df.columns
    species = df.at[0, "Especie"]
    data_copy = pd.DataFrame(
        data=[
            [
                0,
                0,
                species,
                0,
                missing_types,
                0,
            ]
        ],
        columns=columns,
    )
    data_copy = data_copy.explode("Tipo_vegetacion").reset_index(drop=True)
    return pd.concat([df, data_copy]).reset_index(drop=True)

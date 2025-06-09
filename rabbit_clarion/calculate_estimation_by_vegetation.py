import pandas as pd


def separate_vegetations_enums(df):
    df.dropna(subset=["Tipo_vegetacion"], inplace=True)
    df.reset_index(drop=True).fillna(0, inplace=True)
    df["Tipo_vegetacion"] = df["Tipo_vegetacion"].str.split("/")
    return df.explode("Tipo_vegetacion").reset_index(drop=True)


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
    data_copy = pd.DataFrame(
        data=[
            [
                "Conejos_02",
                2.8787878787878785,
                "Oryctolagus cuniculus",
                23.0,
                missing_types,
                2810.793899160166,
            ]
        ],
        columns=columns,
    )
    print(data_copy)
    data_copy = data_copy.explode("Tipo_vegetacion").reset_index(drop=True)
    print(data_copy)

    return pd.concat([df, data_copy])

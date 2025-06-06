import pandas as pd


def separate_vegetations_enums(df):
    df = df.dropna(subset=["Tipo_vegetacion"])
    df = df.reset_index(drop=True).fillna(0)
    new_df = pd.DataFrame(columns=df.columns.values)
    for i in range(len(df)):
        data_copy = df.loc[i].copy(deep=True)
        if "/" in data_copy["Tipo_vegetacion"]:
            vegetal_types = data_copy["Tipo_vegetacion"].split("/")
            data_copy.Tipo_vegetacion = vegetal_types[0]
            new_df = new_df._append(data_copy)
            data_copy.Tipo_vegetacion = vegetal_types[1]
        new_df = new_df._append(data_copy)
    return new_df.reset_index(drop=True)

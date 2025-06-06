import pandas as pd


def separate_vegetations_enums(df):
    df = df.dropna(subset=["Tipo_vegetacion"])
    df = df.reset_index(drop=True).fillna(0)
    new_df = pd.DataFrame(columns=df.columns.values)
    for i in range(len(df)):
        data_copy = df.loc[[i]].copy(deep=True)
        if "/" in data_copy.iloc[0]["Tipo_vegetacion"]:
            vegetal_types = data_copy.iloc[0]["Tipo_vegetacion"].split("/")
            for veg in vegetal_types:
                temp = data_copy.copy(deep=True)
                temp.iloc[0, temp.columns.get_loc("Tipo_vegetacion")] = veg
                new_df = pd.concat([new_df, temp], ignore_index=True)
        else:
            new_df = pd.concat([new_df, data_copy], ignore_index=True)
    return new_df.reset_index(drop=True)

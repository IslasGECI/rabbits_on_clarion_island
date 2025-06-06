import pandas as pd


def separate_vegetations_enums(df):
    df = df.dropna(subset=["Tipo_vegetacion"])
    df = df.reset_index(drop=True).fillna(0)
    new_df = pd.DataFrame(columns=df.columns.values)
    for row_number in range(len(df)):
        new_df = split_vegetation_type(df, new_df, row_number)
    return new_df.reset_index(drop=True)


def split_vegetation_type(df, new_df, i):
    data_copy = df.loc[[i]].copy(deep=True)
    vegetation_type_string = data_copy.at[i, "Tipo_vegetacion"]
    vegetal_types = vegetation_type_string.split("/")
    for veg in vegetal_types:
        data_copy.at[i, "Tipo_vegetacion"] = veg
        new_df = pd.concat([new_df, data_copy], ignore_index=True)
    return new_df

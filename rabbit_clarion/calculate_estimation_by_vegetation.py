import pandas as pd


def separate_vegetations_enums(df):
    df.dropna(subset=["Tipo_vegetacion"], inplace=True)
    df.reset_index(drop=True).fillna(0, inplace=True)
    df["Tipo_vegetacion"] = df["Tipo_vegetacion"].str.split("/")
    return df.explode("Tipo_vegetacion").reset_index(drop=True)

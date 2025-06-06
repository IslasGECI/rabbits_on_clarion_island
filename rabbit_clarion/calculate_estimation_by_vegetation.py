import pandas as pd


def separate_vegetations_enums(df):
    df = df.dropna(subset=["Tipo_vegetacion"])
    df = df.reset_index(drop=True).fillna(0)
    df["Tipo_vegetacion"] = df["Tipo_vegetacion"].str.split("/")
    df = df.explode("Tipo_vegetacion").reset_index(drop=True)
    return df

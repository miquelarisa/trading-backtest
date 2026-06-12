import pandas as pd

def generate_signals(df):

    df = df.copy()

    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna(subset=["Close"])

    df["ma_fast"] = df["Close"].rolling(20).mean()
    df["ma_slow"] = df["Close"].rolling(50).mean()

    entries = (df["ma_fast"] > df["ma_slow"]).fillna(False)
    exits = (df["ma_fast"] < df["ma_slow"]).fillna(False)

    return entries, exits
import pandas as pd
import vectorbt as vbt

from strategy import generate_signals

df = pd.read_csv(
    "../data/spy.csv",
    index_col=0,
    parse_dates=True
)

entries, exits = generate_signals(df)

portfolio = vbt.Portfolio.from_signals(
    close=df["Close"],
    entries=entries,
    exits=exits,
    fees=0.001
)

print(portfolio.stats())

portfolio.plot().show()
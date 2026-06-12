import pandas as pd
import vectorbt as vbt

from strategy import generate_signals

df = pd.read_csv(
    "../data/spy.csv",
    index_col=0,
    parse_dates=True,
    date_format="%Y-%m-%d"
)

df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df = df.dropna(subset=["Close"])

entries, exits = generate_signals(df)

portfolio = vbt.Portfolio.from_signals(
    close=df["Close"],
    entries=entries,
    exits=exits,
    fees=0.001,
    freq="1D"
)

import os

RESULTS_DIR = "../results"
os.makedirs(RESULTS_DIR, exist_ok=True)

stats = portfolio.stats()

summary = (
    "\n========== RESULTADOS DEL BACKTEST ==========\n"
    f"Período:                {stats['Start']} → {stats['End']}\n"
    f"Retorno total:          {stats['Total Return [%]']:.2f}%\n"
    f"Retorno benchmark:      {stats['Benchmark Return [%]']:.2f}%\n"
    f"Sharpe Ratio:           {stats['Sharpe Ratio']:.2f}\n"
    f"Sortino Ratio:          {stats['Sortino Ratio']:.2f}\n"
    f"Max Drawdown:           {stats['Max Drawdown [%]']:.2f}%\n"
    f"Win Rate:               {stats['Win Rate [%]']:.2f}%\n"
    f"Profit Factor:          {stats['Profit Factor']:.2f}\n"
    f"Total operaciones:      {int(stats['Total Closed Trades'])}\n"
    f"Comisiones pagadas:     ${stats['Total Fees Paid']:.2f}\n"
    "=============================================\n"
)

print(summary)

stats_path = os.path.join(RESULTS_DIR, "stats.txt")
with open(stats_path, "w", encoding="utf-8") as f:
    f.write(summary)
print(f"Stats guardadas en: {stats_path}")

vbt.settings.plotting["use_widgets"] = False
plot_path = os.path.join(RESULTS_DIR, "backtest_plot.html")
portfolio.plot().write_html(plot_path)
print(f"Gráfico guardado en: {plot_path}")
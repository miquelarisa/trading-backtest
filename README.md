# Trading Backtesting Framework

A Python-based framework for building, testing, and evaluating systematic trading strategies on historical market data. Designed as an educational environment for quantitative finance experimentation.

---

## Table of Contents

- [Overview](#overview)
- [Strategy](#strategy)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Performance Metrics](#performance-metrics)
- [Roadmap](#roadmap)
- [Disclaimer](#disclaimer)

---

## Overview

This project provides a modular pipeline to:

- Download historical OHLCV data from Yahoo Finance
- Generate entry/exit signals based on technical indicators
- Run vectorized backtests with realistic fee modeling
- Evaluate and visualize strategy performance

The initial focus is on a **Moving Average Crossover** trend-following strategy applied to SPY (S&P 500 ETF).

---

## Strategy

### Moving Average Crossover

| Parameter | Value |
|-----------|-------|
| Asset | SPY (S&P 500 ETF) |
| Fast MA | 20 periods |
| Slow MA | 50 periods |
| Fees | 0.1% per trade |
| Data range | 2014-01-01 to 2025-01-01 |

**Rules:**
- **Buy** when the 20-period MA crosses **above** the 50-period MA
- **Sell** when the 20-period MA crosses **below** the 50-period MA

Performance is benchmarked against a simple **Buy & Hold** position on the same asset.

---

## Project Structure

```
trading-backtest/
│
├── data/                   # Historical market data (auto-generated)
│   └── spy.csv
│
├── notebooks/
│   └── exploration.ipynb   # Analysis and visualization
│
├── results/                # Auto-generated outputs
│   ├── stats.txt           # Plain-text performance summary
│   └── backtest_plot.html  # Interactive Plotly chart
│
├── src/
│   ├── download_data.py    # Fetches data from Yahoo Finance via yfinance
│   ├── strategy.py         # Signal generation (MA crossover logic)
│   ├── backtest.py         # Portfolio simulation and result export (vectorbt)
│   └── metrics.py          # Custom performance metrics (in progress)
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repo-url>
cd trading-backtest
```

### 2. Create and activate a virtual environment

```bash
# Create
python -m venv .venv

# Activate — Windows
.venv\Scripts\activate

# Activate — Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**Key dependencies:** `pandas`, `numpy`, `yfinance`, `vectorbt`, `plotly`, `streamlit`, `jupyter`

---

## Usage

### Step 1 — Download historical data

```bash
python src/download_data.py
```

Downloads SPY data from 2014 to 2025 and saves it to `data/spy.csv`.

### Step 2 — Run the backtest

```bash
cd src
python backtest.py
```

Prints a stats summary to the console and saves two files:
- `results/stats.txt` — key performance metrics in plain text
- `results/backtest_plot.html` — interactive Plotly chart (open in any browser)

### Step 3 — Explore in Jupyter

```bash
jupyter notebook notebooks/exploration.ipynb
```

---

## Performance Metrics

The framework reports the following metrics via `vectorbt`:

| Metric | Description |
|--------|-------------|
| Total Return | Overall % gain/loss vs. Buy & Hold benchmark |
| Sharpe Ratio | Risk-adjusted return (annualized) |
| Sortino Ratio | Downside-risk-adjusted return |
| Max Drawdown | Largest peak-to-trough decline |
| Win Rate | % of closed trades that were profitable |
| Profit Factor | Gross profit / gross loss |
| Total Trades | Total number of closed positions |
| Fees Paid | Total commissions paid in $ |

---

## Latest Results

Backtest run over **2014-01-02 → 2024-12-31** (SPY, MA 20/50, fees 0.1%):

| Metric | Strategy | Benchmark (Buy & Hold) |
|--------|----------|------------------------|
| Total Return | 103.82% | 288.81% |
| Sharpe Ratio | 0.76 | — |
| Sortino Ratio | 1.03 | — |
| Max Drawdown | 29.59% | — |
| Win Rate | 61.54% | — |
| Profit Factor | 2.47 | — |
| Total Trades | 26 | — |
| Fees Paid | $7.35 | — |

---

## Roadmap

- [ ] RSI-based mean reversion strategy
- [ ] Multi-asset / portfolio-level backtesting
- [ ] Transaction cost and slippage modeling
- [ ] Walk-forward validation
- [ ] Hyperparameter optimization grid search
- [ ] Streamlit dashboard for interactive exploration
- [ ] Paper trading integration via broker API

---

## Disclaimer

This project is for **educational purposes only**. It does not constitute financial advice and should not be used for live trading without proper validation and risk management.

---

## License

MIT License
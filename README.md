# Trading Backtesting Project

## Overview

This project is a Python-based framework for building and testing trading strategies using historical market data.  
It is designed as an educational and experimental environment to understand how systematic trading strategies perform under realistic conditions.

The initial focus is on simple trend-following strategies using moving averages applied to ETFs like the S&P 500.

---

## Objectives

- Learn how to build quantitative trading strategies
- Understand backtesting methodology
- Evaluate performance using financial metrics
- Identify risks such as overfitting and drawdown
- Compare strategies against buy-and-hold benchmarks

---

## Strategy Implemented

The baseline strategy is a **Moving Average Crossover Strategy**:

- Buy when the fast moving average crosses above the slow moving average
- Sell when the fast moving average crosses below the slow moving average

Example configuration:
- Fast MA: 20 periods
- Slow MA: 50 periods

---

## Project Structure

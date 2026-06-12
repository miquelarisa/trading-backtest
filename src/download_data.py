import yfinance as yf

ticker = "SPY"

data = yf.download(
    ticker,
    start="2014-01-01",
    end="2025-01-01"
)

data.to_csv("../data/spy.csv")
# Moving Average Strategy Backtesting

A Python backtest of a 50/200-day moving average crossover strategy on SPY (S&P 500 ETF) and the Nifty 50 index, compared against buy-and-hold. Data: daily adjusted prices from Yahoo Finance, January 2015 to October 2026.

## Results

| Metric | SPY Strategy | SPY Buy & Hold | Nifty 50 Strategy | Nifty 50 Buy & Hold |
|---|---|---|---|---|
| CAGR | 8.9% | 13.8% | 3.3% | 8.8% |
| Volatility | 14.4% | 17.5% | 11.6% | 16.2% |
| Sharpe ratio | 0.67 | 0.83 | 0.34 | 0.61 |
| Max drawdown | -33.7% | -33.7% | -42.0% | -38.4% |

## Key findings

* Buy-and-hold earned higher returns in both markets.
* The strategy had lower volatility, but a larger maximum drawdown on the Nifty 50.
* The strategy spends time in cash earning nothing, and its slow signal reacts late to turns in the market.

## Method

* Hold the asset when the 50-day average is above the 200-day average, otherwise hold cash.
* The signal is shifted by one day to avoid look-ahead bias.
* Transaction cost of 0.05% per trade (an assumption).

## Full project

Code, charts, results files and the detailed README are in the [Moving Average Strategy](<Moving Average Strategy>) folder.

**Tools:** Python, pandas, NumPy, Matplotlib, yfinance

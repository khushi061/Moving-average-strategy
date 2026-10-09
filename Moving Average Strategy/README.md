# strategy Backtesting

## Overview

This project backtests a simple moving average crossover strategy using historical market data.

## Strategy

* 50-day Simple Moving Average (SMA)
* 200-day Simple Moving Average (SMA)
* Buy when the 50-day SMA is above the 200-day SMA.
* Hold cash when the 50-day SMA is below the 200-day SMA.

## Markets Tested

* SPY (S&P 500 ETF)
* Nifty 50 Index

## Performance Metrics

* Compound Annual Growth Rate (CAGR)
* Volatility
* Sharpe-like ratio
* Maximum drawdown
* Comparison with buy-and-hold

## Technologies Used

* Python
* yfinance
* pandas
* NumPy
* Matplotlib

## Limitations

This is an educational backtesting project. Results use historical data and may not reflect future performance. Transaction costs and market conditions can affect actual returns.

## Backtesting Results

The strategy was tested on historical data from January 2015 to October 2026 and compared with a buy-and-hold approach.

### SPY (S&P 500 ETF)

* Strategy CAGR: 8.91%
* Buy-and-hold CAGR: 13.82%
* Strategy volatility: 14.37%
* Maximum drawdown: -33.7%

### Nifty 50 Index

* Strategy CAGR: 3.31%
* Buy-and-hold CAGR: 8.84%
* Strategy volatility: 11.64%
* Strategy maximum drawdown: -42.0%

### Key Observation

The moving average strategy had lower volatility for both markets, but it underperformed buy-and-hold in overall returns. This shows that a simple trend-following strategy does not outperform the market in every situation.

*Note: These are historical backtest results, not a guarantee of future performance. Transaction costs are simplified assumptions.*

# Moving Average Strategy Backtesting

# Overview

A Python-based quantitative trading project that implements and evaluates a 50-day and 200-day Simple Moving Average (SMA) crossover strategy across SPY (S&P 500 ETF) and the Nifty 50 Index. The strategy is compared against buy-and-hold to analyse returns, risk, and performance across different market conditions.

# Strategy

* **Indicators:** 50-day SMA and 200-day SMA.
* **Entry:** Invest when the 50-day SMA is above the 200-day SMA.
* **Exit:** Hold cash when the 50-day SMA falls below the 200-day SMA.
* **Benchmark:** Buy-and-hold.

# Markets Tested

* **SPY:** S&P 500 ETF (US equity market).
* **Nifty 50:** Major Indian equity market index.

# Performance Results

Historical backtest results from January 2015 to October 2026.

| Metric                                  | SPY Strategy | SPY Buy & Hold | Nifty 50 Strategy | Nifty 50 Buy & Hold |
| --------------------------------------- | -----------: | -------------: | ----------------: | ------------------: |
| CAGR                                    |        8.91% |         13.82% |             3.31% |               8.84% |
| Volatility                              |       14.37% |         17.52% |            11.64% |              16.16% |
| Sharpe-like Ratio (Zero Risk-Free Rate) |         0.67 |           0.83 |              0.34 |                0.61 |
| Maximum Drawdown                        |       -33.7% |         -33.7% |            -42.0% |              -38.4% |

## Key Findings

* Buy-and-hold achieved higher annualised returns in both markets.
* The moving average strategy had lower volatility in both markets.
* The Nifty 50 strategy experienced a larger maximum drawdown than buy-and-hold.
* The results demonstrate the trade-offs between trend-following strategies and passive market exposure.

# Technologies Used

* Python
* yfinance
* pandas
* NumPy
* Matplotlib

# Project Structure

* `backtest.py` — Strategy implementation and performance calculations.
* `requirements.txt` — Required Python libraries.
* `images/` — Generated performance charts.
* `results/` — CSV files containing backtest results.

# How to Run

1. Install Python 3.

2. Install the required libraries:

   `pip install -r requirements.txt`

3. Run the backtest:

   `python3 backtest.py`

The script downloads historical market data, calculates performance metrics, generates charts, and saves results as CSV files.

# Code Quality

The code is organised for readability and maintainability, following Python style conventions such as consistent indentation, descriptive variable names, and clear structure.

# Limitations

This project is for educational and research purposes. Historical performance does not guarantee future results. Transaction costs, slippage, taxes, and real-world execution constraints can affect actual performance.

# Future Improvements

* Incorporate transaction costs and slippage.
* Test additional technical indicators and strategy parameters.
* Evaluate performance across different market conditions.
* Explore risk management and parameter optimisation.


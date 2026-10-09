
import os
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Settings
tickers = ["SPY", "^NSEI"]
start_date = "2015-01-01"
end_date = "2026-10-09"
cost_per_trade = 0.0005  # Assumed cost: 0.05%
trading_days = 252

# 2. Create output folders
os.makedirs("images", exist_ok=True)
os.makedirs("results", exist_ok=True)

# 3. Backtest each market
for ticker in tickers:
    print(f"\n{'=' * 45}")
    print("MOVING AVERAGE BACKTEST:", ticker)

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        print("No data downloaded. Skipping", ticker)
        continue

    prices = data["Close"].squeeze().dropna()

    # Moving averages
    ma_50 = prices.rolling(50).mean()
    ma_200 = prices.rolling(200).mean()

    # Trading signals (1 = invested, 0 = cash)
    signal = (ma_50 > ma_200).astype(int).shift(1).fillna(0)
    daily_returns = prices.pct_change().fillna(0)
    trades = signal.diff().abs().fillna(0)

    strategy_returns = (
        signal * daily_returns - trades * cost_per_trade
    )

    # Growth of investment
    strategy_growth = (1 + strategy_returns).cumprod()
    buy_hold_growth = (1 + daily_returns).cumprod()

    # Performance metrics
    years = len(prices) / trading_days

    strategy_cagr = strategy_growth.iloc[-1] ** (1 / years) - 1
    buy_hold_cagr = buy_hold_growth.iloc[-1] ** (1 / years) - 1

    strategy_volatility = strategy_returns.std() * np.sqrt(trading_days)
    buy_hold_volatility = daily_returns.std() * np.sqrt(trading_days)

    strategy_sharpe = (
        strategy_returns.mean() / strategy_returns.std()
        * np.sqrt(trading_days)
        if strategy_returns.std() != 0 else 0
    )

    buy_hold_sharpe = (
        daily_returns.mean() / daily_returns.std()
        * np.sqrt(trading_days)
        if daily_returns.std() != 0 else 0
    )

    strategy_drawdown = strategy_growth / strategy_growth.cummax() - 1
    buy_hold_drawdown = buy_hold_growth / buy_hold_growth.cummax() - 1

    # Display results
    print("First date:", prices.index[0].date())
    print("Last date:", prices.index[-1].date())
    print("Trading days:", len(prices))
    print("Days invested:", int(signal.sum()))
    print("Days in cash:", int((signal == 0).sum()))
    print("Position changes:", int(trades.sum()))

    print("\nPERFORMANCE COMPARISON")
    print(f"Strategy final value: {strategy_growth.iloc[-1]:.3f}")
    print(f"Buy-and-hold final value: {buy_hold_growth.iloc[-1]:.3f}")
    print(f"Strategy CAGR: {strategy_cagr * 100:.2f}%")
    print(f"Buy-and-hold CAGR: {buy_hold_cagr * 100:.2f}%")
    print(f"Strategy volatility: {strategy_volatility * 100:.2f}%")
    print(f"Buy-and-hold volatility: {buy_hold_volatility * 100:.2f}%")
    print(f"Strategy Sharpe-like ratio: {strategy_sharpe:.2f}")
    print(f"Buy-and-hold Sharpe-like ratio: {buy_hold_sharpe:.2f}")
    print(f"Strategy max drawdown: {strategy_drawdown.min() * 100:.1f}%")
    print(f"Buy-and-hold max drawdown: {buy_hold_drawdown.min() * 100:.1f}%")

    # 4. Save charts
    charts = [
        (
            prices, ma_50, ma_200,
            f"{ticker}: Price and Moving Averages",
            "Adjusted Price",
            f"{ticker}_moving_averages.png"
        ),
        (
            strategy_growth, buy_hold_growth,
            None,
            f"{ticker}: Investment Growth Comparison",
            "Growth of 1 Unit",
            f"{ticker}_performance.png"
        ),
        (
            strategy_drawdown * 100, buy_hold_drawdown * 100,
            None,
            f"{ticker}: Drawdown Comparison",
            "Drawdown (%)",
            f"{ticker}_drawdown.png"
        )
    ]

    for first, second, third, title, ylabel, filename in charts:
        plt.figure(figsize=(12, 5))
        plt.plot(first, label=(
            "Market Price" if "Price" in title else
            "Strategy Drawdown" if "Drawdown" in title else
            "Strategy"
        ))
        plt.plot(second, label=(
            "50-Day Moving Average" if "Price" in title else
            "Buy and Hold Drawdown" if "Drawdown" in title else
            "Buy and Hold"
        ))
        if third is not None:
            plt.plot(third, label="200-Day Moving Average")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join("images", filename), dpi=300)
        plt.close()

    # 5. Save performance summary
    summary = pd.DataFrame({
        "Metric": [
            "Strategy CAGR (%)",
            "Buy and Hold CAGR (%)",
            "Strategy Volatility (%)",
            "Buy and Hold Volatility (%)",
            "Strategy Sharpe-like Ratio",
            "Buy and Hold Sharpe-like Ratio",
            "Strategy Max Drawdown (%)",
            "Buy and Hold Max Drawdown (%)"
        ],
        "Value": [
            round(strategy_cagr * 100, 2),
            round(buy_hold_cagr * 100, 2),
            round(strategy_volatility * 100, 2),
            round(buy_hold_volatility * 100, 2),
            round(strategy_sharpe, 2),
            round(buy_hold_sharpe, 2),
            round(strategy_drawdown.min() * 100, 2),
            round(buy_hold_drawdown.min() * 100, 2)
        ]
    })

    csv_path = os.path.join("results", f"{ticker}_results.csv")
    summary.to_csv(csv_path, index=False)
    print("\nResults saved to:", csv_path)

    # 6. Compare performance across market periods
    periods = {
        "2015-2019": ("2015-01-01", "2020-01-01"),
        "2020-2022": ("2020-01-01", "2023-01-01"),
        "2023-2026": ("2023-01-01", end_date)
    }

    print("\nPERFORMANCE BY MARKET PERIOD")

    for period_name, (period_start, period_end) in periods.items():
        period_prices = prices.loc[
            (prices.index >= period_start) &
            (prices.index < period_end)
        ]

        if len(period_prices) < 2:
            continue

        period_returns = period_prices.pct_change().fillna(0)
        period_ma50 = period_prices.rolling(50).mean()
        period_ma200 = period_prices.rolling(200).mean()
        period_signal = (period_ma50 > period_ma200).astype(int).shift(1).fillna(0)
        period_trades = period_signal.diff().abs().fillna(0)

        period_strategy_returns = (
            period_signal * period_returns
            - period_trades * cost_per_trade
        )

        years_period = len(period_prices) / trading_days
        strategy_growth_period = (1 + period_strategy_returns).prod()
        buy_hold_growth_period = (1 + period_returns).prod()

        strategy_cagr_period = (
            strategy_growth_period ** (1 / years_period) - 1
        ) * 100
        buy_hold_cagr_period = (
            buy_hold_growth_period ** (1 / years_period) - 1
        ) * 100

        print(f"\n{period_name}")
        print(f"Strategy CAGR: {strategy_cagr_period:.2f}%")
        print(f"Buy-and-hold CAGR: {buy_hold_cagr_period:.2f}%")

print("\nAll available market backtests finished.")
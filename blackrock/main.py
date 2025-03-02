from data_fetch import fetch_stock_data
from risk_metrics import compute_risk_metrics
from monte_carlo import monte_carlo_simulation

# Define assets
assets = ["BLK", "AAPL", "GOOGL", "MSFT", "TSLA"]

if __name__ == "__main__":
    try:
        print("📥 Fetching stock data...")
        data, returns = fetch_stock_data(assets)

        if data is None or returns is None or returns.empty:
            raise ValueError("❌ Stock data fetch failed. Check asset list or data source.")

        print("\n📊 Computing risk metrics...")
        metrics = compute_risk_metrics(assets=assets)
        for key, value in metrics.items():
            print(f"{key}: {value}\n")

        print("\n🎲 Running Monte Carlo simulation...")
        mc_var = monte_carlo_simulation(assets=assets)  # 🔹 Pass assets explicitly

        if mc_var is not None:
            print(f"\n📉 Monte Carlo VaR (95% confidence): {-mc_var:.4f}")
        else:
            print("❌ Monte Carlo simulation failed.")

        print("\n🚀 Run `python dashboard.py` to launch the interactive dashboard.")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

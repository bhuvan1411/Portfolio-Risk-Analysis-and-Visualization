import numpy as np
from risk_metrics import compute_risk_metrics

def monte_carlo_simulation(assets=None, simulations=10000, time_horizon=252):
    """Runs a Monte Carlo simulation to predict portfolio risk."""
    try:
        # Ensure assets are passed correctly
        if assets is None:
            raise ValueError("❌ No assets provided for Monte Carlo simulation.")

        # Compute risk metrics again with assets
        metrics = compute_risk_metrics(assets=assets)
        if metrics is None:
            raise ValueError("❌ Error: Risk metrics could not be computed.")

        portfolio_return = metrics["Portfolio Return"]
        portfolio_volatility = metrics["Portfolio Volatility"]

        if portfolio_return is None or portfolio_volatility is None:
            raise ValueError("❌ Invalid portfolio return or volatility.")

        # Simulate future returns using normal distribution
        simulated_returns = np.random.normal(portfolio_return, portfolio_volatility, (simulations, time_horizon))
        simulated_cumulative_returns = np.cumprod(1 + simulated_returns, axis=1)

        # Compute 5% worst-case scenario (Monte Carlo VaR)
        VaR_monte_carlo = np.percentile(simulated_cumulative_returns[:, -1], 5)

        print("✅ Monte Carlo Simulation Completed Successfully!")
        return VaR_monte_carlo

    except Exception as e:
        print(f"❌ Error in Monte Carlo simulation: {e}")
        return None

if __name__ == "__main__":
    assets = ["BLK", "AAPL", "GOOGL", "MSFT", "TSLA"]
    mc_var = monte_carlo_simulation(assets=assets)
    if mc_var is not None:
        print(f"\n📉 Monte Carlo VaR (95% confidence): {-mc_var:.4f}")
    else:
        print("❌ Monte Carlo simulation failed.")

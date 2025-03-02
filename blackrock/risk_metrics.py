import numpy as np
import pandas as pd
from scipy.stats import norm
from data_fetch import fetch_stock_data

def compute_risk_metrics(assets=None, weights=None, confidence_level=0.95):
    """
    Computes expected returns, covariance matrix, and Value at Risk (VaR).

    Parameters:
        assets (list, optional): List of asset tickers.
        weights (list, optional): Portfolio weights.
        confidence_level (float, optional): Confidence level for VaR (default: 0.95).

    Returns:
        dict: Risk metrics including mean returns, covariance matrix, 
              portfolio return, volatility, and VaR.
    """
    try:
        prices, returns = fetch_stock_data(assets=assets)
        
        if returns is None or returns.empty:
            raise ValueError("❌ No return data available. Check assets or data source.")

        # Compute mean returns & covariance matrix
        mean_returns = returns.mean()
        cov_matrix = returns.cov()

        num_assets = len(mean_returns)

        # Assign equal weights if none are provided
        if weights is None or len(weights) != num_assets:
            print("⚠️ Warning: Invalid weights provided. Using equal weights.")
            weights = np.ones(num_assets) / num_assets  # Equal weights

        weights = np.array(weights)

        # Portfolio Return & Volatility
        portfolio_return = np.dot(weights, mean_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        # Parametric VaR Calculation (Normal Distribution)
        VaR_parametric = norm.ppf(1 - confidence_level) * portfolio_volatility

        return {
            "Mean Returns": mean_returns,
            "Covariance Matrix": cov_matrix,
            "Portfolio Return": portfolio_return,
            "Portfolio Volatility": portfolio_volatility,
            "VaR (Parametric)": VaR_parametric
        }

    except Exception as e:
        print(f"❌ Error computing risk metrics: {e}")
        return None

if __name__ == "__main__":
    assets = ["BLK", "AAPL", "GOOGL", "MSFT", "TSLA"]
    weights = [0.3, 0.2, 0.2, 0.2, 0.1]  # Adjustable weights
    
    metrics = compute_risk_metrics(assets=assets, weights=weights)

    if metrics:
        print("\n✅ Risk Metrics Computed Successfully:\n")
        for key, value in metrics.items():
            print(f"{key}: {value}\n")
    else:
        print("❌ Failed to compute risk metrics.")

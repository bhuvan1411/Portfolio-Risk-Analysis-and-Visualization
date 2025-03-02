import yfinance as yf
import pandas as pd

# Define portfolio assets & date range
assets = ["BLK", "AAPL", "GOOGL", "MSFT", "TSLA"]
start_date = "2020-01-01"
end_date = "2024-01-01"

def fetch_stock_data(assets, start=start_date, end=end_date):
    """
    Fetches historical stock prices and computes daily returns.

    Args:
        assets (list): List of stock tickers.
        start (str): Start date (YYYY-MM-DD).
        end (str): End date (YYYY-MM-DD).

    Returns:
        tuple: (stock price DataFrame, daily returns DataFrame)
    """
    try:
        # Fetch data with auto_adjust=False to ensure 'Adj Close' is available
        data = yf.download(assets, start=start, end=end, auto_adjust=False, progress=False)

        # Check if data is empty
        if data is None or data.empty:
            raise ValueError("❌ No data received. Check ticker symbols or internet connection.")

        # Ensure 'Adj Close' is available
        if "Adj Close" in data.columns:
            prices = data["Adj Close"]
        elif ("Adj Close", "") in data.columns:
            # Multi-index case: Access 'Adj Close' properly
            prices = data.loc[:, "Adj Close"]
        else:
            print("⚠️ Warning: 'Adj Close' not found, using 'Close' instead.")
            prices = data["Close"]

        # Compute daily returns
        returns = prices.pct_change().dropna()

        return prices, returns

    except Exception as e:
        print(f"❌ Error fetching stock data: {e}")
        return None, None

if __name__ == "__main__":
    data, returns = fetch_stock_data(assets)
    
    if data is not None:
        print("✅ Stock data fetched successfully!")
        print(data.head())  # Print sample data

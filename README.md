📊 Portfolio Risk Analysis & Visualization

This project is a portfolio risk analysis and visualization tool that helps investors and financial analysts evaluate the risk and performance of a stock portfolio using quantitative finance techniques. It fetches historical stock data, computes risk metrics, runs Monte Carlo simulations, and provides an interactive Dash-based dashboard for visualization.

🚀 Features

✅ Stock Data Fetching – Fetches historical stock prices using yfinance and computes daily returns.
✅ Risk Metrics Calculation – Computes expected returns, covariance matrix, portfolio volatility, and Value at Risk (VaR).
✅ Monte Carlo Simulation – Runs thousands of simulations to estimate future risk and worst-case losses (Monte Carlo VaR).
✅ Interactive Dashboard – Built with Dash & Plotly to visualize historical prices and risk metrics dynamically.
✅ Error Handling & Logging – Robust exception handling to prevent crashes.

📊 How It Works

✅ Fetching Stock Data
Uses yfinance to pull historical adjusted close prices.
Computes daily returns for each stock.

📉 Computing Risk Metrics
Calculates:
Mean Returns & Covariance Matrix
Portfolio Return & Volatility
Value at Risk (VaR) at 95% confidence

🎲 Running Monte Carlo Simulation
Simulates 10,000+ future return paths.
Estimates the worst 5% percentile of portfolio value.

📈 Visualizing Data (Dash App)
Dropdown menu to select assets.
Historical price chart for selected stocks.
Portfolio VaR displayed dynamically.

👨‍💻 Contributing
Feel free to fork this repository and submit pull requests for enhancements! 🚀

📜 License
This project is licensed under the MIT License. See LICENSE for details.

⭐ Acknowledgments
Yahoo Finance API for stock data.
NumPy, Pandas, SciPy for financial computations.
Dash & Plotly for visualization.

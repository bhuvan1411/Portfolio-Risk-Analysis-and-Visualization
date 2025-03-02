import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from data_fetch import fetch_stock_data
from risk_metrics import compute_risk_metrics

# Define assets list explicitly
assets = ["BLK", "AAPL", "GOOGL", "MSFT", "TSLA"]

# Fetch Data
data, returns = fetch_stock_data(assets)
if data is None or data.empty:
    raise ValueError("❌ Error: No stock data available. Check data source!")

# Compute Risk Metrics
try:
    metrics = compute_risk_metrics(assets=assets, weights=[0.3, 0.2, 0.2, 0.2, 0.1])

except Exception as e:
    raise ValueError(f"❌ Error computing risk metrics: {e}")

# Initialize Dash App
app = dash.Dash(__name__)
app.title = "BlackRock Portfolio Dashboard"

app.layout = html.Div([
    html.H1("📈 BlackRock Portfolio Risk Dashboard", style={"textAlign": "center"}),

    # Dropdown for selecting asset
    dcc.Dropdown(
        id="stock-selector",
        options=[{"label": stock, "value": stock} for stock in data.columns],
        value=assets[0],  # Default to first asset
        clearable=False,
        style={"width": "50%", "margin": "auto"}
    ),

    # Graph for historical prices
    dcc.Graph(id="price-chart"),

    # Risk Metrics Display
    html.Div(id="var-display", style={"fontSize": "20px", "textAlign": "center", "marginTop": "20px"})
])

@app.callback(
    [Output("price-chart", "figure"),
     Output("var-display", "children")],
    [Input("stock-selector", "value")]
)
def update_graph(stock):
    if stock not in data.columns:
        return go.Figure(), "❌ Error: Stock data not available."

    # Create line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data[stock], mode="lines", name=stock))
    fig.update_layout(title=f"{stock} Historical Prices", xaxis_title="Date", yaxis_title="Price")

    # Display Portfolio VaR
    portfolio_var = metrics["VaR (Parametric)"]
    return fig, f"📉 95% Confidence VaR for Portfolio: {-portfolio_var:.4f}"

if __name__ == "__main__":
    app.run_server(debug=True)

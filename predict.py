import joblib
import pandas as pd
import yfinance as yf

from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands, AverageTrueRange


# Load models

LINEAR_MODEL_PATH = "models/linear_regression.pkl"
RF_MODEL_PATH = "models/random_forest.pkl"
FEATURES_PATH = "models/features.pkl"

linear_model = joblib.load(LINEAR_MODEL_PATH)
random_forest_model = joblib.load(RF_MODEL_PATH)
features = joblib.load(FEATURES_PATH)


# Download stock data

def download_stock_data(ticker):

    data = yf.download(
        ticker,
        period="5y",
        auto_adjust=True
    )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    if data.empty:
        raise ValueError(
            f"No data found for ticker: {ticker}"
        )

    return data


# Create features

def create_features(data):

    data = data.copy()

    data["Daily_Return"] = (
        data["Close"].pct_change()
    )

    data["Price_Range"] = (
        (data["High"] - data["Low"])
        / data["Close"]
    )

    data["Volume_MA_20"] = (
        data["Volume"].rolling(window=20).mean()
    )

    data["Rel_Volume"] = (
        data["Volume"]
        / data["Volume_MA_20"]
    )

    data["Price_Range_Pct"] = (
        (data["High"] - data["Low"])
        / data["Close"]
    )

    data["Return_5D"] = (
        data["Close"].pct_change(periods=5)
    )

    data["Return_10D"] = (
        data["Close"].pct_change(periods=10)
    )

    data["Return_20D"] = (
        data["Close"].pct_change(periods=20)
    )

    rsi = RSIIndicator(
        close=data["Close"],
        window=14
    )

    data["RSI"] = rsi.rsi()

    macd = MACD(
        close=data["Close"],
        window_slow=26,
        window_fast=12,
        window_sign=9
    )

    data["MACD"] = macd.macd()

    data["MACD_Signal"] = (
        macd.macd_signal()
    )

    bb = BollingerBands(
        close=data["Close"],
        window=20,
        window_dev=2
    )

    data["BB_Pct"] = (
        bb.bollinger_pband()
    )

    atr = AverageTrueRange(
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        window=14
    )

    data["ATR_Pct"] = (
        atr.average_true_range()
        / data["Close"]
    )

    return data

# Historical price data

def get_price_history(ticker):

    data = yf.download(
        ticker,
        period="6mo",
        auto_adjust=True
    )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    if data.empty:
        raise ValueError(
            f"No historical data found for ticker: {ticker}"
        )

    return data[["Close"]]
# Predict stock return

def predict_stock(ticker):

    data = download_stock_data(ticker)

    data = create_features(data)

    data = data.dropna()

    if data.empty:
        raise ValueError(
            "Not enough data to create features."
        )

    latest_data = data.iloc[-1]

    X = data[features].iloc[[-1]]

    linear_return = linear_model.predict(X)[0]

    rf_return = random_forest_model.predict(X)[0]

    current_price = float(
        latest_data["Close"]
    )

    linear_price = (
        current_price
        * (1 + linear_return)
    )

    rf_price = (
        current_price
        * (1 + rf_return)
    )

    return {
        "ticker": ticker,
        "current_price": current_price,

        "linear_return": float(
            linear_return
        ),

        "linear_price": float(
            linear_price
        ),

        "random_forest_return": float(
            rf_return
        ),

        "random_forest_price": float(
            rf_price
        )
    }


# Test

if __name__ == "__main__":

    result = predict_stock("RELIANCE.NS")

    print("\nSTOCK PREDICTION")

    print(
        "Ticker:",
        result["ticker"]
    )

    print(
        "Current Price:",
        result["current_price"]
    )

    print(
        "Linear Regression:",
        f"{result['linear_return'] * 100:.2f}%"
    )

    print(
        "Linear Regression Price:",
        f"₹{result['linear_price']:.2f}"
    )

    print(
        "Random Forest:",
        f"{result['random_forest_return'] * 100:.2f}%"
    )

    print(
        "Random Forest Price:",
        f"₹{result['random_forest_price']:.2f}"
    )
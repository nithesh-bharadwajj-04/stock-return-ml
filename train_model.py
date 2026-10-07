
# TRAINING PIPELINE
# 5-Day Stock Return Prediction


import os
import joblib
import numpy as np
import pandas as pd
import yfinance as yf

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands, AverageTrueRange



# CONFIGURATION


TICKER = "AAPL"

MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)



# DOWNLOAD DATA


print(f"Downloading data for {TICKER}...")

data = yf.download(
    TICKER,
    period="5y",
    auto_adjust=True
)

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

print("Data downloaded:", data.shape)



# FEATURE ENGINEERING


data["Daily_Return"] = data["Close"].pct_change()

data["Price_Range"] = (
    (data["High"] - data["Low"]) / data["Close"]
)

data["Volume_MA_20"] = (
    data["Volume"].rolling(window=20).mean()
)

data["Rel_Volume"] = (
    data["Volume"] / data["Volume_MA_20"]
)

data["Price_Range_Pct"] = (
    (data["High"] - data["Low"]) / data["Close"]
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



# TECHNICAL INDICATORS


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
data["MACD_Signal"] = macd.macd_signal()


bb = BollingerBands(
    close=data["Close"],
    window=20,
    window_dev=2
)

data["BB_Pct"] = bb.bollinger_pband()


atr = AverageTrueRange(
    high=data["High"],
    low=data["Low"],
    close=data["Close"],
    window=14
)

data["ATR_Pct"] = (
    atr.average_true_range() / data["Close"]
)



# TARGET


data["Target_5D_Return"] = (
    data["Close"].shift(-5) / data["Close"]
) - 1



# REMOVE MISSING VALUES


data = data.dropna()



# FEATURES


FEATURES = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Daily_Return",
    "Price_Range",
    "Volume_MA_20",
    "Rel_Volume",
    "Return_5D",
    "Return_10D",
    "Return_20D",
    "Price_Range_Pct",
    "RSI",
    "MACD",
    "MACD_Signal",
    "BB_Pct",
    "ATR_Pct"
]

X = data[FEATURES]
y = data["Target_5D_Return"]



# TRAIN / TEST SPLIT


split_index = int(len(data) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]



# LINEAR REGRESSION


print("\nTraining Linear Regression...")

linear_model = LinearRegression()

linear_model.fit(
    X_train,
    y_train
)

linear_prediction = linear_model.predict(X_test)

linear_mae = mean_absolute_error(
    y_test,
    linear_prediction
)

print(
    "Linear Regression MAE:",
    linear_mae
)



# RANDOM FOREST


print("\nTraining Random Forest...")

random_forest_model = RandomForestRegressor(
    n_estimators=200,
    max_depth=5,
    min_samples_leaf=10,
    random_state=42
)

random_forest_model.fit(
    X_train,
    y_train
)

rf_prediction = random_forest_model.predict(X_test)

rf_mae = mean_absolute_error(
    y_test,
    rf_prediction
)

print(
    "Random Forest MAE:",
    rf_mae
)



# SAVE MODELS


joblib.dump(
    linear_model,
    os.path.join(
        MODEL_DIR,
        "linear_regression.pkl"
    )
)

joblib.dump(
    random_forest_model,
    os.path.join(
        MODEL_DIR,
        "random_forest.pkl"
    )
)

# Save feature names too
joblib.dump(
    FEATURES,
    os.path.join(
        MODEL_DIR,
        "features.pkl"
    )
)



# RESULTS



print("TRAINING COMPLETE")


print(
    f"Linear Regression MAE: {linear_mae:.6f}"
)

print(
    f"Random Forest MAE: {rf_mae:.6f}"
)

print("\nModels saved successfully.")

print("\nSaved files:")

print("models/linear_regression.pkl")
print("models/random_forest.pkl")
print("models/features.pkl")
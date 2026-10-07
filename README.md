# NIFTY 50 Stock Return Predictor

A beginner-friendly end-to-end Machine Learning project that predicts the expected stock return over the next 5 trading days.

The project combines historical market data, feature engineering, machine learning models, and a Streamlit web interface into a complete ML application.

## Project Overview

The application allows a user to select a stock from the configured NIFTY 50 stock list and generate a 5-day return prediction.

The application:

1. Downloads historical stock data from Yahoo Finance.
2. Performs feature engineering.
3. Calculates technical indicators.
4. Loads trained machine learning models.
5. Generates a 5-day return prediction.
6. Calculates an estimated price after 5 trading days.
7. Displays the result through a Streamlit interface.
8. Shows the stock's historical price movement.

## Project Architecture

```text
                    User
                      |
                      v
             Streamlit Interface
                      |
                      v
              Select NIFTY 50 Stock
                      |
                      v
                Yahoo Finance
                      |
                      v
              Historical Market Data
                      |
                      v
              Feature Engineering
                      |
          +-----------+-----------+
          |                       |
          v                       v
   Linear Regression       Random Forest
          |                       |
          +-----------+-----------+
                      |
                      v
              5-Day Return
                      |
                      v
              Predicted Price
                      |
                      v
               Streamlit Output
````

## Machine Learning Models

The project uses two regression models:

### 1. Linear Regression

Used as a simple baseline regression model for predicting the 5-day future return.

### 2. Random Forest Regressor

Used as a tree-based regression model for predicting the 5-day future return.

The models are intentionally kept simple because the primary goal of this project is to understand and implement the complete end-to-end ML workflow.

Model optimization and improved prediction performance can be explored in future versions.

## Features

The model uses the following features:

### Market Features

* Open
* High
* Low
* Close
* Volume

### Return and Momentum Features

* Daily Return
* 5-Day Return
* 10-Day Return
* 20-Day Return

### Volume Features

* 20-Day Average Volume
* Relative Volume

### Price Features

* Price Range
* Price Range Percentage

### Technical Indicators

* RSI
* MACD
* MACD Signal
* Bollinger Band Percentage
* ATR Percentage

## Target

The target variable is:

```text
5-Day Future Return
```

The model attempts to estimate how much the stock price may change over the next 5 trading days.

The predicted price is then calculated from the current price and predicted return.

## Project Structure

```text
stock-return-ml/
│
├── models/
│   ├── features.pkl
│   ├── linear_regression.pkl
│   └── random_forest.pkl
│
├── app.py
├── predict.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## File Description

### `train_model.py`

Responsible for:

* Downloading historical market data
* Creating features
* Creating the 5-day return target
* Splitting the data chronologically
* Training Linear Regression
* Training Random Forest
* Evaluating the models
* Saving the trained models

### `predict.py`

Responsible for:

* Loading the trained models
* Downloading fresh stock data
* Recreating the required features
* Generating predictions
* Calculating predicted prices
* Providing historical price data for the application

### `app.py`

Contains the Streamlit user interface.

It allows the user to:

* Select a stock
* Run a prediction
* View the current price
* View Linear Regression prediction
* View Random Forest prediction
* View predicted prices
* View historical price movement

### `models/`

Contains the serialized machine learning models and feature list.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Yahoo Finance / yfinance
* Technical Analysis (`ta`)
* Joblib
* Streamlit

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd stock-return-ml
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Train the Models

Run:

```bash
python train_model.py
```

This creates:

```text
models/
├── linear_regression.pkl
├── random_forest.pkl
└── features.pkl
```

## Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in the browser.

## Example Workflow

```text
Select Stock
     |
     v
Download Historical Data
     |
     v
Create Features
     |
     v
Load Trained Models
     |
     v
Generate Predictions
     |
     v
Calculate Predicted Price
     |
     v
Display Results
```

## Example Output

The application displays information such as:

```text
Current Price
₹2743.00

Linear Regression
5-Day Return: -44.44%
Predicted Price: ₹1523.97

Random Forest
5-Day Return: 2.07%
Predicted Price: ₹2799.65
```

The actual values change whenever fresh market data is processed.

## Important Note

This project is intended for educational and portfolio purposes.

The predictions are generated by simple machine learning models and should not be considered financial advice or reliable investment recommendations.

The current version focuses on demonstrating the complete ML application workflow rather than achieving optimized prediction performance.

## Future Improvements

Possible future improvements include:

* Training on a larger multi-stock dataset
* Improving feature engineering
* Hyperparameter tuning
* Cross-validation
* Additional machine learning models
* Better model evaluation
* Automated model retraining
* Prediction confidence analysis
* Improved visualizations
* Deployment to a cloud platform
* Automated data pipelines
* Model monitoring

## Learning Outcomes

This project demonstrates practical understanding of:

* Data ingestion
* Data validation
* Feature engineering
* Technical indicators
* Supervised learning
* Regression
* Model training
* Model evaluation
* Model serialization
* Model inference
* Python project structure
* Streamlit application development
* Building an end-to-end ML application

## Disclaimer

This application is a machine learning demonstration project and is not intended to provide financial advice or investment recommendations.

```

### One important correction

I intentionally worded the README carefully around the **current implementation**. Your models were trained using the training script's `AAPL` dataset, while the Streamlit interface allows NIFTY 50 selections. We have not yet retrained the models on a multi-stock NIFTY 50 dataset.

For this beginner project, that's acceptable given your stated goal, but we should **not claim in the README that the models were trained on the NIFTY 50** when they weren't.


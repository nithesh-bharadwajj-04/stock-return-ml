import streamlit as st

from predict import predict_stock, get_price_history


# NIFTY 50 STOCKS

NIFTY_50 = {
    "Adani Enterprises": "ADANIENT.NS",
    "Adani Ports": "ADANIPORTS.NS",
    "Apollo Hospitals": "APOLLOHOSP.NS",
    "Asian Paints": "ASIANPAINT.NS",
    "Axis Bank": "AXISBANK.NS",
    "Bajaj Auto": "BAJAJ-AUTO.NS",
    "Bajaj Finance": "BAJFINANCE.NS",
    "Bajaj Finserv": "BAJAJFINSV.NS",
    "Bharat Electronics": "BEL.NS",
    "Bharti Airtel": "BHARTIARTL.NS",
    "Cipla": "CIPLA.NS",
    "Coal India": "COALINDIA.NS",
    "Dr. Reddy's Laboratories": "DRREDDY.NS",
    "Eicher Motors": "EICHERMOT.NS",
    "Eternal": "ETERNAL.NS",
    "Grasim Industries": "GRASIM.NS",
    "HCL Technologies": "HCLTECH.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "HDFC Life": "HDFCLIFE.NS",
    "Hero MotoCorp": "HEROMOTOCO.NS",
    "Hindalco Industries": "HINDALCO.NS",
    "Hindustan Unilever": "HINDUNILVR.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "IndusInd Bank": "INDUSINDBK.NS",
    "Infosys": "INFY.NS",
    "ITC": "ITC.NS",
    "Jio Financial Services": "JIOFIN.NS",
    "JSW Steel": "JSWSTEEL.NS",
    "Kotak Mahindra Bank": "KOTAKBANK.NS",
    "Larsen & Toubro": "LT.NS",
    "Mahindra & Mahindra": "M&M.NS",
    "Maruti Suzuki": "MARUTI.NS",
    "Max Healthcare": "MAXHEALTH.NS",
    "Nestle India": "NESTLEIND.NS",
    "NTPC": "NTPC.NS",
    "Oil & Natural Gas Corporation": "ONGC.NS",
    "Power Grid Corporation": "POWERGRID.NS",
    "Reliance Industries": "RELIANCE.NS",
    "SBI Life Insurance": "SBILIFE.NS",
    "State Bank of India": "SBIN.NS",
    "Shriram Finance": "SHRIRAMFIN.NS",
    "Sun Pharmaceutical": "SUNPHARMA.NS",
    "Tata Consultancy Services": "TCS.NS",
    "Tata Consumer Products": "TATACONSUM.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "Tata Steel": "TATASTEEL.NS",
    "Tech Mahindra": "TECHM.NS",
    "Titan Company": "TITAN.NS",
    "Trent": "TRENT.NS",
    "UltraTech Cement": "ULTRACEMCO.NS",
    "Wipro": "WIPRO.NS",
    "Zomato": "ZOMATO.NS"
}


# PAGE CONFIGURATION

st.set_page_config(
    page_title="NIFTY 50 Analytics",
    page_icon="N",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CORPORATE STYLING

st.markdown(
    """
    <style>

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    .stApp {
        background-color: #f5f7fa;
    }

    [data-testid="stSidebar"] {
        background-color: #0f1f33;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    .top-header {
        background: #0f1f33;
        padding: 24px 30px;
        border-radius: 12px;
        margin-bottom: 24px;
        color: white;
        border: 1px solid #1d3552;
    }

    .brand {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    .subtitle {
        font-size: 14px;
        color: #b7c5d6;
        margin-top: 6px;
    }

    .section-title {
        font-size: 20px;
        font-weight: 650;
        color: #16263d;
        margin-top: 24px;
        margin-bottom: 12px;
    }

    .stock-header {
        background: white;
        padding: 20px 24px;
        border-radius: 10px;
        border: 1px solid #e1e6ec;
        margin-bottom: 18px;
    }

    .stock-name {
        font-size: 25px;
        font-weight: 700;
        color: #16263d;
    }

    .ticker {
        font-size: 13px;
        color: #718096;
        margin-top: 4px;
    }

    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e1e6ec;
        min-height: 125px;
    }

    .metric-label {
        font-size: 13px;
        color: #718096;
        margin-bottom: 8px;
    }

    .metric-value {
        font-size: 27px;
        font-weight: 700;
        color: #16263d;
    }

    .metric-description {
        font-size: 12px;
        color: #8a96a6;
        margin-top: 6px;
    }

    .prediction-card {
        background: white;
        padding: 22px;
        border-radius: 10px;
        border: 1px solid #e1e6ec;
        min-height: 170px;
    }

    .prediction-title {
        font-size: 17px;
        font-weight: 650;
        color: #16263d;
        margin-bottom: 18px;
    }

    .prediction-return {
        font-size: 30px;
        font-weight: 700;
        color: #16263d;
    }

    .prediction-price {
        font-size: 15px;
        color: #66758a;
        margin-top: 8px;
    }

    .chart-card {
        background: white;
        padding: 18px 22px 10px 22px;
        border-radius: 10px;
        border: 1px solid #e1e6ec;
    }

    .status {
        display: inline-block;
        background: #e8f1fb;
        color: #24527a;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

    .disclaimer {
        background: #eef2f6;
        padding: 15px 18px;
        border-radius: 8px;
        color: #66758a;
        font-size: 12px;
        margin-top: 25px;
        border: 1px solid #dde3ea;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# HEADER

st.markdown(
    """
    <div class="top-header">
        <div class="brand">NIFTY 50 ANALYTICS</div>
        <div class="subtitle">
            Machine Learning powered stock return analysis and forecasting
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# SIDEBAR

with st.sidebar:

    st.markdown(
        """
        <div style="font-size:22px;font-weight:700;margin-bottom:4px;">
        Market Analysis
        </div>

        <div style="font-size:13px;color:#b7c5d6;margin-bottom:25px;">
        Select a NIFTY 50 constituent
        </div>
        """,
        unsafe_allow_html=True
    )

    stock_name = st.selectbox(
        "Stock",
        list(NIFTY_50.keys())
    )

    ticker = NIFTY_50[stock_name]

    st.markdown("<br>", unsafe_allow_html=True)

    predict_button = st.button(
        "GENERATE FORECAST",
        type="primary",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="
            margin-top:30px;
            padding-top:20px;
            border-top:1px solid #29405d;
            font-size:12px;
            color:#9fb0c4;
            line-height:1.6;
        ">
        Data source<br>
        Yahoo Finance<br><br>

        Forecast horizon<br>
        5 trading days<br><br>

        Models<br>
        Linear Regression<br>
        Random Forest
        </div>
        """,
        unsafe_allow_html=True
    )


# MAIN APPLICATION

if predict_button:

    with st.spinner("Processing market data and generating forecast..."):

        try:

            result = predict_stock(ticker)

            price_history = get_price_history(ticker)

            # STOCK HEADER

            st.markdown(
                f"""
                <div class="stock-header">
                    <div class="stock-name">{stock_name}</div>
                    <div class="ticker">
                        NSE: {ticker.replace(".NS", "")}
                        &nbsp;&nbsp; | &nbsp;&nbsp;
                        <span class="status">LIVE DATA</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # KEY METRICS

            st.markdown(
                '<div class="section-title">Market Overview</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">CURRENT PRICE</div>
                        <div class="metric-value">
                            ₹{result["current_price"]:,.2f}
                        </div>
                        <div class="metric-description">
                            Latest available market price
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            LINEAR REGRESSION RETURN
                        </div>
                        <div class="metric-value">
                            {result["linear_return"] * 100:.2f}%
                        </div>
                        <div class="metric-description">
                            Expected 5-day return
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            RANDOM FOREST RETURN
                        </div>
                        <div class="metric-value">
                            {result["random_forest_return"] * 100:.2f}%
                        </div>
                        <div class="metric-description">
                            Expected 5-day return
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # PRICE HISTORY

            st.markdown(
                '<div class="section-title">Price Performance</div>',
                unsafe_allow_html=True
            )

            # st.markdown(
            #     '<div class="chart-card">',
            #     unsafe_allow_html=True
            # )

            st.line_chart(
                price_history["Close"],
                height=360
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            # MODEL FORECAST

            st.markdown(
                '<div class="section-title">Model Forecast</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                linear_return = result["linear_return"] * 100

                linear_return_color = "#c62828" if linear_return < 0 else "#16803c"

                st.html(
                    f"""
                    <div class="prediction-card">
                        <div class="prediction-title">
                            Linear Regression
                        </div>
                        <div class="prediction-return"
                            style="color:{linear_return_color};">
                            {linear_return:+.2f}%
                        </div>
                        <div class="prediction-label">
                            Expected 5-day return
                        </div>
                        <div class="prediction-price" style="font-size:30px;color:#66758a; font-weight: bold;">
                            ₹{result["linear_price"]:,.2f}
                        </div>
                        <div class="prediction-price-label" style="color:#66758a;">
                            Estimated price after 5 trading days
                        </div>
                    </div>
                    """
                )


            with col2:

                rf_return = result["random_forest_return"] * 100

                rf_return_color = "#c62828" if rf_return < 0 else "#16803c"

                st.html(
                    f"""
                    <div class="prediction-card">
                        <div class="prediction-title">
                            Random Forest
                        </div>
                        <div class="prediction-return"
                            style="color:{rf_return_color};">
                            {rf_return:+.2f}%
                        </div>
                        <div class="prediction-label">
                            Expected 5-day return
                        </div>
                        <div class="prediction-price" style="font-size:30px;color:#66758a; font-weight: bold;">
                            ₹{result["random_forest_price"]:,.2f}
                        </div>
                        <div class="prediction-price-label" style="color:#66758a;">
                            Estimated price after 5 trading days
                        </div>
                    </div>
                    """
                )


            # DISCLAIMER

            st.html(
                """
                <div class="disclaimer">
                    <strong>Important:</strong>
                    This application is an educational machine learning project.
                    Forecasts are generated from historical market data and simple
                    regression models. They should not be interpreted as financial
                    advice or investment recommendations.
                </div>
                """
            )
            

        except Exception as e:

            st.error(
                f"Unable to generate forecast: {e}"
            )

else:

    st.markdown(
        """
        <div style="
            background:white;
            padding:60px 40px;
            border-radius:12px;
            border:1px solid #e1e6ec;
            text-align:center;
            margin-top:20px;
        ">

        <div style="
            font-size:28px;
            font-weight:700;
            color:#16263d;
        ">
        Market Intelligence Dashboard
        </div>

        <div style="
            font-size:15px;
            color:#718096;
            margin-top:12px;
        ">
        Select a NIFTY 50 stock from the sidebar to generate
        a machine learning based 5-day forecast.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="disclaimer">
            Select a stock and click <strong>GENERATE FORECAST</strong>
            to begin the analysis.
        </div>
        """,
        unsafe_allow_html=True
    )
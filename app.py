# app.py
import streamlit as st
import pandas as pd
import time
from backend import generate_data, check_alert

# --- Page Config ---
st.set_page_config(page_title="Coastal Threat Alert System",
                   page_icon="🌊",
                   layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f0f9ff;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 38px;
        color: #005f73;
        font-weight: bold;
    }
    .alert-box {
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        font-weight: bold;
    }
    .danger {
        background-color: #ffccd5;
        color: #b00020;
    }
    .safe {
        background-color: #d3f9d8;
        color: #2d6a4f;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>🌊 Coastal Threat Alert System</div>", unsafe_allow_html=True)

# --- Dashboard ---
placeholder = st.empty()
data_log = []

for i in range(20):  # simulate 20 updates
    data = generate_data()
    alerts = check_alert(data)
    data_log.append(data)

    # Layout
    with placeholder.container():
        col1, col2 = st.columns(2)

        # Sensor Data
        with col1:
            st.subheader("📊 Live Sensor Data")
            df = pd.DataFrame([data])
            st.dataframe(df, use_container_width=True)

        # Alerts
        with col2:
            st.subheader("🚨 Alerts")
            for alert in alerts:
                if "Safe" in alert:
                    st.markdown(f"<div class='alert-box safe'>{alert}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='alert-box danger'>{alert}</div>", unsafe_allow_html=True)

        # Historical Data
        st.subheader("📈 Historical Trends")
        df_hist = pd.DataFrame(data_log)
        st.line_chart(df_hist, use_container_width=True)

    time.sleep(2)

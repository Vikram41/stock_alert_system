# config/settings.py

import streamlit as st

EMAIL_SENDER = st.secrets["email"]["sender"]
EMAIL_PASSWORD = st.secrets["email"]["password"]
SMTP_SERVER = st.secrets["email"]["smtp_server"]
SMTP_PORT = st.secrets["email"]["smtp_port"]

# Scheduler configuration
SCHEDULER_SETTINGS = {
    "hour": 18,   # 6 PM IST
    "minute": 30  # 30 minutes past the hour
}

# Bhavcopy URL structure (base URL for fetching bhavcopy)
BHAVCOPY_BASE_URL = "https://archives.nseindia.com/content/historical/EQUITIES/"

import streamlit as st
from modules.fetch_bhavcopy import fetch_first_trading_day, fetch_bhavcopy
from modules.process_bhavcopy import process_and_check_alerts
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Streamlit app layout
st.title("📈 Stock Alert System Dashboard")
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Manual Update", "Logs & History"])

# Home page: Daily Stock Alerts
if page == "Home":
    st.header("🚀 Daily Stock Alerts")
    st.write("The latest daily stock alerts will appear here after the daily check.")
    
    if st.button("🔄 Run Daily Check Now"):
        st.info("Fetching today's bhavcopy and running checks...")
        latest_bhavcopy = fetch_bhavcopy()
        if latest_bhavcopy:
            st.success(f"Successfully fetched and processed: {latest_bhavcopy}")
            process_and_check_alerts(latest_bhavcopy)
        else:
            st.error("❌ Failed to fetch today's bhavcopy.")

# Manual Update: Monthly Bhavcopy Update
elif page == "Manual Update":
    st.header("🗓 Update Monthly Bhavcopy")
    st.write("Click the button below to fetch and update the bhavcopy for the first trading day of this month.")
    
    if st.button("📅 Fetch First Trading Day Bhavcopy"):
        st.info("Fetching the first trading day's bhavcopy...")
        first_day_bhavcopy = fetch_first_trading_day()
        if first_day_bhavcopy:
            st.success(f"Successfully saved: {first_day_bhavcopy}")
        else:
            st.error("❌ Failed to fetch the first trading day's bhavcopy.")

# Logs & History: Display logs or alert history
elif page == "Logs & History":
    st.header("📜 Logs & History")
    st.write("Display log files or past alert data here.")
    
    try:
        with open("logs/app.log", "r") as log_file:
            logs = log_file.read()
            st.text_area("Logs", logs, height=300)
    except FileNotFoundError:
        st.warning("Log file not found.")

# Footer info
st.sidebar.info("Developed by [Your Name]. Powered by Streamlit.")

# main.py
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from modules.fetch_bhavcopy import fetch_bhavcopy, fetch_first_trading_day
from modules.process_bhavcopy import process_and_check_alerts
from config.settings import EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_PASSWORD

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

scheduler = BlockingScheduler()

def daily_task():
    """
    Daily task to fetch the latest bhavcopy and check if any stocks trigger alerts.
    It checks high, low, and close prices against Fibonacci levels.
    """
    logging.info("Running daily stock check...")
    latest_bhavcopy = fetch_bhavcopy()
    if latest_bhavcopy:
        logging.info(f"Processing daily bhavcopy: {latest_bhavcopy}")
        process_and_check_alerts(latest_bhavcopy)
    else:
        logging.warning("Failed to fetch the daily bhavcopy.")

def monthly_task():
    """
    Monthly task to fetch the bhavcopy for the first trading day of the current month.
    This file is used to calculate the Fibonacci levels for alerts.
    """
    logging.info("Running monthly update to fetch the first trading day's bhavcopy...")
    first_day_bhavcopy = fetch_first_trading_day()
    if first_day_bhavcopy:
        logging.info(f"First trading day bhavcopy saved as: {first_day_bhavcopy}")
    else:
        logging.warning("Failed to fetch the first trading day's bhavcopy.")

# Schedule daily task at 6:30 PM IST (13:00 UTC)
scheduler.add_job(daily_task, 'cron', hour=13, minute=0)

# Schedule monthly task on the 1st day of every month at 6:30 PM IST (13:00 UTC)
scheduler.add_job(monthly_task, 'cron', day=1, hour=13, minute=0)

if __name__ == "__main__":
    logging.info("Scheduler started. Press Ctrl+C to exit.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Scheduler stopped.")

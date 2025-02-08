import requests
import os
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st  # For reading secrets
from modules.settings import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

# Directory to save bhavcopy files
DATA_DIR = "data/bhavcopy"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_first_trading_day():
    """Fetches and saves the bhavcopy for the first trading day of the current month."""
    today = datetime.datetime.now()
    first_day = today.replace(day=1).strftime("%Y%m%d")
    
    url = f"https://archives.nseindia.com/products/content/sec_bhavdata_full_{first_day}.csv"
    response = requests.get(url)
    
    if response.status_code == 200:
        file_path = os.path.join(DATA_DIR, f"bhavcopy_{first_day}.csv")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"✅ First trading day bhavcopy saved at: {file_path}")
        return file_path
    else:
        print(f"❌ Failed to fetch first trading day bhavcopy for {first_day}.")
        return None

def fetch_bhavcopy():
    """Fetches and saves the bhavcopy for today's date."""
    today = datetime.datetime.now().strftime("%Y%m%d")
    url = f"https://archives.nseindia.com/products/content/sec_bhavdata_full_{today}.csv"
    response = requests.get(url)
    
    if response.status_code == 200:
        file_path = os.path.join(DATA_DIR, f"bhavcopy_{today}.csv")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"✅ Today's bhavcopy saved at: {file_path}")
        return file_path
    else:
        print(f"❌ Failed to fetch today's bhavcopy for {today}.")
        return None

def send_email(recipient, subject, message):
    """Sends an email alert with the provided subject and message."""
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    # Example usage
    print("Fetching first trading day bhavcopy...")
    first_day_file = fetch_first_trading_day()
    
    if first_day_file:
        send_email(
            recipient="your_email@example.com",
            subject="First Trading Day Bhavcopy Update",
            message=f"The first trading day's bhavcopy has been saved: {first_day_file}"
        )

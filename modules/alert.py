# modules/alert.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(qualifying_stocks):
    """
    Sends an email alert with the list of stocks that are near Fibonacci levels.
    """
    if not qualifying_stocks:
        print("No stocks to send an alert for.")
        return
    
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    subject = "Stock Alert: Stocks Near Fibonacci Levels"
    
    # Create the email body
    body = "<h3>Stocks Near Fibonacci Levels</h3><ul>"
    for stock in qualifying_stocks:
        body += f"<li>{stock['symbol']} - Level: {stock['level']}, Price: {stock['price']:.2f}, Fibonacci Level: {stock['fibonacci_level']:.2f}</li>"
    body += "</ul>"
    
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    
    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, "your_password")
            server.send_message(msg)
        print("Email alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
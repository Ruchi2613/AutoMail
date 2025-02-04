from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

# Access the variables
EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# List of recipients
recipients = ["ruchipandey2606@gmail.com", "ruchiap2606@gmail.com"]

# Email content
subject = "Test Email"
body = "Hello, this is a test email sent via Python script."

# Create SMTP session
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Use Gmail SMTP server
    server.starttls()  # Secure connection
    server.login(EMAIL_ID, EMAIL_PASSWORD)  # Login to your email

    for recipient in recipients:
        # Construct the email
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ID
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send email
        server.sendmail(EMAIL_ID, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    # Close server connection
    server.quit()
    print("All emails sent successfully!")

except Exception as e:
    print(f"Error: {e}")

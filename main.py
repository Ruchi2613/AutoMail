# from dotenv import load_dotenv
# import os
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# # Load environment variables from .env file
# load_dotenv()
#
# # Access the variables
# EMAIL_ID = os.getenv("EMAIL_ID")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
#
#
# # List of recipients
# recipients = ["ruchipandey2606@gmail.com", "ruchiap2606@gmail.com"]
#
# # Email content
# subject = "Test Email"
# body = "Hello, this is a test email sent via Python script."
#
# # Create SMTP session
# try:
#     server = smtplib.SMTP("smtp.gmail.com", 587)  # Use Gmail SMTP server
#     server.starttls()  # Secure connection
#     server.login(EMAIL_ID, EMAIL_PASSWORD)  # Login to your email
#
#     for recipient in recipients:
#         # Construct the email
#         msg = MIMEMultipart()
#         msg["From"] = EMAIL_ID
#         msg["To"] = recipient
#         msg["Subject"] = subject
#         msg.attach(MIMEText(body, "plain"))
#
#         # Send email
#         server.sendmail(EMAIL_ID, recipient, msg.as_string())
#         print(f"Email sent to {recipient}")
#
#     # Close server connection
#     server.quit()
#     print("All emails sent successfully!")
#
# except Exception as e:
#     print(f"Error: {e}")


'''   This script is to send multiple message to mass recruiters'''
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
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# List of recipients
recipients = [
    # "x@amazon.com",
    # "d@google.com",
    # "h@facebook.com"
    "ruchipandey2606@gmail.com",
    "ruchiap2606@gmail.com"
]

# Mapping email domains to company names
company_map = {
    "amazon.com": "Amazon",
    "google.com": "Google",
    "facebook.com": "Meta",
    "gmail.com":"Google"
}


# Function to extract domain and company name
def get_company(email):
    domain = email.split("@")[-1]  # Extracts domain (e.g., amazon.com)
    # print(domain)
    return company_map.get(domain, "your company")  # Default to "your company" if unknown


# Establish connection to SMTP server
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ID, EMAIL_PASSWORD)

    for recipient in recipients:
        company_name = get_company(recipient)  # Get company name from email domain

        # Email subject and body
        subject = f"Opportunity with {company_name}"

        # body = f"""Hello {company_name} Recruiter,
        body = f"""Hello,

I am excited about opportunities at {company_name} and would love to discuss my qualifications further.

Best regards,
Ruchi Pandey
"""

        # Create MIME email object
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ID
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send email
        server.sendmail(EMAIL_ID, recipient, msg.as_string())
        print(f"Email sent successfully to {recipient} ({company_name})")

except Exception as e:
    print(f"Error: {e}")

finally:
    server.quit()

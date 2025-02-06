
'''   This script is to send multiple message to mass recruiters with resume'''
# Import required libraries
from dotenv import load_dotenv  # Used to load environment variables from a .env file
import os  # Provides functions to interact with the operating system (like accessing environment variables)
import smtplib  # Library to send emails using SMTP (Simple Mail Transfer Protocol)
from email.mime.multipart import MIMEMultipart  # Helps create a multipart email (text + attachments)
from email.mime.text import MIMEText  # Handles the email's plain text content
from email.mime.application import MIMEApplication  # Allows adding attachments to the email

# Load environment variables from the .env file (which contains sensitive credentials securely)
load_dotenv()

# Retrieve email credentials from environment variables to avoid hardcoding sensitive data
EMAIL_ID = os.getenv("EMAIL_ID")  # Your email ID (used as the sender)
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Your email password (or app password if 2FA is enabled)

# SMTP server configuration for Gmail (Change if using another provider)
SMTP_SERVER = "smtp.gmail.com"  # Gmail's SMTP server address
SMTP_PORT = 587  # Port number for sending emails securely using TLS

# List of recipients (Modify this list to add more email addresses)
recipients = [
    "ruchipandey2606@gmail.com",
    "ruchiap2606@gmail.com"
]

# Dictionary to map email domains to company names (Used for a personalized subject and greeting)
company_map = {
    "amazon.com": "Amazon",
    "google.com": "Google",
    "facebook.com": "Meta",
    "gmail.com": "Google"  # If sending to Gmail, default to Google
}

# Function to extract the company name based on the email domain
def get_company(email):
    domain = email.split("@")[-1]  # Extracts domain from the email (e.g., "amazon.com")
    return company_map.get(domain, "your company")  # Returns company name or "your company" if not found

# Path to the resume file that will be attached to the email
resume_path = "/Users/ruchi/Downloads/Ruchi_pandey_Resumee1.pdf"  # Ensure this file exists in the same directory as the script

# Establishing a connection to the SMTP server
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)  # Connect to the SMTP server using the specified address and port
    server.starttls()  # Upgrade the connection to a secure encrypted TLS connection
    server.login(EMAIL_ID, EMAIL_PASSWORD)  # Log in to the SMTP server using the provided credentials

    # Loop through each recipient to send a personalized email
    for recipient in recipients:
        company_name = get_company(recipient)  # Get company name from email domain

        # Define email subject (personalized for each recipient)
        subject = f"Opportunity with {company_name}"

        # Email body content (customized greeting and message)
        body = f"""Hello,

I am excited about opportunities at {company_name} and would love to discuss my qualifications further.

Best regards,  
Ruchi Pandey
"""

        # Create a MIME multipart email object (Allows adding text and attachments)
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ID  # Set sender's email
        msg["To"] = recipient  # Set recipient's email
        msg["Subject"] = subject  # Set the email subject
        msg.attach(MIMEText(body, "plain"))  # Attach the plain text email body

        # Attempt to attach the resume file
        try:
            with open(resume_path, "rb") as attachment:  # Open the file in binary mode
                part = MIMEApplication(attachment.read(), Name=os.path.basename(resume_path))  # Read file content
                part["Content-Disposition"] = f'attachment; filename="{os.path.basename(resume_path)}"'  # Set attachment name
                msg.attach(part)  # Attach the file to the email
        except Exception as e:
            print(f"Could not attach file: {e}")  # Print an error message if the file cannot be attached

        # Send the email
        server.sendmail(EMAIL_ID, recipient, msg.as_string())  # Convert message to string format and send
        print(f"Email sent successfully to {recipient} ({company_name})")  # Confirmation message

except Exception as e:
    print(f"Error: {e}")  # Print any errors that occur during email sending

finally:
    server.quit()  # Close the SMTP connection after sending emails

Why dotenv?

.env files store sensitive credentials securely (e.g., email/password) instead of hardcoding them.
load_dotenv() reads variables from .env, and os.getenv("KEY") retrieves them.
Why smtplib?

This is Python’s built-in library for sending emails using an SMTP server.
server.starttls() ensures a secure connection using encryption.
server.sendmail(EMAIL_ID, recipient, msg.as_string()) sends the email.
Why email.mime libraries?

MIMEMultipart: Allows emails to have multiple parts (text + attachment).
MIMEText: Stores plain text content.
MIMEApplication: Handles attachments like PDFs.
Why try-except-finally?

Ensures the email process does not crash if an error occurs.
The SMTP connection always closes in finally, preventing memory leaks.
Why is the file opened in "rb" mode?

"rb" (read binary) is used because attachments (like PDFs) are not plain text.

# Handles sending emails
import smtplib
from email.mime.text import MIMEText
from config.config_loader import Config

class EmailSender:
    def __init__(self):
        self.config = Config()
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.email_address = self.config.email_address
        self.email_password = self.config.email_password

    def send_email(self, to_address, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.email_address
        msg['To'] = to_address

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.sendmail(self.email_address, [to_address], msg.as_string())
        print(f"Email sent to {to_address}")

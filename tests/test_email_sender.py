
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mail.email_sender import EmailSender

def main():
    sender = EmailSender()
    to_address = input("Enter recipient email: ")
    subject = "Test Email from Email Agent"
    body = "This is a test email sent by the Email Wake-Up Agent."
    sender.send_email(to_address, subject, body)
if __name__ == "__main__":
    main()


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mail.email_receiver import EmailReceiver

def main():
    receiver = EmailReceiver()
    emails = receiver.fetch_unread_emails()
    if not emails:
        print("No unread emails found.")
    for idx, mail in enumerate(emails, 1):
        print(f"\nEmail #{idx}")
        print(f"From: {mail['from']}")
        print(f"Subject: {mail['subject']}")
        print(f"Body: {mail['body']}")

if __name__ == "__main__":
    main()

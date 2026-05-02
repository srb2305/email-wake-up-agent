# Handles receiving emails
import imaplib
import email
from config.config_loader import Config

class EmailReceiver:
    def __init__(self):
        self.config = Config()
        self.imap_server = 'imap.gmail.com'
        self.email_address = self.config.email_address
        self.email_password = self.config.email_password

    def fetch_unread_emails(self):
        def safe_decode(payload, charset=None):
            if charset:
                try:
                    return payload.decode(charset)
                except Exception:
                    pass
            try:
                return payload.decode('utf-8')
            except Exception:
                try:
                    return payload.decode('latin1')
                except Exception:
                    return payload.decode(errors='replace')

        with imaplib.IMAP4_SSL(self.imap_server) as mail:
            mail.login(self.email_address, self.email_password)
            mail.select('inbox')
            status, messages = mail.search(None, '(UNSEEN)')
            email_ids = messages[0].split()
            emails = []
            for eid in email_ids:
                status, msg_data = mail.fetch(eid, '(RFC822)')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = msg['subject']
                        from_ = msg['from']
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == 'text/plain' and not part.get('Content-Disposition'):
                                    charset = part.get_content_charset()
                                    body = safe_decode(part.get_payload(decode=True), charset)
                        else:
                            charset = msg.get_content_charset()
                            body = safe_decode(msg.get_payload(decode=True), charset)
                        emails.append({'from': from_, 'subject': subject, 'body': body})
            return emails

import smtplib
from email.mime.text import MIMEText

class AlertSystem:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_alert(self, recipient_email, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, [recipient_email], msg.as_string())

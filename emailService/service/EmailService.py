import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

from service.MysqlService import save_email

load_dotenv()

sender = os.environ["email-sender"]
password = os.environ["email-password"]
recipients = os.environ["email-recipient"]
subject = "Message from Portfolio Website"


def send_email(message):
    save_email(message)
    email_content = f"""
                Name: {message['name']},
                Email: {message['email']},
                Message: {message['message']}
                """
    msg = MIMEText(email_content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

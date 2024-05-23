import mysql.connector
import os
from dotenv import load_dotenv

from model.email import Email

load_dotenv()
db_host = os.environ["db-host"]
db_username = os.environ["db-username"]
db_password = os.environ["db-password"]


def save_email(message):
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_username,
        password=db_password,
        database='email_service_prod'
    )

    email = Email(message['email'], message['name'], message['message'])

    add_email = ("INSERT INTO email "
                 "(email_from, name_from, body, timestamp) "
                 "VALUES (%s, %s, %s, %s)")
    email_data = (email.email, email.name, email.message, email.created_at)

    cursor = mydb.cursor()
    cursor.execute(add_email, email_data)

    mydb.commit()
    cursor.close()
    mydb.close()

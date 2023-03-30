from dotenv.main import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import os

load_dotenv()

email_sender = "siddharthsaachi@gmail.com"
password = os.environ['PASSWORD']
email_receiver = "yomaji1178@asoflex.com"

subject = "Hi There"

body = "My First PYthon Project"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


# 465 is the default port that is used for secure sending and receiving of email

# 🚩 Dada Ki Jay Ho 🚩


import smtplib
from datetime import datetime
from email.message import EmailMessage


def send_stated_email(sub="Achintya Activated", body="Achintya is Activated at " + str(datetime.now())):
    password = "qcpbwpcnfjvjnijd"
    msg = EmailMessage()
    msg['Subject'] = sub
    msg['From'] = "rajdaveomns1@gmail.com"
    msg['To'] = "rajdaveomns1@gmail.com"
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('rajdaveomns1@gmail.com', password)
        smtp.send_message(msg)
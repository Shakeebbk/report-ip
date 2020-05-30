#!/usr/bin/env python3

import sys
import smtplib, ssl
import os

from_email = sys.argv[1]
to_email = sys.argv[2]
subject = sys.argv[3]
message_file = sys.argv[4]

import json
SERVER_EMAIL_USER = ''
SERVER_EMAIL_PASS = ''
with open('secret.json') as f:
    json_str = f.read()
    secret = json.loads(json_str)
    SERVER_EMAIL_USER = secret['EMAIL_USER']
    SERVER_EMAIL_PASS = secret['EMAIL_PASS']

def sendmail():
    import smtplib, ssl
    import os
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    port = 465  # For SSL
#    server_email = os.getenv("EMAIL_USER")
#    server_password = os.getenv("EMAIL_PASS")
    server_email = SERVER_EMAIL_USER
    server_password = SERVER_EMAIL_PASS

    # Create a secure SSL context
    context = ssl.create_default_context()

    msg = MIMEMultipart()
    msg['Subject'] = f"[Automated pymail] {subject}"
    msg['From'] = from_email
    msg['To'] = to_email
#    img_data = open(message, 'rb').read()
#    image = MIMEImage(img_data, name=os.path.basename(message))
#    msg.attach(image)
    with open(message_file) as f:
        msg.attach(MIMEText(f.read()))
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(server_email, server_password)
            server.sendmail(from_email, to_email, msg.as_string())

sendmail()

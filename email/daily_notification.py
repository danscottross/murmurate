import smtplib
from email.mime.text import MIMEText
import datetime as dt
import sys

sys.path.append('/Users/danross/GitHub/murmurate/words')
sys.path.append('/Users/danross/GitHub/murmurate/email')

import get_words_from_sheets as gswords

today = dt.datetime.today().strftime("%A, %B %-d, %Y")

df = gswords.retrieve(3)

df_html = df.to_html()

subject = f"Murmurate - {today}"
body = f"""
<html>
  <head><b><u>Words of the Day</b></u></head>
  <body>
    <p>
        {df_html}
        <br>
       <i>This message was sent on {dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}</i>
    </p>
  </body>
</html>
"""
sender = "murmurate8@gmail.com"
recipients = ["danscottross@gmail.com"]

with open("email/gmail_app_password.txt") as f:
    password = f.read()

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)

#print(subject, body, sender)

# 12 21 * * * /Users/danross/anaconda3/bin/python.app /Users/danross/Desktop/murmurate/Words/email_notification.py

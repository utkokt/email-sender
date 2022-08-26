import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'from email'
email['to'] = 'to email'
email['subject'] = 'Subject'

email.set_content(html.substitute(name= 'to name'), 'html')

with smtplib.SMTP(host='smtp.emailservice.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('from email', 'from password')
    smtp.send_message(email)
    print('all good boss!')

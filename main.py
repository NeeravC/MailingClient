import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('neeravcr@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Neerav'
msg['To'] = 'fazeclansorra@gmail.com'
msg['Subject'] = 'Testing'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'lion.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('neeravcr@gmail.com', 'fazeclansorra@gmail.com', text)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email

def connect_to_gmail():
    url = 'smtp.gmail.com'
    try:
        mail = smtplib.SMTP(url, 587)
        mail.starttls()
        mail.login("<gmail email>", "<gmail app apssword>")
        print("Connected To SMTP")
        return mail
    except Exception as e:
        raise

gmailsmtp = connect_to_gmail()
msg = MIMEMultipart()
msg['From'] = '<email>'
msg['To'] = input("To: ")
msg['Subject'] = input('Subject: ')
msg.attach(MIMEText(input('Body: '), 'plain'))
print('Created Email')
gmailsmtp.send_message(msg)
print('Sent Email')
gmailsmtp.quit()
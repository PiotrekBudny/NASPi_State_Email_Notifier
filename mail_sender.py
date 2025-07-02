import smtplib, ssl
import config
from email.message import EmailMessage
from email.mime.text import MIMEText
import os

settings = config.mailSettings

def send_notification_mail(mailContent):
    message = generate_mail_template_with_data(mailContent);       
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(settings['smtp_address'], settings['port'])
        server.starttls(context=context) 
        server.login(settings['sender_mail'], settings['app_password'])
        server.send_message(message, settings['sender_mail'], settings['destination_mail'])
    except Exception as e:
        print(e)
    finally:
        server.quit()

def generate_mail_template_with_data(content):
    msg = EmailMessage()
    msg['Subject'] = settings['default_subject']
    msg['From'] = settings['default_from']
    msg['To'] = settings['default_to']
    path = os.getcwd()
    
    with open(path + '/resources/mailTemplate.html', 'r') as f:
        html_string = f.read()
        new_html = html_string.replace("{{driveState}}", content)
    
    body = MIMEText(new_html, 'html')
    
    msg.set_content(body)
    return msg

import smtplib, ssl
import config
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

settings = config.mailSettings

def sendNotificationMail(mailContent):
    message = generateMailTemplateWithData(mailContent);       
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

def generateMailTemplateWithData(content):
    msg = EmailMessage()
    msg['Subject'] = settings['default_subject']
    msg['From'] = settings['default_from']
    msg['To'] = settings['default_to']
    
    with open('resources/mailTemplate.html', 'r') as f:
        html_string = f.read()
        new_html = html_string.replace("{{driveState}}", content)
    
    body = MIMEText(new_html, 'html')
    
    msg.set_content(body)
    return msg

import smtplib, ssl
import config
from email.message import EmailMessage

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
    msg.set_content(content)
    return msg
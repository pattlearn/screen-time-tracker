import os
import smtplib
import threading
from email.message import EmailMessage
import mimetypes

SENDER = os.getenv("EMAILING_EMAIL")
RECIEVER = os.getenv("EMAILING_EMAIL")
PASSWORD = os.getenv("EMAILING_PASSWORD")

def send_email(filename, date):
    msg = EmailMessage()
    msg["Subject"] = f"Productivity report on {date}"
    msg.set_content(f"This is a user productivity report on day {date}")
    
    # guess type
    mime_type, _ = mimetypes.guess_type(filename)
    mime_type, mime_subtype = mime_type.splt("/")
    
    with open(filename, "rb") as file:
        file_data = file.read()
        msg.add_attachment(
            file_data, 
            maintype=mime_type, 
            subtype=mime_subtype,
            filename=filename
        )
    
    # send the email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, msg.as_string())
    gmail.quit()
    
    print("Email was sent")
    
    return
import os
import smtplib
from threading import Thread
from email.message import EmailMessage
import mimetypes

SENDER = os.getenv("EMAILING_EMAIL")
RECIEVER = os.getenv("EMAILING_EMAIL")
PASSWORD = os.getenv("EMAILING_PASSWORD")

# sending email with attached file
def send_email(filename, date, folder_path="./records"):
    file_path = os.path.join(folder_path, filename)
    msg = EmailMessage()
    msg["Subject"] = f"Productivity report on {date}"
    msg.set_content(f"This is a user productivity report on day {date}")
    
    # guess type
    mime_type, _ = mimetypes.guess_type(file_path)
    mime_type, mime_subtype = mime_type.split("/")
    
    with open(file_path, "rb") as file:
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
    
    remove_file_thread = Thread(target=remove_file(filename=filename))
    remove_file_thread.daemon = True
    remove_file_thread.start()
    
    return

# check number of files in folder
def check_sending(folder_path="./records"):
    file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    
    return file_count

# clean folder
def remove_file(filename, folder_path="./records"):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

if __name__ == "__main__":
    if check_sending() > 0:
        remove_file()
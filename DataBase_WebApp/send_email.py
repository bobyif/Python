import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#The mail addresses and password
def send_email(email, height, average_height, count):
    from_email = "boyanfotev@gmail.com"
    from_password = "belograd4ik2006"
    to_email = email
    subject = "Height data"
    mail_content ="Hello,This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.Thank You"

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(from_email, from_password)
    text = message.as_string()
    session.sendmail(from_email, to_email, text)
    session.quit()
    print('Mail Sent')

#>>>>>>>>>>>>>>>>>>> GIVE AN UP VOTE IF YOU LIKED IT <<<<<<<<<<<<<<<<<<<<<
#Easiest and Readable way to Email
#through Python SMTPLIB library
#This works with >>> Gmail.com <<<
import smtplib 
from email.message import EmailMessage

EmailAdd = "bobyif.if@gmail.com" #senders Gmail id over here
Pass = "guccibagador222" #senders Gmail's Password over here

msg = EmailMessage()
msg['Subject'] = 'hello' # Subject of Email
msg['From'] = "boyanfotev@gmail.com"
msg['To'] = 'boyanfotev@gmail.com' # Reciver of the Mail
msg.set_content('boyanfotev@gmail.com') # Email body or Content

#### >> Code from here will send the message << ####
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #Added Gmails SMTP Server
    smtp.login(EmailAdd,Pass) #This command Login SMTP Library using your GMAIL
    smtp.send_message(msg) #This Sends the message
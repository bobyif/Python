import smtplib
from datetime import datetime
time = datetime.now()
time1 = time.strftime("%x, %X")
SUBJECT = "We saw action on you cameras you may have to check them!"

TEXT = "At that time there was detected movement :" + time1
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)


def send_email():
    print("start")
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("boyanfotev@gmail.com", "belograd4ik2006")
    server.sendmail("boyanfotev@gmail.com",
                    "bobyif.if@gmail.com",
                    message)

    server.quit()
    print("end")


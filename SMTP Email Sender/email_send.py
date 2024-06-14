import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import speechtotext
import time

# smtp gmail

def email_main():
    to = "xyx@gmail.com"
    user = "abc@gmail.com"
    password = "I can't tell you !!"


    smtpserver = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
    print("Here")
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login ( user, password)

    print("Here")

    msg = MIMEMultipart()

    msg['To']=to
    msg['From']=user
    print("say subject")
    text=speechtotext.stot()
    print(text)
    msg['Subject']=text

    msg.attach(MIMEText("Hello"))


    #mail
    fp=open('dog.png','rb')
    msg.attach(MIMEImage(fp.read()))

    smtpserver.sendmail ( user, to , msg.as_string())

    #smtpserver.close()

    print("mailed !!")



import smtplib

sender01 = 'mhatreanushka99@gmail.com'
receiver01 = ['akshay.mewada@neosoftmail.com']
password01 = input("Enter your password: ")
message01 = """From: From Anushka <mhatreanushka99@gmail.com>
To: To Akshay Mewada <akshay.mewada@neosoftmail.com>
Subject: test mail

this mail is sent using python
"""
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.starttls()
smtp_obj.login(sender01, password01)
print("Login success")
smtp_obj.sendmail(sender01, receiver01, message01)
print("Successfully sent")


Bcc: Bcc Rohan.dhere <rohan.dhere@neosoftmail.com>,Vibha rawan <vibha.rawan@neosoftmail.com>
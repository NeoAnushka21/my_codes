import smtplib

try:
    from configparser import ConfigParser
except ImportError:
    from configparser import ConfigParser

my_config = ConfigParser()
my_config.read('my_config01_.ini')

sender_mail = my_config.get('section A', 'sender_mail')
sender_mail_password = my_config.get('section A', 'sender_mail_password')

cc = my_config.get('section A', 'cc')
cc01 = cc.split(',')

bcc = my_config.get('section A', 'bcc')
bcc01 = bcc.split(',')
receiver_mail = [my_config.get('section A', 'receiver_mail')] + cc01 + bcc01


message01 = """From: From Anushka <anushka.mhatre@neosoftmail.com>
To: To Akshay Mewada <akshay.mewada@neosoftmail.com>
Cc: Cc Arun Nadar <arun.nadar@neosoftmail.com> ,
Subject: test mail

this mail is sent using python
"""
smtp_obj = smtplib.SMTP('neosoftmail.com', 587)
smtp_obj.starttls()
smtp_obj.login(sender_mail, sender_mail_password)
smtp_obj.sendmail(sender_mail, receiver_mail, message01)
print("sent successfully")

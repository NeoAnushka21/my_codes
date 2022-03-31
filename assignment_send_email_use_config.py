# importing smtp(simple mail transfer protocol ) library
import smtplib

# using exception handing to tackle error
try:
    from configparser import ConfigParser
except ImportError:
    from configparser import ConfigParser

# created a config file for storing passwords , email ID's and other sensitive data
# Creating an object for class ConfigParser()
my_config = ConfigParser()
my_config.read('my_config_file_.ini')            # reading data from config file

# fetching mails and password
sender_mail = my_config.get('section A', 'sender_mail')
sender_mail_password = my_config.get('section A', 'sender_mail_password')

cc = my_config.get('section A', 'cc')
cc01 = cc.split(',')

bcc = my_config.get('section A', 'bcc')
bcc01 = bcc.split(',')
receiver_mail = [my_config.get('section A', 'receiver_mail')] + cc01 + bcc01

# message in string will get sent as it is
message01 = """From: Anushka <anushka.mhatre@neosoftmail.com>
To: 'vibha.rawan@neosoftmail.com' <vibha.rawan@neosoftmail.com>
Cc: Arun Nadar <arun.nadar@neosoftmail.com> 
Subject: Test mail

This mail is sent using python
"""

smtp_obj = smtplib.SMTP('neosoftmail.com', 587)
smtp_obj.starttls()
smtp_obj.login(sender_mail, sender_mail_password)
smtp_obj.sendmail(sender_mail, receiver_mail, message01)
print("sent successfully")

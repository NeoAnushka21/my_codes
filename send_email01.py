import smtplib
sender01 = 'anushka.mhatre@neosoftmail.com'
cc01 = ['arun.nadar@neosoftmail.com']
bcc01 = ['rohan.dhere@neosoftmail.com', 'vibha.rawan@neosoftmail.com']
receiver01 = ['akshay.mewada@neosoftmail.com'] + cc01 + bcc01
message01 = """From: From Anushka <anushka.mhatre@neosoftmail.com>
To: To Akshay Mewada <akshay.mewada@neosoftmail.com>
Cc: Cc Arun Nadar <arun.nadar@neosoftmail.com>
Subject: test mail

this mail is sent using python
"""
smtp_obj = smtplib.SMTP('neosoftmail.com', 587)
smtp_obj.starttls()
smtp_obj.login('anushka.mhatre@neosoftmail.com', '08fAxaAONaAV')
smtp_obj.sendmail(sender01, receiver01, message01)
print("sent successfully")

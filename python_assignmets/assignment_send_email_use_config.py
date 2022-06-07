# Importing smtp(simple mail transfer protocol ) library
import smtplib
# For accessing data from config file
from configparser import ConfigParser


def main():
    # Created a config file for storing passwords , email ID's and other sensitive data

    # Creating an object for class ConfigParser()
    my_config = ConfigParser()

    # Reading data from config file
    my_config.read('/home/neosoft/PycharmProjects/python_practice_codes/_my_config_file_.ini')

    # Fetching mails and password
    sender_mail = my_config.get('credentials', 'sender_mail')
    sender_mail_password = my_config.get('credentials', 'sender_mail_password')

    cc = my_config.get('email_details', 'cc')
    cc01 = cc.split(',')
    bcc = my_config.get('email_details', 'bcc')
    bcc01 = bcc.split(',')
    subject = my_config.get('email_details', 'subject')
    message_content = my_config.get('email_details', 'message')
    receiver_mail = [my_config.get('email_details', 'receiver_mail')] + cc01 + bcc01

    message01 = "From: %s\r\n" % sender_mail \
              + "To: %s\r\n" % receiver_mail \
              + "CC: %s\r\n" % ",".join(cc01) \
              + "Bcc: %s\r\n" % ",".join(bcc01) \
              + "Subject: %s\r\n" % subject \
              + "\r\n" + message_content

    smtp_obj = smtplib.SMTP('neosoftmail.com', 587)
    smtp_obj.starttls()   # Establishing secure connection
    smtp_obj.login(sender_mail, sender_mail_password)
    smtp_obj.sendmail(sender_mail, receiver_mail, message01)
    print("sent successfully")


if __name__ == "__main__":
    main()

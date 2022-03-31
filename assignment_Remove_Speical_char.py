# re is the Regular Expression (RegEx module)
import re

# A string with special characters
str1 = "This#string%contains^special*characters&."

# Giving a regular expression which will only accept alphanumeric values
# when encounter with any other replace it with space
new_str1 = re.sub(r'[^a-zA-Z0-9]', ' ', str1)
print(new_str1)


str2 = "hey@yo%ggs_xbshd&nfnf%gdbv%"

# declaring a string with all speical characters
# if given string encounter any of those from regEx , replace with space
regex01 = r'@_!#$%^&*()<>?/\|}{~:;[]'
for i in str2:
    if i in regex01:
        str2 = str2.replace(i, " ")
print(str2)

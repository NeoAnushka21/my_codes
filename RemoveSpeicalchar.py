import re              # Regular Expression (RegEx module)
str1 = "This#string%contains^special*characters&."
new_str1 = re.sub(r'[^a-zA-Z0-9]', ' ', str1)
print(new_str1)


str2 = "hey@yo%ggs_xbshd&nfnf%gdbv%"
regex01 = r'@_!#$%^&*()<>?/\|}{~:;[]'
for i in str2:
    if i in regex01:
        str2 = str2.replace(i, " ")
print(str2)


str3 = 'gsgs#bs@nx!nbx$*hg(n@ndd&'
new_str3 = "".join(char for char in str3 if char.isalnum())
print(new_str3)

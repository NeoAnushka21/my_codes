# importing the regular expressions module
import re


str02 = "my first number is 736367828283 and second number is 36537228"

# Extracting the combination of digits from a string
regex = '\d+'
match02 = re.findall(regex, str02)
print(match02)

# Extracting characters between given regEx class from the string

# compile() creates regular expression character class [a-g] that is a to g chars
c1 = re.compile('[a-g]')
# findall() search for reg ex in the string
c = c1.findall(str02)
print(c)


my_str = 'I went to * office at@ 10:00 am on 11th-March 2022 '

# Extracting the digits  one by one from string
c2 = re.compile('\d')
print(c2.findall(my_str))

# Extracting combination of digits
c2 = re.compile('\d+')
print(c2.findall(my_str))

# Extracting all alphanumeric values one by one
c2 = re.compile('\w')
print(c2.findall(my_str))

# Extracting combinations of alphanumeric
c2 = re.compile('\w+')
print(c2.findall(my_str))

# Extracting spaces and special characters one by one
c2 = re.compile('\W')
print(c2.findall(my_str))

# checking for given pattern
c3 = re.compile('abb*')
print(c3.findall('ababbaabbabbabba'))

# print string one by one and split when on special char
c4 = re.split('\W+',my_str)
print(c4)

# split on occurrence of a digit but only ONCE
c5 = re.split('\d+', my_str, 1)
print(c5)

# split when characters are in given range of regEx class
print(re.split('[a-d]+', my_str, flags=re.IGNORECASE))

my_str2 = 'My Favorite COLOR is black AND Blue '

# Replacing the part of string with ** where 'or' is present
m1 = re.sub('or','**', my_str2, flags=re.IGNORECASE)
print(m1)

# Replacing the part of string with ** where only lower case 'or' is present
m1 = re.sub('or', '**', my_str2)
print(m1)

#  Replacing string the part of string with ** on first occurrence of 'or'
m1 = re.sub('or', '**', my_str2, count=1, flags=re.IGNORECASE)
print(m1)

# Replacing a  certain sub-string inside string with other
m2 = re.sub(r'\sAND\s', ' & ', my_str2)
print(m2)






import re

str02 = "my first number is 736367828283 and second number is 36537228"
regex = '\d+'
match02 = re.findall(regex, str02)
print(match02)

c1 = re.compile('[a-g]')               # compile() creates regular expression character class [a-g] that is a to g chars
c = c1.findall(str02)                 # findall() search for reg ex in the string
print(c)

my_str = 'I went to * office at@ 10:00 am on 11th-March 2022 '
c2 = re.compile('\d')
print(c2.findall(my_str))
print(my_str)
c2 = re.compile('\d+')
print(c2.findall(my_str))
print(my_str)
c2 = re.compile('\w')
print(c2.findall(my_str))
print(my_str)
c2 = re.compile('\w+')
print(c2.findall(my_str))
print(my_str)
c2 = re.compile('\W')
print(c2.findall(my_str))

c3 = re.compile('abb*')
print(c3.findall('ababbaabbabbabba'))
print(my_str)
c4 = re.split('\W+',my_str)
print(c4)
print(my_str)
c5 = re.split('\d+', my_str, 1)
print(c5)
print(my_str)
print(re.split('[a-d]+', my_str, flags=re.IGNORECASE))

my_str2 = 'My Favorite COLOR is black AND Blue '
m1 = re.sub('or','**', my_str2, flags=re.IGNORECASE)
print(m1)
m1 = re.sub('or', '**', my_str2)
print(m1)
m1 = re.sub('or', '**', my_str2, count=1, flags=re.IGNORECASE)
print(m1)

m2 = re.sub(r'\sAND\s', ' & ', my_str2)
print(m2)

m1 = re.subn('or', '**', my_str2, flags=re.IGNORECASE)
print(m1)
print(m1[0])

my_str3 = 'My name is anushka'
my_str4 = 'this is [a-t] okay \ and ^ up'
print(re.escape(my_str3))
print(re.escape(my_str4))




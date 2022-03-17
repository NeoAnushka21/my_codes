import re
str01 = 'Python is a high-level, general-purpose 1 and a very popular programming language. '

match = re.search(r'.', str01)
print(match)

match = re.search(r'\.', str01)    # \ drops the special meaning of the metachar "."
print(match)


match01 = re.search(r'\d', str01)
print(match01)
match01 = re.search(r'\APyt', str01)
print(match01)



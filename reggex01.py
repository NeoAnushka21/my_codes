import re
str01 = "Python is a high-level, general-purpose and a very popular programming language."
match01 = re.search(r'very', str01)
print("Start Index of very is :", match01.start())
print("End  Index of very is :", match01.end())


# The raw string (r)is a bit different from a regular string,
# it won’t interpret the \ character as an escape character.
# This is because the regular expression engine uses \ character for its own escaping purpose.

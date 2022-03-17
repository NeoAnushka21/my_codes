import re
regex = r"([a-zA-Z]+) (\d+) (\d+)"
match = re.search(regex, "I was born on feb 21 1999")
if match != None:

    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))
    print("Year: %s" % (match.group(3)))

else:
    print("The regex pattern does not match.")

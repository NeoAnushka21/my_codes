file01 = open("python_intro.txt", "r")
read_file = file01.read()
print(read_file)

regex = "aeiou"
for i in read_file:
    i.lower()
    if i in regex:
        print(i, end=" ")

word01 = input("Enter search word:")
file01 = open("python_intro.txt", "r")
read_file = file01.read()
if word01.casefold() in read_file.casefold():        # casefold() used to remove case sensitivity
    print(word01, "is present in the file")
else:
    print(word01, "is not present in the file")



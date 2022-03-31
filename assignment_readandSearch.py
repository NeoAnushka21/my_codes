# Take any word as input to search in a text file
word01 = input("Enter search word:")

# opening file in read mode
file01 = open("python_intro.txt", "r")

# accessing the file
read_file = file01.read()

# checking existence of the  word the in file
if word01.casefold() in read_file.casefold():        # casefold() used to remove case sensitivity
    print(word01, "is present in the file")
else:
    print(word01, "is not present in the file")



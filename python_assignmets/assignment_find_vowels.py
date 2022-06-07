# Opening a file in read mode and storing it in a variable
file01 = open("python_intro.txt", "r")

read_file = file01.read()

# Printing the file which we have read
print(read_file)


def my_function():

    regex = "aeiou"  # Regular Expression
    for i in read_file:  # check each alphabet present in file
        i.lower()  # convert all characters to lower

        # for any character in file equals any character from regex, print the regex char
        if i in regex:
            print(i, end=" ")


my_function()

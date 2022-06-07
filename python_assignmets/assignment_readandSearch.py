class Read:

    def word_existence(self):

        # Take any word as input to search in a text file
        word01 = input("Enter search word:")

        # Opening file in read mode
        file01 = open("python_intro.txt", "r")

        # Accessing the file
        read_file = file01.read()

        # Checking existence of the  word the in file
        if word01.casefold() in read_file.casefold():  # Casefold() used to remove case sensitivity
            print(word01, "is present in the file")
        else:
            print(word01, "is not present in the file")


obj = Read()
obj.word_existence()

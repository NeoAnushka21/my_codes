file01 = open("python_intro.txt", "r")
my_dict = {}

for line in file01:
    line = line.strip()              # to remove leading spaces and new line chars
    line = line.lower()              # covert lowercase
    words = line.split(" ")          # split line into words

    for word in words:                  # to iterate each word in the line
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1   # if word is present in dict then increment the count by 1
        else:
            my_dict[word] = 1                    # if word is not present then add that word to dict with count=1


for key in list(my_dict.keys()):
    print(key, ":", my_dict[key],end=" ")

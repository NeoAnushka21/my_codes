n = int(input("Enter number of rows:"))
my_list = []

# i are rows
for i in range(n):
    tl = []
    # j are columns
    for j in range(i+1):
        # all values on index 0 and index i will be one
        if j == 0 or j == i:
            tl.append(1)
        else:
            # for in between values, i-1 is above row , and j is the index above sum value
            tl.append(my_list[i-1][j-1] + my_list[i-1][j])
    my_list.append(tl)

# here we have the pascals triangles rows as lists inside a list
print(my_list)

# to print each list t form triangle pattern
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(my_list[i][j], end=" ")
    print()

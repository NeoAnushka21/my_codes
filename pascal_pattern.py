n = int(input("Enter number of rows:"))
my_list = []

for i in range(n):           # i are rows j are columns
    tl = []
    for j in range(i+1):
        if j == 0 or j == i:          # all values on index 0 and index i will be one
            tl.append(1)
            # print(tl.append(1))
        else:
            tl.append(my_list[i-1][j-1] + my_list[i-1][j])              # for inbetween values, i-1 is above row , and j is the index above sum value
            # print(tl.append(my_list[i-1][j-1] + my_list[i-1][j]))
    my_list.append(tl)

print(my_list)

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(my_list[i][j],end=" ")
    print()
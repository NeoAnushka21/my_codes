# take a target integer from user
tgt = int(input("enter a target integer:"))

# take array as input with spaces from user
my_arr01 = list(map(int, input("elements of array:-").strip().split()))
print(my_arr01)

# storing length of the array in a variable
l01 = len(my_arr01)

# declaring an empty list
op = []

for i in range(l01):
    for j in range(i+1, l01):

        # fetching the indexes
        ind_i = my_arr01.index(my_arr01[i])
        ind_j = my_arr01.index(my_arr01[j])

        # storing the value of target integer minus The value present at i th index,in k
        k = tgt - my_arr01[i]

        # Checking the existence of k in the array j th  index
        if my_arr01[j] == k:
            op.extend([ind_i, ind_j])
            print(op)

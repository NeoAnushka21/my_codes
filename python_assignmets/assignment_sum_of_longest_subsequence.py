# take input from user and append it to a list
my_list = []
l = int(input("Enter number of elements you want in list : "))
print(f"Enter the {l} elements of list :")
for i in range(0, l):
    item01 = int(input())
    my_list.append(item01)
print('my_list=', my_list)

# for increment in sequence
long_incr = []              # declaring a list for storing the longest increment sequence

# loop upto length of list
for i in range(l):

    # creating a temporary list for storing increment sequence
    l0i = []

    # loop upto length of list-1
    for j in range(i, l - 1):

        # for current value less than next value in lit , append it to the temporary list
        if my_list[j] <= my_list[j + 1]:
            l0i.append(my_list[j])
        else:
            break

    # Checking for last and last second index
    if (my_list[-2] <= my_list[-1]) and my_list[j] == my_list[-2]:
        l0i.append(my_list[-1])
    else:
        l0i.append(my_list[j])

    if len(l0i) > len(long_incr) and len(l0i) > 1:
        long_incr = l0i

# for decrement in sequence
long_decr = []                 # declaring a list for storing the longest decrement sequence

# loop upto length of list
for i in range(l):

    # creating a temporary list for storing decrement sequence
    l0d = []

    # loop upto length of list-1
    for j in range(i, l - 1):

        # For current value greater than next value in lit , append it to the temporary list
        if my_list[j] >= my_list[j + 1]:
            l0d.append(my_list[j])
        else:
            break

    # Checking for last and last second index
    if (my_list[-2] >= my_list[-1]) and my_list[j] == my_list[-2]:
        l0d.append(my_list[-1])
    else:
        l0d.append(my_list[j])
    if (len(l0d) > len(long_decr)) and len(l0d) > 1:
        long_decr = l0d


# Function to check which among list long increment and long decrement is longest
def sum_of_longest_seq(long_incr, long_decr):

    if len(long_incr) > len(long_decr):
        print(sum(long_incr))
    elif len(long_incr) < len(long_decr):
        print(sum(long_decr))
    elif len(long_incr) == len(long_decr):
        print(sum(long_incr), sum(long_decr))
    else:
        if long_incr.index(long_incr[0]) < long_decr.index(long_decr[0]):
            print(sum(long_incr))
        else:
            print(sum(long_decr))


print(f"The longest continuous Incremented sequence is {long_incr}")
print(f"The longest continuous decremented sequence is {long_decr}")

sum_of_longest_seq(long_incr, long_decr)



my_list = []
l = int(input("Enter number of elements you want in list : "))
print(f"Enter the {l} elements of list :")
for i in range(0, l):
    item01 = int(input())
    my_list.append(item01)
print('my_list=', my_list)

# for increment in sequence
long_incr = []
for i in range(l):
    l0i = []
    for j in range(i, l - 1):
        if my_list[j] <= my_list[j + 1]:
            l0i.append(my_list[j])
        else:
            break
    if (my_list[-2] <= my_list[-1]) and my_list[j] == my_list[-2]:
        l0i.append(my_list[-1])
    else:
        l0i.append(my_list[j])

    if len(l0i) > len(long_incr) and len(l0i) > 1:
        long_incr = l0i

# for decrement in sequence
long_decr = []
for i in range(l):
    l0d = []
    for j in range(i, l - 1):
        if my_list[j] >= my_list[j + 1]:
            l0d.append(my_list[j])
        else:
            break
    if (my_list[-2] >= my_list[-1]) and my_list[j] == my_list[-2]:
        l0d.append(my_list[-1])
    else:
        l0d.append(my_list[j])
    if (len(l0d) > len(long_decr)) and len(l0d) > 1:
        long_decr = l0d


#def sum_of_longest_seq(long_incr, long_decr):

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


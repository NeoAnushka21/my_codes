l = [11, 5, 4, 9, 4, 5, 8, 9, 1]
increment = []
decrement = []
replace_incr = 0
first = 0
second = 1
replace_decrement = 0
while second < len(l):
    print(l[second] < l[first], l[second], l[first])
    if (l[second] < l[first]):
        increment.append(l[replace_incr:second])
        replace = second
        print(increment)
    else:
        decrement.append(l[replace_decrement:second])
        replace_decrement = second
    first += 1
    second += 1

increment.append(l[replace:second])
print(decrement)
print(increment)

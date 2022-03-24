# Taking input from user
l = list(map(int, input("Enter numbers in list: ").split(',')))


# This function gives the summation of list in list which has max length
def max_length(increment):
    length = 0
    for i in range(len(increment)):
        if len(increment[i]) > length:
            length = len(increment[i])
            index = i
            sequence = increment[i]
            summation = sum(increment[i])
    return sequence, length, index, summation


# This function segregates into two lists in lists of increment and decrement sequence
def sequence(l):
    increment = []
    decrement = []
    first = 0
    replace = 0
    replace_decrement = 0
    second = 1
    while second < len(l):
        if (l[second] < l[
            first]):  # comparing second element with first and then forming list till there is a sequence
            increment.append(l[replace:second])
            replace = second
        else:
            decrement.append(l[replace_decrement:second])
            replace_decrement = second
        first += 1
        second += 1

    # adding the last element to the increment and decrement list
    increment.append(l[replace:second])
    decrement.append(l[replace_decrement:second])

    # calling the above defined function
    increment_sequence, increment_length, increment_index, increment_seq_sum = max_length(increment)
    decrement_sequence, decrement_length, decrement_index, decrement_seq_sum = max_length(decrement)

    # Condition to compare the length and give result
    if increment_length == decrement_length:
        if (increment_index < decrement_index):
            print(f'sequence = {increment_sequence} summation = {increment_seq_sum}')
        else:
            print(f'sequence = {decrement_sequence} summation = {decrement_seq_sum}')
    elif increment_length > decrement_length:
        print(f'sequence = {increment_sequence} summation = {increment_seq_sum}')
    else:
        print(f'sequence = {decrement_sequence} summation = {decrement_seq_sum}')


sequence(l)
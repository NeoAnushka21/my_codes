num = int(input("Enter any integer between range (0-99) : "))

num_dict = {0: 'zero', 1: 'one', 2: 'two',
            3: 'three',  4: 'four',5: 'five',
            6: 'six',  7: 'seven',  8: 'eight',
            9: 'nine', 10: 'ten'}


if num < 100:
    if num in num_dict:
        # num is equal to key in num_dict print the value associated with it
        print(num_dict.get(num))
    elif num in range(11, 20):
        # (num % 10) will give a remainder , which will be equal to a key in num_dict
        print('ten', num_dict.get(num % 10))
    else:
        # for the num not in num_dict

        # for num divisible by 10
        if num % 10 == 0:
            # num // 10 gives an integer value which will be equal to a key in num_dict
            print(num_dict.get(num // 10), 'ten')

        # for num not divisible by 10
        else:
            print(num_dict.get(num // 10), 'ten', num_dict.get(num % 10))

# If users input goes out of asked range
else:
    print("opps !! exceeding range")


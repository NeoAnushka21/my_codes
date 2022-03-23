num = int(input("Enter any integer between range (0-99) : "))
num_dict = {0: 'zero', 1: 'one', 2: 'two',  3: 'three',  4: 'four',
            5: 'five',  6: 'six',  7: 'seven',  8: 'eight',  9: 'nine', 10: 'ten'}

if num < 100:
    if num in num_dict:
        print(num_dict.get(num))
    elif num in range(11, 20):
        print('ten', num_dict.get(num % 10))
    else:
        if num % 10 == 0:
            print(num_dict.get(num // 10), 'ten')
        else:
            print(num_dict.get(num // 10), 'ten', num_dict.get(num % 10))
else:
    print("opps !! exceeding range")


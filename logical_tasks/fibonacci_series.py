# To print the fibonacci series upto given integer

n = int(input("Enter the maximum range:"))

first_num = 0
next_num = 1
next_next_num = first_num + next_num

print(first_num)
print(next_num)

while next_next_num <= n:
    print(next_next_num)
    first_num = next_num
    next_num = next_next_num
    next_next_num = first_num + next_num



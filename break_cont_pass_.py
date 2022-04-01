# we have 3 available chocolates
ava = 3
# user will tell how many chocolates they want
x = int(input("How many chocolates do you want?\n answer: "))

# break is to get out of the loop
i = 1
while i <= x:
    if i > ava:
        print("out of stock")
        break
    print("chocolate", )
    i += 1
print("Bye1")

# continue is to skip the condition but stay in the loop
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        continue
        print(i)
print("bye2")


# pass is to ignore the block
for i in range(1, 51):
    if i % 2 != 0:
        pass
    else:
        print(i)
print("bye3")

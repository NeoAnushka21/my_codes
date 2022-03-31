ava = 3
x = int(input("How many chocolates do you want?\n answer: "))

i = 1
while i <= x:
    if i > ava:
        print("out of stock")
        break
    print("chocolate", )
    i += 1
print("Bye1")

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        continue
        print(i)
print("bye2")

for i in range(1, 51):
    if i % 2 != 0:
        pass
    else:
        print(i)
print("bye3")

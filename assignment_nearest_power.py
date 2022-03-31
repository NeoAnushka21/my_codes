b = int(input("Enter a base integer :"))
n = int(input("Enter any integer :"))
list01 = []

# when condition is true ,append b power i to the list
for i in range(0, n+1):
    if b ** i <= n:
        list01.append(b ** i)
    elif b ** i > n:
        list01.append(b ** i)
        break

# extracting the last and second last items of the list
e1 = list01[-1]
e2 = list01[-2]
# extracting the index of last and second last item
ind_e1 = list01.index(e1)
ind_e2 = list01.index(e2)

if abs(n - e1) > abs(n - e2):
    print(f"{ind_e2} times {b} has nearest value to {n}")
else:
    print(f"{ind_e1} times {b} has nearest value to {n}")

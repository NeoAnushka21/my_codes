b = int(input("Enter a base integer :"))
n = int(input("Enter any integer :"))
list01 = []
for i in range(0, n+1):
    if b ** i <= n:
        list01.append(b ** i)
    else:
        break
print(list01)
max1 = max(list01)
ind = list01.index(max1)
print(f"power {ind} of {b} has the nearest value to {n}")

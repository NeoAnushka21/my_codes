# To print the prime number in given range

rng =int(input("Enter the max range: "))

for n in range(2, rng):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=" ")

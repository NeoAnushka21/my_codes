LB = int(input("Give a lower bound:"))
UB = int(input("Give an upper bound:"))
print("Below are the prime numbers in range : ", LB, "-", UB)
for number in range(LB, UB):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number, end=" ")

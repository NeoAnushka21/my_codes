class PrimeNumber:

    def prime_nums(self):

        for num in range(1, 21):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


# created an object for class PrimeNumber
prime = PrimeNumber()

# Initiated the method of class
prime.prime_nums()

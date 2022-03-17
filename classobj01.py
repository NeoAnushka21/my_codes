class Dog:

    attr1 = "Dog"
    attr2 = "Labrador"
    attr3 = "Brown"

    def fun(self):
        print("he is a", self.attr1)
        print("he is a", self.attr2)
        print("he is ",  self.attr3)

max = Dog()         #max is the object name


print(max.attr1)
max.fun()

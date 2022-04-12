# creating a Parent class
class A:

    def feature1(self):
        print("feature 1 is of A")

    def feature2(self):
        print("feature 2 is of A")


# creating other Parent class
class B:

    def feature3(self):
        print("feature 3 is of B")

    def feature4(self):
        print("feature 4 is of B")


# creating a child class of both Parent classes
class C(A, B):
    def feature5(self):
        print("feature 5 is of C")


# object of Parent class
a1 = A()

print("A--parent class ")
# accessing its features
a1.feature1()
a1.feature2()

# Object of other Parent class
b1 = B()

print("B--Parent class")
# Accessing its features
b1.feature3()
b1.feature4()

# Object of other child class
c1 = C()
print("C-- child of A and B")

# Accessing its features as well as of parents A and B
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()




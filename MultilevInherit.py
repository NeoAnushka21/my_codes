# declaring a parent class
class A:
    def feature1(self):
        print("feature 1 is of A")

    def feature2(self):
        print("feature 2 is of A")


# declaring a child class of parent
class B(A):
    def feature3(self):
        print("feature 3 is of B")

    def feature4(self):
        print("feature 4 is of B")


# declaring child class of the child class
class C(B):
    def feature5(self):
        print("feature 5 is of C")


# creating an object of parent class
a1 = A()

print("A--parent class ")

# accessing the functions of it
a1.feature1()
a1.feature2()

# creating object of child class
b1 = B()

print("B--Child class of A")

# accessing its functions as well as of the parent class
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

# creating object of the grand-child class
c1 = C()
print("C-- child of B")

# accessing its functions as well as of the parent and grandparent
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()




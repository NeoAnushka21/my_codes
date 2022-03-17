class A:

    def __init__(self):
        print('This is init of A')

    def feature1(self):
        print("feature 1 is of A")

    def feature2(self):
        print("feature 2 is of A")


class B:

    def __init__(self):
        print('This is init of B')

    def feature1(self):
        print("feature 1 is of B")

    def feature4(self):
        print("feature 4 is of B")


class C(A, B):

    def __init__(self):
        super().__init__()
        print('This is init of C')

    def feature5(self):
        super().feature2()
        print("feature 5 is of C")


c1 = C()
c1.feature1()
c1.feature5()


# feature1 is present in both A and B , it will execute of A as A is LEFT parent.
# This is called "Method resolution Order"

# In multiple inheritance Child will always take Property of parent on LEFT

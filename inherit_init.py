class A:

    def __init__(self):
        print('This is init of A')

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")


class B(A):

    def __init__(self):
        super().__init__()                # accessing init of A , this will execute first then init of B
        print('This is init of B')

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")


b1 = B()             # b1 is object of class B

# While printing, it will first check if init is present in B
# if init in B - print init block of B
# if init not in B - it will print init of A

# Object of sub class will try to find init of subclass , if not found it will go for super class






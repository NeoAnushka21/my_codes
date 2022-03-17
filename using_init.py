class Person:

    #__init__ method
    def __init__(self,name):
        self.name = name

    #normal method
    def greet(self):
        print("hello , my name is ",self.name)

per =  Person('anushka')
per.greet()

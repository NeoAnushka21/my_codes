class OverloadDemo:

   def multiply(self, a, b):
       print(a*b)

   def multiply(self, a, b, c):
       print(a*b*c)


m = OverloadDemo()
m.multiply(5, 10,1)
"""will get an error when run we this, 
because python will only accept 3 arguments and it will ignore the first multiply function with 2 arguments"""
# multiply(5,10,2)

"""Method overloading --
use of numerous methods within a class with same name but accepting different number of arguments.
This is a technique to define a method in such a way that there are more than one way to call it."""


class m_overload():

    def greet(self, name=None):

        if name is not None:
            print("Welcome", name)
        else:
            print("welcome")


load_obj = m_overload()
load_obj.greet()
load_obj.greet("Anushka")






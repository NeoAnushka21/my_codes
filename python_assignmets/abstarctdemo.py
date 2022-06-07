# Importing libraries for creating an Abstract class
from abc import abstractmethod, ABC


# Creating an abstract class
class Bank(ABC):

    def greetings(self):
        print("Welcome")

    @abstractmethod
    def interest(self):
        # Abstract method
        pass


# Child class of abstract class
class Kotak(Bank):

    def interest(self):
        # Implement of abstract class
        print("In Kotak you can have a zero balance savings account")


# Creating an object for Child class
intsrt = Kotak()

# Calling the class method
intsrt.greetings()

# Calling the method of child class
intsrt.interest()


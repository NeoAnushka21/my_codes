"""an {abstract class} is a class that cannot be instantiated.
However, you can create classes that inherit from an abstract class.
What is an Abstract Class?
An abstract class is a class, but not one you can create objects from directly.
Its purpose is to define how other classes should look like, i.e. what methods and properties they are expected to have.
The methods and properties defined (but not implemented) in an abstract class are called abstract methods and abstract properties.
All abstract methods and properties need to be implemented in a child class in order to be able to create objects from it.
An {abstract method} is an method without an implementation.
An abstract class may or may not include abstract methods."""

from abc import abstractmethod,ABC


class Bank(ABC):

    def Bank_info(self):
        print("Welcome __/\__")
    @abstractmethod
    def interest(self):
        "Abstract method"
        pass


class Kotak(Bank):

    def interest(self):
        "Implement of abstract class"
        print("In Kotak you can have a zero balance savings account")


intsrt = Kotak()
intsrt.Bank_info()
intsrt.interest()

class Pets:

    def sound(self):
        print("pets make sound")


class Dog(Pets):               # dog is child of Pets class

    def sound(self):
        print("Dog barks")           # dog and pets both have method sound


d1 = Dog()
d1.sound()
"""d1 the object of Dog class , when sound() is called it didn't print  'pets make sound' , this called overriding"""

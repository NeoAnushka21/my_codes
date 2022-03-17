class Pets:

    def sound(self):
        print("pets make sound")


class Dog(Pets):

    def sound(self):
        Pets.sound(self)            # or  super().sound()
        print("Dog Barks")


d1 = Dog()
d1.sound()


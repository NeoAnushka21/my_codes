class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# creating common interface

def test_fly(bird):
    bird.fly()             # calling fly() for both


paro = Parrot()
peng = Penguin()


test_fly(paro)
test_fly(peng)

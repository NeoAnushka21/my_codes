class Parrot:

    # class attribute
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


#  creating object/instance
boo = Parrot('boo', 5)
poo = Parrot('poo', 7)

# accessing class attribute
print("Boo is a {}".format(boo.__class__.species))
print("poo is also a {}".format(poo.__class__.species))

# accessing instance attributes
print("{} is {} years old".format(boo.name, boo.age))
print("{} is {} years old".format(poo.name, poo.age))

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self, playing):
        return "{} is {}".format(self.name, playing)

    def sleeping(self):
        return "{} is now sleeping".format(self.name)


d1 = Dog("max", 10)


print(d1.play("playing"))
print(d1.sleeping())


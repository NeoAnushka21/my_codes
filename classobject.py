class Fruits:

    def config (self):
        print("red,sweet")


apple1 = Fruits()
apple2 = Fruits()


Fruits.config(apple1)
apple2.config()

class Dog:                           # class with name dog

    animal = 'dog'                   # class variable

    def __init__(self, breed):        # the __init__ method/ constructor
        self.breed = breed           # instance variable

    def set_color(self, color):       # adds an instance variable
        self.color = color

    def get_color(self):              # retrieves instance variable
        return self.color


Max = Dog("pug")
Max.set_color("Black")
print(Max.get_color())

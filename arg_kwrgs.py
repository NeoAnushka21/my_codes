a1 = 'hello'
a2 = 'how are you?'
a3 = 'How have you been?'


def greet(*args):

    for greets in args:
        print(greets)


print(">>>>Passing one argument")
greet(a1)
print(">>>>Passing two argument")
greet(a1, a2)
print(">>>>Passing three argument")
greet(a1, a2, a3)


def greet01(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print(">>>>Passing arguments in key: value pair")
greet01(a1='hello', a2='how are you?', a3='How have you been?')

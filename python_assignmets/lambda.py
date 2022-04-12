# Creating lambda functions

# single parameter
e1 = lambda a: a+10
print(e1(3))

# 2 parameters
e2 = lambda a, b: a*b
print(e2(5, 2))

# multiple parameters
e3 = lambda a, b, c : a+b+c
print(e3(1, 3, 5))


# on strings
full_name = lambda fn, ln : fn.strip().title()+" "+ln.strip().title()
print(full_name("anushka", "mhatre"))

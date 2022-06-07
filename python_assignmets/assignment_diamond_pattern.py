# To take input of rows of upper triangle in the diamond
h = int(input("Enter height of the upper triangle: "))

# Printing the upper triangle
for i in range(h):
    print((" "*(h-i) + " *"*(i+1)))

# Printing the lower triangle
# The lower (reflected) triangle will have one row less than upper triangle
k = h-1
for j in range(k):
    print(" "*(j+2)+" *"*(k-j))

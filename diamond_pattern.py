h = int(input("Enter height of the upper triangle: "))

for i in range(h):
    print((" "*(h-i) + " *"*(i+1)))
k=h-1
for j in range(k):
    print(" "*(j+2)+" *"*(k-j))

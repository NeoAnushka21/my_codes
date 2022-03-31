a = int(input("Enter 1st integer value: "))
b = int(input("Enter 2nd integer value: "))
quest01 = "which operation would you like to execute?" \
          "\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division"
print(quest01)
opr_num = int(input("Enter the operation number:"))


# defining a function with arithmetic operations
def arth_operations():

    if opr_num == 1:
        print(f"Addition: {a}+{b} :", a+b)          # prefix f is for formatted string
    elif opr_num == 2:
        print(f"Subtraction: {a}-{b} :", a-b)
    elif opr_num == 3:
        print(f"Multiplication: {a}*{b} :", a*b)
    elif opr_num == 4:
        if b == 0:
            print(f"Can't divide {a} by 0 ,sorry")
        else:
            print("Division: {}/{} :".format(a, b), a/b)
    else:
        print("error: Available operation  numbers are 1 ,2 , 3 , 4 only")


# calling the function
arth_operations()


# For true condition, we execute the while block
while True:

    print("Do you want to perform another operation?(Y/N)")
    # to remove case sensitivity ,used casefold()
    ans02 = str(input().casefold())

    if ans02 == 'y':
        # for answer y , ask operation number and then call function
        opr_num = int(input("Enter the operation number:"))
        arth_operations()
    elif ans02 == 'n':
        print("Thankyou , Have a good day !!")
        break
    else:
        print("Error: Please enter Y or N")


def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y



def divide(x, y):
    if x or y == 0:
        print("Cant divide by zero")
    return x / y


def multiply(x, y):
    return x * y

def calculator():
    print("choose if you want to add 1, subtract 2, divide 3, or multiply 4")
    choice=input("choose choice 1/2/3/4")
    num1=int(input("what is your 1st number"))
    num2=int(input("what is your 2nd number"))
    if choice == '1':
        print(num1, "+", num2, "=", addition(num1,num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == '3':
        print(num1, "/", num2, "=", divide(num1,num2))
        

    elif choice == '4':
        print(num1, "*", num2, "=", multiply(num1,num2))

    else:
        print("not possible")
calculator()


def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y



def divide(x, y):
    if x or y == 0:
        print("Cant divide by zero")
    return x / y


def multiply(x, y):
    return x * y

def calculator():
    print("choose if you want to add 1, subtract 2, divide 3, or multiply 4")
    choice=input("choose choice 1/2/3/4")
    num1=int(input("what is your 1st number"))
    num2=int(input("what is your 2nd number"))
    if choice == '1':
        print(num1, "+", num2, "=", addition(num1,num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == '3':
        print(num1, "/", num2, "=", divide(num1,num2))
        

    elif choice == '4':
        print(num1, "*", num2, "=", multiply(num1,num2))

    else:
        print("not possible")
calculator()






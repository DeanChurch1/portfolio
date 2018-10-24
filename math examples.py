##import math
##
##
##
##def pythagoras_theorem(ap,bp):
##    #a^2+b^2=c^2
##    a=float(ap)
##    b=float(bp)
##    c=a*a+b*b
##    c=math.sqrt(c)
##    print("the third side is",c)
##
##
##
##ax=(input("enter first side of triangle"))
##bx=(input("enter second side of triangle"))
##pythagoras_theorem(ax,bx)
##
##
##



def add_numbers(x,y):
    num1=x
    num2=y
    num3=int(num1)+int(num2)
    print(num1,"this is num1")
    print(num2,"this is num 2")
        
    return num3

##x=input("enter a number")
##Y=input("enter a second number")
##num4=add_numbers()
##print("the sum of your numbers is",num4)


def get_name(name_input):
    
    name = name_input
    name = name.lowercase()
    name = name.title()

print("the name you entered was", name)

get_name(name)
    





    

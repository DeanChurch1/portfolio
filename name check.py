##
##age=input("what is your age")
##
##if age < "65" or age > "16" and age.isdigit():
##    print("I can drive")
##
##    
##elif age > "65" and age.isdigit():
##    print("sorry you cant drive cant see")
##elif age < "16" and age.isdigit():
##    print("you need to grow up")
##else:
##    print("you shouldnt be driving")

##num1:input from the user; cast to int
##num2:input from the user; cast to int
##check numbers if num1 and num2 are all digits
##If both are digits tell user(compound if)
##if one or the other is a digit tell user
##If neither are digits tell user

num1= input("enter a number")
num2= input("enter a number")

if num1.isdigit() and num2.isdigit():
    print(num1,num2,"are both digits")
elif num1.isdigit() or num2.isdigit():
    print("only one of the numbers is a digit")
else:
    print("those are not digits")

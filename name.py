###Dean Church
###9/13
###get name function
##def get_name():
##    
##
###ask user for name
##    name=input("what is your name")
###verify name
##    #@name=input("did you enter", name)
##    
###display name
##    print("the name you entered was", name)
##
##
##print("this is our function")
##get_name()



def areaOfCircle():
    PI=3.14159265
#1 get a radius
    radius = input("what is the radius")
    
#2 compute the area
    radius = float(radius)
    area = radius*radius*PI
#3 display information
    print("the area of the circle is: ",area)


areaOfCircle()

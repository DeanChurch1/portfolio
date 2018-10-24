def east():
    print("Can't do that")
    choices3()
def north():
    print("Can't do that")
    choices3()
def west():
    print("Can't do that")
    choices3()


#def choices1():
    #choice=str(input("Where do you want to go: \n"))
                     
#def choices2():
    #ch2=choice=str(input("Where do you want to go: \n"))
    
def choices3():
    if ch1 == 'south':
          ch1 == south()

    if ch1 == 'east':
          ch1 == east()

    if ch1 == 'west':
          ch1 == west()

    if ch1 == 'north':
          ch1 == north()


def choices4():
    if ch1 == 'south':
          ch1 == south()

    if ch1 == 'east':
          ch1 == east()

    if ch1 == 'west':
          ch1 == west()

    if ch1 == 'north':
          ch1 == north()
    
def choice4():
    ch4=str(input("You're in the middle floor of the house the door behind you is closed tight. \nYou notice stairs leading up and down. Where do you go(down,up)"))
    if ch4 == 'down':
        choice5()
    if ch4 == 'up':
        choice6()


def choice5():
    print("You go down to see a skeleton on a mattress and nothing else")
    ch6 = input("Where do you go(down,up)")
    if ch6 == 'down':
        print("You can't do that and go back upstairs")
        choice4()
    if ch6 == 'up':
        choice4()


    
def choice6():
    ch5=input("There is a zombie up there and it charges towards you, what do you use: ")
    if ch5 == 'rock':
        print("You break its head off and it uses its arm to kill you")
        print("You find yourself back at the middle floor")
        choice4()
    if ch5 == 'backpack':
        print("That was dumb. The zombie killed you")
        print("You find yourself back at the middle floor")
        choice4()
    if ch5 == 'needle':
        ch7=input("You kill it with the needle. Good Job. You notice a key in the zombies pocket.\nDo you want to pick it up(y/n)")
    if ch7 == 'y':
        choiceY()
    if ch7 == 'n':
        choiceN()



def choice7():
    ch10=str(input("You're in the middle floor of the house the door behind you is closed tight. \nYou notice stairs leading up and down. Where do you go(down,up)"))
    if ch10 == 'down':
        choice8()
    if ch10 == 'up':
        choice9()


def choice8():
    print("You go down to see a skeleton on a mattress and nothing else")
    ch11 = input("There's a little glimmer in the corner of the mattress that you notice\nDo you want to lift the mattress(y/n)")
    if ch11 == 'y':
        choicey2()
    if ch12 == 'n':
        choicen2()


def choicey3():
    print("You lifted the mattress and see a tunnel leading to the south and north")
    ch14 = input("Do you want to go south or north")
    if ch14 == 'south':
        print("You follow the tunnel down and arrive into a forest full of white trees")
        south2()
    if ch14 == 'north':
        print("You took one step and fell down into a never ending hole")
        choicen3()



#def south2():
    




def choicen3():
    ch13 = input("Do you want to lift the mattress (y/n)")
    if ch13 == 'y':
        choicey3()
    if ch13 == 'n':
        choicen3()

    
         
##def choicey2():
##    print("There was a trap door with a lock on it")
##    ch12=input("Do you want to use the key (y/n)")
##    if ch12 == 'y':
        
    

def choicen2():
    ch12 = input("Do you want to lift the mattress (y/n)")
    if ch12 == 'y':
         choicey2()
    if ch12 == 'n':
        choicen2()






    
def choiceY():
    print("You took the key")
    ch9 = input("Choose(up/down)")
    if ch9 == 'up':
        print("You can't do that")
        choiceY()
    if ch9 == 'down':
        choice7()



        
def choiceN():
    ch8 = input("Do you want to take the key (y/n)")
    if ch8 == 'y':
         choiceY()
    if ch8 == 'n':
        choiceN()


        
def south():
    print("You look out the window\nThere is a house north but you can't get there yet")
    ch2=str(input("You see a window \nWhat do you use to break the window?"))
    if ch2 == 'rock':
        print('Window broke and you jumped out, you see another house north with the door open')
        ch2=str(input("Where do you go: \n"))
        choice4()
    if ch2 == 'needle':
        print("you broke the needle exposing a deadly toxin and died")
        ch2=str(input("You've been given a second chance and wake back up in the middle of the room\nwhere do you go: \n"))
        choices3()
    if ch2 == 'backpack':
        print("That was ineffective and your bounced back in the middle of the room")
        ch2=str(input("Where do you go: \n"))
        south()



print("You are in a closed room with no doors. You look around and see a window to the south. There is a rock in your hand, a needle in your pocket, and a backpack on your back\n")
num=input("Type in begin to begin: ")
ch1 = str(input("Where do you want to go:\n"))

if num == 'begin':
    num == choices3()


if ch1 not in ('east', 'west', 'north','south'):
    print('You died from poor grammar')
    

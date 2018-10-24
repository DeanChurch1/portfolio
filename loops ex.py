#loops

##
##loops = 0
##while True:
##    print("I have looped", loops, " times")
##    loops += 1
##    if loops > 1000:
##        break
##    

##count = 0
##while True:
##    count += 1
##    if count > 100:
##        break
##    if count == 5 or count == 25 or count == 50:
##        continue
##    print(count)
##
##input("\n\n press enter to exit")

##i="enter"
##while i <= "enter":
##    print("looping")
##    x=input("do you want to keep looping yes or no")
##    if x == "yes":
##        continue
##    else:
##        i=""

##health = 10
##trolls = 0
##damage = 3
##
##while health != 0:
##    trolls += 1
##    health -= damage
##    print("Your hero swings and defeats an evil troll,"\
##          "but takes",damage,"damage points.\n")
##
##print("Your hero fought valiantly and defeated",trolls,"trolls")
##print("But alas, your hero is no more.")
##
##input("\n\nPress the enter key to exit")
import random
win=0
mHealth=100
pHealth=100
choice = input("attack or run")

while choice == "attack":

    
    playerDamage = random.randrange(0, 25)
    monsterDamage = random.randrage(0, 50)
    print("you attack the monster for",playerDamage)
    mHealth -= playerDamage
    if mHealth > 0:
        print("the monster attacks you for", monsterDamage)
        pHealth -= monsterDamage
    if pHealth <= 0:
        win = 0
        print("You have died")
        break
    elif mHealth <= 0:
        win = 1
        print("You have killed the monster")
        break
    elif pHealth <= 0 and mHealth >= 0:
        print("you have ", pHealth,"health")
        print("The monster has", mHealth,"health")
        choice = input("attack or run")
    if choice != "attack" or choice != "run":
        print("not sure what that is")
        choice = "attack"
        continue
    else:
        continue
    
if choice == "run":
    print("You are a coward")
if win == 0:
    print("Game Over")

else:
    print("You have won")


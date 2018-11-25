from monsterSlayerFunctions import *

game = True
while game == True:
    play = input("Hello brave adventurer, the world is in need of saving! \n"
                  "Do you wish to slay some Monsters?(y/n) : ")

    if play == "y":
        print("your legend begins!")
        while playerLevel == 1:
            i = randint(0, len(monsters)-1)
            monster = monsters[i]
            encounterMonster(monster, i)
            print("health is now", health)
    elif play == "n":
        print("coward")
        game = False
    else:
        print("please enter (y/n)")

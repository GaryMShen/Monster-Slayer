from monsterSlayerFunctions import *

game = True
while game == True:
    play = input("Hello brave adventurer, the world is in need of saving! \n"
                  "Do you wish to slay some Monsters?(y/n) : ")

    if play == "y":
        print("Your legend begins!")
        sleep(0.5)
        print("You need to go through the forest path to get to the city")
        sleep(0.5)

        print("You pick up a sturdy stick, it'll have to do as a weapon for now... ")
        while playerLevel == 1:
            i = randint(0, 1)
            monster = monsters[i]

            if health <= 0:
                isAlive = checkAlive(health)
                if isAlive == False:
                    game = False
            else:
                    
                fight = encounterMonster(monster, i)
                health = fight[0]
                exp = fight[1]
                print("exp is now", exp)
                check = checkLevel(exp)
                if check == 2:
                    levelUp(check)
                    playerLevel = 2
                    sleep(0.5)
                print("")
                print("You're moving along the path")
                print("")
        while playerLevel == 2:
            loopNum = 1
            if loopNum == 1:
                print("getting closer to city !")
            loopNum = loopNum + 1
            i = randint(0, 2)
            if health <= 0:
                isAlive = checkAlive(health, monster)
                if isAlive == False:
                    game = False
            else:
                monster = monsters[i]
                fight = encounterMonster(monster, i)
                health = fight[0]
                exp = fight[1]
                print("exp is now", exp)
                check = checkLevel(exp)
                if check == 3:
                    levelUp(check)
                    playerLevel = 3
                    sleep(0.5)
                print("")
                print("You're moving along the path")
                print("")
                
        while playerLevel == 3:
            loopNum = 1
            if loopNum == 1:
                print("getting closer to the city !")
            loopNum = loopNum + 1
            i = randint(0, 2)
            if health <= 0:
                isAlive = checkAlive(health)
                if isAlive == False:
                    game = False
            else:
                monster = monsters[i]
                fight = encounterMonster(monster, i)
                health = fight[0]
                exp = fight[1]
                print("exp is now", exp)
                print("")
                print("You're moving along the path")
                print("")
                
                

                      
    elif play == "n":
        print("coward")
        game = False
    else:
        print("please enter (y/n)")

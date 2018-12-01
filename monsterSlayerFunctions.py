from monsterSlayerFunctions import *


game = True
loopNum4 = 1
loopNum = 1
loopNum3 = 1
y
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
            if loopNum3 == 1:
                print("getting closer to the city !")
            loopNum3 = loopNum3 + 1
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
                check = checkLevel(exp)
                if check == 4:
                    levelUp(check)
                    playerLevel = 4
                    sleep(0.5)
                print("exp is now", exp)
                print("")
                print("You're moving along the path")
                print("")
        while playerLevel == 4:
            i = randint(0,3)
            if loopNum4 == 1:
                print("Almost at the city")
                print("You're moving along the path")
                sleep(0.5)
                print("Ambushed by a gang of goblins!!!")
                sleep(0.5)
                print("goblins are usually found by themselves...")
                sleep(0.5)
                print("if they're grouping up this could mean trouble!")
                sleep(0.5)
                print("Something could be up... I should look into this")
                sleep(0.5)
                print("need to beat up these filthy goblins first")

            loopNum4 = loopNum4 + 1
            if health <= 0:
                isAlive = checkAliveBoss(health)
                if isAlive == False:
                    game = False
            else:
                if bossSlayed == 0:
                    x = 0
                    boss = bosses[x]
                    bossFight = encounterBoss(boss, x)
                    health = bossFight[0]
                    exp = bossFight[1]
                    bossSlayed = bossFight[2]
                else:
                    monster = monsters[i]
                    fight = encounterMonster(monster, i)
                    health = fight[0]
                    exp = fight[1]
                    check = checkLevel(exp)


                
                

                      
    elif play == "n":
        print("coward")
        game = False

        
    else:
        print("please enter (y/n)")


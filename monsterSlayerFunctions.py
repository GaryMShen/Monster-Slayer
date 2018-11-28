from math import *
from time import *
from random import *

global health, power, defense
originalHealth = 50
health = originalHealth 
power = 1
defense = 0
powerIncrease = 0
leveledUp2 = 0
leveledUp3 = 0

monsterSlayed = 0

exp = 21
playerLevel = 1
moves = ["slash", "stab"]
monsters = ["slime", "goblin", "gremlin"]
monsterDrops = [" ","goblin's short sword"," "]
monstersExp = [3,5,7]
monstersHealth = [10,20,25]
s = randint(1,2)
g = randint(3,5)
gr = randint(4,6)
monstersDamage = [s, g, gr]
hasGoblinSword = False

def encounterMonster(monster, i):
    global health, defense, monstersHealth, damage, monstersDamage, hasGoblinSword
    global exp, monsterSlayed, monstersExp, power
    sleep(0.5)
    print("Encountered a", monster,"!")
    encounter = input("Stand and fight like a hero? (f) \n"
          "Run like a coward? (r) : ")
    if encounter == "f":
        currentMonstersHealth = monstersHealth[i]
        currentMonstersExp = monstersExp[i]

        bothAlive = True
        while bothAlive == True:
            print("moves: ")
            s = randint(1,2)
            g = randint(3,5)
            gr = randint(4,6)
            monstersDamage = [s, g, gr]
            currentMonstersDamage = monstersDamage[i]
            
            for i in range(0,len(moves)):
                print(moves[i],"(",i,")")
            number = int(input("how will you attack? : "))
            
##            while number != 0 and number != 1:
##                number = int(input("how will you attack? (please enter a valid input): "))
                

            attack = moves[number]
            pickedAttack(attack)
            if number == 2:
                currentMonstersHealth = currentMonstersHealth - damage
                print("you did", damage, "damage! the", monster,"'s health is now:", currentMonstersHealth)
                print("slash again!")
                currentMonstersHealth = currentMonstersHealth - damage
                print("you did", damage, "damage! the", monster,"'s health is now:", currentMonstersHealth)
            else:
                currentMonstersHealth = currentMonstersHealth - damage
                print("you did", damage, "damage! the", monster,"'s health is now:", currentMonstersHealth)
                
            trueMonstersDamage = currentMonstersDamage - defense

            if currentMonstersHealth < 0:
                currentMonstersHealth = 0
                

            if health <= 0:
                print("death falls on you")
                print("you slayed", monsterSlayed, "monsters")
                bothAlive = False

            elif currentMonstersHealth == 0:
                exp = exp + currentMonstersExp
                monsterSlayed = monsterSlayed + 1
                print("you slayed", monster,"!")
                print("exp went up by", currentMonstersExp, "!")
                print("you have slayed", monsterSlayed, "monsters !")
                if monster == "goblin" and hasGoblinSword == False:
                    drop = randint(1,3)
                    if drop == 1:
                        print("goblin short sword with power 2 dropped!")
                        pickUp = input("Pick up item? (y/n) : ")
                        if pickUp == "y":
                            power = 2
                            hasGoblinSword = True
                            print("item successfully picked up!")
                            bothAlive = False

                bothAlive = False
            
            else:
                health = health - trueMonstersDamage
                print(monster,"did", trueMonstersDamage, "damage! your health is now:", health)
                            
        return health, exp, monsterSlayed, power
    
    elif encounter == "r":
        damage = randint(1,5) - defense
        health = health - damage
        if health > 0:
            print("got away safely this time but you took", damage, "damage!")
            print("your health is", health)
        if health <= 0:
            print("death falls on you")
            game = False
        return health, exp, monsterSlayed

    else:
        print("please enter (f/r)")
        return health, exp

def pickedAttack(attack):
    global power, damage
    if attack == "slash":
        damage = power + powerIncrease + randint(0, 9)
    elif attack == "stab":
        damage = power + powerIncrease + 4
    elif attack == "double slash":
        damage = power + powerIncrease + randint(0, 5)
        


    return damage

def checkAlive(health, monster):
    if health <= 0:
        print(monster, "dealt a fatal blow!")

        return False

def checkLevel(exp):
    if exp > 40:
        playerLevel = 3
        return playerLevel
    elif exp > 15:
        playerLevel = 2
        return playerLevel




def levelUp(check):
    global power, health, defense, leveledUp2, leveledUp3, powerIncrease, originalHealth
    if check == 2 and leveledUp2 == 0:
        leveledUp2 = 1
        print("*"*30)
        print("LEVEL UP!")
        print("*"*30)

        health = originalHealth
        print("Level 2")
        print("you're now fully healed, health is now", health)
        print("pick a stat to level up:" )
        print("current stats")
        print("-"*30)
        print("power   ( p ) : ", power)
        print("health  ( h ) : ", health)
        print("defense ( d ) : ", defense)

        statIncrease = input("enter what you would like to power up here :")
        loopAgain = True
        if loopAgain == True:
            if statIncrease == "p":
                powerIncrease = 0.5
                print("power level increased !")
                loopAgain = False

            elif statIncrease == "h":
                originalHealth = originalHealth + 10
                health = originalHealth
                print("health increased !")
                loopAgain = False

            elif statIncrease == "d":
                defense = defense + 0.5
                print("defense level increased !")
                loopAgain = False
            else:
                print("please enter a valid input")
                loopAgain = True
            
                
    elif check == 3 and leveledUp3 == 0:
        leveledUp3 = 1

        print("*"*30)
        print("LEVEL UP!")
        print("*"*30)

        health = originalHealth
        print("Level 3")
        print("you're now fully healed, health is now", health)
        print("pick a stat to level up: ")
        print("current stats")
        print("-"*30)
        print("power   ( p ) : ", power)
        print("health  ( h ) : ", health)
        print("defense ( d ) : ", defense)

        statIncrease = input("enter what you would like to power up here :")
        loopAgain = True
        if loopAgain == True:
            if statIncrease == "p":
                powerIncrease = 1.5
                loopAgain = False

            elif statIncrease == "h":
                orginalHealth = orginalHealth + 15
                loopAgain = False

            elif statIncrease == "d":
                defense = defense + 1.5
                loopAgain = False
            else:
                print("please enter a valid input")
                loopAgain = True

        print("new move learned! : double slash")
        moves.append("double slash")
        

        
          


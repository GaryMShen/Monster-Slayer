from math import *
from time import *
from random import *

global health, power, defense


gold = 0
originalHealth = 50
health = originalHealth 
power = 1
defense = 0
powerIncrease = 0
leveledUp2 = 0
leveledUp3 = 0
leveledUp4 = 0
monsterSlayed = 0
exp = 0
playerLevel = 1
moves = ["slash", "stab"]
monsters = ["slime", "goblin", "gremlin", "giant snake"]
monsterDrops = [" ","goblin's short sword"," "]
monstersExp = [3,5,7,10]
monstersHealth = [10,20,25,40]
s = randint(1,2)
g = randint(3,5)
gr = randint(4,6)
gs = randint(6,8)
g1 = randint(1,2)
g2 = randint(2,3)
g3 = randint(4,5)
g4 = randint(7,9)
monsterGold = [g1, g2, g3, g4]

monstersDamage = [s, g, gr, gs]
hasGoblinSword = False
hasRaggedLeatherVest = False
bosses = ["Goblin squad"]
bossHealth = [60]
bossSlayed = 0
numGoblins = 3


def encounterMonster(monster, i):
    global health, defense, monstersHealth, damage, monstersDamage, hasGoblinSword, hasRaggedLeatherVest
    global exp, monsterSlayed, monstersExp, power, gold
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
            gs = randint(6, 8)
            g1 = randint(1,2)
            g2 = randint(2,3)
            g3 = randint(4,5)
            g4 = randint(7,9)
            monstersDamage = [s, g, gr, gs]
            monsterGold = [g1, g2, g3, g4]
            currentMonstersGold = monsterGold[i]

            currentMonstersDamage = monstersDamage[i]
  #          s.create_rectangle(10, 10, 10 + health, 20, fill = "red")

            
            for i in range(0,len(moves)):
                print(moves[i],"(",i,")")
            number = int(input("how will you attack? : "))
            if len(moves) == 3:
                while number != 0 and number != 1 and number !=2:
                   number = int(input("how will you attack? (please enter a valid input): "))

            elif len(moves) == 2:
                while number != 0 and number != 1:
                   number = int(input("how will you attack? (please enter a valid input): "))
                

            attack = moves[number]
            pickedAttack(attack)
            if number == 2:
                currentMonstersHealth = currentMonstersHealth - damage
                print("you did", damage, "damage! the", monster,"'s health is now:", currentMonstersHealth)
                print("slash again!")
                pickedAttack(attack)

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
                print(monster, "dealt a fatal blow!")

                print("you slayed", monsterSlayed, "monsters")
                bothAlive = False

            elif currentMonstersHealth == 0:
                gold = gold + currentMonstersGold
                print("you now have", gold, "gold")
                exp = exp + currentMonstersExp
                monsterSlayed = monsterSlayed + 1
                print("you slayed", monster,"!")
                print("exp went up by", currentMonstersExp, "!")
                print("you have slayed", monsterSlayed, "monsters !")
                if monster == "goblin" and hasGoblinSword == False:
                    drop = randint(1,3)
                    if drop == 1:
                        print("goblin short sword with power 2 dropped!")
                        print("=l==>")
                        pickUp = input("Pick up item? (y/n) : ")
                        if pickUp == "y":
                            power = 2
                            hasGoblinSword = True
                            print("item successfully picked up!")
                            bothAlive = False
                if monster == "gremlin" and hasRaggedLeatherVest == False:
                    drop = randint(1,5)
                    if drop == 1:
                        print("Ragged Leather Vest with defense 1 dropped!")
                        pickUp = input("Pick up item? (y/n) : ")
                        if pickUp == "y":
                            defense = defense + 1
                            hasRaggedLeatherVest = True
                            print("item successfully picked up!")
                            bothAlive = False

                bothAlive = False
            
            else:
                health = health - trueMonstersDamage
                print(monster,"did", trueMonstersDamage, "damage! your health is now:", health)
                            
        return health, exp, monsterSlayed, power, gold
    
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
    
currentBossHealth = 60
bothAlive = True

def encounterBoss(boss, x): #add individuals goblins health
    global health, defense, monstersHealth, damage, monstersDamage, currentBossHealth
    global exp, monsterSlayed, monstersExp, power, numGoblins, bossSlayed, bothAlive

    

    while bothAlive == True:

        print("moves: ")
        gs = randint(4, 6)
        bossDamage = [gs]
        currentBossDamage = bossDamage[x]
        if x == 0:
            
            for i in range(0,len(moves)):
                print(moves[i],"(",i,")")
            number = int(input("how will you attack? : "))
            
            attack = moves[number]
            pickedAttack(attack)

            if len(moves) == 3:
                while number != 0 and number != 1 and number !=2:
                   number = int(input("how will you attack? (please enter a valid input): "))

            elif len(moves) == 2:
                while number != 0 and number != 1:
                   number = int(input("how will you attack? (please enter a valid input): "))
                   
            if number == 2:
                currentBossHealth = currentBossHealth - damage
                print("you did", damage, "damage! the", boss,"'s health is now:", currentBossHealth)
                print("slash again!")
                pickedAttack(attack)

                currentBossHealth = currentBossHealth - damage
                print("you did", damage, "damage! the", boss,"'s health is now:", currentBossHealth)

            else:
                currentBossHealth = currentBossHealth - damage
                print("you did", damage, "damage! the", boss,"'s health is now:", currentBossHealth)

                
            trueBossDamage = currentBossDamage - defense
            if currentBossHealth < 20:
                
                print("You've slayed two goblins!")
                print("one left!")
                numGoblins = 1
            elif currentBossHealth < 40:
                print("You've slayed one goblin!")
                numGoblins = 2

            
                

            if health <= 0:
                print("death falls on you")
                print(boss, "dealt a fatal blow!")

                print("you slayed", monsterSlayed, "monsters")
                bothAlive = False

            elif currentBossHealth <= 0:
                exp = exp + 25
                bossSlayed = bossSlayed + 1
                print("you slayed", boss,"!")
                print("exp went up by 25")
                print("you have slayed", monsterSlayed, "monsters !")
                print("you have slayed", bossSlayed, "bosses !")
                bothAlive = False
            
            else:
                for i in range(0,numGoblins):
                    health = health - trueBossDamage
                    print("goblin", i+1, "did", trueBossDamage, "damage! your health is now:", health)
                            
        return health, exp, bossSlayed, monsterSlayed, power, 




def pickedAttack(attack):
    global power, damage
    if attack == "slash":
        damage = power + powerIncrease + randint(0, 9)
    elif attack == "stab":
        damage = power + powerIncrease + 4
    elif attack == "double slash":
        damage = power + powerIncrease + randint(0, 4)
        


    return damage

def checkAliveBoss(health):
    if health <= 0:
        print("The overwhelming number of goblins where too much!")
        
        return False
        
    
def checkAlive(health, monster):
    if health <= 0:

        return False

def checkLevel(exp):
    if exp > 60:
        playerLevel = 4
        return playerLevel

    elif exp > 35:
        playerLevel = 3
        return playerLevel

    elif exp > 15:
        playerLevel = 2
        return playerLevel




def levelUp(check):
    global power, health, defense, leveledUp2, leveledUp3, leveledUp4, powerIncrease, originalHealth
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
        print("power   ( p ) : ", power + powerIncrease)
        print("health  ( h ) : ", health)
        print("defense ( d ) : ", defense)

        statIncrease = input("enter what you would like to power up here :")
        loopAgain = True
        if loopAgain == True:
            if statIncrease == "p":
                powerIncrease = 1.5
                loopAgain = False

            elif statIncrease == "h":
                originalHealth = originalHealth + 15
                loopAgain = False

            elif statIncrease == "d":
                defense = defense + 1.5
                loopAgain = False
            else:
                print("please enter a valid input")
                loopAgain = True

        print("new move learned! : double slash")
        moves.append("double slash")

    elif check == 4 and leveledUp4 == 0:
        leveledUp4 = 1

        print("*"*30)
        print("LEVEL UP!")
        print("*"*30)

        health = originalHealth
        print("Level 4")
        print("you're now fully healed, health is now", health)
        print("pick a stat to level up: ")
        print("current stats")
        print("-"*30)
        print("power   ( p ) : ", power + powerIncrease)
        print("health  ( h ) : ", health)
        print("defense ( d ) : ", defense)

        statIncrease = input("enter what you would like to power up here :")
        loopAgain = True
        if loopAgain == True:
            if statIncrease == "p":
                powerIncrease = 2
                loopAgain = False

            elif statIncrease == "h":
                originalHealth = originalHealth + 20
                loopAgain = False

            elif statIncrease == "d":
                defense = defense + 2
                loopAgain = False
            else:
                print("please enter a valid input")
                loopAgain = True

from math import *
from time import *
from random import *

global health, power, defense

health = 100
power = 1
defense = 0

monsterSlayed = 0

exp = 0
playerLevel = 1

moves = ["slash", "stab"]
monsters = ["slime", "goblin"]
monstersExp = [1,2]
monstersHealth = [10,20]
g = randint(1,5)
s = randint(1,3)
monstersDamage = [s, g]


def encounterMonster(monster, i):
    global health, defense, monstersHealth, damage, monstersDamage
    global exp, monsterSlayed, monstersExp

    print("You have encountered a", monster,"!")
    fight = input("Stand and fight like a hero? (f) \n"
          "Run like a coward? (r) : ")
    if fight == "f":
        monstersHealth = monstersHealth[i]
        monstersDamage = monstersDamage[i]
        monstersExp = monstersExp[i]
        bothAlive = True
        while bothAlive == True:
            g = randint(1,5)
            s = randint(1,3)
            print("you currently know: ")
            for i in range(0,len(moves)):
                print(moves[i],"(",i,")")
            number = int(input("how will you attack? : "))
            attack = moves[number]
            pickedAttack(attack)
            monstersHealth = monstersHealth - damage
            print("you did", damage, "damage! the", monster,"'s health is now:", monstersHealth)
            health = health - monstersDamage
            print(monster,"did", monstersDamage, "damage! your health is now:", health)
            if health <= 0:
                print("death falls on you")
                print("you slayed", monsterSlayed, "monsters")
                game = False
            elif monstersHealth <= 0:
                exp = exp + monstersExp
                monsterSlayed = monsterSlayed + 1
                print("you slayed", monster,"!")
                print("exp went up by", monstersExp, "!")
                print("you have slayed", monsterSlayed, "monsters !")

                bothAlive = False

            
            
            

                    
    elif fight == "r":
        damage = randint(1,5) - defense
        health = health - damage
        if health > 0:
            print("got away safely this time but you took", damage, "damage!")
            print("your health is", health)
        if health <= 0:
            print("death falls on you")
            game = False
    else:
        print("please enter (f/r)")

def pickedAttack(attack):
    global power, damage
    if attack == "slash":
        damage = power * randint(1, 10)
    elif attack == "stab":
        damage = power * 5

    return damage
    

          

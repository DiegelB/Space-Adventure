import random
from npcClass import NPC

def distressMain(PlayerShip):
    number = random.randrange(1,2, 1)

    if number == 1: encounterOne(PlayerShip)
    elif number == 2: encounterTwo(PlayerShip)
    elif number == 3: encounterThree(PlayerShip)
    elif number == 4: encounterFour(PlayerShip)
    elif number == 5: encounterFive(PlayerShip)
    elif number == 6: encounterSix(PlayerShip)

def encounterOne(PlayerShip):
    ally = NPC()
    ally.randomNPC()
    print("hello i am ",ally.name, " here are my wares:")

    for x in range(len(ally.items)):
        print(ally.items[x])

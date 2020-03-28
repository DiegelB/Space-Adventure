import random 
from os import system
from enemyClass import EnemyShip

EnemyShip = EnemyShip()

#main screen of the game. allows the player to work on ship or travel around.
def mainLoop(PlayerShip):
    playerChoice = ""
    
    while playerChoice != "5":
        system("clear")
        playerChoice = input("\n\t1. Travel"+
                             "\n\t2. Repairs"+
                             "\n\t3. Shop"+
                             "\n\t4. Stats"+
                             "\n\t5. Save & Exit"+
                             "\n\nThe "+str(PlayerShip.shipName[0])+"\n>>")
        if playerChoice == "1":
            travel(PlayerShip)
        elif playerChoice == "2":
            repairs(PlayerShip)
        elif playerChoice == "3":
            shop(PlayerShip)
        elif playerChoice == "4":
            PlayerShip.printStats()
    exitGame(PlayerShip)

#differnet encouters on a random base
#fight enemies, fight anamolies, befriend allies, gain money or powerlvl.
def travel(PlayerShip):
    randomRoll = random.randrange(1,4)
    if randomRoll == 1 or randomRoll == 2:
        print("you gone bb", str(randomRoll))
    else:
        enemyEncounter(PlayerShip)    
    input()

#repair shop to fix the hull, shield, or weapons.
def repairs(PlayerShip):
    print("repair bb")
    input()

#shop to buy new weapons or upgrades 
def shop(PlayerShip):
    print("heres some gold! +10")
    PlayerShip.currency = PlayerShip.currency + 10
    input()

#exit and save the game.
def exitGame(PlayerShip):
    PlayerShip.saveGame()

#TEST ENEMY ENCOUNTER
def enemyEncounter(PlayerShip):
    enemyDamage = EnemyShip.damage(10)
    PlayerShip.takeDamage(enemyDamage)
    print("Bad guy dealt " + str(enemyDamage) + " damage!")
    print("Hull strenght now at "+ str(PlayerShip.hullStr))
    input()
        
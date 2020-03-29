import random 
from os import system
from enemyClass import EnemyShip
from encounterMain import drawCard

EnemyShip = EnemyShip()

#main screen of the game. allows the player to work on ship or travel around.
def mainLoop(PlayerShip):
    playerChoice = ""
    while playerChoice != '5':
        if PlayerShip.hullStr <= 0:
            print("you lose")
            playerChoice = '5'
        else:
            system("clear")
            playerChoice = input("\n\t1. Encounter Card"+
                                 "\n\t2. 3 Repair Cards"+
                                 "\n\t3. 3 Shop Cards"+
                                 "\n\t4. Stats"+
                                 "\n\t5. Save & Exit"+
                                 "\n\nThe "+str(PlayerShip.shipName[0])+"\n>>")
            if playerChoice == "1":
                encounter(PlayerShip)
            elif playerChoice == "2":
                repairs(PlayerShip)
            elif playerChoice == "3":
                shop(PlayerShip)
            elif playerChoice == "4":
                PlayerShip.printStats()
    exitGame(PlayerShip)


#differnet encouters on a random base
#fight enemies, fight anamolies, befriend allies, gain money or powerlvl.
def encounter(PlayerShip):
    drawCard(1)
    input()

#repair shop to fix the hull, shield, or weapons.
def repairs(PlayerShip):
    userChoice = input("Reair hull for "+str(100-PlayerShip.hullStr)+ " credits?(y)/(n)\n>>")
    if userChoice == 'y': 
        PlayerShip.currency -= (100-PlayerShip.hullStr)
        PlayerShip.hullStr = 100
        input("The "+str(PlayerShip.shipName[0])+"'s back to 100%")
    else:
        return
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
        
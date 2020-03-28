#Space game. Test for a card game of the same idea.
#main player controls a star ship and is introduced
#to random encounters. They have to maintain a sheild,
#power levels, crew members, hull strength, and more.
#the player will encounter enemies, allies, missions,
#and anamolies.

import pickle
from os import system
from playerClass import PlayerShipClass
from gameplayLoop import mainLoop

#starts the main program
def startScreen():
    PlayerShip = PlayerShipClass()
    system("clear")
    print("\t\tWelcome to Space Adventure\n" +
          "\t\t\tName WIP\n\n" +
          "\tSpace Adventure will test you like no other\n"+
          "\tgame has before. So prepare yourself for an\n" +
          "\tadventure of a lifetime!\n\n" +
          "\t\t1. New Game (WILL ERASE PREVIOUS SAVE)\n"+
          "\t\t2. Load Game\n")

    #asks for players input and starts a new game or loads old one.
    playerChoice = input(">>")
    if(playerChoice == '1'): 
        newGame(PlayerShip)
        return PlayerShip 
    elif(playerChoice == '2'): PlayerShip.loadGame()

#WIP need to functianlize this and make sure it can save. 
def newGame(PlayerShip):
    playerChoice = "n"
    while playerChoice == "n" or playerChoice == "N":
        system("clear")
        newName = input("\n\tPlease enter your ship name.\n>>")
        PlayerShip.shipName[0] = newName
        system("clear")
        weaponChoice = input("\n\tPlease pick your starting weapon."+
                            "\n\t1. Lasers[v1] +10 DMG -5 PWR"+
                            "\n\t2. Torpedos[v1] +15 -7 PWR"+
                            "\n\t3. Mines[v1] +20 -10 PWR\n>>")
        if weaponChoice == '1':
            PlayerShip.weaponNames[0] = "Lasers[v1]"
            PlayerShip.weaponDmg[0] = 10
        elif weaponChoice == '2':
            PlayerShip.weaponNames[0] = "Torpedos[v1]"
            PlayerShip.weaponDmg[0] = 15
        elif weaponChoice == '3':
            PlayerShip.weaponNames[0] = "Mines[v1]"
            PlayerShip.weaponDmg[0] = 20
        system("clear")
        PlayerShip.printStats()
        playerChoice = input("\n\tDo these status look good? Y/N\n>>")
        PlayerShip.saveGame()
    #starts the main loop from a new game
    mainLoop(PlayerShip) 

startScreen()
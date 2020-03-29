import pickle
from gameplayLoop import mainLoop
from os import system


#delcared palyer class with default stats.
class PlayerShipClass:
    #Default valuse to new ships
    def __init__(self, shipName = ["Enterprise-E"], 
                 hullStr = 100, 
                 sheildStr = 50, 
                 powerLvl = 0,
                 rollMaximum = 6,
                 currency = 1500,
                 weaponNames = ["Slot1","Slot2","Slot3"],
                 weaponDmg = [0,0,0]):
        self.shipName = shipName

        self.hullStr = hullStr #overall health
        self.sheildStr = sheildStr #sub health
        self.powerLvl = powerLvl #overall energy of the ship. used to cast weapons and charge shield. 

        self.weaponNames = weaponNames #ship holds up to three weapons
        self.weaponDmg = weaponDmg #power of each weapon

        self.rollMaximum = rollMaximum #highest number player can roll for modifiers
        self.currency = currency #money in da bank

    #the amount of damage the players ship does. adds all the 
    def damage(self):
        return sum(self.weaponDmg) + random.randrange(1, self.rollMaximum)
    
    def takeDamage(self, sheildDmg, hullDmg):
        self.sheildStr -= sheildDmg
        self.hullStr -= hullDmg
        
    
    #nicely prints out all the stats for the player.
    def printStats(self):
        print("\tShip Name: ", self.shipName,
              "\n\tCredits: ", self.currency,

              "\n\n\tHull Stregth: ", self.hullStr,
              "\n\tSheild Stregth: ", self.sheildStr,
              "\n\tCurrent Power: ", self.powerLvl,

              "\n\n\tWeapons:",self.weaponNames[0],self.weaponNames[1],self.weaponNames[2],
              "\n\tDamage:\t   ",self.weaponDmg[0],"\t    ",self.weaponDmg[1],
              "\t     ",self.weaponDmg[2])
        input()

    #saves the entire class as PlayerSaveFile. only 1 save per game
    def saveGame(self):
        with open("playerSaveFile", "wb") as f:
            playerInfo = self
            pickle.dump(playerInfo, f)
        print("Thank you Captain, game saved!")
        input()

    #loads the entire class from playersavefile.
    def loadGame(self):
        with open("playerSaveFile", "rb") as f:
            self = pickle.load(f)
        system("clear")
        input("Welcome back Captian. Your crew on the "+self.shipName[0]+ " awaits.")
        #starts the main loop for a loaded game. called also in the source.py file for newgame()
        #also imports the PlayerShip class from file
        mainLoop(self)  
    

#delcared the playership once for the whole file.



        
    
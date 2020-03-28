import random

class EnemyShip:

    def __init__(self, 
                 hullStr = 25, 
                 sheildStr = 10, 
                 powerLvl = 10,
                 rollMaximum = 4):
        self.hullStr = hullStr
        self.sheildStr = sheildStr
        self.powerLvl = powerLvl
        self.rollMaximum = rollMaximum

    def damage(self, amount):
        return amount + random.randrange(1,self.rollMaximum)
         

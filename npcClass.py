import random

#npc class to use throughout the game wheter its a good guy or bad.
class NPC():

    def __init__(self,
                 name = "",
                 currency = 100,
                 items = []):

        self.name = name
        self.currency = currency
        self.items = items

    #creates a random character 
    def randomNPC(self):
        randomNumber = random.randint(0,19)
        nameList = ['Vincenzo', 'Clark', 'Dev', 'Melendez',
                    'Chace', 'Blevins', 'Etienne', 'Sims',
                    'Kirby', 'Tillman', 'Reon', 'Griffin',
                    'Raees', 'Calhoun', 'Eshaal', 'Krause',
                    'Ema', 'Snow', 'Mohammed', 'Valentine']
        self.name = nameList[randomNumber]
        self.curreny = random.randint(25,100)
        
        randomNumber1 = random.randint(0,8)
        randomNumner2 = random.randint(0,8)
        itemsList = ['Lasers[v1]', 'Lasers[v2]', 'Lasers[v3]',
                     'Torpedos[v1]', 'Torpedos[v2]', 'Torpedos[v3]',
                     'Mines[v1]', 'Mines[v2]', 'Mines[v3]']
        
        #clears the npc list to add new items
        self.items.clear()
        self.items.append(itemsList[randomNumber1])
        self.items.append(itemsList[randomNumner2])

    

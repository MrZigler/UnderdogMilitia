
class Livingbeing():
    
    def __init__(self, name, health, armor, inventory):
        self.name = name
        self.health = health
        self.armor = armor
        self.inventory = inventory
        self.hunger = 0
        self.thirst = 0
        
        
    def takeDamage(self, dmgAmount):
        if dmgAmount > self.armor:
            self.health = self.health - (dmgAmount - self.armor)    
        
        
        
        
#create a player
playerx = Livingbeing('Platinum Falcon', 72, 5, {})



dogs = 1

while dogs < 9:


    dmbgz = int(input('damage: '))
    playerx.takeDamage(dmbgz)

    print(playerx.health)
    
    dogs += 1
    
else:
    quit()
    
    
    
    

''' {Underdog Militia, a text based adventure.}
    Copyright (C) {2015}  {Michael G Zigler Jr}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    Mr Zigler's contact bitmessage BM-NB5C7KBGPPxjEFSuHTqJwsVzFGELJfVZ
'''



import random
import time
from landplots import *




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BROWN = (160, 82, 45)

zards = 1



class Livingbeing():
    
    
    
    
    def __init__(self, name, health, armor, mindset, emotion, skills, inventory):
        self.name = name
        self.health = health
        self.armor = armor
        self.mindset = mindset
        self.emotion = emotion
        self.skills = skills
        self.inventory = inventory
        self.hunger = random.randrange(1, 5)
        self.thirst = 0
        


        
        
        
    def takeDamage(self, dmgAmount):
        if dmgAmount > self.armor:
            self.health = self.health - (dmgAmount - self.armor)    
        
        else:
            pass
        
        
''' mindset (1 Liberty minded - 100 authoritiarian psycopath), emotion (1 happy - 100 blind rage)
patriots, hackers, writers (authors), artists, snitches, mercs, breaucrats
CFR, Executives, Landlords


'''        

''' skills (leatherworking, blacksmith, woodworking, carpentry, chemistry, engineering, machining, disernment, discretion)


'''                
        
        

        



landplot1 = Landplots('none', 5, 7, 4, 37, {})

















# Create a surface we can draw on



   
        
#create a player
playerx = Livingbeing('Platinum Falcon', 72, 5, 2, 22, {}, {})



dogs = 1

while dogs < 9:


    dmbgz = int(input('damage: '))
    playerx.takeDamage(dmbgz)

    print(playerx.health)
    
    dogs += 1
    
else:
    quit()
    
    
time.sleep(9)    

quit()
    
    

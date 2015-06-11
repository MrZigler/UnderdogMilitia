

import random

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
        
        
        
        

    quit()
    
    
    
    

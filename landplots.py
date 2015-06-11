import time
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BROWN = (160, 82, 45)




class Landplots():
    
    def __init__(self, owner, umtype, locationregion, jurisdiction, umvalue, inventory):
        self.owner = owner
        self.umtype = umtype
        self.locationregion = locationregion
        self.jurisdiction = jurisdiction
        self.umvalue = umvalue
        self.inventory = inventory
        
        
        
        
        
        
'''        
class Umbuildings(): blacksmithshop (anvil, fire, metal) safehouse, farms (hulgerculter, agria, forest, hort, mixxed)

library (books ) 
    
    def __init__(self, owner):   
        self.owner = owner    '''
        
 
 
''' mines (gold, silver, copper, rareearths, titanium) smelter_furnace (eros to bars)
mints (coins) '''       
        
        
'''Farm - umtype (1 depleted agra, 5 agra, 10, hort, 15 hort hugercult) locationregion (reseved), jurisdiction (1 heavyzoning & regulations,
5 minimum zoning but taxed, 10 no zoning regulations or taxes) umvalue (1 low to 100 highest value)
inventory (improvements, farmanimals, chicken coops, barns etc)
'''        

class Farm(Landplots):  
     
    def __init__(self, owner, umtype, locationregion, jurisdiction, umvalue, inventory):   
        Landplots.__init__(self, owner, umtype, locationregion, jurisdiction, umvalue, inventory)
    
     
     
        
    def producefood(self):
        self.umvalue + self.jurisdiction
            
        
        


#orchard1 = Farm('Platinum Falcon', 5, 7, 42, 37, {})     
   
        

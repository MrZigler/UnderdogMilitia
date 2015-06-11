#! python3



class Weapons():
    
    def __init__(self, owner, umtype, energy, ammo):
        self.owner = owner
        self.umtype = umtype
        self.energy = energy
        self.ammo = ammo
        
        


        
''' umtypes (revolver, blade, laser, granade)
 
 
'''
        
        
        
        
        
''' skills (leatherworking, blacksmith, woodworking, carpentry, chemistry, engineering, machining, disernment, discretion)


'''        
        
        
        
        
        
class Umcontainer():  
    
    def __init__(self, owner, umtype, umvalue, inventory): 
        self.owner = owner
        self.umtype = umtype
        self.umvalue = umvalue
        self.inventory = inventory
        
'''  types (pouch, bag, backpack, bookbag)      
        
 '''       
        
class Umvehicle():  
    
    def __init__(self, owner, umtype, umvalue, energy):      
        self.owner = owner
        self.umtype = umtype
        self.umvalue = umvalue
        self.energy = energy
        
        
        
'''  types (bicycle, car, pickuptruck, stationwagon, tank)       
        
        
        '''        
        
class Drones():        
    
    def __init__(self, umidentity, umlvl, owner, energy):
        self.umidentity = umidentity
        self.umlvl = umlvl
        self.owner = owner
        self.energy = energy
        





class RobotDog(Drones):  
    
    def __init__(self, umidentity, umlvl, owner, energy):      
        Drones.__init__(self, umidentity, umlvl, owner, energy)

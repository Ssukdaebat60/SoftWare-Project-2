class Skill:
    
    def __init__(self, Sinfo):
        self.ID = Sinfo[0] 		#type = string
        self.condition = Sinfo[1] 	#type = int
        self.property = Sinfo[2] 	#type = tuple
    
    def skillActive(self, GameCondition):	#GameCondition type = int
        return True if self.condition <= GameCondition else False
    
    def getType(self):
        return self.property[0]
        
    def getAmount(self):
        return self.property[1]
    
    def getID(self):
        return self.ID
    
    def getCondition(self):
        return self.condition

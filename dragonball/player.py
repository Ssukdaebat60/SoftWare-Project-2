Ptext = { 
'normal':
'''\
  o
 /|\\
  |
 / \\
''',
'human':
'''\
  o
 /|->
 / \\
''',
'AI':
'''\
   o
 <-|\\
   |
  / \\
''',
    }

class Player:
    
    def __init__(self, ID, controller):
        self.ID = ID
        self.controller = controller
        self.appearance = self.getOutfit(controller)
        self.energy = 0
        self.life = 2
        self.atk = 0
        self.dfs = 0
    
    def getOutfit(self, controller):
        appearance = [Ptext['normal']]
        appearance.append(Ptext[controller])
        return appearance
    
    def decreaseLife(self, num):
        if num < 0:
            return
        self.life -= num
        
    def getAppearance(self, skillType): #skill이 Gi면 appearance[0], 나머지 skill은 appearance[1]
        if skillType == 'energy':
            return self.appearance[0]
        else:
            return self.appearance[1]
            
    def increaseEnergy(self):
        self.energy += 1
    
    def decreaseEnergy(self, num):
        if num:
            self.energy = 0
        
    def getEnergy(self):
        return self.energy
    
    def getLife(self):
        return self.life if self.life >= 0 else 0
        
    def setAtk(self, num):
        self.atk = num
    
    def setDfs(self, num):
        self.dfs = num
        
    def getAtk(self):
        return self.atk
    
    def getDfs(self):
        return self.dfs
        
    def getID(self):
        return self.ID

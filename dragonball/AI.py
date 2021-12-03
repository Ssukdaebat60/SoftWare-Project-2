import random
from skill import Skill

class AI:

    def __init__(self, skillList):
        self.skillList = skillList
        self.randomList = [
                [90, 10, 0, 0, 0, 0],
                [45, 20, 70, 50, 0, 0],
                [90, 20, 50, 50],
                [10, 20, 0, 0, 100, 0],
            ]
        
    def AIChoice(self, energy): #random을 사용할 때는  어떻게 테스트 해야 하나요?
        index = 0
        if energy == 0:
            index = self.randomChoice(self.randomList[0])
        elif energy == 1:
            index = self.randomChoice(self.randomList[1])
        elif energy >= 2 and energy < 5:
            index = self.randomChoice(self.randomList[2])
        elif energy >= 5 :
            index = self.randomChoice(self.randomList[3])
        return self.skillList[index]
    
    def randomChoice(self, RList):
        for i in range(len(RList)):
            if RList[i] > random.randrange(0,100):
                return i
        return 0

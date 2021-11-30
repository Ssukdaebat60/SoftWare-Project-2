#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QToolButton, QTextEdit

from skill import Skill
from player import Player
from AI import AI

from skill_Info import ENE, DFS, PA, SDFS, WON, SUPER


class Button(QToolButton):

    def __init__(self, skill, callback):
        super().__init__()
        self.skill = skill
        self.setText(self.skill.getID())
        self.clicked.connect(callback)
        self.setMaximumHeight(100)
        self.setMaximumWidth(100)
        self.setEnabled(False)
    
    def getSkill(self):
        return self.skill
        

class DragonBall(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.player1Text = QTextEdit()
        self.player1Text.setReadOnly(True)
        self.player1Text.setAlignment(Qt.AlignLeft)
        font = self.player1Text.font()
        font.setFamily('Courier New')
        self.player1Text.setFont(font)
        
        self.player2Text = QTextEdit()
        self.player2Text.setReadOnly(True)
        self.player2Text.setAlignment(Qt.AlignLeft)
        font = self.player2Text.font()
        font.setFamily('Courier New')
        self.player2Text.setFont(font)

        skillLayout = QGridLayout()
        self.Ene = Skill(ENE)
        self.Dfs = Skill(DFS)
        self.Pa = Skill(PA)
        self.Sdfs = Skill(SDFS)
        self.Won = Skill(WON)
        self.Super = Skill(SUPER)
        
        skillList=[self.Ene, self.Dfs, self.Pa, self.Sdfs, self.Won, self.Super]
        self.AI = AI(skillList)
        
        self.startButton = QToolButton()
        self.startButton.setText('Game Start')
        self.startButton.clicked.connect(self.startGame)
        skillLayout.addWidget(self.startButton, 0, 0)
        
        self.buttonList=[]
        
        for i in range(1, len(skillList)//2+1):
           for j in range(0, 2):
               index = (i-1)*2 + j
               button = Button(skillList[index], self.gameManager)
               self.buttonList.append(button)
               skillLayout.addWidget(button, i, j)
        
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.player1Text, 0, 0)
        mainLayout.addWidget(self.player2Text, 0, 1)
        mainLayout.addLayout(skillLayout, 1, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle('Dragon Ball')

    def startGame(self):
        self.P1 = Player('You', 'human')
        self.P2 = Player('AI', 'AI')
        self.startButton.setEnabled(False)
        self.player1Text.setText("\n목숨: " + str(self.P1.getLife()) + "\n기: " + str(self.P1.getEnergy()) + "\n\n\n" + self.P1.getAppearance('energy'))
        self.player2Text.setText("\n목숨: " + str(self.P2.getLife()) + "\n\n\n\n" + self.P2.getAppearance('energy'))
        self.updateButton()
        
        
    def gameManager(self):
        self.P1.setAtk(0)
        self.P1.setDfs(0)
        self.P2.setAtk(0)
        self.P2.setDfs(0)
        
        P2Choice = self.AI.AIChoice(self.P2.getEnergy())
        
        if self.sender().getSkill().getType() == 'energy':
            self.P1.increaseEnergy()
        elif self.sender().getSkill().getType() == 'defense':
            self.P1.setDfs(self.sender().getSkill().getAmount())
            self.P1.decreaseEnergy(self.sender().getSkill().getCondition())
        elif self.sender().getSkill().getType() == 'attack':
            self.P1.setAtk(self.sender().getSkill().getAmount())
            self.P1.decreaseEnergy(self.sender().getSkill().getCondition())
        
        if P2Choice.getType() == 'energy':
            self.P2.increaseEnergy()            
        elif P2Choice.getType() == 'defense':
            self.P2.setDfs(P2Choice.getAmount())
            self.P2.decreaseEnergy(P2Choice.getCondition())
        elif P2Choice.getType() == 'attack':
            self.P2.setAtk(P2Choice.getAmount())
            self.P2.decreaseEnergy(P2Choice.getCondition())
        
        self.P1.decreaseLife(self.P2.getAtk()-self.P1.getAtk()-self.P1.getDfs())
        self.P2.decreaseLife(self.P1.getAtk()-self.P2.getAtk()-self.P2.getDfs())
        
        self.updateButton()
        self.updateDisplay(self.sender().getSkill(), P2Choice)
        
        if self.P1.getLife() <= 0 or self.P2.getLife() <= 0:
            self.endGame()
    
    
    def updateButton(self):
        for B in self.buttonList:
            B.setEnabled(B.getSkill().skillActive(self.P1.getEnergy()))
        
    
    def updateDisplay(self, P1Skill, P2Skill):
        self.P1Text = "\n목숨: " + str(self.P1.getLife()) + "\n기: " + str(self.P1.getEnergy()) + "\n\n"\
            + P1Skill.ID + "\n" + self.P1.getAppearance(P1Skill.getType())
        self.P2Text = "\n목숨: " + str(self.P2.getLife()) + "\n\n\n" + P2Skill.ID + "\n"\
            + self.P2.getAppearance(P2Skill.getType())
        self.player1Text.setText(self.P1Text)
        self.player2Text.setText(self.P2Text)
        
        
    def endGame(self):
        self.player1Text.setText(self.P1.getID() + (' Win ' if self.P1.getLife()>0 else ' Lose') + self.P1Text)
        self.player2Text.setText(self.P2.getID() + (' Win ' if self.P2.getLife()>0 else ' Lose') + self.P2Text)
        for B in self.buttonList:
            B.setEnabled(False)
        self.startButton.setEnabled(True)
    
        
if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = DragonBall()
    game.show()
    sys.exit(app.exec_())


import unittest

from skill import Skill
from skill_Info import ENE, DFS, WON
from player import Player, Ptext

class Test(unittest.TestCase):

    def setUp(self):
        self.s1 = Skill(ENE)
        self.s2 = Skill(DFS)
        self.s3 = Skill(WON)
        self.p1 = Player('You', 'human')
        self.p2 = Player('AI', 'AI')
        
    def testSkillInfo(self):
        self.assertEqual(self.s1.getID(), '기 모으기')
        self.assertEqual(self.s1.getType(), 'energy')
        self.assertEqual(self.s1.getAmount(), 1)
        self.assertEqual(self.s1.getCondition(), 0)

    def testSkillActivate(self):
        self.assertTrue(self.s1.skillActive(0))
        self.assertTrue(self.s2.skillActive(0))
        self.assertFalse(self.s3.skillActive(0))
        self.assertFalse(self.s3.skillActive(4))
        self.assertTrue(self.s3.skillActive(5))
        self.assertTrue(self.s3.skillActive(6))
    
    def testPlayerEnergy(self):
        self.p1.increaseEnergy()
        self.assertEqual(self.p1.getEnergy(), 1)
        self.p2.increaseEnergy()
        self.p2.increaseEnergy()
        self.assertEqual(self.p2.getEnergy(), 2)
        self.p1.decreaseEnergy(1)
        self.p2.decreaseEnergy(0)
        self.assertEqual(self.p1.getEnergy(), 0)
        self.assertEqual(self.p2.getEnergy(), 2)
        self.p2.decreaseEnergy(5)
        self.assertEqual(self.p2.getEnergy(), 0)
    
    def testPlayerLife(self):
        self.assertEqual(self.p1.getLife(), 2)
        self.p1.decreaseLife(1)
        self.assertEqual(self.p1.getLife(), 1)
        self.p1.decreaseLife(-5)
        self.assertEqual(self.p1.getLife(), 1)
        self.p1.decreaseLife(0)
        self.assertEqual(self.p1.getLife(), 1)
        self.p1.decreaseLife(2)
        self.assertEqual(self.p1.getLife(), -1)
        
    def testPlayerAppearance(self):
        self.assertEqual(self.p1.getOutfit('human'), [Ptext[0], Ptext[1]]) #오류
        self.assertEqual(self.p2.getOutfit('AI'), [Ptext[0], Ptext[2]])
        self.assertEqual(self.p1.getAppearance('energy'), self.p1.getOutfit()[0])
        self.assertEqual(self.p1.getAppearance('attack'), self.p1.getOutfit()[1])
        self.assertEqual(self.p1.getAppearance('defense'), self.p1.getOutfit()[1])
        self.assertEqual(self.p2.getAppearance('energy'), self.p2.getOutfit()[0])
        self.assertEqual(self.p2.getAppearance('attack'), self.p2.getOutfit()[1])
        self.assertEqual(self.p2.getAppearance('defense'), self.p2.getOutfit()[1])

if __name__ == '__main__':
    unittest.main()


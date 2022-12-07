from graphics import *
from weapons import *
from random import *

class Char:

    def __init__(self, win, Name, FighterPic, Picture, RightPic, Battlepic, SmallPic):
        self.ctpoint = Point(640,640)
        self.LevelUpScreen = Image(Point(640,360), "LVUP/Background.png")
        self.player1_battle_pic__point = Point(200,410) 
        self.enemy1_battle_pic__point = Point(1050,410)
        
        self.Battlepic = Battlepic

        self.SmallPic = SmallPic

        self.BattlePostion = ''

        self.win = win
        
        self.Name = Name
        
        self.char_base_attack = 0

        self.Real_Armor = armor("Clothes", 0, "None", "None", 'None')
        self.Dream_Armor = armor("Clothes", 0, "None", "None", 'None')

        self.char_defense = self.Real_Armor.getDefense()
        self.char_dream_defense = self.Dream_Armor.getDefense()
        
        self.char_special = int(40)
        self.char_maxspecial = int(40)
        
        self.char_health = int(100)
        self.char_maxhealth = int(100)
        
        self.char_exp = int(0)
        
        self.level = int(0)
        
        self.char_FighterPic = FighterPic

        self.char_Picture = Picture

        self.char_RightPic = RightPic

        self.char_intelligence = int(0)
        self.char_agility = int(0)
        self.char_persuasion = int(0)
        self.char_probsolve = int(0)
        self.char_understanding = int(0)
        self.char_creativity = int(0)
        self.char_spanishcommunication = int(0)
        self.char_strength = int(1)

        self.char_accuracy = int(1)
        
        self.char_money = int(20)
        self.char_memory = int(0)

        self.char_real_inventory = []
        self.char_dream_inventory = []
        self.char_key_items_inventory = []

        self.RealWeapon = Weapon("Fist", 30, "Blunt", 0,[Special("Upper Cut", "BattleIcon/SpecialPictures/Blunt/UpperCut.png", "Damage", 40, 10,'None')], "None", 'None', 'R')
        self.RealSpecials = self.RealWeapon.getSpecials()
        self.char_attack = self.char_base_attack + self.RealWeapon.getAttack()

        self.DreamWeapon = Weapon("Fist", 30, "Blunt", 0, [Special("Upper Cut", "BattleIcon/SpecialPictures/Blunt/UpperCut.png", "Damage", 40, 10, 'None')], "None","None", 'D')
        self.DreamSpecials = self.DreamWeapon.getSpecials()
        self.char_dream_attack = self.char_base_attack + self.DreamWeapon.getAttack()

        self.char_damage_multi = 1
        
        self.Real_Element = self.Real_Armor.getElement()
        self.Dream_Element = self.Dream_Armor.getElement()

        self.multi = 2

        varx = 650
        vary = 300

        self.LVUPMessage = []

        for i in ["LVUP/messages/1.png","LVUP/messages/2.png","LVUP/messages/3.png","LVUP/messages/4.png","LVUP/messages/5.png"]:
            self.LVUPMessage.append(Image(Point(varx,vary), i))

    def SetBattlePos(self, pos):
        self.BattlePostion = pos

    def DrawBattle(self, x):
        if x == "P":
            self.DrawnBattlePicture = Image(self.player1_battle_pic__point, self.Battlepic)
            self.DrawnBattlePicture.draw(self.win)
        
        elif x == "E":
            self.DrawnBattlePicture = Image(self.enemy1_battle_pic__point, self.Battlepic)
            self.DrawnBattlePicture.draw(self.win)

    def UndrawBattle(self):
        self.DrawnBattlePicture.undraw()
        
    def getPicture(self):
        return self.char_Picture
        
    def getFighterPicture(self):
        return self.char_FighterPic

    def loadName (self, name):
        self.Name = str(name)

    def getName(self):
        return self.Name

    def increaseIntelligence(self, multiplyer):
        self.char_intelligence = self.char_intelligence + (10*multiplyer)

    def getIntelligence(self):
        return self.char_intelligence

    def DrawFighterPic(self, xpos,ypos):
        self.Fighterpic = Image(Point(xpos,ypos), self.char_FighterPic)
        self.Fighterpic.draw(self.win)

    def UndrawFighterPic(self):
        self.FighterPic.undraw()

    def getSmallFighterPicture(self):
        return self.SmallPic

    def getHealthPercents(self):
        x = (self.char_health/self.char_maxhealth)*10
        return int(x)

    def getSpecialPercents(self):
        HelloAPPeopleThisVariableIsJustForYou = (self.char_special/self.char_maxspecial)*10
        return int(HelloAPPeopleThisVariableIsJustForYou)

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.char_attack = self.char_attack + self.weapon.getAttack()

    def getRealAttack(self):
        return self.char_attack

    def getDreamAttack(self):
        return self.char_dream_attack

    def getRealDefense(self):
        return self.char_defense

    def getDreamDefense(self):
        return self.char_dream_defense

    def getRealItems(self):
        return self.char_real_inventory

    def getDreamItems(self):
        return self.char_dream_inventory

    def lowerHP(self, x):
        self.char_health = (self.char_health - randint(0,x)) * self.char_damage_multi
        self.char_damage_multi = 1

    def getHP(self):
        return self.char_health

    def IncreaseHP(self, x):
        self.char_health = self.char_health + x

    def RemoveRealItem(self, x):
        self.char_real_inventory.remove(x)

    def RemoveDreamItem(self,x):
        self.char_dream_inventory.remove(x)
    
    def getRealSpecial(self):
        return self.RealSpecials

    def getDreamSpecial(self):
        return self.DreamSpecials

    def lowerSP(self, Undead):
        self.char_special = self.char_special - Undead

    def increaseSP(self,x):
        self.char_special = self.char_special + x

    def getSP(self):
        return self.char_special

    def Block(self,x):
        self.char_damage_multi = x

    def getSpecialNum(self,t):
        if t == 'R':
            w =  len(self.RealSpecials)
            return w

        elif t == 'D':
            
            w = len(self.DreamSpecials)
            return w

    def getSpecial(self,x,t):
        if t == 'R':
            return (self.RealSpecials[x])
        elif t == 'D':
            return (self.DreamSpecials[x])

    def loadWeapon(self, weapon, loc):
        if loc == 'R':
            self.RealWeapon = weapon
            self.RealSpecials = self.RealWeapon.getSpecials()
            self.char_attack = self.char_base_attack + self.RealWeapon.getAttack()

        elif loc == 'D': 
            self.DreamWeapon = weapon
            self.DreamSpecials = self.DreamWeapon.getSpecials()
            self.char_dream_attack = self.char_base_attack + self.DreamWeapon.getAttack()

    def getRealWeapon(self):
        return self.RealWeapon

    def getDreamElement(self):
        return self.Dream_Element

    def getRealArmor(self):
        return self.Real_Armor

    def getDreamArmor(self):
        return self.Dream_Armor

    def getDreamDefense(self):
        return self.char_dream_defense

    def getRealDefense(self):
        return self.char_defense

    def getMulti(self):
        return self.multi

    def loadArmor(self, armor, loc):
        if loc == 'R':
            self.Real_Armor = armor
            self.char_defense = self.Real_Armor.getDefense()
        

        elif loc == 'D': 
            self.Dream_Armor = armor
            self.char_dream_defense = self.Dream_Armor.getDefense()
    
    def reloadHealth(self, num):
        if num == 'max':
            ws = self.char_maxhealth
            self.char_health = ws

        else:
            self.char_health = self.char_health + num

    def reloadSP(self, num):
        if num == 'max':
            ws = self.char_maxspecial
            self.char_special = ws

        else:
            self.char_special = self.char_special + num

    def getDreamWeapon(self):
        return self.DreamWeapon

    def getMaxHP(self):
        return self.char_maxhealth

    def LevelUp2Screen(self):
        self.LevelUpScreen.draw(self.win)
        x = randint(0,len(self.LVUPMessage)-1)
        print(x)
        w = self.LVUPMessage[x]
        w.draw(self.win)
        y = Image(Point(500, 498), self.char_Picture)
        y.draw(self.win)
        self.win.getMouse()
        y.undraw()
        w.undraw()
        self.LevelUpScreen.undraw()
        


    def checkLevel(self):
        var = (9801/2000000)*(self.level + 1)
        if self.char_exp >= var:
            self.level = self.level + 1
            self.char_base_attack = self.char_base_attack + self.level*self.char_strength + randint(0,10)
            self.char_maxhealth = int(self.char_maxhealth * 1.25) + randint(0,10)
            self.char_maxspecial = int(self.char_maxspecial * 1.25) + randint(0,5)
            self.LevelUp2Screen()

            
    def IncreaseEXP(self,var):
        self.char_exp = self.char_exp + var            
        
    def addItem(self,loc,item):
        if loc == 'D':
            self.char_dream_inventory.append(item)
        elif loc == 'R':
            self.char_real_inventory.append(item)
        elif loc == 'Key':
            self.char_key_items_inventory.append(item)
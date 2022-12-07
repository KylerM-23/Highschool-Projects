import battle as b

class Weapon:
        def __init__(self, name, attack, atype,ammo, Specials, theme, weakness,world):
                self.name = name
                self.Attack = attack
                self.type = atype
                self.ammo = ammo
                self.Specials = Specials
                self.theme = theme
                self.world = world
                self.element = weakness
                
        def getAttack(self):
                return self.Attack

        def getSpecials(self):
                return self.Specials

        def getElement(self):
                return self.element

class Item:
        def __init__(self, name, pfile, itype, thing):
                self.name = name
                self.file = pfile
                self.type = itype
                self.thing = thing
        
        def getFile(self):
                return self.file
        
        def Work(self, pchara, echara):
                self.pchar = pchara
                self.echara = echara

                if self.type == 'Heal':
                        self.pchar.IncreaseHP(self.thing)
                
                return self.pchar, self.echara
        
        def GetType(self):
                return self.type

        def getName(self):
                return self.name


class Special:
        def __init__(self, name, pfile, itype, thing, SP, weakness):
                self.name = name
                self.file = pfile
                self.type = itype
                self.thing = thing
                self.SP = SP
                self.element = weakness
        
        def getFile(self):
                return self.file

        def Work(self, pchara, echara, who, world, multi):
                self.pchar = pchara
                self.echara = echara

                if who == 'P':
                        if self.type == 'Heal':
                                self.pchar.IncreaseHP(self.thing)
                        
                        if self.type == 'Damage': 
                                if world == 'R':
                                        junkvar2 = self.echara.getRealArmor()    

                                if world == 'D':
                                        junkvar2 = self.echara.getDreamArmor()              

                                tempvar = multi * self.thing - junkvar2.getDefense()

                                if tempvar <0:
                                        tempvar = 0

                                self.echara.lowerHP(tempvar)
                                
                        if self.type == 'Block':
                                self.echara.Block(self.thing)

                        self.pchar.lowerSP(self.SP)

                elif who == 'E':
                        if self.type == 'Heal':
                                self.echara.IncreaseHP(self.thing)
                        
                        if self.type == 'Damage':
                                self.pchar.lowerHP(self.thing)
                                
                        if self.type == 'Block':
                                self.pchar.Block(self.thing)

                        self.echara.lowerSP(self.SP)

                return self.pchar, self.echara

        def getSP(self):
                return self.SP

        def GetType(self):
                return self.type

        def getName(self):
                return self.name

        def getElement(self):
                return self.element

class armor:
        def __init__(self, name, defnese, atype, theme, weakness):
                self.name = name
                self.defense = defnese
                self.atype = atype
                self.theme = theme
                self.element = weakness

        def getDefense(self):
                return self.defense

        def getElement(self):
                return self.element
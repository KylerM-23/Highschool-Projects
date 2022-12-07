from text import *
from graphics import *
from classesforPYR import *
from tests import *
from drawchar import *
from player import *
from Name import FindName
from Button import *
import random as r

class Battle:
    def __init__(self, win, PlayerParty, EnemyParty,userfile, first, location, flee):
        self.ctpoint = Point(640,640)
        self.pyr_health_point = Point(80,80) 
        self.enemy_health_point = Point(1220,80) 
        self.attack_name_point = Point(650,340)
        self.PlayerParty = PlayerParty
        self.EnemyParty = EnemyParty
        self.userfile = userfile
        self.win = win
        self.BattleParty = []
        self.exp = 0
        self.First = first
        self.Location = location
        self.Flee = flee
        self.text = gameText(self.win)
        self.turn = 0 
        self.WIN = "Hey I doubt you should ever see this player, but if you do I would like to say nice to meet you. I am the creator of this world and you may know me by my human name cause that's my only name, but good bye until we meet again."

    def DrawPage(self,list):
        for i in list:
            i.draw()
    
    def UndrawPage(self,list):
        for i in list:
            i.undraw()

    def DrawButtons(self, list):
        for i in list:
            i.draw()

    def GetEnemy(self):
        self.Enemy1 = self.EnemyParty[0]
        
        self.EnemyBattleParty = []
        self.EnemyBattleParty.append(self.Enemy1)
        self.Enemy1.SetBattlePos('Enemy1')
        
        if len(self.EnemyParty) >=2:
            self.Enemy2 = self.EnemyParty[1]
            self.EnemyBattleParty.append(self.Enemy2)
            self.Enemy2.SetBattlePos('Enemy2')

    def determineWeakness(self, vari, vari2):
        if vari == 'Fire':
            if vari2 in ['Ice', 'Metal','Water']:
                return True
            else:
                return False
        
        if vari == 'Ice':
            if vari2 in ['Fire']:
                return True
            else:
                return False

        if vari == 'Water':
            if vari2 == 'Fire':
                return True
            else:
                return False

        else:
            return False

    def checkCharHP(self):
        if (self.PlayerActive.getHP() <= 0):
            self.text.BattleText(self.EnemyActive.getName() + ' has ','vanquished ' + self.PlayerActive.getName(),'')
            self.PlayerParty.remove(self.PlayerActive)
            if self.PlayerParty == []:
                self.WIN = 'Enemy'
                self.text.BattleText(self.EnemyActive.getName() + ' has' ,'vanquished your', 'whole party...')
                return self.WIN
                
            else:
                self.PlayerActive = self.PlayerParty[0]
            
        if (self.EnemyActive.getHP() <= 0):
            self.text.BattleText(self.PlayerActive.getName() + ' has ', 'vanquished '  +self.EnemyActive.getName(),'')
            self.exp = self.exp + ((self.EnemyActive.getMaxHP())/4)
            self.EnemyParty.remove(self.EnemyActive)
            if self.EnemyParty == []:
                self.WIN = 'Player'
                self.text.BattleText(self.PlayerActive.getName() + ' has' , 'vanquished the ','enemy party.')
                return self.WIN
                
            else:
                self.EnemyActive = self.EnemyParty[0]

        if self.WIN == 'Fled':
            self.text.BattleText("You ran away....",'','')
            self.BattleDone = 1

    def BattleScreenDraw(self, PA, EA):
        self.ButtonsPage1 = []

        self.ButtonsPage1.append(Button(self.win,"Attack", "BattleIcon/Attack.png",125,660))
        self.ButtonsPage1.append(Button(self.win,"Item", "BattleIcon/Item.png",360,660))
        self.ButtonsPage1.append(Button(self.win,"Text", "BattleIcon/Textbox.png", 640, 616))
        self.ButtonsPage1.append(Button(self.win,"Flee", "BattleIcon/Flee.png",1155,660))
        self.ButtonsPage1.append(Button(self.win,"P1HP","BattleIcon/HPicon.png",40,100))
        self.ButtonsPage1.append(Button(self.win,"P1SS","BattleIcon/SPicon.png",40,165))
        self.ButtonsPage1.append(Button(self.win,"E1HP","BattleIcon/ENHPicon.png",1280-40,100))
        self.ButtonsPage1.append(Button(self.win,"E1SS","BattleIcon/ENSPicon.png",1280-40,165))
        self.ButtonsPage1.append(Button(self.win,"Special", "BattleIcon/Special.png",920,660))

        self.ActionButtonsPage1 = []

        self.ActionButtonsPage1.append(Button(self.win,"Attack", "BattleIcon/Attack.png",125,660))
        self.ActionButtonsPage1.append(Button(self.win,"Item", "BattleIcon/Item.png",360,660))
        self.ActionButtonsPage1.append(Button(self.win,"Flee", "BattleIcon/Flee.png",1155,660))
        self.ActionButtonsPage1.append(Button(self.win,"Special", "BattleIcon/Special.png",920,660))

        self.PlayerActive = PA

        self.EnemyActive = EA

        self.PlayerSmallFighter = []

        dummyx =  40

        self.Side = Button(self.win,"Side", "BattleIcon/BattleList.png",239,360)
        self.ChooseItem = Button(self.win, "ChooseItem", "BattleIcon/ChooseItem.png", 239, 50)
        self.ChooseSpecial = Button(self.win, "ChooseSpecail", "BattleIcon/ChooseSpecial.png", 239, 50)

        for i in self.PlayerParty:
            w = Button(self.win,"FighterPic",i.getSmallFighterPicture(),dummyx,32)
            self.PlayerSmallFighter.append(w)
            dummyx = dummyx + 70

        self.EnemySmallFighter = []

        dummyx =  1280-40

        
        for i in self.EnemyParty:
            w = Button(self.win,"FighterPic",i.getSmallFighterPicture(),dummyx,32)
            self.EnemySmallFighter.append(w)
            dummyx = dummyx - 70

        self.Background = Button(self.win,"Background", self.userfile,640,360)
        self.Background.draw()

        self.DrawButtons(self.ButtonsPage1)
        
        for i in self.PlayerSmallFighter:
            i.draw()

        for i in self.EnemySmallFighter:
            i.draw()
        
        self.HealthBars = []

        self.dummyx = 40 + 50

        for i in range (self.PlayerActive.getHealthPercents()):
            self.HealthBars.append(Button(self.win,"HealthBar","BattleIcon/HP.png",self.dummyx,100))
            self.dummyx = self.dummyx + 36

        for i in self.HealthBars:
            i.draw()

        self.SpecialBars = []

        self.dummyx = 40 + 50

        for i in range (self.PlayerActive.getSpecialPercents()):
            self.SpecialBars.append(Button(self.win,"SpecialBar","BattleIcon/SP.png",self.dummyx,165))
            self.dummyx = self.dummyx + 36

        for i in self.SpecialBars:
            i.draw()        

        self.ENHealthBars = []

        self.dummyx = 1280- 40 - 50

        for i in range (self.EnemyActive.getHealthPercents()):
            self.ENHealthBars.append(Button(self.win,"HealthBar","BattleIcon/ENHP.png",self.dummyx,100))
            self.dummyx = self.dummyx - 36

        for i in self.ENHealthBars:
            i.draw()

        self.ENSpecialBars = []

        self.dummyx = 1280- 40 - 50

        for i in range (self.EnemyActive.getSpecialPercents()):
            self.ENSpecialBars.append(Button(self.win,"SpecialBar","BattleIcon/ENSP.png",self.dummyx,165))
            self.dummyx = self.dummyx - 36

        for i in self.ENSpecialBars:
            i.draw()

        self.PlayerActive.DrawBattle('P')

        self.EnemyActive.DrawBattle('E')

    def PlayerTurn(self, x, y):
        if self.First == 'P':
            for i in range(len(self.PlayerParty)):
                if self.turn != 0:
                    self.undraw()    
                self.BattleScreenDraw(self.PlayerParty[x], self.EnemyParty[y])
                Action = 0
                
                while(Action == 0):
                    for i in self.ActionButtonsPage1:
                        click = self.win.getMouse()
                        if (click.getX() < (i.getX() + 230/2)) and (click.getX() > (i.getX() - 230/2)):
                            if (click.getY() < (i.getY() + 115/2)) and (click.getY() > (i.getY() - 115/2)):
                                if i.getName() == 'Attack':
                                    if self.Location == 'R':
                                        multi = 1
                                        junkvar = self.PlayerActive.getRealWeapon().getElement()
                                        junkvar2 = self.EnemyActive.getRealArmor().getElement()
                                        
                                        if (self.determineWeakness(junkvar, junkvar2) == True):
                                            multi = self.PlayerActive.getMulti()
                                        
                                        tempvar = multi * self.PlayerActive.getRealAttack() - self.EnemyActive.getRealDefense()
                                        if tempvar <0:
                                            tempvar = 0
                                    elif self.Location == 'D':
                                        multi = 1
                                        junkvar = self.PlayerActive.getDreamWeapon()
                                        junkvar2 = self.EnemyActive.getDreamArmor()
                                        
                                        if self.determineWeakness(junkvar.getElement(), junkvar2.getElement()) == True:
                                            multi = self.PlayerActive.getMulti()
                                        
                                        tempvar = multi * self.PlayerActive.getDreamAttack() - self.EnemyActive.getDreamDefense()
                                        if tempvar <0:
                                            tempvar = 0
                                    self.EnemyActive.lowerHP(tempvar)
                                    self.text.BattleText(self.PlayerActive.getName() + " attacked " ,self.EnemyActive.getName() + " for " ,str(tempvar) + " damage." )
                                    Action = 1

                                if i.getName() == 'Item':
                                    if self.Location == 'R':
                                        Items = self.PlayerActive.getRealItems()
                                
                                    elif self.Location == 'D':
                                        Items = self.PlayerActive.getDreamItems()
                                    
                                    if Items == []:
                                        self.text.BattleText("You Have No Items.",'','')
                                        Action = 0

                                    else:
                                        self.Side.draw()
                                        self.ChooseItem.draw()
                                        DrawnItems = []
                                        x = 239
                                        y = 100 + 60
                                        for i in Items:
                                            w  = Button(self.win, "Don't Worry", i.getFile(), x, y)
                                            w.StoreItem(i)
                                            DrawnItems.append(w)
                                            y = y + 100

                                        for i in DrawnItems:
                                            i.draw()

                                        SubAction = 0

                                        while(SubAction == 0):
                                            for i in DrawnItems:
                                                Subclick = self.win.getMouse()
                                                if (Subclick.getX() < (i.getX() + 239)) and (Subclick.getX() > (i.getX() - 239)):
                                                    if (Subclick.getY() < (i.getY() + 50)) and (Subclick.getY() > (i.getY() - 50)):
                                                        Business = i.getItem()
                                                        self.PlayerActive, self.EnemyActive = Business.Work(self.PlayerActive, self.EnemyActive)
                                                        
                                                        if Business.GetType() == 'Heal':
                                                            Macarena = self.PlayerActive.getName()

                                                        elif Business.GetType() == 'Damage':
                                                            Macarena == self.EnemyActive.getName()

                                                        self.text.BattleText(self.PlayerActive.getName() + ' used ' ,Business.getName() + " to " , Business.GetType() +' '+ Macarena +'.')
                                                        
                                                        if self.Location == 'R':
                                                            self.PlayerActive.RemoveRealItem(Business)
                                                        
                                                        elif self.Location == 'D':
                                                            self.PlayerActive.RemoveDreamItem(Business)
                                                        
                                                        DrawnItems.remove(i)
                                                        Action = 1
                                                        SubAction = 1

                                if i.getName() == 'Special':
                                    if self.Location == 'R':
                                        Specials = self.PlayerActive.getRealSpecial()
                                
                                    elif self.Location == 'D':
                                        Specials = self.PlayerActive.getDreamSpecial()
                                    
                                    if Specials == []:
                                        self.text.BattleText("You Have No Specials.",'','')
                                        Action = 0

                                    else:
                                        self.Side.draw()
                                        self.ChooseSpecial.draw()
                                        DrawnItems = []
                                        x = 239
                                        y = 100 + 60
                                        for i in Specials:
                                            w  = Button(self.win, "Don't Worry", i.getFile(), x, y)
                                            w.StoreItem(i)
                                            DrawnItems.append(w)
                                            y = y + 100

                                        for i in DrawnItems:
                                            i.draw()

                                        SubAction = 0

                                        while(SubAction == 0):
                                            for i in DrawnItems:
                                                Subclick = self.win.getMouse()
                                                if (Subclick.getX() < (i.getX() + 239)) and (Subclick.getX() > (i.getX() - 239)):
                                                    if (Subclick.getY() < (i.getY() + 50)) and (Subclick.getY() > (i.getY() - 50)):
                                                        RingADingDingDong = i.getItem()
                                                        if self.PlayerActive.getSP() >= RingADingDingDong.getSP(): 
                                                            Business = i.getItem()
                                                            multi = 1
                                                            if self.Location == 'R':
                                                                junkvar = self.PlayerActive.getRealWeapon()
                                                                junkvar2 = self.EnemyActive.getRealArmor()
                                                                
                                                                if self.determineWeakness(junkvar.getElement(), junkvar2.getElement()) == True:
                                                                    multi = self.PlayerActive.getMulti()
                                            
                                                            elif self.Location == 'D':
                                                                junkvar = self.PlayerActive.getDreamWeapon()
                                                                junkvar2 = self.EnemyActive.getDreamArmor()
                                                                
                                                                if self.determineWeakness(junkvar.getElement(), junkvar2.getElement()) == True:
                                                                    multi = self.PlayerActive.getMulti()
                                                        
                                                            self.PlayerActive, self.EnemyActive = Business.Work(self.PlayerActive, self.EnemyActive,'P', self.Location, multi)
                                                            
                                                            if 1==1:
                                                                if Business.GetType() == 'Heal':
                                                                    Shoe = Business.GetType()
                                                                    LaBamba = self.PlayerActive.getName()
                                                                
                                                                elif Business.GetType() == 'Blocked':
                                                                    Shoe = Business.GetTpe()
                                                                    LaBamba = self.EnemyActive.getName()

                                                                else:
                                                                    Shoe = 'Damage'
                                                                    LaBamba = self.EnemyActive.getName()
                                                            
                                                            self.text.BattleText(self.PlayerActive.getName() + ' performed ' , Business.getName() + " to " , Shoe + ' ' + LaBamba + '.')

                                                            Don = 'No Worry'
                                                            SubAction = 1
                                                            
                                                        else:
                                                            self.text.BattleText("You lack SP.",'','')    
                                                            Don = 'Worry'
                                                            SubAction = 1
                                        
                                        self.Side.undraw()
                                        self.ChooseSpecial.undraw()

                                        for i in DrawnItems:
                                            i.undraw()
                                        if Don == 'No Worry':
                                            Action = 1
                                
                                if i.getName() == 'Flee':
                                    if self.Flee == 'F':
                                        self.WIN = 'Fled'
                                        self.Action = 1

                                    else:
                                        self.text.BattleText("You can't run away","from this one...",'')


                    if (x+1)< len(self.PlayerParty):
                        x = x + 1
                        self.PlayerActive = self.PlayerParty[x]
    
    def EnemyTurn(self, x, y):
        for i in self.EnemyParty:
                self.BattleScreenDraw(self.PlayerParty[x], self.EnemyParty[y])
                randomnumber = r.randint(0,2)
                if randomnumber == 0:
                    if self.Location == 'R':
                        multi = 1
                        junkvar2 = self.PlayerActive.getRealArmor()
                        junkvar = self.EnemyActive.getRealWeapon()
                            
                        if self.determineWeakness(junkvar.getElement(), junkvar2.getElement()) == True:
                            multi = self.PlayerActive.getMulti()
                                            
                        tempvar = multi * self.EnemyActive.getRealAttack() - self.PlayerActive.getRealDefense()

                        if tempvar <0:
                            tempvar = 0
                        self.text.BattleText(self.EnemyActive.getName() + " attacked " ,self.PlayerActive.getName() + " for " ,str(tempvar) + " damage." )
                                        
                    elif self.Location == 'D':
                        multi = 1
                        junkvar2 = self.PlayerActive.getDreamArmor()
                        junkvar = self.EnemyActive.getDreamWeapon()
                            
                        if self.determineWeakness(junkvar.getElement(), junkvar2.getElement()) == True:
                            multi = self.PlayerActive.getMulti()
                                            
                        tempvar = multi * self.EnemyActive.getDreamAttack() - self.PlayerActive.getDreamDefense()
                        if tempvar <0:
                            tempvar = 0
                        self.text.BattleText(self.EnemyActive.getName() + " attacked " ,self.PlayerActive.getName() + " for " ,str(tempvar) + " damage." )
                    
                    self.PlayerActive.lowerHP(tempvar)

                elif randomnumber == 1:
                    multi = 1
                    num = i.getSpecialNum(self.Location)
                    if num == 1:
                        Business = i.getSpecial(0,self.Location)

                    elif num > 1:
                        Business = i.getSpecial(randint(0,i.getSpecialNum()), self.Location)

                    self.PlayerActive, self.EnemyActive = Business.Work(self.PlayerActive, self.EnemyActive, 'E', self.Location, multi)

                    if Business.GetType() == 'Heal':
                        Live_Mas = self.EnemyActive.getName()

                    elif Business.GetType() == 'Damage':
                        Live_Mas = self.PlayerActive.getName()
                                                                
                    elif Business.GetType() == 'Blocked':
                        Live_Mas = self.PlayerActive.getName()
  
                    self.text.BattleText(self.EnemyActive.getName() + ' performed ' , Business.getName() + " to " , Business.GetType() + ' ' + Live_Mas + '.')

                    
                    
                if (y+1)< len(self.EnemyParty):
                    y = y + 1
                    self.EnemyActive = self.EnemyParty[y]

    def Fight(self):
        self.BattleDone = 0
        
        while(self.BattleDone == 0):
            x = 0
            y = 0
            
            self.PlayerTurn(x,y)

            x = 0                                       
            y = 0

            NetzaVar = self.checkCharHP()

            if NetzaVar != None:
                return NetzaVar, self.exp

            self.EnemyTurn(x,y)
               
            y = 0

            self.PlayerActive = self.PlayerParty [x]
            self.EnemyActive = self.EnemyParty[y]

            NetzaVar = self.checkCharHP()

            if NetzaVar != None:
                return NetzaVar, self.exp
            
            self.turn = 1

    def undraw(self):
        self.UndrawPage(self.ButtonsPage1)
        self.PlayerActive.UndrawBattle()
        self.EnemyActive.UndrawBattle()
        '''
        self.Background.undraw()
        '''

    def closeScreen(self):
        self.UndrawPage(self.ButtonsPage1)
        self.PlayerActive.UndrawBattle()
        self.EnemyActive.UndrawBattle()
        self.Background.undraw()
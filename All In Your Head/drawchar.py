from graphics import *
from text import *
from Button import *

class Screen:
    def __init__(self, win):
        self.ctpoint = Point(640,640)
        self.pyr_health_point = Point(80,80) 
        self.enemy_health_point = Point(1220,80) 
        self.attack_name_point = Point(650,340)
        self.win = win
        self.text = gameText(self.win)
    
    def drawCharInLeftChat(self,filelist):
        xpos = 200
        ypos = 350
        self.CharModelList = []
        for i in filelist:
            self.CharModelList.append(Image(Point(xpos,ypos),i))
            xpos = xpos + 225
        
        for i in self.CharModelList:
            i.draw(self.win)

    def undrawCharInLeftChat(self):
        for i in self.CharModelList:
            i.undraw()

    def drawScreen(self,background,char,name):
        self.text.setDrawBackground(background)
        self.drawCharInLeftChat(char)
        self.text.drawTextBox()
        self.text.characterName(name)
    
    def undrawScreen(self):
        self.undrawCharInLeftChat()
        self.text.undrawBackground()
        self.text.undrawTextBox()  
        self.text.undrawName()

    def updateScreen(self,background,char, name):
        if background != '':
            self.undrawScreen()
            self.drawScreen(background,char,name) 
            
        else:
            self.undrawCharInLeftChat()
            self.text.undrawTextBox()  
            self.text.undrawName()
            
            self.drawCharInLeftChat(char)
            self.text.drawTextBox()
            self.text.characterName(name)

    def MakeChoice(self, choice, choicefiles, name):
        self.text.undrawTextBox()
        self.text.undrawName()

        y = 100
        choices = []
        Persona = 0
        for i in choice:    
            choices.append(Button(self.win,i, choicefiles[Persona], 900, y ))
            y = y + 160
            Persona = Persona + 1

        for i in choices:
            i.draw()

        while(True):
            for i in choices:
                click = self.win.getMouse()
                if (click.getX() < (i.getX() + 230/2)) and (click.getX() > (i.getX() - 230/2)):
                    if (click.getY() < (i.getY() + 115/2)) and (click.getY() > (i.getY() - 115/2)):
                        for w in choices:
                            w.undraw()
                        self.text.drawTextBox()
                        self.text.characterName(name)
                        return i.getName() 


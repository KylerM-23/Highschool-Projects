from graphics import *

class gameText:
    def __init__(self, win):
        self.ctpoint = Point(640,640)
        self.pyr_health_point = Point(80,80) 
        self.enemy_health_point = Point(1220,80) 
        self.attack_name_point = Point(650,340)
        self.win = win
        self.qpoint = Point(640,140)
        self.opt1point = Point(640,240)
        self.opt2point = Point(640,340)
        self.opt3point = Point(640,440)
        self.opt4point = Point(640,540)
        self.questionbox = Point(640,640)
        self.center = Point(640,360)
        self.fontsize = 22
    
    def characterName(self, word):
        if len(word) >= 30:
            self.nam = word[0:30]
            self.name = Text(Point(100,480),self.nam)
            self.name.setFace('DS_Mysticora Medium')
            self.name.setFill('white')
            self.name.setSize(25)
            self.name.draw(self.win)
        else:
            self.nam = word
            self.name = Text(Point(90,480),self.nam)
            self.name.setFace('DS_Mysticora Medium')
            self.name.setFill('white')
            self.name.setSize(25)
            self.name.draw(self.win)

    def undrawName(self):
        self.name.undraw()

    def changeName(self,word):
        self.undrawName()
        self.characterName(word)

    def drawTextBox(self):
        self.box = Image(self.center,"background/textbackground.png")
        self.box.draw(self.win)
    
    def undrawTextBox(self):
        self.box.undraw()

    def text(self,message):
        altmessage = message
        label = Text(self.ctpoint,altmessage)
        label.setFace('DS_Mysticora_Medium')
        label.setSize(self.fontsize)
        label.setFill('white')
        label.draw(self.win)
        self.win.getMouse()
        label.undraw()
    
    def BattleText(self, message, message1, message2):
        messages = []
        messagesback = []
        
        if message1 == '':
            messages.append(Text(Point(640, 616),message))
            messagesback.append(Text(Point(640, 616),message))
        
        elif message1 != '':
            y = 580
            messages.append(Text(Point(640, y),message))
            messagesback.append(Text(Point(640, y),message))
            
            y = y + 40
            messages.append(Text(Point(640, y),message1))
            messagesback.append(Text(Point(640, y),message1))
            y = y + 40
            if message2 != '':
                messages.append(Text(Point(640, y),message2))
                messagesback.append(Text(Point(640, y),message2))


        for label in messagesback:
            label.setSize(25)
            label.setFill('black')
            label.draw(self.win)

        for label in messages:
            label.setSize(24)
            label.setFill('white')
            label.draw(self.win)
        
        self.win.getMouse()
        
        for label in messages:   
            label.undraw()

        for i in messagesback:
            i.undraw()
                

    def doubleText(self,message1,message2):
        altmessage1 = message1
        altmessage2 = message2
        label1 = Text(Point(640,580),altmessage1)
        label1.setFace('DS_Mysticora Medium')
        label1.setSize(self.fontsize)
        label1.setFill('white')
        label2 = Text(Point(640,620),altmessage2)
        label2.setSize(self.fontsize)
        label2.setFace('DS_Mysticora Medium')
        label2.setFill('white')
        label1.draw(self.win)
        label2.draw(self.win)
        self.win.getMouse()
        label1.undraw()
        label2.undraw()

    def tripleText(self,message1,message2,message3):
        altmessage1 = message1
        altmessage2 = message2
        altmessage3 = message3
        label1 = Text(Point(640,580),altmessage1)
        label1.setSize(self.fontsize)
        label1.setFill('White')
        label2 = Text(Point(640,620),altmessage2)
        label2.setSize(self.fontsize)
        label2.setFill('White')
        label3 = Text(Point(640,660),altmessage3)
        label3.setSize(self.fontsize)
        label3.setFill('White')
        label1.draw(self.win)
        label2.draw(self.win)
        label3.draw(self.win)
        self.win.getMouse()
        label1.undraw()
        label2.undraw()
        label3.undraw()

    def textQuestionNoPic(self,message,var1,var2,var3,var4):
        quesstionm = (message)
        question = Text(self.qpoint,quesstionm)
        question.draw(self.win)
        optm1 = (var1)
        opt1 = Text(self.opt1point,optm1)
        opt1.draw(self.win)
        optm2 = (var2)
        opt2 = Text(self.opt2point,optm2)
        opt2.draw(self.win)
        optm3 = (var3)
        opt3 = Text(self.opt3point,optm3)
        opt3.draw(self.win)
        optm4 = (var4)
        opt4 = Text(self.opt4point,optm4)
        opt4.draw(self.win)
        disans = (Entry(self.questionbox,30))
        disans.draw(self.win)
        disans.setText('1')

        self.win.getMouse()
        
        ans = int(disans.getText())
        
        disans.undraw()
        question.undraw()
        opt1.undraw()
        opt2.undraw()
        opt3.undraw()
        opt4.undraw()  
        
        return ans
    
    def textQuestionOnePic(self,message,var1,var2,var3,var4,image1):
        quesstionm = (message)
        question = Text(self.qpoint,quesstionm)
        question.draw(self.win)
        
        optm1 = (var1)
        opt1 = Text(self.opt1point,optm1)
        opt1.draw(self.win)
        optm2 = (var2)
        opt2 = Text(self.opt2point,optm2)
        opt2.draw(self.win)
        optm3 = (var3)
        opt3 = Text(self.opt3point,optm3)
        opt3.draw(self.win)
        optm4 = (var4)
        opt4 = Text(self.opt4point,optm4)
        opt4.draw(self.win)

        optpic1 = Image(Point(250,240), image1)
        optpic1.draw(self.win)
        
        disans = (Entry(self.questionbox,30))
        disans.setText('1')
        disans.draw(self.win)
        
        self.win.getMouse()
        
        ans = int(disans.getText())
        
        question.undraw()

        opt1.undraw()
        opt2.undraw()
        opt3.undraw()
        opt4.undraw()  
        disans.undraw()
        optpic1.undraw()

        return ans

    def textQuestionTwoPic(self,message,var1,var2,var3,var4,image1,image2):
        quesstionm = (message)
        question = Text(self.qpoint,quesstionm)
        question.draw(self.win)
        
        optm1 = (var1)
        opt1 = Text(self.opt1point,optm1)
        opt1.draw(self.win)
        optm2 = (var2)
        opt2 = Text(self.opt2point,optm2)
        opt2.draw(self.win)
        optm3 = (var3)
        opt3 = Text(self.opt3point,optm3)
        opt3.draw(self.win)
        optm4 = (var4)
        opt4 = Text(self.opt4point,optm4)
        opt4.draw(self.win)

        optpic1 = Image(Point(250,240), image1)
        optpic1.draw(self.win)
        optpic2 = Image(Point(1030,240), image2)
        optpic2.draw(self.win)
        
        disans = (Entry(self.questionbox,30))
        disans.setText('1')
        disans.draw(self.win)

        self.win.getMouse()
        
        ans = int(disans.getText())
        
        question.undraw()

        opt1.undraw()
        opt2.undraw()
        opt3.undraw()
        opt4.undraw()  
        disans.undraw()
        optpic1.undraw()
        optpic2.undraw()

        return ans

    def textQuestionThreePic(self,message,var1,var2,var3,var4,image1,image2,image3):
        quesstionm = (message)
        question = Text(self.qpoint,quesstionm)
        question.draw(self.win)
        
        optm1 = (var1)
        opt1 = Text(self.opt1point,optm1)
        opt1.draw(self.win)
        optm2 = (var2)
        opt2 = Text(self.opt2point,optm2)
        opt2.draw(self.win)
        optm3 = (var3)
        opt3 = Text(self.opt3point,optm3)
        opt3.draw(self.win)
        optm4 = (var4)
        opt4 = Text(self.opt4point,optm4)
        opt4.draw(self.win)

        optpic1 = Image(Point(250,240), image1)
        optpic1.draw(self.win)
        optpic2 = Image(Point(250,480), image2)
        optpic2.draw(self.win)
        optpic3 = Image(Point(1030,240), image3)
        optpic3.draw(self.win)
        
        disans = (Entry(self.questionbox,30))
        disans.setText('1')
        disans.draw(self.win)
        
        self.win.getMouse()
        
        ans = int(disans.getText())
        
        question.undraw()

        opt1.undraw()
        opt2.undraw()
        opt3.undraw()
        opt4.undraw()  
        disans.undraw()
        optpic1.undraw()
        optpic2.undraw()
        optpic3.undraw()

        return ans

    def textQuestionFourPic(self,message,var1,var2,var3,var4,image1,image2,image3,image4):
        quesstionm = (message)
        question = Text(self.qpoint,quesstionm)
        question.draw(self.win)
        
        optm1 = (var1)
        opt1 = Text(self.opt1point,optm1)
        opt1.draw(self.win)
        optm2 = (var2)
        opt2 = Text(self.opt2point,optm2)
        opt2.draw(self.win)
        optm3 = (var3)
        opt3 = Text(self.opt3point,optm3)
        opt3.draw(self.win)
        optm4 = (var4)
        opt4 = Text(self.opt4point,optm4)
        opt4.draw(self.win)

        optpic1 = Image(Point(250,240), image1)
        optpic1.draw(self.win)
        optpic2 = Image(Point(250,480), image2)
        optpic2.draw(self.win)
        optpic3 = Image(Point(1030,240), image3)
        optpic3.draw(self.win)
        optpic4 = Image(Point(1030,480), image4)
        optpic4.draw(self.win)
        
        disans = (Entry(self.questionbox,30))
        disans.setText('1')
        disans.draw(self.win)
        

        self.win.getMouse()
        
        ans = int(disans.getText())
        
        question.undraw()

        opt1.undraw()
        opt2.undraw()
        opt3.undraw()
        opt4.undraw()  
        disans.undraw()
        optpic1.undraw()
        optpic2.undraw()
        optpic3.undraw()
        optpic4.undraw()

        return ans
        
    def atktext(self,message):
        altmessage = (message)
        label = Text(ctpoint,altmessage)
        label.draw(win)
        win.getMouse()
        label.undraw()
    
    def setDrawBackground(self,file):
        self.background = Image(self.center, file)
        self.background.draw(self.win) 
    
    def undrawBackground(self):
        self.background.undraw()

    
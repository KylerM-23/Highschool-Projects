from text import *
from graphics import *
from drawchar import *

def FindName(win):
        class Keyboard:
                def __init__(self, file, letter,x,y,win):
                        self.file = file
                        self.letter = letter
                        self.x = x
                        self.y = y
                        self.win = win
                        self.postion = Point(self.x,self.y)
                        self.picture = Image(self.postion, file)

                def draw(self):
                        self.picture.draw(self.win)
                
                def getXpoint(self):
                        return self.x

                def getYpoint(self):
                        return self.y
                
                def getLetter(self):
                        return self.letter
                def getFile(self):
                        return self.file

                def undraw(self):
                        self.picture.undraw()

        def demo(letters,win):
                name = ''

                for i in letters:
                        i.draw() 
                
                charlength = 0
                
                while(True):
                        click = win.getMouse()
                        xpoint = click.getX()
                        ypoint = click.getY()
                        
                        xplot = 340
                        yplot = 310 

                        for i in letters:      
                                if ((i.getXpoint()+25) >= xpoint  and xpoint>= (i.getXpoint()-25)) :
                                        if ((i.getYpoint()+25) >= ypoint  and ypoint >= (i.getYpoint()-25)):
                                                if i.getLetter()=='Done':
                                                        if charlength == 10:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()
                                                                Letter4.undraw()
                                                                Letter5.undraw()
                                                                Letter6.undraw()
                                                                Letter7.undraw()
                                                                Letter8.undraw()
                                                                Letter9.undraw()
                                                                Letter10.undraw()
                                                        
                                                        elif charlength == 9:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()
                                                                Letter4.undraw()
                                                                Letter5.undraw()
                                                                Letter6.undraw()
                                                                Letter7.undraw()
                                                                Letter8.undraw()
                                                                Letter9.undraw()
                                                        
                                                        elif charlength == 8:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()
                                                                Letter4.undraw()
                                                                Letter5.undraw()
                                                                Letter6.undraw()
                                                                Letter7.undraw()
                                                                Letter8.undraw()

                                                        elif charlength == 7:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()
                                                                Letter4.undraw()
                                                                Letter5.undraw()
                                                                Letter6.undraw()
                                                                Letter7.undraw()

                                                        elif charlength == 6:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()
                                                                Letter4.undraw()
                                                                Letter5.undraw()
                                                                Letter6.undraw()

                                                        elif charlength == 5:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()
                                                                Letter4.undraw()
                                                                Letter5.undraw()

                                                        elif charlength == 4:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()
                                                                Letter4.undraw()
                                                        
                                                        elif charlength == 3:
                                                                Letter1.undraw()
                                                                Letter2.undraw()
                                                                Letter3.undraw()

                                                        elif charlength == 2:
                                                                Letter1.undraw()
                                                                Letter2.undraw()

                                                        elif charlength == 1:
                                                                Letter1.undraw()

                                                        return name
                                                elif i.getLetter() == 'BackArrow':
                                                        name = name[:-1]
                                                        print(name)
                                                        
                                                        if charlength == 1:
                                                                Letter1.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 2:
                                                                Letter2.undraw()           
                                                                charlength = charlength - 1                             
                                                        elif charlength == 3:
                                                                Letter3.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 4:
                                                                Letter4.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 5:
                                                                Letter5.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 6:
                                                                Letter6.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 7:
                                                                Letter7.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 8:
                                                                Letter8.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 9:
                                                                Letter9.undraw()
                                                                charlength = charlength - 1
                                                        elif charlength == 10:
                                                                Letter10.undraw()
                                                                charlength = charlength - 1
                                                else:
                                                        if charlength <10:
                                                                name = name + i.getLetter()
                                                                charlength = charlength + 1
                                                                if charlength == 1:
                                                                        Letter1 = Image(Point(xplot,yplot),i.getFile())
                                                                        Letter1.draw(win)
                                                                elif charlength == 2:
                                                                        Letter2 = Image(Point(xplot+65,yplot),i.getFile())
                                                                        Letter2.draw(win)
                                                                elif charlength == 3:
                                                                        Letter3 = Image(Point(xplot+2*65,yplot),i.getFile())
                                                                        Letter3.draw(win)
                                                                elif charlength == 4:
                                                                        Letter4 = Image(Point(xplot+3*65,yplot),i.getFile())
                                                                        Letter4.draw(win)
                                                                elif charlength == 5:
                                                                        Letter5 = Image(Point(xplot+4*65,yplot),i.getFile())
                                                                        Letter5.draw(win)
                                                                elif charlength == 6:
                                                                        Letter6 = Image(Point(xplot+5*65,yplot),i.getFile())
                                                                        Letter6.draw(win)
                                                                elif charlength == 7:
                                                                        Letter7 = Image(Point(xplot+6*65,yplot),i.getFile())
                                                                        Letter7.draw(win)
                                                                elif charlength == 8:
                                                                        Letter8 = Image(Point(xplot+7*65,yplot),i.getFile())
                                                                        Letter8.draw(win)
                                                                elif charlength == 9:
                                                                        Letter9 = Image(Point(xplot+8*65,yplot),i.getFile())
                                                                        Letter9.draw(win)
                                                                elif charlength == 10:
                                                                        Letter10 = Image(Point(xplot+9*65,yplot),i.getFile())
                                                                        Letter10.draw(win)
        txt = gameText(win)

        txt.setDrawBackground('KeyboardLetters/Name.png')
        
        Question = Image(Point((1280/2),350),'KeyboardLetters/Title.png')
        Question.draw(win)
        
        x = 340
        y = 300
        z = 65

        Space1 = Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space1.draw(win)
        x = x + z
        Space2 = Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space2.draw(win)
        x = x + z
        Space3 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space3.draw(win)
        x = x + z
        Space4 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space4.draw(win)
        x = x + z
        Space5 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space5.draw(win)
        x = x + z
        Space6 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space6.draw(win)
        x = x + z
        Space7 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space7.draw(win)
        x = x + z
        Space8 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space8.draw(win)
        x = x + z
        Space9 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space9.draw(win)
        x = x + z
        Space10 =Image(Point(x,y),'KeyboardLetters/ST/US.png')
        Space10.draw(win)

        screen = Screen(win)

        x1 = 65
        x2 = 130
        x3 = 195
        x4 = 260
        x5 = 325
        x6 = 390
        x7 = 455
        x8 = 520
        x9 = 585
        x10 = 650
        x11 = 715
        x12 = 780
        x13 = 845
        x14 = 910
        x15 = 975
        x16 = 1040
        x17 = 1105
        x18 = 1170
        x19 = 1235

        y0 = 395
        y1 = 460 
        y2 = 525
        y3 = 590
        y4 = 655

        A = Keyboard("KeyboardLetters/UCB/A.png", 'A',x1,y1,win)
        B = Keyboard("KeyboardLetters/UCB/B.png",'B',x2,y1,win)
        C = Keyboard("KeyboardLetters/UCB/C.png",'C',x3,y1,win)
        D = Keyboard("KeyboardLetters/UCB/D.png",'D',x4,y1,win)
        E =Keyboard("KeyboardLetters/UCB/E.png",'E',x5,y1,win)
        F = Keyboard("KeyboardLetters/UCB/F.png",'F',x6,y1,win)
        G =Keyboard("KeyboardLetters/UCB/G.png",'G',x7,y1,win)
        H = Keyboard("KeyboardLetters/UCB/H.png",'H',x1,y2,win)
        I = Keyboard("KeyboardLetters/UCB/I.png",'I',x2,y2,win)
        J =Keyboard("KeyboardLetters/UCB/J.png",'J',x3,y2,win)
        K =Keyboard("KeyboardLetters/UCB/K.png",'K',x4,y2,win)
        L =Keyboard("KeyboardLetters/UCB/L.png",'L',x5,y2,win)
        M =Keyboard("KeyboardLetters/UCB/M.png",'M',x6,y2,win)
        N = Keyboard("KeyboardLetters/UCB/N.png",'N',x7,y2,win)
        O =Keyboard("KeyboardLetters/UCB/O.png",'O',x1,y3,win)
        P =Keyboard("KeyboardLetters/UCB/P.png",'P',x2,y3,win)
        Q =Keyboard("KeyboardLetters/UCB/Q.png",'Q',x3,y3,win)
        R =Keyboard("KeyboardLetters/UCB/R.png",'R',x4,y3,win)
        S =Keyboard("KeyboardLetters/UCB/S.png",'S',x5,y3,win)
        T =Keyboard("KeyboardLetters/UCB/T.png",'T',x6,y3,win)
        U =Keyboard("KeyboardLetters/UCB/U.png",'U',x7,y3,win)
        V =Keyboard("KeyboardLetters/UCB/V.png",'V',x1,y4,win)
        W = Keyboard("KeyboardLetters/UCB/W.png",'W',x2,y4,win)
        X =Keyboard("KeyboardLetters/UCB/X.png",'X',x3,y4,win)
        Y =Keyboard("KeyboardLetters/UCB/Y.png",'Y',x4,y4,win)
        Z = Keyboard("KeyboardLetters/UCB/Z.png",'Z',x5,y4,win)
        Underscore =Keyboard("KeyboardLetters/SB/US.png",' ',x6,y4,win)
        Period = Keyboard("KeyboardLetters/SB/PERIOD.png",'.',x7,y4,win)
        a =Keyboard("KeyboardLetters/LCB/a.png",'a',x9,y1,win)
        b =Keyboard("KeyboardLetters/LCB/b.png",'b',x10,y1,win)
        c =Keyboard("KeyboardLetters/LCB/c.png",'c',x11,y1,win)
        d =Keyboard("KeyboardLetters/LCB/d.png",'d',x12,y1,win)
        e =Keyboard("KeyboardLetters/LCB/e.png",'e',x13,y1,win)
        f =Keyboard("KeyboardLetters/LCB/f.png",'f',x14,y1,win)
        g =Keyboard("KeyboardLetters/LCB/g.png",'g',x15,y1,win)
        h =Keyboard("KeyboardLetters/LCB/h.png",'h',x9,y2,win)
        i =Keyboard("KeyboardLetters/LCB/i.png",'i',x10,y2,win)
        j =Keyboard("KeyboardLetters/LCB/j.png",'j',x11,y2,win)
        k =Keyboard("KeyboardLetters/LCB/k.png",'k',x12,y2,win)
        l =Keyboard("KeyboardLetters/LCB/l.png",'l',x13,y2,win)
        m =Keyboard("KeyboardLetters/LCB/m.png",'m',x14,y2,win)
        n =Keyboard("KeyboardLetters/LCB/n.png",'n',x15,y2,win)
        o =Keyboard("KeyboardLetters/LCB/o.png",'o',x9,y3,win)
        p =Keyboard("KeyboardLetters/LCB/p.png",'p',x10,y3,win)
        q =Keyboard("KeyboardLetters/LCB/q.png",'q',x11,y3,win)
        r =Keyboard("KeyboardLetters/LCB/r.png",'r',x12,y3,win)
        s =Keyboard("KeyboardLetters/LCB/s.png",'s',x13,y3,win)
        t =Keyboard("KeyboardLetters/LCB/t.png",'t',x14,y3,win)
        u =Keyboard("KeyboardLetters/LCB/u.png",'u',x15,y3,win)
        v =Keyboard("KeyboardLetters/LCB/v.png",'v',x9,y4,win)
        w = Keyboard("KeyboardLetters/LCB/w.png",'w',x10,y4,win)
        x =Keyboard("KeyboardLetters/LCB/x.png",'x',x11,y4,win)
        y =Keyboard("KeyboardLetters/LCB/y.png",'y',x12,y4,win)
        z =Keyboard("KeyboardLetters/LCB/z.png",'z',x13,y4,win)
        
        Apostrophe =Keyboard("KeyboardLetters/SB/'.png","'",x14,y4,win)
        Quotation =Keyboard("KeyboardLetters/SB/quotation.png",'"',x15,y4,win)

        One =Keyboard("KeyboardLetters/SB/1.png",'1',x17,y1,win)
        Two =Keyboard("KeyboardLetters/SB/2.png",'2',x18,y1,win)
        Three =Keyboard("KeyboardLetters/SB/3.png",'3',x19,y1,win)
        Four =Keyboard("KeyboardLetters/SB/4.png",'4',x17,y2,win)
        Five =Keyboard("KeyboardLetters/SB/5.png",'5',x18,y2,win)
        Six =Keyboard("KeyboardLetters/SB/6.png",'6',x19,y2,win)
        Seven =Keyboard("KeyboardLetters/SB/7.png",'7',x17,y3,win)
        Eight =Keyboard("KeyboardLetters/SB/8.png",'8',x18,y3,win)
        Nine =Keyboard("KeyboardLetters/SB/9.png",'9',x19,y3,win)
        Zero =Keyboard("KeyboardLetters/SB/0.png",'0',x18,y4,win)
        
        Excalmation =Keyboard("KeyboardLetters/SB/!.png",'!',x17,y4,win)
        Dash = Keyboard("KeyboardLetters/SB/-.png",'-',x19,y4,win)
        
        BackArrow =Keyboard("KeyboardLetters/SB/BackArrow.png",'BackArrow',(((x18-x17)/2)+x17),y0,win)
        Done = Keyboard("KeyboardLetters/SB/Done.png",'Done',x19,y0,win)

        letters = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,Underscore,Period,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,Apostrophe, Quotation,One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Zero,Excalmation,Dash,BackArrow, Done]
        
        name = demo(letters,win)

        Space1.undraw()
        Space2.undraw()
        Space3.undraw()
        Space4.undraw()
        Space5.undraw()
        Space6.undraw()
        Space7.undraw()
        Space8.undraw()
        Space9.undraw()
        Space10.undraw()

        Question.undraw()

        txt.undrawBackground()

        for i in letters:
                i.undraw()
        return name
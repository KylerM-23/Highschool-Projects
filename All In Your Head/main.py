from graphics import *
from gameTime import *
from dayone import *
import sys as s
import cv2
import numpy as np
import winsound as w

def main ():                
    win = GraphWin("All In your Head", 1280, 720)
    titleScreen = Image(Point(640, 360), 'background/titlescreen.png')
    titleScreen.draw(win)
    win.getMouse()
    titleScreen.undraw()
    returnvar = day1(win)
    returnvar2 = day2(returnvar)

def deathending():
    pass

def badending1():
    w.PlaySound("Music/lionsleeps.wav" , w.SND_ASYNC)
    cap = cv2.VideoCapture("Videos/badending1.mp4")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            # & 0xFF is required for a 64-bit system
            if cv2.waitKey(1/60) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    s.exit()
    

def day1(win):
    loadingscreen = Image(Point(640, 360), 'background/Loading.png')
    loadingscreen.draw(win)

    d1 = DayOne(win) 

    time = gTime(win)
    
    d1.intro()

    d1.news()
    
    d1.dream()

    time.printDateTime()

    d1.morn()
    
    time.updateTime('')
    time.printDateTime()
        
    d1.walk2skool()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.pickclass()
 
    time.updateTime(4)
    time.printDateTime()
    
    d1.lunch()
    
    time.updateTime(1)
    time.printDateTime()
    
    d1.passout()
    
    time.updateTime(0)
    time.printDateTime()
    
    d1.nurseoffice()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.docoffice()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.pillpickup()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.gangedup()

    time.updateTime('')
    time.printDateTime()
    
    d1.dreamworld()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.snapback()

    time.updateTime('')
    time.printDateTime()
   
    x = d1.dreamland()

    if x == 1:
        y = d1.dayonefight()
        if y == 1:
            badending1()

    elif x == 3:
        deathending()

    else:
        return d1


def day2(returnvar1):
    loadingscreen = Image(Point(640, 360), 'background/Loading.png')
    loadingscreen.draw(win)

    time = gTime(win)
    
    time.updateTime([6])
    time.printDateTime()

    d2.wakeup()
    
    time.updateTime('')
    time.printDateTime()
        
    d1.walk2skool()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.pickclass()
 
    time.updateTime(4)
    time.printDateTime()
    
    d1.lunch()
    
    time.updateTime(1)
    time.printDateTime()
    
    d1.passout()
    
    time.updateTime(0)
    time.printDateTime()
    
    d1.nurseoffice()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.docoffice()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.pillpickup()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.gangedup()

    time.updateTime('')
    time.printDateTime()
    
    d1.dreamworld()
    
    time.updateTime('')
    time.printDateTime()
    
    d1.snapback()

    time.updateTime('')
    time.printDateTime()
   
    x = d1.dreamland()

    if x == 1:
        y = d1.dayonefight()
        if y == 1:
            badending1()

    elif x == 3:
        deathending()


main()

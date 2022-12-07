from text import *

class gTime:
    def __init__(self, win):
        self.time = int(6)
        self.timeStamp = 'am'
        self.wday = "Wed"
        self.month = "Sep"
        self.day = int(1)
        self.ctpoint = Point(640,640)
        self.win = win
        self.gText = gameText(win)
        self.death = int(30)
        

    def changeCheck(self):
        self.checkStamp = self.timeStamp
        self.checkTime = self.time
        return self.checkStamp, self.checkTime
    
    def changeTimeStamp(self):
        if self.checkStamp == 'am':
            if self.checkTime < 12:
                return self.timeStamp

            else:
                if self.checkTime == 12:
                    self.timeStamp = 'pm'
                    return self.timeStamp 
                else:
                    self.timeStamp = 'pm'
                    return self.timeStamp 
                      
        if self.checkStamp == 'pm':
            if self.checkTime < 12:
                self.timeStamp = "pm"
                return self.timeStamp
            else:
                if self.checkTime == 12:
                    self.timeStamp = 'am'
                    return self.timeStamp 
    
    def changeTime(self,x):

        if x == '':
            w = 1
        
        elif x != '':
            w = x

        if self.checkStamp == 'am':
            if self.checkTime == 12:
                self.time = int(1) + (w-1)
                return self.time
                      
        if self.checkStamp == 'pm':
            if self.checkTime == 12:
                self.time = int(1) + (w-1)
                return self.time

        self.time = self.time + int(w)

        if type(x) == type([]):
            self.time = x[0] 
        return self.time

    def increaseDay(self):
        self.day = self.day + int(1)
        self.death = self.death - 1

        return self.day

    def changeWeekday(self):
        if self.wday == 'Mon':
            self.wday == 'Tue'
            return self.wday
        
        if self.wday == 'Tue':
            self.wday == 'Wed'
            return self.wday
        
        if self.wday == 'Wed':
            self.wday == 'Thu'
            return self.wday
        
        if self.wday == 'Thu':
            self.wday == 'Fri'
            return self.wday
        
        if self.wday == 'Fri':
            self.wday == 'Sat'
            return self.wday
        
        if self.wday == 'Sat':
            self.wday == 'Sun'
            return self.wday
        
        if self.wday == 'Sun':
            self.wday == 'Mon'
            return self.wday
    
    def updateTime(self,x):
        self.checkStamp, self.checkTime = self.changeCheck()
        self.time = self.changeTime(x)
        self.timeStamp = self.changeTimeStamp()
    
    def updateDay(self):
        self.wday = self.changeWeekday()
        self.day = self.increaseDay()
        
    def printDateTime(self):
        if (self.time >= 6 and self.timeStamp == 'am') or (self.time == 12 and self.timeStamp == 'pm') or (self.time < 6 and self.timeStamp == 'pm'):
            self.background = Image(Point(640,360),'timebackground/timebackground.png')

        elif (self.time >= 6 and self.timeStamp == 'pm') or (self.time == 12 and self.timeStamp == 'am') or (self.time < 6 and self.timeStamp == 'am'):
            self.background = Image(Point(640,360),'timebackground/darktimebackground.png')
        
        if self.time == 12:
            self.timearrow = Image(Point(640,360),'timebackground/clock/12.png')

        elif self.time == 1:
            self.timearrow = Image(Point(640,360),'timebackground/clock/1.png')

        elif self.time == 2:
            self.timearrow = Image(Point(640,360),'timebackground/clock/2.png')

        elif self.time == 3:
            self.timearrow = Image(Point(640,360),'timebackground/clock/3.png')

        elif self.time == 4:
            self.timearrow = Image(Point(640,360),'timebackground/clock/4.png')

        elif self.time == 5:
            self.timearrow = Image(Point(640,360),'timebackground/clock/5.png')

        elif self.time == 6:
            self.timearrow = Image(Point(640,360),'timebackground/clock/6.png')

        elif self.time == 7:
            self.timearrow = Image(Point(640,360),'timebackground/clock/7.png')

        elif self.time == 8:
            self.timearrow = Image(Point(640,360),'timebackground/clock/8.png')

        elif self.time == 9:
            self.timearrow = Image(Point(640,360),'timebackground/clock/9.png')

        elif self.time == 10:
            self.timearrow = Image(Point(640,360),'timebackground/clock/10.png')

        elif self.time == 11:
            self.timearrow = Image(Point(640,360),'timebackground/clock/11.png')

        if self.wday == 'Mon':
            self.datewday = Image(Point(640,360),'timebackground/date/mon.png')

        elif self.wday == 'Tue':
            self.datewday = Image(Point(640,360),'timebackground/date/tues.png')
        
        elif self.wday == 'Wed':
            self.datewday = Image(Point(640,360),'timebackground/date/wed.png')

        elif self.wday == 'Fri':
            self.datewday = Image(Point(640,360),'timebackground/date/fri.png')

        elif self.wday == 'Thu':
            self.datewday = Image(Point(640,360),'timebackground/date/thurs.png')

        elif self.wday == 'Sat':
            self.datewday = Image(Point(640,360),'timebackground/date/sat.png')

        elif self.wday == 'Sun':
            self.datewday = Image(Point(640,360),'timebackground/date/sun.png')

        if self.month == 'Jan':
            self.datemonth = Image(Point(640,360),'timebackground/date/jan.png')

        elif self.month == 'Feb':
            self.datemonth = Image(Point(640,360),'timebackground/date/feb.png')

        elif self.month == 'Mar':
            self.datemonth = Image(Point(640,360),'timebackground/date/mar.png')

        elif self.month == 'Apr':
            self.datemonth = Image(Point(640,360),'timebackground/date/april.png')

        elif self.month == 'May':
            self.datemonth = Image(Point(640,360),'timebackground/date/may.png')

        elif self.month == 'Jun':
            self.datemonth = Image(Point(640,360),'timebackground/date/june.png')

        elif self.month == 'Jul':
            self.datemonth = Image(Point(640,360),'timebackground/date/july.png')

        elif self.month == 'Aug':
            self.datemonth = Image(Point(640,360),'timebackground/date/aug.png')

        elif self.month == 'Sep':
            self.datemonth = Image(Point(640,360),'timebackground/date/sept.png')

        elif self.month == 'Oct':
            self.datemonth = Image(Point(640,360),'timebackground/date/oct.png')

        elif self.month == 'Nov':
            self.datemonth = Image(Point(640,360),'timebackground/date/nov.png')

        elif self.month == 'Dec':
            self.datemonth = Image(Point(640,360),'timebackground/date/dec.png')

        if self.day == 1:
            self.dateday = Image(Point(640,360),'timebackground/date/1.png')

        elif self.day == 2:
            self.dateday = Image(Point(640,360),'timebackground/date/2.png')

        elif self.day == 3:
            self.dateday = Image(Point(640,360),'timebackground/date/3.png')

        elif self.day == 4:
            self.dateday = Image(Point(640,360),'timebackground/date/4.png')

        elif self.day == 5:
            self.dateday = Image(Point(640,360),'timebackground/date/5.png')

        elif self.day == 6:
            self.dateday = Image(Point(640,360),'timebackground/date/6.png')

        elif self.day == 7:
            self.dateday = Image(Point(640,360),'timebackground/date/7.png')

        elif self.day == 8:
            self.dateday = Image(Point(640,360),'timebackground/date/8.png')

        elif self.day == 9:
            self.dateday = Image(Point(640,360),'timebackground/date/10.png')

        elif self.day == 10:
            self.dateday = Image(Point(640,360),'timebackground/date/10.png')

        elif self.day == 11:
            self.dateday = Image(Point(640,360),'timebackground/date/11.png')

        elif self.day == 12:
            self.dateday = Image(Point(640,360),'timebackground/date/12.png')

        elif self.day == 13:
            self.dateday = Image(Point(640,360),'timebackground/date/13.png')

        elif self.day == 14:
            self.dateday = Image(Point(640,360),'timebackground/date/14.png')

        elif self.day == 15:
            self.dateday = Image(Point(640,360),'timebackground/date/15.png')

        elif self.day == 16:
            self.dateday = Image(Point(640,360),'timebackground/date/16.png')

        elif self.day == 17:
            self.dateday = Image(Point(640,360),'timebackground/date/17.png')

        elif self.day == 18:
            self.dateday = Image(Point(640,360),'timebackground/date/18.png')

        elif self.day == 19:
            self.dateday = Image(Point(640,360),'timebackground/date/19.png')

        elif self.day == 20:
            self.dateday = Image(Point(640,360),'timebackground/date/20.png')

        elif self.day == 21:
            self.dateday = Image(Point(640,360),'timebackground/date/21.png')

        elif self.day == 22:
            self.dateday = Image(Point(640,360),'timebackground/date/22.png')

        elif self.day == 23:
            self.dateday = Image(Point(640,360),'timebackground/date/23.png')

        elif self.day == 24:
            self.dateday = Image(Point(640,360),'timebackground/date/24.png')

        elif self.day == 25:
            self.dateday = Image(Point(640,360),'timebackground/date/25.png')

        elif self.day == 26:
            self.dateday = Image(Point(640,360),'timebackground/date/26.png')

        elif self.day == 27:
            self.dateday = Image(Point(640,360),'timebackground/date/27.png')

        elif self.day == 28:
            self.dateday = Image(Point(640,360),'timebackground/date/28.png')

        elif self.day == 29:
            self.dateday = Image(Point(640,360),'timebackground/date/29.png')

        elif self.day == 30:
            self.dateday = Image(Point(640,360),'timebackground/date/30.png')       
            
        elif self.day == 31:
            self.dateday = Image(Point(640,360),'timebackground/date/31.png')

        if self.death <= 0:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/0.png')
      
        if self.death == 1:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/1.png')

        if self.death == 2:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/2.png')

        if self.death == 3:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/3.png')

        if self.death == 4:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/4.png')

        if self.death == 5:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/5.png')

        if self.death == 6:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/6.png')

        if self.death == 7:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/7.png')

        if self.death == 8:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/8.png')

        if self.death == 9:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/9.png')

        if self.death == 10:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/10.png')

        if self.death == 11:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/11.png')

        if self.death == 12:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/12.png')

        if self.death == 13:
          self.deathday = Image(Point(640,360), 'timebackground/countdown/13.png')

        if self.death == 14:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/14.png')

        if self.death == 15:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/15.png')

        if self.death == 16:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/16.png')

        if self.death == 17:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/17.png')

        if self.death == 18:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/18.png')

        if self.death == 19:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/19.png')

        if self.death == 20:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/20.png')

        if self.death == 21:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/21.png')

        if self.death == 22:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/22.png')

        if self.death == 23:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/23.png')

        if self.death == 24:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/24.png')

        if self.death == 25:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/25.png')

        if self.death == 26:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/20.png')

        if self.death == 27:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/27.png')

        if self.death == 28:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/28.png')

        if self.death == 29:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/29.png')

        if self.death == 30:
           self.deathday = Image(Point(640,360), 'timebackground/countdown/30.png')


    
        self.countdown = Image(Point(640,360), 'timebackground/countdown/countdown.png')

        self.background.draw(self.win)
        self.timearrow.draw(self.win)
        self.datewday.draw(self.win)
        self.datemonth.draw(self.win)
        self.dateday.draw(self.win)
        self.countdown.draw(self.win)
        self.deathday.draw(self.win)

        self.win.getMouse()
        
        self.timearrow.undraw()
        self.datewday.undraw()
        self.datemonth.undraw()
        self.dateday.undraw()
        self.countdown.undraw()
        self.deathday.undraw()
        self.background.undraw()
from graphics import *

class Button:
    def __init__(self, win,name, namefile, x, y):
        self.win = win
        self.name = name
        self.file = namefile
        self.x = x
        self.y = y
        self.point = Point(self.x,self.y)
        self.picture = Image(self.point,self.file)

    def draw(self):
        self.picture.draw(self.win)

    def undraw(self):
        self.picture.undraw()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getName(self):
        return self.name

    def StoreItem(self, Item):
        self.SafeItem = Item

    def getItem(self):
        return self.SafeItem
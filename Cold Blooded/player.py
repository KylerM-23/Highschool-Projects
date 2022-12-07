class Enemy: 
  def __init__(self, name, Ammo, Clip, Rate, HP, Reload, attack):
    self.name = str(name)
    self.rate = float(Rate)
    self.gun = ''
    self.hp = int(HP)
    self.clipammon = int(Clip)
    self.ammo = int(Ammo)
    self.gunreload = int(Reload)
    self.attack = attack 

  def getName(self):
    return self.name

  def lowerHP(self, amount):
    self.hp = self.hp - amount
  
  def getHP(self):
    return self.hp
  
  def getattack(self):
    return self.attack
  
  def getclipammo(self):
      return int(self.clipammon)

  def getammo(self):
    return self.ammo
  
  def getrate(self):
    return self.rate

  def getgunreload(self):
    return self.gunreload
    
class Player: 
  def __init__(self):
    self.name = ''
    self.hp = int(100)
    self.maxhp = int(100)
    self.money = float(20)

    self.exp = float(0)
    self.level = int(0)
    self.levelup = int(200)
    
    self.gunname = ''
    self.rate = int(0)
    self.clipammo = int(0)
    self.ammo = int(0) 
    self.attack = int(0)
    self.gtype = ''

  def setgtype(self, gun):
    self.gtype = gun
  
  def getgtype(self):
    return self.gtype

  def increaseammo(self,n):
    self.ammo = self.ammo + n

  def setHP(self):
    self.hp = self.maxhp
    
  def lowerMoney(self, num):
    self.money = self.money - num
  
  def getMoney(self):
    return self.money

  def increasemoney(self, num):
    self.money = self.money + num
    
  def lowerHP(self, amount):
    self.hp = self.hp - amount

  def getattack(self):
    return self.attack
  
  def setattack(self, attack):
    self.attack = attack

  def setName(self):
    self.name = str(input("What is your name Soldier?"))

  def levelupam(self):
    self.level = self.level + 1
    self.exp = self.exp - self.levelup
    self.maxhp = int(self.maxhp * 1.2)
    self.levelup = self.levelup * 1.05
    print("You have leveled up to level ", self.level)
  
  def upexp(self, num):
    self.exp = self.exp + num
    
  def checkiflevelup(self):
    check = int(self.exp/self.levelup)
    if check >= 1:
      self.levelupam()
    else:
      print("You need ", int(self.levelup - self.exp), " exp in order to level up.")

  def getName(self):
    return self.name

  def getHP(self):
    return self.hp
  
  def setclipammo(self, ammo):
    self.clipammo = ammo
  
  def getclipammo(self):
    return self.clipammo

  def getammo(self):
    return self.ammo

  def lowerAmmo(self, num):
    self.ammo = self.ammo - num
    
  def setammo(self, ammo):
    self.ammo = ammo

  def setrate(self, rate):
    self.rate = rate

  def getrate(self):
    return self.rate

  def setgunreload(self,x):
    self.gunreload = x
  
  def getgunreload(self):
    return self.gunreload
  
  def setgunname(self, N):
    self.gunname = N
  
  def getgunname(self):
    return self.gunname
     
  def gunchange(self, N,R, AT, GR, A, C, T):
    self.setgunname(N)
    self.setrate(R)
    self.setattack(AT)
    self.setgunreload(GR)
    self.setammo(A)
    self.setclipammo(C)
    self.setgtype(T) 

  def safety(self, N,R,AT, GR, A, C, T):
    self.safegunname = (N)
    self.saferate = (R)
    self.safeattack = (AT)
    self.safegunreload = GR
    self.safeammo = A
    self.safeclipammo = C
    self.safesgtype = T 

  def switch(self, N,R,AT, GR, A, C, T):
    temp1 = N
    temp2 = R
    temp3 = AT
    temp4 = GR
    temp5 = A
    temp6 = C
    temp7 = T

    self.gunchange(self.safegunname ,self.saferate, self.safeattack, self.safegunreload, self.safeammo, self.safeclipammo, self.safesgtype)

    self.safety(temp1,temp2,temp3,temp4,temp5,temp6,temp7)

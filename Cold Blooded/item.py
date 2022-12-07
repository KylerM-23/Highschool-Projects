class Item():
    def __init__(self, name, price, ammo, clip, gtype, attack, rate, rload):
        self.name = name
        self.price = price
        self.ammo = ammo
        self.clip = clip
        self.gtype = gtype
        self.attack = attack
        self.rate = rate
        self.rload = rload 

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getAmmo(self):
        return self.ammo

    def getClip(self):
        return self.clip

    def getType(self):
        return self.gtype

    def getRate(self):
        return self.rate

    def getAttack(self):
        return self.attack

    def getrload(self):
      return self.rload

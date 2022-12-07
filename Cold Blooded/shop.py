import item as i

class Shop():
    def __init__(self,item1,item2, shopname):
        self.item1 = item1
        self.item2 = item2

        self.item1N = item1.getName()
        self.item2N = item2.getName()
        self.item3N = 'Ammo'
        
        self.item1P = item1.getPrice()
        self.item2P = item2.getPrice()
        

        self.item1T = item1.getType()
        self.item2T = item2.getType()

        self.item1A = item1.getAmmo()
        self.item2A = item2.getAmmo()

        self.item1C = item1.getClip()
        self.item2C = item2.getClip()

        self.item1AT = item1.getAttack()
        self.item2AT = item2.getAttack()

        self.item1R = item1.getRate()
        self.item2R = item2.getRate()

        self.item1Re = item1.getrload()
        self.item2Re = item2.getrload()

        self.shopname = shopname

    def openShop(self, player):
        self.item3P = 3 *int(player.getclipammo())
        print('Welcome to', self.shopname,'.')
        print('This is what we have for sale today.')
        
        print(self.item1N, 'a ', self.item1T, ' with a clip size of', self.item1C, ' and a total ammo of', self.item1A)
        print('with a damage output of', self.item1AT, ' with an accuracy of', self.item1R, 'at the price of', self.item1P)
        
        print(self.item2N, 'a ', self.item2T, ' with a clip size of', self.item2C, ' and a total ammo of', self.item2A)
        print('with a damage output of', self.item2AT, ' with an accuracy of', self.item2R, 'at the price of', self.item2P)
        
        print("Fill up your ammo")

        print('On the form he gave us we can either write the number "1" for item 1, "2" for item 2, and "3" for item "3".')
        print('Or we can return by telling the shop keeper "No Thank You"')
        
        while(1==1):
            choice = input('Which item would you like to purchse?')
            
            if choice == '1':
                if (player.getMoney() >= self.item1P):
                    player.lowerMoney(self.item1P)
                    player.gunchange(self.item1N, self.item1R, self.item1AT, self.item1Re, self.item1A, self.item1C, self.item1T)

                else:
                    print('Sorry you don\'t have enough money')
                    break
            
            elif choice == '2':
                if (player.getMoney() >= self.item2P):
                    player.lowerMoney(self.item2P)
                    player.gunchange(self.item2N, self.item2R, self.item2AT, self.item2Re, self.item2A, self.item2C, self.item2T)

                else:
                    print('Sorry you don\'t have enough money')
                    break

            elif choice == '3':
                if (player.getMoney() >= self.item3P):
                    player.lowerMoney(self.item3P)
                    player.increaseammo(2*int(player.getclipammo()))
                else:
                    print('Sorry you don\'t have enough money')
                    break
            
            else:
              break
        
        print("Thank you for visiting ", self.shopname)
        return
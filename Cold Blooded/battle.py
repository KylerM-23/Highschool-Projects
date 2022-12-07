import random

def checkHP(player,enemy):
  player = player
  enemy = enemy
  if player.getHP()<=0:
    battle = 'Lose'
    return battle

  elif enemy.getHP()<=0:
    battle = 'Win'
    player.checkiflevelup()
    return battle
  
  else:
    battle = 'Active'
    return battle

def playerfight(player,enemy):
  player = player
  enemy = enemy
  
  if player.getammo() > 0:
    print("You have", int(player.getammo()), "ammo.")
    print(enemy.getName(), 'is at ', enemy.getHP(), 'health.')
    print(player.getName(), 'is at', player.getHP(), 'health.')
    
    for n in range(player.getclipammo()):
      player.lowerAmmo(int(1))
      input('Press Enter To Fire')
      shot = random.randint(0,100)
      if float(player.getrate()) > shot and  shot > 0:
        enemy.lowerHP(player.getattack())  
    
    for i in range(int(player.getgunreload())):
      while(1==1):
        choice = input('Type RELOAD')
        if choice.lower() == 'reload':
          break
        print('That\'s not how you reload your weapon')

def enemyfight(enemy, player):
  enemy = enemy
  player = player
  for n in range(enemy.getclipammo()):
      shot = random.randint(0,100)
      if float(enemy.getrate()) > shot and  shot > 0:
        player.lowerHP(enemy.getattack())

def battle(battle, enemy, player):
  battle = battle
  enemy = enemy
  player = player

  player.setHP()

  x = enemy.getHP()

  player.increasemoney(random.randint((x/2),((x/2) + 20) ))

  num = random.randint(x, (x+20))
  player.upexp(int(1.5*num))

  while (battle == 'Active'):
    playerfight(player,enemy)
    enemyfight(enemy,player)
    battle = checkHP(player,enemy)
  return battle

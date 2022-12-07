import player as p
import story as s
import battle as b

def game():
  player = p.Player()
  s.Opening()
  player.setName()
  PlayerName = player.getName()
  s.text(PlayerName + " get yourself out of here we are all going to die!",2)

  s.Act1()
  
  enemy = p.Enemy('Nazi Soldier',10,7,30,100, 1, 10)
  player.gunchange('Colt 1911', 60, 15, 2, 100, 8, 'Pistol')
  
  battle = b.battle('Active', enemy, player)
  
  if battle == 'Lose':
    return 'GG'
  
  
  decison = s.Act2(PlayerName)

  choice = s.Act3AA(PlayerName, player)

  if choice == 'GG':
    return choice
    
  choice1 = s.Act4AA(PlayerName, player)
    
  if choice1 == 'GG':
    return choice1

def main():
  game()
  

main()
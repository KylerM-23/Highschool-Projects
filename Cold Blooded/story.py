import random
import time
import player as p
import battle as b
import item as i
import shop as s

def text(text, num):
  print(text)
  time.sleep(num)
  #input()
  print('')
  #Copyright Kyler 2018 Rights Reserved

def moveuptext(slep, num):
  for n in range (num):
    print("")
    time.sleep(slep)

def credits():
  print("Coder & Writer")
  print("Kyler Martinez")

  while(1==1):
    x = input()
    x = x.lower()

    if x == "hi":
      print("Hi how ya doing?")
    if x == "heaven":
      print("I guess Heaven is a place on this planet.")
      print("Sadly this isn't heaven.")

def gameOver():
  print("Game Over")
  while(True):
    x = input()
    if x == 'Hell':
      print("Yes, this is where you are, enjoy.")

def Opening():
  text("You awake inside a bunker and hear artillery shells falling among you.",3)
  text("A figure walks up to you, grabing for your hand and asks",2.5)

def Act1():
  text("You run out of a half destroyed barrack and immediately the scene is horrid.\nBombs blowing the Nazis to pieces,the sound of shells and gun fire surrounds.\nThen out of nowhere the opponent appears in front of you and a set of weapons stand between you.\nYou impatiently run for the pistol and your opponent is on the brink of reloading his gun.\nTHE FIGHT HAS BEGUN!",12)

def Act2(PlayerName):
  text("You've completed your first kill. Shocked you seek your leader. Sergeant Collin asks you what branch you belong to. Airforce or United States Army?",4)
  text("You say the Army, even though you aren't sure exactly",6)
  
  return



def Act3AA(PlayerName, player):
  player = player 
  text("Sergeant: Well soldier looks like you are in the perfect spot. Now get on out of here I will put you in Bravo Company, they just lost three men and could use some reinforcements. I would normally check your identification but I couldn’t care less. You are obviously an American I see it in your face and how you talk and you seem willing enough to go and kill any tyrannical Nazi and send him to the pits of Hell. Now get out their soldier.",10)

  text("After going to the barracks of Bravo Company, you meet the three men you will have to call your brothers for the foreseeable future.",4)
  
  text("???: Looks like we got ourselves fresh, or I guess meat that will die with us.",4)
  
  text("???: Shut up Night. I don’t feel like we need to be scaring the damned kid.",4)
  
  text("Night: Don’t tell me what I need to do Light boy.",2)
  
  text("Light: Now that just sounds racist.",2)
  
  text("???: Hey kid, ignore those two. They like to fight they are cousins and they were lucky enough to end up with me. The other guys here wanted to name them Night and Day, but Light didn’t like the name Day so he called himself Light. I’m Moon to these fools, but in private you can call me Dave.",7)
  
  text("Moon: For some reason, the original company was keen on codenames and it became a tradition for the idiots that come and go. I am sadly the only one to survive out of both the first, second, and third full iterations of the company. Give them a couple of seconds and they’ll spring to give you a name and then we’ll discuss where we will go from here.",7)
  
  text(PlayerName + ": Thanks, Moon.",1)
  
  text("Light & Night: We are Night and Light and the old man is Moon. We need to get you a name it has been a tradition. We will call you Apollo, we don’t need your actual name, it personally doesn't matter out here.",5)

  text("Night: Yeah you are more than likely will be gone in a couple of days and we will retire the name and never use it again until we are gone.",5)

  text("Light: Moon will be a cool name one day.",1)

  text("Moon: Who says any of you will get it?",1)

  text("Night: Don’t kid yourself, you will die of cardiac arrest before you get shot in combat." , 3.5)

  text("Moon: Don’t give me that I at least have 25 years of life left in me.", 3.5)

  text("Light: I’ll believe that when I see that.", 2.5)

  text("Night: Well Apollo, you better get used to us; we are leaving for the Rhineland tomorrow morning. I don’t know how well you like it here, but it is going to get a lot worse. So what happened to you, you sure look like you went through hell." , 8.5)

  text("You loosely explain to the men what had happened to you that past day." , 2.5)

  text("Light: So you don’t remember exactly how you got here. You just vaguely remember airplanes and tanks.", 3.5) 

  text("Night: Well, at least you think you remember your name and I guess something told you that you belonged in the Army, but I personally think you would fair off in the Air Force. However, I don’t think it matters if you are slaughtering Japs and Nazis, they both deserve to die, and will." , 8.5) 

  text("Light: I bet you didn't expect to fight the Germans again Moon. The Japanese and Italians must have been a surprise as well." ,3)

  text("Moon: I am not that old. I wasn’t born soon enough to be drafted into the Great War. My father was. I could have enlisted in the war, but someone needed to look after my Momma.", 7)

  text("Light: Whatever... We better make it to the castle before the Soviets.", 3.5)

  text("Night: Why we are on the same side; they’re our allies for the war and if they get to him first we still win the war.", 8)

  text("Light: I don’t know about them Soviets, they just seem off to me. We are only allies to them just because Hitler thought it would be a wise move to try and conquer the whole world at the same time.", 7)

  text("Night: I think it’s fine; you didn’t see the Soviets storming the beaches of Normandy.",  3)

  text("Light: Trust me the Soviets will be remembered more because they actually got to Hitler whereas we will only be remembered in history books and then be overshadowed.", 5)

  text("Night: Whatever you think is right then believe it. I don’t personally care anymore. How do you think the war is going in the Pacific Apollo?", 4)

  choice = input("What are you going to respond with? 1. I think we are going to just bomb them until they give up. 2. We aren’t going to win that easily, their defenses are extremely strong and don’t seem like the people to give up. 3. I personally don’t know, we may lose if we struggle here.")

  if choice == '1':
    text("Light: Well that’s oddly specific. I guess that could work when we get closer to the island but we’ll have to wait and see.", 3)

  elif choice == '2':
    text("Moon: Yeah I noticed that as well. Hopefully, MacArthur can pull his weight over there. It may take a while though.", 2.5)

  elif choice == '3':
    text("Night: Don’t go talking like that you act like we are going to fail over here. You better not go and make that happen. If you want us to fail then I think you know what you should do then.",5)

  else:
    text("No one understood what you said.",1)

  text("Light: You better head off to bed soon Apollo, it is going to get late soon and no sleep is going to prepare you for going out there again.",3.5)

  text("Night: You act like he hasn’t been in the war already.",1)

  text("Light: Just go to bed everyone.",1)
  Act4AA(PlayerName, player)

def Act5AA(PlayerName, player):
  player = player
  text("You arrive at the location and as you open the door, you find a French resistance soldier hiding in the corner and inform him that you are a friendly.", 4)
  
  text("French Soldier: Oh an American. It was hell. The phantoms destroyed our forces and I have been hiding in here for a while.", 4)
  
  text(PlayerName +": What ghosts are you talking about?",2)

  text("French Soldier: The panzers…",1)

  text(PlayerName + ": I’m sorry I don’t know what youre talking about but we can take you out of here to safety.", 4)

  text("French Soldier: There’s another…",2)

  text(PlayerName + ": What?",1)

  text("The soldier passses out and you clear out the surrounding five rooms and proceed to take the soldier out of the bunker and back to the vehicules. As you are doing this, Light encounters something strange.",6)

  text("Light: Hopefully this damn bunker is empty so we can continue on and get this war over with.",3)

  text("You hear a noise towards the right of you.", 2)

  text("Light: This is Bravo Company of the American forces. I will not shoot just come out with your hands up.", 4)

  text("???: You are justin going to shoot me and take whatever I have left on me. You don’t care about me you just want to kill me. No one will take my life from me. You better walk out of here before I have to put a bullet in your head.", 7)

  text("Light: Calm down I just want to tell you two things. First, I can’t leave until I confirm that this place is abandoned and I can’t do that with you in here. I can take you back to base and I will ensure that no harm will come to you. Second, I will drop my gun if you agree to put down your weapon and talk to me. So is it a deal, I really don’t want to hurt you or get hurt.", 9)

  text("???: I told you…", 1)

  text("*Blam Blam*",1)

  text("???: The weaklings die in this world. He wouldn’t listen to me, he could have lived.", 2)

  text("You hear two gunshots in the distance.",2)

  text(PlayerName + ": What the hell was that?", 1)

  text("French Soldier: The other one…he’s one hell of a shot.", 2)

  text(PlayerName + ": I am going to leave you here and check it out.", 2)

  text("French Soldier: Don’t die.", 1)

  text("You run into the bunker and hear a voice…",2)

  text("???: Should’ve known that there would be another close by.", 2)

  text("Light’s corpse is laying on the ground with his weapon unloaded and placed on the ground. His head has a clean hole in his forehead. He was dead a while ago and there weren’t any ways to save him. You hear footsteps behind you are arm your weapon and turn around with finger on trigger.", 7)

  text(PlayerName + ": It is too late to leave here alive. You will either come out and surrender or make me fight you. Either way, you will have a couple of bullets in you.", 7)
  
  enemy = p.Enemy('Crazy Dude',20,7,30,110, 1, 10)
  
  battle = b.battle('Active', enemy, player)
        
  if battle == 'Lose':
    gameOver()

  text("Moon: What is going on here? I cleared out my sector already. Where is Light…",3)

  text("Night: Where is he? Holy… Teddy. What did they do to you?",2)

  text(PlayerName+": The bastard killed him.",2)

  text("Night: Thank you for taking care of this sorry excuse for a human, but I will be taking my brother’s body back home. I am the last of kin for my family and I will be returning. Thank you for all you have done.", 6)

  text(PlayerName +" & Moon: Your welcome.", 2)

  text("French Soldier: I am sorry for what this man has caused you. I knew he was here btu I was too weak to tell you about it.", 4)

  text("Night: You just had to conveniently be fine after my brother was killed.", 3)

  text("French Soldier: Look I am sorry. I am still weak right now and wish that i had been able to solve this problem. I am Andre and was stranded here with that monster.", 5)

  text("Andre: He left me alone if I stayed on that side of the bunker and I listened to him. I haven’t had food for a week and water for a couple of days.", 6)

  text("Night: I will pass on my name to you Andre.", 3)

  text("Andre: Umm…",1)

  text(PlayerName+": I will explain it later.", 2)

  text("Night: I don’t know what darkness is in French but I know that black is Noir so you are Noir now.",3)

  text("Andre: Sure that is umm… a good name.", 3)

  text("Night: I will go and wait in the trucks to be transported back to base.", 3)

  text(PlayerName+": Goodbye Night, stay safe out there.", 3)

  text("Night: I should be telling you guys that. My brother was the only one that could light up my day out here. He kept me stable out here. Now all that is left is the darkness. Goodluck I don’t foresee much good coming out of your lives.", 7)

  text("Moon: Thank you.", 2)

  text(PlayerName+": Night I don’t want to cause you any more pain but can I talk to you for moment?", 3)

  text("Night: Sure",1)

  text("What are you going to ask him?",1)
  Check1 = 0
  Check2 = 0

  while(1==1):
    Choice  = input("1. Why did you lie about Ted being your cousin? 2. What will happen to you and your brother now? 3. I’m sorry for your loss.")
    if Choice == '1' :
      if Check1 == 'done':
        text('I already said that.')
    
      else:
        text("Night: Look we have come from a long line of soldiers and we weren’t going to allow just one of us going on out there. I was hoping that while here I could keep an eye on him and make sure that he was safe, but I guess I was wrong. My mother said not to do this because she just knew harm would result from this and I had been keeping safe for the past year and I personally didn’t think we would have survived the invasion but we made it this far.",10)
      
        Check1 = 'done'
    
    if Choice == '2' :
      if Check2 == 'done':
        text('I already said that.', 2)
      
      else:
        text("Night: We will probably stay at the base for the time being and wait for some sort of transportation back home. There I will be discharged and my brother declared a hero who gave his life up to protect me. We will then have a funeral and hopefully be able to put this past us.", 8)
        Check2 = 'done'
    
    else:
      text(PlayerName+": I’m sure he is in a better place now, but you probably should return home to your family. They will probably need you now more than ever. We will continue the fight.", 6)
      
      text("Night: My name was Tom.", 2)
      
      text("Tom: I’m no longer Night to you guys, that battle name is now gone. I pray you make it out of here alive.", 4)
      
      text(PlayerName+": Likewise...Likewise...", 2)
      
      break
 

  text("The truck took Night and Light back to base where you may never see them again. You sit next to Andre and talk to him about your current situation.", 5)

  text(PlayerName+": Look Andre I understand that you are probably still weak but if you are going to stay with us then you better get fired up. There is only more hell to go through from here on.", 5)

  text("Andre: Yeah, you haven’t even seen the worst that’s out there.", 3)

  text(PlayerName+": I know…", 1)

  text("Andre: What is whole thing with these names? I know I’m black and you are Apollo and the older man is Moon.", 4)

  text(PlayerName+": Moon said that the people of the Companies did this as a tradition, you were given Noir, I know it’s black in French but it may not be best for you going around saying you are Black.", 7)

  text("Noir: The Frenchmen will think I’m crazy but whatever, it’s that soldier’s wish.", 3)

  text("Moon: I have been informed that a tanks are going to be coming our way that need reinforcements.", 3)

  text("Noir: When will they be here?", 2)

  text("Moon: in the morning, we’ll have to stay here for the night.", 2)

  text("You try to sleep in the bunker but all you can smell is the death and blood that covers this place. All you can think about in your dreams is the man that killed Light and his dead body next to Light. Artillery shells and tanks begin to roll in beside you and the sky turns blood red as snow falls among you. You wake up and hear the tanks that are here for you.", 12)

  text("Tank Driver: Bravo Company please exit and hurry on over.", 3)

  text("You go outside to see Noir and Moon waiting for you.", 3)

  text("Tank Driver: I need someone with an immense experience in a Hellcat.", 3)

  text("Noir: I don’t know what tank that exactly is but I am a tank technician and have experience in most tanks.", 4)

  text("Tank Driver: Well you are probably best with us. Welcome to the tank destroyer, let’s go.", 4)

  text("Noir: Stay safe men.",1)

  text("You watch Noir leave with the tank and you see another down the road approaching. The tank arrives and you can hear the behemoth of the Sherman. The tank driver exits the tank and begins to talk to you", 5)

  text("Tank Driver: I need three men for my crew.", 3)

  text("Moon: I’m sorry but there are only two of us left.", 3)

  text("Tank Driver: I was told that there were four members of Bravo Company and one was supposed to go elsewhere.", 3)

  text(PlayerName+": We had a K.I.A.", 1)

  text("Tank Driver: I see, I see. Well we are going to have to make due with just us. We must hurry on with just ourselves. Winter is fast approaching and we don’t want to get left out in the snow.", 5)

  text("You leave with Moon and embark for a couple of days and end up in a field by some woods.", 2.5)

  text("Tank Driver: Men get out.", 1)

  text("Everyone exits the tank and await orders from the Tank Driver.", 2)

  text("Tank Driver: We are going to have to stop here. Someone malfunctioned with the navigation controls and it would be unwise to continue this way. I want you guys to go and scout the surrounding area for any signs of danger. I’ll stay here and repair the systems. They really make these Sherman's seem like they are god-like, but they are too damn weak and fragile to actively compete.", 15)

  text("You paired up with Moon and choose the south side of the woods to investigate.", 2)

  text("Moon: What could even be out in these woods, I don’t expect any animals nor Nazis coming out against us out here.", 3)

  text(PlayerName+": Maybe a Panzer.",2 )

  text("Moon: There wouldn’t be a Panzer out here…", 2.5)

  text(PlayerName+": I shouldn’t have spoken.", 2)

  text("You hear shouting from the distance that is in German, but don’t know where it is exactly from. You walk a few places forward and discover a King Tiger.", 5)

  text("Moon: Want to try and hijack a King Tiger?", 2)

  text(PlayerName+": How are we going to do that?", 2)

  text("Moon: Simple we will open the top hatch and shoot whoever is in there or we can use the gas grenade I have to drive whoever is in there out.", 7)

  text(PlayerName+": Where did you get that? We were never given those.", 3)

  text("Moon: Found it", 1)

  text(PlayerName+": Fair enough, throw it in.", 2)

  text("Moon: Come here and help me open the hatch so I can throw in the grenade.", 3)

  for n in range(15):
    input("Press Enter")

  text("Moon: Incoming!", 1)

  text("Two Nazi soldiers start running toward your position screaming at you.", 3)

  text("Moon: I got one of them, you take on the other.", 2)

  text(PlayerName+": All Right", 1)

  enemy = p.Enemy('Naiz Soldier', 15,8,40,120, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text(PlayerName+": How long until the tank will be aired out?", 2)

  text("Moon: I am not sure. Let’s open the hatch again and see if they are dead.", 3)

  text("You open the hatch to see no one inside the tank.", 2)

  text("Moon: We are going to have to wait for about thirty minutes before we can go inside.", 4)

  text(PlayerName+": Then what was the point in throwing the gas grenade.", 4)

  text("Moon: It would have saved us from having to waste more ammo on them and I do hate having to pull the trigger sometimes. Plus we could have damaged the interior.", 8)

  text(PlayerName+": I’ll head back to the driver and tell him of our find.", 4)

  text("You return to the driver and inform him of the tank you and Moon seized.", 4)

  text("Tank Driver: That’s great but how will we identify you as a friendly.", 4)

  text(PlayerName+": I could paint a flag or something.", 2)

  text("Tank Driver: Take the flag off of our tank and throw it on the tiger. There are no guarantees though. When we meet up with someone who has paint then we’ll change it but for now be weary. You could be useful. We also go toward that you have another person join our crew. He’ll be here by night.", 10)

  text(PlayerName+": So what are we going to do in the meantime?", 3)

  text("Tank Driver: Well I will wait for the others to return and then we will head to the randevu.", 5)

  text(PlayerName+": I will now return to the captured tank.", 3)

  text("You return to Moon and inform him of your situation.", 3)

  text("Moon: Well the tank has aired out. Let’s get into the mother umm… King of the Jungle.", 4)

  text(PlayerName+": The Lion is supposed to be the king but let’s roll with it.", 4)

  text("You guys get into the tank and then start to plow through the wood.", 4)

  player.safety(player.getgunname(), player.getrate(),player.getattack(), player.getgunreload(), player.getammo(), player.getclipammo(), player.getgtype())
  player.gunchange('King Tiger', 75, 40, 5, 36, 9, 'Heavy Tank')
  
  text(PlayerName +": This bastard sure isn’t good in rough terrain.", 2)

  text("Moon: And this thing is called the King of the Jungle. The Jungle would tear this apart in minutes.", 5)

  text(PlayerName +": If the thing wasn’t so slow we would have returned already. Look up ahead we are almost there.", 4)

  text("You arrive to the tank and the other soldier returns thinking you are under.", 3)

  text("Soldier: I knew I should have waited to drafted…", 2)

  text("Tank Driver: Shut up. The other two men went and captured a King Tiger.", 4)

  text("Soldier: Oh…", 1)

  text("The two of you exit the tank and speak the driver.", 2.5)

  text("Moon: Where’s the flag so we can be identified?", 3)

  text("Tank Driver: Here you go. I also informed over the radio that we had a King Tiger that would head into battle. So as far as we know you are safe. However, you need to complete you crew. So we are going to go in the tiger with you guys. This Sherman is dead, I disabled the combat functionality so it’s safe to leave it out here. We need to leave now so that we could meet up with our new addition.", 10)

  text("Tank Driver: we got company, everyone get in!", 2.5)
  enemy = p.Enemy('King Tiger', 70 ,40,5, 100, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("You ride for a couple of hours and find a makeshift camp. Snow begins to fall slowly.", 3)

  player.switch(player.getgunname(), player.getrate(),player.getattack(), player.getgunreload(), player.getammo(), player.getclipammo(), player.getgtype())

  text("Tank Driver: You go and do whatever you need here but I need you to then go and bring the soldier.", 3)

  text("What are you going to do?",1)

  while(1==1):
    Choice  = input("1. Go to the armory. 2. Go and see the soldier.")
    if Choice == '1' :
      text("Store Manager: I got some of the things you may want here. Just buy something and leave it’s getting cold out here.", 4)
      
      item1 = i.Item("M1 Garand", 40, 48, 4, "Semi-Automatic Rifle", 20, 70, 1)

      item2 = i.Item("Remington Model 31", 40,10, 2, "Pump Action Shogun" , random.randint(80,100), random.randint(30,80), 3)

      shop1 = s.Shop(item1, item2, "Fat Man Weapons")
      shop1.openShop(player)


    else:
      text("You went to see the soldier and see Night of all people sitting on a bed.", 2)
      
      text("Night: How in this Hell did I end up meeting you again?", 2)
      
      text(PlayerName +": What happened, I thought you were going back home?", 3.5)
      
      text("Night: I explained what we did and they gave me two choices, either send my brother back home as a war criminal and have myself go into a military trial for fraud or go back into the battlefield and both return as war heros. I wasn’t going to allow my family name to go down as criminals. I would rather die out here as a hero then return home as a villain. What happened to you, I was told that I was joining Delta Company? I never thought it’d see Bravo Company this quick, or someone from it I mean.", 12)

      text(PlayerName +": We got absorbed and sectioned off, Noir went off with someone else, but Moon is still with me.", 5)

      text("Night: Well let’s get out of here and join him.", 2)
      break

  text("The two of you leave and go and see Moon and Night explains how he ended up in his predicament.", 4)

  text("Moon: We need to hurry on and cover more ground, the Nazis are going on the defensive at the Ardennes. Something feels off though.", 4)

  text("How will you respond?", 1)
  
  while (1==1):
    choice = input("1. Yeah I feel the same way too. 2.Why wouldn’t they be on the defensive?")
    
    if choice == '1':
      text("Night: I don’t know they do seem to be cornered it would make sense for them to try and repel any attacks from us.", 4)
      text("Moon: Trust me it'd take a lot more force from us tom make Hitler feel 'cornered.'", 3)
      break

    elif choice == '2':
      text("Night: I agree with you, it only makes sense.", 3)
      text("Moon: It could be a part of their strategy; they aren’t idiots", 3)
      break

    else:
      text("Night: I didn't understand what you said.", 2)

      text("Moon: Kid you sure you are fine? Are you nervous or something?", 3)
      break
  text("Moon: Well we need to head out about now.", 2)

  text("Night: Whatever happened to that Noir guy?", 2) 

  text(PlayerName +": He went with another tank, he’s manning a Hellcat.", 3)

  text("Night: That’s interesting, didn’t expect that to him.", 2.5)

  text("You trek onward for a few weeks until it’s Thanksgiving.", 2)

  text("Night: I would have loved to be back home eating a turkey with my family.", 3)  

  text("Moon: You still miss that?", 2)

  text("Night: It’s a great holiday. It’s not as easy to celebrate it out here than back home, unless you can find me a turkey to cook.", 3)

  text("Tank Driver: Shut up already. If we make it out of here than you can be a fat ass as much as you want and have all the turkey you could want.", 4)

  text("Night: Fine I’ll shut up for now. Just wait for it to be Christmas.", 3)

  text("Moon: This tank isn’t the best in this snowy environment, you can never tell if you are going to run over something, someone, or tip over.", 5)

  text("Night: It was one time.", 2)

  text("Moon: Sure it was only one time.", 2)

  text("Night: How was I supposed to know that that snow heap was also a tank?", 3)

  text("Moon: Now how did you not noticed the tank that was next to it?",3)

  text("Night: That doesn’t count as two.", 1.5)

  text(PlayerName + ": It wasn’t fun to move this bastard.", 2)

  text("Tank Driver: You set us back a day.", 2)

  text("Soldier: I hate to interrupt you but there is a Panzer in the distance.", 3)

  text("Tank Driver: Well looks like we’ll have to deal with him.", 3)

  text("Night: We never gave you a name Tank Driver. We have always been calling you Tank Driver.", 5)

  text("Tank Driver: Shut up we have more important businesses to attend to.", 3)

  text("Night: Ok Chief.", 1)

  text("Chief: You went and done it.", 2)

  text("Night: Yes Chief, let’s go and take this swine out Chief.", 2)

  text("Chief: I hate you people…", 2)
  player.switch(player.getgunname(), player.getrate(),player.getattack(), player.getgunreload(), player.getammo(), player.getclipammo(), player.getgtype())

  enemy = p.Enemy('Panzer', 75 ,45,10, 120, 7, 20)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("Night: Now I think we are fine for some turkey.", 2)

  text("Everyone Else: Shut up about that turkey.", 2)

  text("Night: …", 1)

  text("You travel for a few months and arrive at the Ardennes forest.", 1.5)

  text("Chief: We are here boys.", 1.5)

  text("Night: Well what the hell are we waiting for.", 2)

  text("Everyone exits the vehicle and speak to an officer.", 2.5)
  
  text("Officer: State your company and business here.", 2.5)

  text("Chief: Delta Company and we are here for the same reason as everyone else around here.", 4)

  text("Officer: Why are you a week late and why are you in a Tiger?", 3)

  text("Chief: We captured the tank and broke the tank and fixed it.", 4)

  text("Officer: Well… we’ll just ignore that. Gte out there we may be seeing action soon. We are planning an assault on the Na…", 6)

  text("Artillery begins to fall among you with the foggy snowy terrain.", 3)

  text("Officer: We are under attack! Everyone prepare for battle.", 3)

  text("Night: Come out Apollo show us your rays of sunshine.", 2.5)

  text("Noir: You bastards are here too?", 2)

  text("Night: I was really hoping I didn't see you again.", 2)

  text("Noir: Nice to see you too.", 1.5)

  text("Night: We have basically the same name.", 2)

  text("Noir: No we don’t.", 1)

  text(PlayerName + ": you guys can bicker later, we need to at least survive this you idiots.", 4)

  text("Noir: Fine... This isn't over yet.", 3)

  player.switch(player.getgunname(), player.getrate(),player.getattack(), player.getgunreload(), player.getammo(), player.getclipammo(), player.getgtype())

  text("You head off into the forest with Noir",2)

  text("Noir: I will go to the left of this tree, you go to the right. Try and clear out any soldiers that you see.", 4)

  text("You see one man charging at you and doesn't seem eager to die...", 3)
  
  enemy = p.Enemy('Naiz Soldier', 15,8,40,120, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()
  
  text("Noir: Nice one, I'm going west of our location now.", 2)

  text(PlayerName +": Don’t die out there.", 3)

  text("Noir: Sur-", 1)

  text("Noir is obliterated by an artillery shell, you become covered in his blood and are on the ground dazed. You hear Night yelling out at you.", 5)

  text("Night: Get your ass up, I’m not losing another brother out here. ", 2)

  text(PlayerName+": Thanks", 1)

  text("Night: We are surrounded.", 1.5)

  text(PlayerName+": What do you mean ? I don’t see anyone.", 3)

  text("Night: We surrender.", 2.5)

  text("Night throws away his gun and you do the same.", 3)
  
  player.gunchange('0',0, 0, 0,0, 0, '0')
  
  text("Naiz Soldier: On knees. No talk. No kill.", 3)

  text("You are taken off to a Nazi camp where you are grouped with other American soldiers and are forced to freeze in the snow for a few weeks. Then a miracle occurs.", 6)

  text("Nazi Soldier: Prisoners Free. Only some.", 3)

  text("He begins to point to random soldiers and as they leave a Nazi soldier is returned to the camp. He points at you and tells you to leave. You are returned to the American camp and you must buy yourself a new weapon.", 7)

  text("American Captain: You better get yourself a gun and get out there, I’m not sure if you could purchase a weapon, but if you can’t then you will be granted a weapon.", 7)

  while(1==1):
    Choice  = input("1. Go to the armory. 2. Take whatever’s left.")
    if Choice == '1' :
      text("Store Manager: It sure is hell out there. I got a gun that will fit all gangsters and moonshiners. We also secured a few MP44s that we scavenged off of Nazi prisoners. It’ll be at a hefty price though.", 6)
      
      item4 = i.Item("Thompson Submachine Gun", 60, 90, 30, "Submachine Gun" , 20,40, 4)
      item3 = i.Item("MP44",100 , 90, 30, "Selective-Fire Rifle",30,70, 3)

      shop1 = s.Shop(item4, item3, "Bulgey Guns")

      shop1.openShop(player)
      break


    else:
      player.gunchange('M1 Carbine', 30, 50, 3,90, 15, 'Carbine Rifle')
      break

  text("Captain: Now get out there. The Nazis are only going to continue to kill.", 2.5)

  text("As you leave, you realize that you were the last of the prisoners to be released. The Captain talks quietly on the radio and slowly puts it down. Gunshots soon follow and the blood curdling screams of men are heard. You can’t go back and save him even if you could. Night is finally with his brother, however you can return for his body later.", 14)

  text("Captain: We lost everyone of them…", 2.5)

  text("You walk away and find yourself alone in the snow and hear footsteps behind you.", 4)

  text("Nazi Soldier: Drop weapon.", 2.5)

  text(PlayerName+": Yes…", 1)

  enemy = p.Enemy('Naiz Soldier', 15,8,40,120, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("Back up begins to come and you must finish off every last one of them.", 4)

  enemy = p.Enemy('Naiz Soldier', 15,8,40,120, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  enemy = p.Enemy('Naiz Soldier', 15,8,40,120, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()
  
  enemy = p.Enemy('Naiz Soldier', 15,8,40,120, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("More keep coming and you can’t keep up with all of them forever. You run away and eventually make it back to base. You find Moon surprised to see you.", 7)

  text("Moon: I thought you would have died by now.", 3)

  text(PlayerName+": Everyone else is.", 2)

  text("Moon: God… We have to get into the tank, we have King Tigers approaching our perimeter and we have to fight them off if we are going to win this war. The Tiger was decommissioned when we were surrounded. All we have left is the Sherman. Chief is already in it with some soldiers he found.", 12)

  text("You make it to the Sherman and Chief is yelling at you to hurry up and get inside.", 5)

  player.switch(player.getgunname(), player.getrate(),player.getattack(), player.getgunreload(), player.getammo(), player.getclipammo(), player.getgtype())

  player.gunchange('M4 Sherman', 60, 40, 4, 48, 9, 'Medium Tank')

  text("Chief: Get in you two, I don’t want to be driving this hunk of junk as much as you guys, but I don’t want to die out there also.", 10)

  text("You guys get in the tank and head into battle and find yourself fighting two King Tigers.", 6)

  enemy = p.Enemy('King Tiger', 70 ,40,5, 100, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  enemy = p.Enemy('King Tiger', 70 ,40,5, 100, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("Chief: Our systems can’t take anymore of this.", 3)

  text("A loud noise is heard and the Sherman is shaken.", 3)

  text("Chief: Dammit we’ve been hit and that’s the last King Tiger on the field. I need someone to stay with me to shoot the thing. Everyone else get out you still can fight.", 9)

  text("Before Moon could sacrifice himself one of the other soldiers said…", 3)

  text("Soldier: I’ll stay I’ll ensure that the Tiger will be salin.", 4)

  text("Everyone else left the vehicle and hid in the snow to watch the Sherman’s last stand. The Sherman managed to flank the tank and get a few shots on the Tiger disabling it, but had a fatal shot towards the heart of the Sherman. The tank was no more and the crew of the Tiger exited the vehicle to be executed by a Hellcat approaching from the side. You signaled to the Hellcat and joined its crew.", 15)

  player.safety(player.getgunname(), player.getrate(),player.getattack(), player.getgunreload(), player.getammo(), player.getclipammo(), player.getgtype())

  player.gunchange('M18 Hellcat', 60, 100, 5, 64, 9, 'Light Tank Destroyer')

  text("Tank Driver: Welcome boys, I understand it’s crowded in here but it’s time to go hunting.", 6)

  text("The tank speed off at high speeds and in turn were able to catch up to the retreating tank divisions. You spot a Panzer attempting to flee, ready aim fire!", 10)

  enemy = p.Enemy('Panzer', 75 ,45,10, 120, 7, 20)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()
  
  text("A King Tiger appears before you struggling to escape the forest terrain.", 4)

  enemy = p.Enemy('King Tiger', 70 ,40,5, 100, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("You reach the edge of the forest and continue to push back the forces.", 4)

  enemy = p.Enemy('Panzer', 75 ,45,10, 120, 7, 20)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  enemy = p.Enemy('Panzer', 75 ,45,10, 120, 7, 20)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("As soon as you think you are in the clear a shell hits the tank and nearly blows it to bits and it has to be your last stand against a King Tiger.", 10)

  enemy = p.Enemy('King Tiger', 70 ,40,5, 100, 2, 15)
  battle = b.battle('Active', enemy, player)

  if battle == 'Lose':
    gameOver()

  text("The tank is totaled and you have to abandon it if you expect to get anywhere. The driver leaves and a shot is heard. The driver falls back into the cockpit with a clean bullet hole through his head. The crew members that you don’t know are beginning to panic as they don’t know what to do.", 17)

  text("Soldier: What are we going to do, I wish I was never drafted, I could have been back at home and went to school. Now I am going to die with strangers.", 9)

  text("Moon: Quiet kid, if you want that then step out of this tank and try and take out the sniper, because talking like that isn’t going to help anyone.", 9)

  text("Soldier: Go to Hell, if you want that then I’ll step out and kill him myself.", 4)

  text("Moon: Don't!", 1)

  text("Like the driver the kid fell back inside with a similar wound. Moon looks at the other soldier and speaks.", 6)

  text("Moon: Are you going to try the same stupid thing?", 4)

  text("Soldier: No sir.", 1)

  text("Moon: Good thing we go that covered. Now does anyone have an idea of how we are going to get out of here? We are pinned down and this sniper isn’t going to leave us be.", 9) 

  text("Soldier: We can try and leave the tank from the exit cause by that first shell we took damaged from. We could try and squeeze through it after trying to open the hole more. The armor is thinner and we could try and move it to fit through.", 12)

  text("Moon: That’s worth a shot and I’ll go through first ot check if its safe and I’d be able to get through the quickest since I’m the smallest.", 6)

  text("Moon exits the tank and you follow squeezing through. The kid couldn’t fit and you told him that you and Moon would go and take care of the sniper and come back for him.", 8)

  text("Soldier: Please hurry, I don’t want to wait here long.", 4)

  text("Shielded by the snow, you were able to crawl to the position of the sniper, but the kid opens the top of the tank but doesn’t rise. The sniper takes a shot and realizes that no one is exiting. He lauunches a grenade into the tank and you hear the scream of the kid as he is blown out of the tank while trying to escape.", 12)

  text("Soldier: Help me!", 1.5)

  text("The sniper silences him and you and Moon approach his position. Moon take out his pistol and shoots him.", 7)

  text("Moon: We did it Apollo, we did it, we finally ended our struggle. We can finally go ho-", 5)

  text("Moon is shot through the chest and you pull out your weapon and…", 4)

  for n in range(8):
	  input("Press Enter to Fire")

  text("The sniper doesn’t move and won’t ever hurt another soul again.", 4)
  
  text("Moon: Apollo, I don’t have much time left. I just want to spend my last moments with you. Do you know who your father is?", 7)

  text(PlayerName+": No.",1)

  text("Moon: Well I never got to see my kid since I joined the service ten years ago. He would have been about your age. The more time I spent with you, the more you reminded me of him. I know you don’t remember me but I want you to return to your mother and take her my belongings. The address is written on the paper. She will be happy to see you. This war is over in Europe, the Soviets will be in Berlin in a few months at the latest. Just remember I love you and will alway be with you.", 17)

  text(PlayerName+": Thank you father.", 3)

  text("While covered in blood the artillery fell alongside the snow, and your world turned red with blood flowing into your eyes. Moon died in your arms and you stayed there for a few hours until a truck came by and picked you up.", 10)

  text("Officer: What happened out there soldier? You look like you went through hell.", 4)

  text("???: So that’s what happened to my father?", 3)

  text(PlayerName+": He died protecting me like I was his own son. I felt that you needed to know this. I am sorry that I thought your father was mine.", 9)

  text("Moon's Son: What are you going to do now?", 2.5)

  text(PlayerName+": I don’t know where I belong in this world anymore. I have a medal of honor for my actions but that’s all I have to my name. I probably will never know what would have happened to me if I had done anything differently, but I’m glad I was able to be there for your father. I should have perished, but I wanted to fulfill his dying wish and ensure your mother received his belongings and his son knew his story even if it wasn’t me.", 15)

  text("Moon's Son: Thank you, how can I ever repay you?", 1.5)

  text(PlayerName + ": By keeping this medal for your father because he was the real hero out there and by remembering what I had told you.", 5.5)

  text("You walked away from Arlington cemetery and never looked back at your old friends. You were only able to visit Night, Light, Moon, and Chief, since Noir was buried and honored in France. You don’t know what will happen to you on your path onwards, but you knew that your life would never be the same.",9)

  credits()

def Act4AA(PlayerName, player):
  player = player

  text("It was hard to sleep that night due to the Night Light keeping you up. However, the voices of people are comforting for you, but still a bulwark to your sleep.",5)

  text("Moon: Get up kid, we have to get to the trucks. We have to be out of here in 20 minutes. We will be waiting for you to get your stuff together.", 4.5)

  text("What do you want to do during your remaining time?", 2)

  choice = input("1. Visit the armory and buy new weapons. 2. Visit the Church. 3. Write a will 4. Go to the restroom, it may be awhile before you find a nicer one.")

  if choice == '1':
    text("With you whatever money you found,  you go to the local armory in hopes to purchase a new weapon.",3)
    text("Manager: Jesus kid you sure do look awfully young to be here but whatever, as long as you have enough money to buy something, I don’t care what you do.", 5)

    item1 = i.Item('M1918 BAR', 20, 60, 20, 'Automatic Rifle', 40, 60, 4)
    
    item2 = i.Item('Winchester Model 18', 50, 15, 3, 'Bolt Action Rifle', 40, 75, 3)

    shop1 = s.Shop(item1, item2, "Chubby Boy Guns")

    shop1.openShop(player)
  
  if choice == '2':
    ye = input("Pastor: Welcome my child, we here understand the pain and sorrow you must be experiencing here. Would you wish to participate in  prayer, Yes or No?")
    ye = ye.lower()

    if ye == 'yes':
      text("Pastor: Thank you child and let the Lord have mercy on your soul.",2)
    
      text("You participated in the prayer for the day and feel better, slightly.", 2)

    elif ye == 'no':
      text("Pastor: I am sorry to hear that answer but I hope you find yourself on the path to the Lord another time. I'm thankful that you have made the initiative to set forth here.",5.5) 

    else:
      text("You just stood there saying gibberish, you left and everyone stared at you.",3)
      text("Lady Inside: God have mercy on his soul. This war is really hurting these kids.", 2.5)

  if choice == '3':
      text("You write a will that you plan to keep on yourself if you die.", 2)
      text('It reads, “I am sorry but I cannot recall who I am or was and can only inform whoever that finds my body that I relinquish all my belongings to whoever finds this or to whoever manages to discover my family. I am satisfied with either of these outcomes.', 8.5)

  if choice == '4':
    text("Yes you really did that…",1)

  text("You return to the rest of the company and board the truck to go off to the battlefield. After a couple of hours you arrive to the location where you are to be deployed. It appears to be quiet and you for some reason know that it is too quiet. Moon begins to inform the company of your guys’ mission.",10)

  text("Moon: Up ahead there is a bunker that has been abandoned supposedly and it’s our job to scout it and ensure that it is safe for us to camp for the night  and to convert it to an outpost. We are allowed to take any weapons that we find but that’s about it. We will be entering from the four different entrances. Night you will enter from the South West entrance, Light you have the Northeast, I’ll take the South East entrance, and Apollo you will enter the entrance that is a klick North of our position. It may be wise for you to avoid the path that goes by the turret position.", 20)

  text("Night: How dangerous should this be?", 1.5)

  text("Moon: It shouldn’t be unless we have any animals or stragglers…",3)

  text("Light: I think we can take on anything that ends up in there.",2)

  text("Night: You act like you can take on a bear.",2)

  text("Light: How much you wanna bet?",1.5)

  text("Night: Go to hell.",1)

  text("Light: You never said I couldn’t.", 1)

  text("Moon: Just hurry up, I don’t want to camp here for the night.",2)

  text("Night: What Moon?",1.5)

  text("Moon: I really want to hit you with the butt of my gun just so I don’t have to hear another word from you.",3)

  text("Night: Okay we are going.",1.5)

  text("You leave the rest of the group and have two options: You can either go through a dark passageway or tread the forest around the bunker and get to the proper entrance. However, there may be a risk of badgers being out and about this time of year and that it might not be good to deal with one right now.",7)

  text("What path are you going to take?",1)
    
  choice1 = input('1. Badgers don\'t scare me! 2.I ain\'t afraid of the dark!')
    
  if choice1 == '1':
    while(True):
      x = random.randint(0,100)
      
      if x < 30:
        text("You traversed the wooded area and didn’t come across any animals thankfully.",4)
        break
      
      else:
        text("Damnit a wild badger crosses your path and it is pissed off at you for crossing into its territory. There doesn’t appear to be a way out of this.",5)
        enemy = p.Enemy('Badger',15,7,30,60, 1, 10)
        battle = b.battle('Active', enemy, player)
        
        if battle == 'Lose':
          gameOver()
        
        
        break
  
    text("You approach the turret location and choose to proceed by it slowly. You hear a noise but are unsure whether or not it is an enemy.",4)
    
    choice1 = Act5AA(PlayerName, player)
    
    if choice1 == 'GG':
      return choice1

  else:
    text("You walk through the dark corridors and encounter a dead end inside the passageway. However you found an exit to the outside of the bunker and see the door to go inside.",4)

    return Act5AA(PlayerName, player)
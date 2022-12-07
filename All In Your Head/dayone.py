from text import *
from graphics import *
from classesforPYR import *
from tests import *
from drawchar import *
from player import *
from battle import *
from Name import FindName
from weapons import *
import winsound as w


class DayOne:
    def __init__(self, win):
        self.ctpoint = Point(640,640)
        self.pyr_health_point = Point(80,80) 
        self.enemy_health_point = Point(1220,80) 
        self.attack_name_point = Point(650,340)
        self.win = win

        self.PYR = Char(win,'Name',"FighterIcon/PYRFighter.png", "charpic/PYRLeft.png",'No Right Pic', 'BattlePicture/PYR.png', "Fightericon/Small/PYRFighter.png" )
        
        self.CNR = Char(win,'Connor','FighterIcon/CNRFighter.png','charpic/CNRLeft.png','No Right Pic', 'No Battle Pic','')
        self.CNRName = self.CNR.getName()

        self.RCL = Char(win,'Rachel','No Fighter Pic','','No Right Pic', 'No Battle Pic','')
        self.RCLName = self.RCL.getName()
        
        self.IBA = Char(win,'Isabella','No Fighter Pic','','No Right Pic', 'No Battle Pic','')
        self.IBAName = self.IBA.getName()

        self.DYN = Char(win,'Dr.Yin','','','', 'No Battle Pic','')
        self.DYNName = self.DYN.getName()

        self.DYG = Char(win,'Dr.Yang','','','', 'No Battle Pic','')
        self.DYGName = self.DYG.getName()

        self.TDE = Char(win,'Thedore','','charpic/TDE.png','', 'No Battle Pic','')
        self.TDEName = self.TDE.getName() 

        self.JRH =  Char(win,'???','','charpic/Jeriah.png','', 'No Battle Pic','')
        self.JRHName = self.JRH.getName()

        self.JHT = Char(win, '???', '', 'charpic/Johnathan.png','charpic/JohnathanRight.png', 'BattlePicture/Johnathan.png',"Fightericon/Small/JHT.png")
        self.JHTName = self.JHT.getName()

        self.FM = Char(win, '??', '', 'charpic/FirstMate.png','charpic/FirstMateRight.png', 'BattlePicture/FirstMate.png',"Fightericon/Small/FM.png")
        self.FMName = self.FM.getName() 

        self.DFM = Char(win, '???', '', 'charpic/DFirstMate.png','charpic/DFirstMateRight.png', 'BattlePicture/DFirstMate.png',"Fightericon/Small/DFM.png")
        self.DFMName = self.DFM.getName()

        self.MOM = Char(win,'Mom','','charpic/Mom.png','', 'No Battle Pic','')
        self.MOMName = self.MOM.getName() 

        self.SHN = Char(win,'Shaun','','charpic/SHN.png','', 'No Battle Pic','')
        self.SHNName = self.SHN.getName() 

        self.text = gameText(self.win)

        self.courses = Courses()

        self.screen = Screen(self.win)

        self.tests = SchoolTests(self.win,self.PYR)
        
        self.PlayerParty = [self.PYR]

    def intro(self):
        #w.PlaySound("Music/Mystica.wav" , w.SND_ASYNC)
        self.screen.drawScreen('background/introlivingroom.png',['charpic/Chuck.png'],'???')
        self.text.text("This is nice isn't it Todd?")

        self.screen.updateScreen('',['charpic/Todd.png'],"Todd")
        self.text.text("Do you think that we should be drinking the day before school?")

        self.screen.updateScreen('',['charpic/Luis.png'],'???')
        self.text.text("Chuck, leave him be, he has a slight point, but just don't get wasted.")

        self.screen.updateScreen('',['charpic/Chuck.png'],'Chuck')
        self.text.text("You have always been a tightass, why can't you ever have fun?")

        self.screen.updateScreen('',['charpic/Luis.png'],'???')
        self.text.text("A hangover is never fun, especially when we have stuff to do the next day.")

        self.screen.updateScreen('',['charpic/Chuck.png'],'Chuck')
        self.text.text("Luis, you have to learn how to live your life.")

        self.screen.updateScreen('',['charpic/Luis.png'],'Luis')
        self.text.text("I told you we should have done this yesterday.")

        self.screen.updateScreen('',['charpic/Todd.png'],"Todd")
        self.text.text("I'll be back, I'm going to the bathroom.")

        self.screen.updateScreen('',['charpic/Luis.png'],'Luis')
        self.text.text("I still don't understand why the bathroom is on a higher floor.")
        self.text.text("Anyways, look now he's sick, hopefully we don't have to take him to the hospital.")
        
        self.screen.updateScreen('',['charpic/Chuck.png'],'Chuck')
        self.text.text("He barely took a few sips of his drink, he can usually hold his own.")

        self.screen.updateScreen('',['charpic/Luis.png'],'Luis')
        self.text.text("Did you make the drinks strong?")

        self.screen.updateScreen('',['charpic/Chuck.png'],'Chuck')
        self.text.text("I knew we had school, so I didn't add much to them.")
        self.text.text("It shouldn't even get us...")

        #w.PlaySound("Soundeffects/glassshatter.wav" , w.SND_ASYNC)

        self.text.text("Dammit, I will go up and check on him.")

        self.screen.updateScreen('',['charpic/Luis.png'],'Luis')
        self.text.text("Dammit, we probably have to go to the hospital now...")

        self.screen.updateScreen('',['charpic/Chuck.png'],'Chuck')
        self.text.text("Sh!t, Luis hurry get up here.")
        self.text.text("Call the paramedics, now!")

        self.screen.updateScreen('background/bloodybathroom.png',['charpic/Luis.png'],'Luis')
        self.text.text("They are on their way.")
        self.text.text("Where is he?")
        
        #w.PlaySound("Soundeffects/sirens.wav" , w.SND_ASYNC)
        
        self.screen.updateScreen('',['charpic/Chuck.png'],'Chuck')
        self.text.text("Outside...")

        #w.PlaySound(None, w.SND_PURGE)

        self.screen.undrawScreen()


    def news(self):
        #w.PlaySound("Music/goodbye.wav" , w.SND_ASYNC)
        self.screen.drawScreen('background/newsintro.png',['charpic/Reporter.png'],'Reporter')
        self.text.text("We bring your attention to breaking news.")
        self.text.text("A high school boy has been found dead after an apparant suicude.")
        self.text.text("This has been the fifth suicide in the past five months.")
        self.text.text("Officers are still stumped on the reasoning why the boy Todd-")
        self.text.text("I have just been informed that I can't say the boy's last name for privacy.")
        self.text.doubleText("His friends also don't know why he did this, stating that he","didn't exhibit signs of suicide and depression.")
        self.text.text("This is another part of the strings of misfortunes that have plague our city.")
        self.text.text("Make sure to watch out for the signs and we can protect our kids from more harm.")

        self.screen.updateScreen('background/livingroomtv.png',[self.MOM.getPicture()],"???")
        self.text.text("Dear God, the poor soul. I think I know the mother.")

        self.screen.updateScreen('',[self.PYR.getPicture()],"You")
        self.text.text("What happened Mom?")

        self.screen.updateScreen('',[self.MOM.getPicture()],self.MOMName)
        self.text.text("Just go to bed, we can talk about it tomorrow.")

        #w.PlaySound("Music/goodandevil.wav" , w.SND_ASYNC)

        self.screen.updateScreen('background/Firstdreambackground.png',["charpic/PYRMind.png"],"Your Mind") 
        self.text.text('You go to bed and wake up somewhere odd.')
        self.text.text("Some black figure approaches you and asks you a question.")

        self.screen.undrawScreen()
        
        temp = FindName(self.win)
        self.PYR.loadName(temp)
        self.PYRName = self.PYR.getName()

    def dream(self):
        self.screen.drawScreen('background/Firstdreambackground.png',[self.TDE.getPicture()],'???')

        self.text.text("I know some crazy stuff has been occuring here right?")
        self.text.text("Some people from your land have been dying.")
        self.text.text("I'm guessing you don't know why either, but I can help.")
        self.text.text("However, our time is thining and I have much more to tell you.")
        self.text.doubleText("The only problem is that you are beginning to wake up ","and I won't be able to talk to you until you fall asleep.")
        
        self.screen.undrawScreen()
        #w.PlaySound(None, w.SND_PURGE)

    def morn(self):
        #w.PlaySound("Music/NYclub.wav" ,w.SND_ASYNC)
        self.screen.drawScreen('background/bedroom.png',["charpic/PYRMind.png"],'Your Mind')
        self.text.text("You woke up sweating from your strange dream.")
        self.text.text("Something doesn't feel right, but you are going to have to ignore it and head to school.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text(self.CNRName+" will be pisssed if I keep him waiting.")
        self.text.text("Something doesn't feel good but I will be fine until after school.")
        
        self.screen.undrawScreen()

    def walk2skool(self):
        self.screen.drawScreen('background/sidewalk.png',["charpic/PYRMind.png"],'Your Mind')
        self.text.text("You meet up with "+ self.CNRName+ " and are walking to school.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("It's about time you arrived. I've been waiting for five minutes already we better hurry or we'll be late.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Yeah I know, I slept in a little too late. I had an odd dream though.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("That's funny it's cool dude, what happened.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Some person recapped the deaths and everything that had been happening here.")
        self.text.text("It said he'd be meeting me as soon as I fall asleep again.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("Woah..., do you think that you'll see it again when you go to bed? Like a second part of a dream.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("I don't know I'll have to find out tonight.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("Ok, let's hurry on to class.")

        self.screen.undrawScreen()

    def pickclass(self):
        self.screen.drawScreen('background/school.png',["charpic/PYRMind.png"],'Your Mind')

        self.text.text("This week of school is a test week for your classes.")
        self.text.text("You must choose your classes wisely.") 
        self.text.text("If one has differnt requirements and rewards.") 
        self.text.text("They meet on differnt days so keep track of what work must be done for each class.") 
        self.text.text("If you fail you may have to retake it and pay the fine for retaking a class.") 
        self.text.text("For your morning class on MONDAYS you have to choose a math class.")
        self.text.text("Every class except Algebra 1 has a test requirement.")
        self.text.text("The options that are available for you are Algebra 1, Geometry, and Algebra 2.")
        self.text.doubleText("Geometry and Algebra 2 have a test that you can ","take that has topics from Algebra 1 and Geometry.")
        self.text.text("If you pass with a 70% you'll be able to go into that class.")
        self.text.text("The bubble sheet has the classes assagined to numbers.")
        self.text.text("Algebra 1 is bubble one and so on.")
        self.text.text("This class wil boost your PROBLEM SOLVING skill.")


        self.text.text("What class will you take? Algebra 1, Geometry, and Algebra 2.")
        option = self.screen.MakeChoice(["Algebra 1", 'Geometry', 'Algebra 2'],["Choices/algebra1.png","Choices/geometry.png","Choices/algebra2.png"], self.PYRName)


        if option == "Algebra 1":
            self.courses.setMathClass(1)
            
        elif option == 'Geometry':
            self.text.text("You have chosen Geometry. You must answer a ten question quiz to determine if you are suitable for this course.")
            self.screen.undrawScreen()
            self.tests.geometrytest()
            self.screen.drawScreen('background/Firstdreambackground.png',"charpic/PYRMind.png",'Your Mind')

        elif option == 'Algebra 2':
            self.text.text("You have chosen Algebra 2. You must answer a take the Geometry and Algebra Test.")
            self.screen.undrawScreen()
            self.tests.geometrytest()
            self.tests.algebra2test()
            self.screen.drawScreen('background/Firstdreambackground.png',"charpic/PYRMind.png",'Your Mind')

        self.text.text("You are enrolled in " + self.courses.getMathCourse())

        self.text.text("On Monday in the afternoon you have English 1. This will boost your PERSUASUION SKILL")
        self.courses.setEnglishClass(1)
        
        self.text.doubleText("On Tuesday in the morning you have the Earth Science class.","This will boost your INTELLGIGENCE skill")
        self.courses.setScienceClass(1)
        
        self.text.doubleText("On Tuesday in the afternoon you will have PE."," This will boost your AGILITY skill.")
        self.courses.setPEClass(1)

        self.text.doubleText("On Wednesday morning you will have United States History","This will boost UNDERSTANDING & INTELLIGENCE skills slightly")
        self.courses.setHistoryClass(1)
        
        self.text.text("On Wednesday afternoon you will have Spanish 101.")
        self.text.doubleText("This will boost COMMUNICATION and allow you to ","communicate with people speaking Spanish on a basic level.")
        self.courses.setSpanLangClass(1)
        
        self.text.doubleText("On Thursday Morning you have Sculputuring. ","This will boost CREATIVITY")
        self.courses.setCraftingClass(1)

        self.text.text("For Thursday afternoon and Friday morning you get to choose two electives.")
        self.text.text("They can either be free time so you can go home early or classes that will boost other skills.")
        self.text.text("The bubble sheet has two options for Thursday afternoon.")
        self.text.text("Option 1: for Sociology which will boost UNDERSTANDING.")
        self.text.text("Option 2: Art which will help boost CREATIVITY.")

        self.text.text("What class do you want.")
        option = self.screen.MakeChoice(["Sociology", 'Art'],["Choices/sociology.png","Choices/art.png"], self.PYRName)

        self.courses.setFallElective1 = option

        self.text.text("For Friday morning there are three options.")
        self.text.text("Option 1: Engineering 1 which will boost INTELLIGENCE and boost CREATVITY.")
        self.text.tripleText("Option 2: Thinking For Yourself which doesn't have homework or tests," ,"and boosts CREATIVLY, greatly but is an all day class," ,"meaning you get out at 4pm.")
        self.text.text("Option 3: Study Hall, it allows you to skip school entirly on Friday.")

        self.text.text("What class do you want.")
        option = self.screen.MakeChoice(["Engineering 1", 'Thinking For Yourself', 'Study Hall'],["Choices/engineering1.png","Choices/thinkingforyourself.png","Choices/studyhall.png"], self.PYRName)

        self.courses.setFallElective2 = option

        self.screen.undrawScreen()

    def lunch(self):
        self.screen.drawScreen('background/lunchtable.png',["charpic/PYRMind.png"],'Your Mind')
        self.text.text("You left the school and went out to lunch with your friends.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("I can't believe the classes I got. I'm stuck with Algebra 1 for math.")

        self.screen.updateScreen('',["charpic/RCLRight.png"],self.RCLName)
        self.text.text("I at least got into Geometry. I don't know how you couldn't get into Geometry.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("Don't bring it up.")

        self.screen.updateScreen('',["charpic/RCLRight.png"],self.RCLName)
        self.text.text(self.IBAName + " what class did you get?")

        self.screen.updateScreen('',["charpic/IBARight.png"],self.IBAName)
        self.text.text("Algebra 2.")
        self.text.text(self.PYRName+" what class did you get?")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text(self.courses.getMathCourse())

        if self.courses.getMathCourse() == 'Algebra 1':
            self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
            self.text.doubleText("Well looks like we're in the same boat.","Damned math class.") 

        elif self.courses.getMathCourse() == 'Geometry':
            self.screen.updateScreen('',["charpic/RCLRight.png"],self.RCLName)
            self.text.doubleText("That's good, we'll have a class together.","You can help me if I need it.") 

        elif self.courses.getMathCourse() == 'Algebra 2':
            self.screen.updateScreen('',["charpic/IBARight.png"],self.IBAName)
            self.text.text("I guess we go into the harder math class, but I think we can handle it.")

        #w.PlaySound("Music/goodandevil.wav" , w.SND_ASYNC)
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("I'm not feeling so good.")
        
        self.screen.updateScreen('',[self.CNR.getPicture(),"charpic/IBARight.png","charpic/RCLRight.png"],('Con. ' + 'Rac. ' + 'Isa'))
        self.text.text("What's wrong?!")
        
        self.screen.updateScreen('',["charpic/PYRMind.png"],"Your Mind")
        self.text.text("You begin losing conciousness randomly...")
        
        self.screen.undrawScreen()

    def passout(self):
        self.screen.drawScreen('background/Firstdreambackground.png',["charpic/TDE.png"],'???')
        self.text.text("Welcome back I knew this was going to happen soon.")
        self.text.text("It's like morning sickness, but you aren't pregnant.")
        self.text.text("You'll feel this way for the next few days.")
        self.text.text("You'll pass out randomly like this, but I'll be able to explain what's going on.")
        self.text.text("So you know how these people seemingly go mad and say that the root is in the...")
        
        self.screen.undrawScreen()

    def nurseoffice(self):
        #w.PlaySound("Music/NYclub.wav" , w.SND_ASYNC)
        self.screen.drawScreen('background/schoolnurse.png',["charpic/PYRMind.png"],'Your Mind')
        self.text.text("You wake up in the nurses office with Connor near you.")
        
        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("What happened to you.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("I dont't know but that dreamed continued until I woke up right now.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("Now isn't the time to talk about this.")
        self.text.text("I will go outside with the rest and tell them that you are now fine.")         
        self.text.text("The nurse is going to talk to you know that you are awake.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Bye, I'll try and see you guys when I'm done.")
        
        self.screen.updateScreen('',["charpic/NRERight.png"],"Nurse")
        self.text.text("Has this ever happned to you before?")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("No.")
        
        self.screen.updateScreen('',["charpic/NRERight.png"],"Nurse")
        self.text.text("Okay then. I will send you to a doctor that said that he's seen this before.")
        
        self.screen.undrawScreen()

    def docoffice(self):
        self.screen.drawScreen('background/examinationroom.png',["charpic/PYRMind.png"],'Your Mind')
        self.text.text("You were transferred to Dr. Yang's office where he will see you.")
        
        self.screen.updateScreen('',["charpic/DYGRight.png"],self.DYGName)
        self.text.doubleText("An old friend of mine at your school said you started passing out ","of nowhere and that it hadn't happened before.")
        self.text.text("I recommened you to come here because I personally think you have that dream madness thing.")
        self.text.text("Don't be alarmed even though I don't have a way to treat it.")
        self.text.text("You have about 30 days until you go mad to the point where someone you know whats.")
        self.text.text("I want to help you but I don't know where to begin.")
        self.text.doubleText("An old friend of mine at your school said you started", "passing out of nowhere and that it hadn't happened before.")
        self.text.doubleText("I have noticed people being troubled almost as if they were depressed","so I will give you anti-depressants since my last patient was able to go longer with them.")
        self.text.doubleText("Each bottle added about a month's time to him compared to others, ","but after multiple treatments, the effects began to be lesser until it became a placebo.")
        self.text.doubleText("I don't currently have any treatments other than this to help you.", "Unless you can figure out how to help people I can't do anything as of now.")
        self.text.text("My sister Dr.Yin will be able to give you a bottle for this week.")
        self.text.text("Please be safe, if anything happens come to me and I'll try to help you.")

        self.screen.updateScreen('',["charpic/PYRMind.png"],'Your Mind')
        self.text.doubleText("You can visit Dr.Yang for a few hours which will add a couple days to your life,", "but don't rely on this since he may be booked during times or can be off from work.")
        
        self.screen.undrawScreen()

    def pillpickup(self):
        self.screen.drawScreen('background/pharmacy.png',["charpic/DYNRight.png"],self.DYNName)
        self.text.doubleText(("Hello, "+ self.PYRName + " I have been expecting you, my brother told me that this " ),"is your prescription that you have to refill every week.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("How much are they going to be?")

        self.screen.updateScreen('',["charpic/DYNRight.png"],self.DYNName)
        self.text.text("$20.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Thankfully I have $20 on me.")

        self.screen.updateScreen('',["charpic/DYNRight.png"],self.DYNName)
        self.text.text("Thank you I will see you next week bye.")

        self.screen.undrawScreen()
    
    def gangedup(self):
        #w.PlaySound("Music/Shadows.wav" ,w.SND_ASYNC)
        self.screen.drawScreen("background/Park.png",["charpic/PYRMind.png"],"Your Mind")
        self.text.text("While walking home through a park three men come up to you.")
       
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Is there anyhting I can do to help you guys?")
        
        self.screen.updateScreen('',[self.JHT.getPicture()],"???")
        self.text.text("Yeah you can give us whatever money you have on you.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Sorry I don't have any money on me so...")

        self.screen.updateScreen('',[self.FM.getPicture()],"???")
        self.text.text("What is this bag though?")
        
        self.screen.updateScreen('',[self.JRH.getPicture()],"???")
        self.text.text("It's medicine, just look at it,")
        
        self.screen.updateScreen('',[self.JHT.getPicture()],"???")
        self.text.doubleText("Well since you don't have any money on you, we'll","hold onto your meds and wait for you to get $100.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("That's a bit excessive don't you think.")
        self.text.text("Look, I don't feel good, I just want to go home and rest.")
        
        self.screen.updateScreen('',[self.JHT.getPicture(),self.FM.getPicture()],"??? " + "???")  
        self.text.doubleText("Fine then, I guess we'll kick your ass and then take the meds."," If you change your mind you can have them back.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("This won't turn out good.")
        self.screen.undrawScreen()
        
        self.PYR.addItem('R',Item("Bandage", "BattleIcon\ItemPicture\Bandage.png","Heal", 50))
        self.PYR.addItem('R',Item("Bandage", "BattleIcon\ItemPicture\Bandage.png","Heal", 50))
            
        self.PlayerParty = [self.PYR]
        self.EnemyParty = [self.JHT, self.FM]

        self.Battle = Battle(self.win,self.PlayerParty,self.EnemyParty,"background/Park.png", "P", 'R', 'NF')
        var, var2 = self.Battle.Fight()
        self.PYR.IncreaseEXP(var2)
        self.PYR.checkLevel()
        self.Battle.closeScreen()

        loadingscreen = Image(Point(640, 360), 'background/Loading.png')
        loadingscreen.draw(self.win)

    def dreamworld(self):
        #w.PlaySound("Music/sexpest.wav" ,w.SND_ASYNC)
        self.screen.drawScreen('background/Firstdreambackground.png',["charpic/PYRMind.png"],"Your Mind")
        self.text.text("Wow that didn't go well. They knocked us out.")
       
        self.screen.updateScreen('',[self.TDE.getPicture()],'???')
        self.text.text("I'm surprised you returned on such short notice. I was getting bored.")
        self.text.text("I was expecting you to come back in a few of your hours.")
        self.text.text("You seem to be a bit nausiated. Did something happen to you?")
        
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)

        speech = self.screen.MakeChoice(["No, of course not...", 'I may or may not have gotten whopped out there.', 'Nope', 'I might have broken a rib.'],["Choices/Noofcoursenot.png","Choices/Imayormaynothavegottenwhoppedoutthere.png","Choices/Nope.png","Choices/Imighthavebrokenarib.png"], self.PYRName)

        self.text.text(speech)

        self.screen.updateScreen('',[self.TDE.getPicture()],'???')

        if speech == 'No, of course not...':
            speech = "You don't sound very sure."

        elif speech == 'I may or may not have gotten whopped out there.':
            speech = "Hmm... I think you may have."

        elif speech == 'Nope':
            speech = "Ha, that's funny."

        elif speech == 'I might have broken a rib.':
            speech = "Never would have known."


        self.text.text(speech)
        self.text.doubleText("Ain't that awful, well, that's fine you'll recover with some rest,", "but I guess now is a better time than never to explain what's going on.")
        self.text.text("So my name is Theodore and I have been stuck in this land for so long.")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Whoever is doing this has been targeting people who are suspectiable to stress.")
        self.text.doubleText("The amygdala will be targeted and science stuff" ,"occurs and the individual could then become depressed.")
        self.text.doubleText("It works like a sickness; getting worse as time","progresses and will eventually kill the host if let untreated.")
        self.text.text("I've helped people like you in the past, but they have failed...")
        self.text.doubleText("What makes it worse is while depressed the person","can dwell on the dark moments of the past if they have times where they don't forgive themselves.")
        self.text.text("It's imperative for you to change your outlook on life, especially in the future.")
        self.text.text("After prolonged time in this state they eventually kick the bucket.")
        self.text.text("However, you will find out something odd; you will be having a lot more dreams.")
        self.text.text("I believe that these dreams are where you can find your answers.")

        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)

        speech = self.screen.MakeChoice(["Like having a dream that has an underlying message?", "I don't get what you mean?", "I'll just roll with it.", "How do I get more dreams?"],["Choices/Likehavingadreamthathasanunderlyingmessage.png","Choices/idontgetwhatyoumean.png","Choices/illjustrollwithit.png","Choices/howdoigetmoredreams.png"], self.PYRName)

        self.text.text(speech)

        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)

        if speech == "Like having a dream that has an underlying message?":
            speech = "Kind of like that."

        elif speech == "I don't get what you mean?":
            speech = "Hmm... I think you may have."

        elif speech == "I'll just roll with it.":
            speech = "Yeah you should do that."

        elif speech == 'How do I get more dreams?':
            speech = "Umm... I don't know. It just sort of happens."

        self.text.text(speech)

        self.text.text("However before you go off in your search for the key to your problems, you must know one thing.")
        self.text.text("I can't remeber where you were last at, you must keep track of where you last were.")
        self.text.text("A dream journal like ones that help people lucid dream may be able to help you.")
        self.text.doubleText("I've had ony one person come and be able to find the key,", "but after he left to face his problems, I never saw him again.")
        self.text.doubleText("I don't know if he ws able to escape this hell or succumb to", "himself, since I only know of my old world through these vists.")
        self.text.doubleText("I should let you know that every person here is a figment of", "your imagination and that they can help you more than I can.")
        self.text.text("The currency here is not paper but your own memory.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("That's preety meta...")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Be quiet I need to hurry up and explain stuff.")
        self.text.text("You can free up memory by destroying entites here and erasing them from your mind.")
        self.text.doubleText("You can also try memory games to increase your memory","which you can then use to construct objects to aid you here.")
        self.text.doubleText("Reading and watching televison can help you think of ideas", "for tools, but will need some planning and memory to build.")
        self.text.text("Sadly our time is thining once more but I'm glad we were able to talk again.")
        self.text.text("Hopefully next time you come you are able to get a start on helping yourself.")

        self.screen.undrawScreen()
    
    def snapback(self):
        self.screen.drawScreen('background/Park.png',["charpic/PYRMind.png"],"Your Mind")
        self.text.text("You wake up on the ground with your family staring at you.")
            
        self.screen.updateScreen('',[self.MOM.getPicture()],self.MOMName)
        self.text.text("What the hell happened to you.")
            
        self.screen.updateScreen('',[self.SHN.getPicture()],self.SHNName)
        self.text.text("The police notified us that you were found unconcious in the park.")
        self.text.text("We thought you have overdosed on drugs or something worse.")
            
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Don't worry it was nothing.")
        
        self.screen.updateScreen('',[self.MOM.getPicture()],self.MOMName)
        self.text.text("It sure looks like nothing happened to you.")
            
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("I'll take care of it; end of story.")
            
        self.screen.updateScreen('',[self.SHN.getPicture()],self.SHNName)
        self.text.text("Don't make me have to go and kick someone's ass, I will if I have to.")
            
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Thanks for the offer but I'll deal with it; let's go home.")

        self.screen.updateScreen('',["charpic/PYRMind.png"],"Your Mind")
        self.text.text("We should get to the car, this will get worse if we continue like this.")

        self.screen.updateScreen('',[self.MOM.getPicture()],self.MOMName)
        self.text.text("Some days this kid kills me.")

        self.screen.updateScreen('',[self.SHN.getPicture()],self.SHNName)
        self.text.text("I know. I wonder what has gotten into him all of a sudden, he wasn't like this earlier right?")

        self.screen.updateScreen('',[self.MOM.getPicture()],self.MOMName)
        self.text.text("I don't know, something has changed inside him though.")

        self.screen.updateScreen('background/livingroomtv.png',["charpic/PYRMind.png"],"Your Mind")
        self.text.doubleText("You just go up to your room and try to go to bed,", "it will be better if we don't talk to them anymore today.")
        self.text.doubleText("You wonder if you are going to head back into the dream", "world oncemore and encounter that guy when you go to bed.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("What if what he said was right?")
        self.text.doubleText("It'd probably take a while for any symptoms to show," ,"but I'll have to get back my medication.")
        self.text.text("I'll deal with that problem tomorrow")

        self.screen.undrawScreen()

    def dayonefight(self):
        self.screen.drawScreen('background/Firstdreambackground.png',[self.PYR.getPicture()],self.PYRName)
        self.text.text("There's nothing around me.")
        self.text.text("There's something in the distance.")
        self.text.text("I wonder why I'm speaking out loud so much?")

        self.screen.updateScreen('',["charpic/PYRMind.png"],"???")
        self.text.text("I see you decided to betray me.")
        self.text.text("It took you long enough however.")
        self.text.text("No matter the outcome you either will kill me or I will kill you.")
        self.text.text("In both scenarios I will die.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("I mean I wouldn't want it to be this way though.")
        self.text.text("Who are you anyway?")

        self.screen.updateScreen('',["charpic/PYRMind.png"],"???")
        self.text.text("I'm you, but I'm essentially your shadow.")

        self.screen.updateScreen('',["charpic/PYRMind.png"],"My Shadow")
        self.text.text("I'm the innerworkings of your mind and will have to teach you a lesson then.")
        self.text.text("Let's get this over with. I'm tired of waiting.")
        self.text.text("If I'm going to die, I'm taking you with me.")
        
        self.screen.undrawScreen()
        self.PlayerParty = [self.PYR]
        
        self.SPYR = Char(self.win,'Shadow Me',"FighterIcon/PYRFighter.png", "charpic/PYRLeft.png",'No Right Pic', 'BattlePicture/SPYR.png', "Fightericon/Small/PYRFighter.png" )
        
        self.SPYR.loadWeapon(Weapon("Emotion", 90, 'Mind','None', [Special("AnxietyAttack", "BattleIcon/SpecialPictures/Mind/AnxietyAttack.png", "Damage", 80, 20, 'None')],'Mind', 'None', 'D'), 'D')
        self.SPYR.loadArmor(armor("Self-Esteem", 60, "Light Armor", "Mind", 'None'), 'D')
        
        self.EnemyParty = [self.SPYR]        

        for i in self.PlayerParty:
            i.reloadSP('max')

        for i in self.PlayerParty:
            i.reloadHealth('max')
            
        #w.PlaySound("Music/lastmanstanding.wav" ,w.SND_ASYNC)
        self.DBattle = Battle(self.win,self.PlayerParty,self.EnemyParty,"background/Firstdreambackground.png", "P", 'D', 'NF')
        outcome,var2 = self.DBattle.Fight()
        self.PYR.IncreaseEXP(var2)
        self.PYR.checkLevel()

        if outcome == 'Player':
            loadingscreen = Image(Point(640, 360), 'background/Loading.png')
            loadingscreen.draw(self.win)
            self.screen.drawScreen('background/Firstdreambackground.png',[self.PYR.getPicture()],self.PYRName)
            self.text.text("What happens now.")
            return 1
        
        else:
            loadingscreen = Image(Point(640, 360), 'background/Loading.png')
            loadingscreen.draw(self.win)
            self.screen.drawScreen('background/Firstdreambackground.png',[self.TDE.getPicture()],self.TDEName)
            self.text.doubleText("I was worried that this would happen. Don't worry" ,"I will take you to safety we'll figure this out tomorrow.")
            return 0

    def dreamland(self):
        self.screen.drawScreen('background/Firstdreambackground.png',["charpic/PYRMind.png"],"Your Mind")
        self.text.text("You begin to drift asleep....")
        self.text.text("...and wake up to see Thedore.")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.doubleText("Welcome back, I believe we'll have enough time to go over fighting" ,"here since you don't appear to be in the best shape to do it out there.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Well I was outnumbered, the odds weren't in my favor")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("What? Do you think that the world will treat you fair.")
        self.text.text("You are in for a surprise then.")
        self.text.text("Here there is one enemy, you; you aren't even fair to yourself.")
        self.text.doubleText("With an infinite amount of monsters to poison you and", "either turn you figurativly brain dead or literally.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("So... what are we going to do?")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Well, first we need a weapon and I think you can think of one.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("What about a sword?")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Well make it.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Well how the hell would that work")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Just imagine it, this is your mind afterall.")
        self.text.text("You can make just about anything you can think of.")
        self.text.text("All you need is the inspiration and the memory.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("What do you mean by memory?")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.doubleText("The more items and enemies you erase here turn" ,"into open memory that you can use.")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("So how do I make a weapon?")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("I can make it for you this time, next time you'll have to do it yourself.")
        self.text.text("Will I'm at it I'll also get you a suit of armor to seal the look.")
     
        self.PYR.loadWeapon(Weapon("Claymore Sword", 100, 'Slash','None', [Special("Charged Strike", "BattleIcon/SpecialPictures/Slash/ChargedStrike.png", "Damage", 120, 40, 'None'), Special("Battle Cry", "BattleIcon/SpecialPictures/Mind/BattleCry.png", "Heal", 50, 20,'Mind')],'Medievil', 'None', 'D'), 'D')
        self.PYR.loadArmor(armor("Chainmail Tunic", 70, "Light Armor", "Medevil", 'Metal'), 'D')

        self.screen.updateScreen('',["charpic/PYRMind.png"],"Your Mind") 
        self.text.text(self.PYRName +' now has a ' + 'Claymore Sword and a chainmail tunic' + ' to use in combat in the dream world.')
        self.text.text("You see someone that looks familair.")

        self.screen.updateScreen('',[self.DFM.getPicture()],"???")
        self.text.text("It didn't take long for us to meet again.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Something isn't right with how he looks.")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Well...fix it, try and think about how it looks like.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("I guess.")

        self.screen.updateScreen('',[self.FM.getPicture()],"???")
        self.text.text("It's time to take care of business I guess.")

        self.screen.updateScreen('',[self.JHT.getPicture()],"???")
        self.text.text("We will take care of business and knock you into an eternal sleep.")

        self.screen.updateScreen('',[self.FM.getPicture()],"???")
        self.text.text("We'll just kick his ass again and give him a rude awakening.")
        
        self.screen.updateScreen('',[self.JHT.getPicture()],"???")
        self.text.text("We'll haunt you out there and in your mind.")
        
        self.screen.updateScreen('',[self.JHT.getPicture(), self.FM.getPicture()],"??? & ???")
        self.text.text("There will be no escape.")
        self.text.text("We'll end him once and for all!")
        
        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Take them on here and then come to peace with yourself, this is what I was refering to.") 
        self.text.text("You must fight your demons in order for them to leave you alone.")
        self.text.text("Don't let them consume you and make them think that you are weak.")
        self.text.text("Find your inner strength and destroy any opposition that comes your way.") 

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Fine... let's do this.")

        self.PlayerParty = [self.PYR]

        for i in self.PlayerParty:
            i.reloadSP('max')
        
        self.EnemyParty = [self.JHT, self.FM]

        for i in self.PlayerParty:
            i.reloadHealth('max')

        for i in self.EnemyParty:
            i.reloadHealth('max')

        #w.PlaySound("Music/goodandevil.wav" ,w.SND_ASYNC)
        self.DBattle = Battle(self.win,self.PlayerParty,self.EnemyParty,"background/Firstdreambackground.png", "P", 'D', 'NF')
        wer,var2 = self.DBattle.Fight()
        self.PYR.IncreaseEXP(var2)
        self.PYR.checkLevel()

        if wer == 'Enemy':
            self.undrawScreen()
            return 3
        loadingscreen = Image(Point(640, 360), 'background/Loading.png')
        loadingscreen.draw(self.win)

        self.screen.updateScreen('background/Firstdreambackground.png',[self.TDE.getPicture()],self.TDEName)
        self.text.text("Great job, but there's more to overcome.") 
        self.text.text("Thankfully the virus hasn't taken root just yet and is young enough to kill now.")
        self.text.text("I know where you are.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        speech = self.screen.MakeChoice(["Aren't I right here?", "Is there another me?"],["Choices/arentirighthere.png","Choices/isthereanotherme.png"], self.PYRName)
        self.text.text(speech)

        self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
        self.text.text("I understand that you are confused, but you'll understand.") 
        self.text.text("I'm sure you have heard of you are your own worst enemy.")
        self.text.text("You are ultimately the one who is killing yourself and driving yourself to madness.")
        self.text.text("Your body is going to be putting tons of resources into combating the plague.") 
        self.text.text("You'll began to feel tired and exhausted.")
        self.text.text("This is further take a toll on you and feelings of hopelessness will beign to set in.")
        self.text.text("Look I will explain what we can do.") 
        self.text.text("We can go and take care of that plague and hopefully rid yourself of the dream plague forever.")
        self.text.text("Or we can return back another time and if you don't think you can handle it.")
        self.text.text("We may be able to use you to try and understand the dream plague a bit more.")
        self.text.text("However, I undertsand that your life is at stake.") 
        self.text.doubleText("I've seen how this ultimately affects people and", "wouldn't want you to go through the same ordeal.")
        self.text.text("The choice is yours, what do you want to do?.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        speech = self.screen.MakeChoice(["Let's do this.", "I don't think I'm ready yet."],["Choices/letsdothis.png","Choices/idontthinkimreadyyet.png"], self.PYRName)
        self.text.text(speech)

        if speech == "I don't think I'm ready yet.":
            self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
            self.text.text("It's fine we'll just hold off till later.") 
            self.text.text("We don't need to be in such a hurry. I'll help you return to normal sleep...")
            self.screen.undrawScreen()
            return 0

        elif speech == "Let's do this.":
            self.screen.updateScreen('',[self.TDE.getPicture()],self.TDEName)
            self.text.text("I'll take you over there.") 
            self.text.text("Here's some bandages.")
            self.PYR.addItem('R',Item("Bandage", "BattleIcon\ItemPicture\Bandage.png","Heal", 50))
            self.PYR.addItem('D',Item("Bandage", "BattleIcon\ItemPicture\Bandage.png","Heal", 50))
            self.text.text("Good luck in the fight, I'll be waiting for you.")
            self.screen.undrawScreen()
            return 1


    def wakeup(self):
        self.screen.drawScreen('background/bedroom.png',["charpic/PYRMind.png"],"Your Mind")
        self.text.text("Wake up you fool we have to get to school.")
        self.text.doubleText("You have to hurry up and meet your teachers"," and Connor is waiting for you.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.doubleText("I need to get this problem solved, I'll probably talk with Thedore", "tonight and see what his plans are for overcoming this.")

        self.screen.updateScreen('background/sidewalk.png',["charpic/PYRMind.png"],'Your Mind')
        self.text.text("You meet up with "+ self.CNRName+ " again and are walking to school.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.doubleText("I had that dream again Connor with the dude.", "Overall it said I had the dream plague and I had to defeat myself.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("That doesn't make any sense, what do you mean defeat yourself?")
        
        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("I have to fight another version of me and destory it before I am saved.")
        self.text.text("I wasn't ready to take me on, and now I'm here trying to solve it.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("You know you sound like you are speaking a lot of nonsense.")
        self.text.text("Those people must have hurt you really bad.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("How'd you know?")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("Your Mom told my Mom and she told me.")
        self.text.text("Don't worry too much about it she explained how it was 3 v 1.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("One of them didn't fight me.")

        self.screen.updateScreen('',[self.CNR.getPicture()],self.CNRName)
        self.text.text("Your Mom told my Mom and she told me.")
        self.text.text("Don't worry too much about it")
        self.text.doubleText("Let's go to the batting cages after school", "you said a couple times that you were interested in the team.")

        self.screen.updateScreen('',[self.PYR.getPicture()],self.PYRName)
        self.text.text("Fine, I guss.")



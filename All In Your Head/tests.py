from text import *
from graphics import *
from score import *
from player import *
from classesforPYR import *

class SchoolTests:
    def __init__(self,win,player):
        self.win = win
        self.PYR = player
        self.text = gameText(self.win) 
        self.mathBackground = Image(Point(640,360),"background/mathtestbackground.png")
        self.courses = Courses()

    def geometrytest(self):
        tScore = Score()
        tScore.resetScore()
        score = tScore.getScore()
        
        self.mathBackground.draw(self.win)
        total = int(10)
        self.text.text("The Algebra 1 test shall now begin.")
        gtestq1 = self.text.textQuestionNoPic("2x + 5 = 29. What must x equal for this equation to be true.", "1. x = 12" , "2. x = 17." , "3. x = -12" , "4. x = 48")
        if gtestq1 == 1:
           tScore.increaseScore()
        
        gtestq2 = self.text.textQuestionNoPic("Find the solutions of the following quadratic *Note ^ means exponet*. 5x^2 - 40x - 48 = 0", "1. x = -4 or x=-12" ," 2. x = 4 or x=12", "3. x = 4 or x = -12", "4. x = -4 or x = 12") 
        if gtestq2 == 4:
           tScore.increaseScore()
        
        gtestq3 = self.text.textQuestionNoPic("What is the slope of 2x + 3y = 17.", "1. m = 2/3", "2. m = -2/3", "3. m = 2", "4. m = -2")
        if gtestq3 == 2:
           tScore.increaseScore()
        
        gtestq4 = self.text.textQuestionNoPic("Expand *Note ^ means exponet* (x^3 + 2x^2 + 9x + 4)(x^4 - x^3 - 2x^2 + 10x - 12)","1. -x^7 + 3x^6 + 5x^5 - 27x^4 + 18x^3 + 74x^2 - 148x + 48","2. -x^7 - x^6 + 13x^5 - 11x^4 - 30x^3 + 106x^2 - 44x - 48","3. x^7 + x^6 + 5x^5 - 37x^4 - 54x^3 - 122x^2 - 148x - 48","4. -x^7 + 9x^6 + 7x^5 - 27x^4 - 180x^3 + 4x^2 - 18x + 48")
        if gtestq4 == 3:
            tScore.increaseScore()

        gtestq5 = self.text.textQuestionFourPic("Which graph is equivilant of y = |x|" , "1.","2.","3.","4.", 'testq/geotestque5opt1.png', 'testq/geotestque5opt2.png' ,"testq/geotestque5opt3.png","testq/geotestque5opt4.png")
        if gtestq5 == 2:
           tScore.increaseScore()
        
        gtestq6 = self.text.textQuestionNoPic("Solve the inequality, -15x - 7 >= -13x + 9","1. x <= 8","2. x < 8","3. x >= 8","4. x > 8")
        if gtestq6 == 1:
           tScore.increaseScore()
        
        gtestq7 = self.text.textQuestionFourPic("Which graph is prepresented by the graph 4x + 5 >= y","1.","2.","3.","4.","testq/geotestque7opt1.png","testq/geotestque7opt2.png.","testq/geotestque7opt3.png","testq/geotestque7opt4.png")
        if gtestq7 == 1:
           tScore.increaseScore()
        
        gtestq8 = self.text.textQuestionNoPic("What equation produces a horizontal line.","1. x = 5","2. x = y","3. 2x +5 = y","4. y = 5")
        if gtestq8 == 4:
           tScore.increaseScore()
           
        gtestq9 = self.text.textQuestionFourPic("Which graph is prepresented by the graph x = 2", "1.","2.","3.","4.","testq/geotestque9opt1.png","testq/geotestque9opt2.png","testq/geotestque9opt3.png","testq/geotestque9opt4.png")
        if gtestq9 == 3:
           tScore.increaseScore()
           
        gtestq10 = self.text.textQuestionNoPic("What is the slope of x=5","1. m = 0","2. m = Undefined","3. m = 5","4. m = 1/5")
        if gtestq10 == 2:
           tScore.increaseScore()
        
        score = tScore.getScore()

        if score < (total *.7):
            self.text.text('You failed')
            self.courses.setMathClass(1)

        if score >= (total *.7):
            self.text.text("Congrats you passed the Algebra Test.")
            self.text.text("You are now able to enter Geometry")
            self.courses.setMathClass(2)
            self.courses.completeMath(1)
            self.PYR.increaseIntelligence(1)

        self.mathBackground.undraw()
    
    def algebra2test(self):
        tScore = Score()
        tScore.resetScore()
        score = tScore.getScore()
        self.mathBackground.draw(self.win)
        total = 10
        if self.courses.getCompletedMathCourses(1) == 'Incomplete':
            self.text.text("You can't continue you will be placed in Algebra 1.")
            return
        
        self.text.text("The Geometry test shall now begin.")

        gtestq1 = self.text.textQuestionThreePic("Which triangles are similiar to each other.","1. ABC & NOP","2. WUD & NOP","3. WUD & ABC","4. All of them", "testq/agbtestque1op1.png","testq/agbtestque1op2.png","testq/agbtestque1op3.png")
        if gtestq1 == 1:
           tScore.increaseScore()

        gtestq2 = self.text.textQuestionOnePic("Find the measurement of angle x in degrees.","1. x = 20","2. x = 150","3. x = 160","4. x = 30","testq/agbtestque2op1.png")
        if gtestq2 == 3:
           tScore.increaseScore()

        gtestq3 = self.text.textQuestionThreePic("Which trinagles are congruent.","1. All of them ","2. ABC & LMP","3. DEF & LMP ","4. ABC & DEF","testq/agbtestque3op1.png","testq/agbtestque3op2.png","testq/agbtestque3op3.png")
        if gtestq3 == 4:
           tScore.increaseScore()

        gtestq4 = self.text.textQuestionOnePic("Solve for the missing leg","1. 612","2. 23.2379","3. 24.7386","4. 540","testq/agbtestque4opt1.png")
        if gtestq4 == 3:
           tScore.increaseScore()

        gtestq5 = self.text.textQuestionOnePic("Solve for the missing legs","1. 8.4853","2. 4.2426","3.8.342","4. 4.4521","testq/agbtestque5opt1.png")
        if gtestq5 == 2:
           tScore.increaseScore()

        gtestq6 = self.text.textQuestionOnePic("What is sin(x)","1. x = 3/4","2. x = 7/6","3. x = 7/8","4. x = 6/7","testq/agbtestque6opt1.png")
        if gtestq6 == 1:
           tScore.increaseScore()

        gtestq7 = self.text.textQuestionOnePic("Solve for side b using the law of sines","1. b = 4.95","2. b = 2.93","3. b = 4.52","4. b = 5.72","testq/agbtestque6opt1.png")
        if gtestq7 == 4:
            tScore.increaseScore()

        gtestq8 = self.text.textQuestionOnePic("Solve for side a by using the law of cosines.","1. a = 12.46","2. a = 10.34","3. a = 11.42","4. a = 24.11","testq/agbtestque8opt1.png")
        if gtestq8 == 3:
           tScore.increaseScore()

        gtestq9 = self.text.textQuestionOnePic("Find the measurement of angle A","1. A = 41.81","2. A = 48.19","3. A = 33.69","4. A = 31.00","testq/agbtestque9opt1.png")
        if gtestq9 == 1:
           tScore.increaseScore()
        
        gtestq10 = self.text.textQuestionTwoPic("The triangle ABC was reflected across the line x = 8, which image depicts this reflection.","1.","2.","3.","4.","testq/agbtestque10opt1.png","testq/agbtestque10opt2.png")
        if gtestq10 == 4:
           tScore.increaseScore()
        
        score = tScore.getScore()

        if score < (total *.7):
            self.text.text('You failed')

        if score >= (total *.7):
            self.text.text("Congrats you passed the Geometry Test.")
            self.text.text("You are now able to enter Algebra 2")
            self.courses.setMathClass(3)
            self.courses.completeMath(2)
            self.PYR.increaseIntelligence(2)

        self.mathBackground.undraw()
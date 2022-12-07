class Courses:
    def __init__(self):
        self.Math = int(0)
        self.MathCourseName = ''
        self.Algebra1 = 'Incomplete'
        self.Geometry = 'Incomplete'
        self.Algebra2 = 'Incomplete'

        self.English = int(0)
        self.EnglishCourseName = ''
        self.English1 = 'Incomplete'
        self.English2 = 'Incomplete'
        self.English3 = 'Incomplete'

    def completeMath(self,mathcourse):
        if mathcourse == 1:
            self.Algebra1 = 'Complete'

        if mathcourse == 2:
            self.Geometry = 'Complete'
        
        if mathcourse == 3:
            self.Algebra2 = 'Complete'

    def getCompletedMathCourses(self,mathcourse):
        if mathcourse == 1:
            return self.Algebra1

        if mathcourse == 2:
            return self.Geometry
        
        if mathcourse == 3:
            return self.Algebra2

    def setMathClass(self,mathcourse):
        self.Math = mathcourse        
        
        if self.Math == 1:
            self.MathCourseName = 'Algebra 1'

        if self.Math == 2:
            self.MathCourseName = 'Geometry'    
        
        if self.Math == 3:
            self.MathCourseName = 'Algebra 2'    
    
    def getMathCourse(self):
        return self.MathCourseName

    def completeEnglish(self,englishcourse):
        if englishcourse == 1:
            self.English1 = 'Complete'

        if englishcourse == 2:
            self.English2 = 'Complete'
        
        if englishcourse == 3:
            self.English3 = 'Complete'

    def setEnglishClass(self,englishcourse):
        self.English = englishcourse      
        
        if self.English == 1:
            self.EnglishCourseName = 'English 1'

        if self.English == 2:
            self.EnglishCourseName = 'English 2'    
        
        if self.English == 3:
            self.EnglishCourseName = 'English 3'    
    
    def getEnglishCourse(self):
        return self.EnglishCourseName

    def completeScience(self,englishcourse):
        if sciencecourse == 1:
            self.Science1 = 'Complete'

        if sciencecourse == 2:
            self.Science2 = 'Complete'
        
        if sciencecourse == 3:
            self.Science3 = 'Complete'

    def setScienceClass(self,sciencecourse):
        self.Science = sciencecourse      
        
        if self.Science == 1:
            self.ScienceCourseName = 'Earth Science'

        if self.Science == 2:
            self.ScienceCourseName = 'Biology'    
        
        if self.Science == 3:
            self.ScienceCourseName = 'Chemistry'    
    
    def getScienceCourse(self):
        return self.ScienceCourseName
    
    def completePE(self,pecourse):
        if pecourse == 1:
            self.PE1 = 'Complete'

        if pecourse == 2:
            self.PE2 = 'Complete'
        
        if pecourse == 3:
            self.PE3 = 'Complete'

    def setPEClass(self,pecourse):
        self.PE = pecourse      
        
        if self.PE == 1:
            self.PECourseName = 'Running Session'

        if self.PE == 2:
            self.PECourseName = 'WeightLifitng'    
        
        if self.PE == 3:
            self.PECourseName = 'Sports Games'    
    
    def getPECourse(self):
        return self.PECourseName
    
    def completeHistory(self,historycourse):
        if historycourse == 1:
            self.History1 = 'Complete'

        if historycourse == 2:
            self.History2 = 'Complete'
        
        if historycourse == 3:
            self.History3 = 'Complete'

    def setHistoryClass(self,historycourse):
        self.History = historycourse      
        
        if self.History == 1:
            self.HistoryCourseName = 'U.S. History'

        if self.History == 2:
            self.HistoryCourseName = 'European History'    
        
        if self.History == 3:
            self.HistoryCourseName = 'Asian History'    
    
    def getHistoryCourse(self):
        return self.HistoryCourseName
    
    def completeSpanLang(self,spanlangcourse):
        if spanlangcourse == 1:
            self.SpanLang1 = 'Complete'

        if spanlangcourse == 2:
            self.SpanLang2 = 'Complete'
        
        if spanlangcourse == 3:
            self.SpanLang3 = 'Complete'

    def setSpanLangClass(self,spanlangcourse):
        self.SpanLang = spanlangcourse      
        
        if self.SpanLang == 1:
            self.SpanLangCourseName = 'Spanish 1'

        if self.SpanLang == 2:
            self.SpanLangCourseName = 'Spanish 2'    
        
        if self.SpanLang == 3:
            self.SpanLangCourseName = 'Spanish 3'    
    
    def getSpanLangCourse(self):
        return self.SpanLangCourseName
    
    def completeCrafting(self,craftingcourse):
        if craftingcourse == 1:
            self.Crafting1 = 'Complete'

        if craftingcourse == 2:
            self.Crafting2 = 'Complete'
        
        if craftingcourse == 3:
            self.Crafting3 = 'Complete'

    def setCraftingClass(self,craftingcourse):
        self.Crafting = craftingcourse
        
        if self.Crafting == 1:
            self.CraftingCourseName = 'Sculputuring'

        if self.Crafting == 2:
            self.CraftingCourseName = 'Wood Shop'    
        
        if self.Crafting == 3:
            self.CraftingCourseName = 'Sewing'    
    
    def getCraftingCourse(self):
        return self.CraftingCourseName
    
    def completeFallElective1(self,fallelective1course):
        if fallelective1course == 1:
            self.FallElective11 = 'Complete'

        if fallelective1course == 2:
            self.FallElective12 = 'Complete'
        
        if fallelective1course == 3:
            self.FallElective13 = 'Complete'

    def setFallElective1Class(self,fallelective1course):
        self.FallElective1 = fallelective1course  
        
        if self.FallElective1 == 1:
            self.FallElective1CourseName = 'Sociology'

        if self.FallElective1 == 2:
          self.FallElective1CourseName = 'Study Hall' 

        else:
            self.FallElective1CourseName = 'Study Hall' 
            

    def getFallElective1Course(self):
        return self.FallElective1CourseName
    
    def completeFallElective2(self,fallelective2course):
        if fallelective2course == 1:
            self.FallElective21 = 'Complete'

        if fallelective2course == 2:
            self.FallElective22 = 'Complete'
        
        if fallelective2course == 3:
            self.FallElective23 = 'Complete'


    def setFallElective2Class(self,fallelective2course):
        self.FallElective2 = fallelective2course      
        
        if self.FallElective2 == 1:
            self.FallElective2CourseName = 'Engineering 1'

        if self.FallElective2 == 2:
            self.FallElective2CourseName = 'Thinking For Yourself'    
        
        if self.FallElective2 == 3:
            self.FallElective2CourseName = 'Study Hall'    
    
    def getFallElective2Course(self):
        return self.FallElective2CourseName
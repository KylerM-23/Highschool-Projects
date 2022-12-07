def showmajor(majorval):
	print("Here is the list of available majors. You must pick one, even if you don't know which major you're planning to go into.")

	place = 1

	for i in majorval:
		print(place, ". ", i)
		place = place+1
	
def learncoord():
	print("You will have to research what your coordinates are and then input them into the program eventually.") 
	
	print("")

	print("You'll get a North/South coordinate and a West/East Coordinate and we'll be using the decimal versions of them where we just put the numerical information, for example, 90.5 degrees would just be 90.5")
	
	print("")

	print("Finally North/West coordinates are postive and for South/East, the number will be negative, for example 92 degrees East is -92.")
  
	print("")

	donehelp = input("Do you understand this? (Yes or No)")
	donehelp = donehelp.lower()
        
	if donehelp == "no":
		print("Let's try this again...")
		
		print("")
		
		learncoord()

def learn():
	print("Now we are going to get your coordinates.")
	print("")
	help = input("Do you need to learn how coordinates work? (Yes or No)")
	help = help.lower()
	if help == "no":
		print("")
		print("Your wish...")

	else:
		learncoord()

def getinfo():
	try:
		majorval = ['History', 'Computer Science', 'Computer Engineering', 'Spanish', 'Economics', 'Anthropology','Physics','English', 'Cognitive Science', 'Art', 'Psychology', 'Philosophy','Mathematics', 'Applied Mathematics', 'Bioengineering', 'Biology', 'Chemistry', 'Earth Systems Science', 'Environmental Engineering', 'Global Arts', 'Management', 'Business Economics', 'Materials Science', 'Materials Engineering', 'Political Science', 'Public Health', 'Sociology', 'Civil Engineering','Italian','Japanese','Jewish Studies','Korean','Latin','Latin America Studies','Neuroscience','African American Studies','Chicano Studies','Classical Civilization','Climate Science','Communications','Comparative Literature','Computational systems','Earth Science','Environmental Science','Ecology','Electrical Engineering','Geology','Dance']

		Homestate = input("What's your home state two letter abrivation? ")
		Homestate = Homestate.upper() 
		Homestate = Homestate[0:2]
    
		print("")
		GPA1 = float(input("What is your GPA?"))

		print("")
		GPA2 = float(input("What is your GPA scale? Ex: 4, 4.5, 5"))

		GPA = (GPA1 * 5)/GPA2

		print("")
		SAT = float(input("What is your SAT scores?")) + 30

		learn()

		lat = float(input("What is your latitude (North or South)"))

		lon = float(input("What is your longitude (West or East)"))

		showmajor(majorval)

		majornum = int(input("What major are you wishing to pursue?"))
		if majornum < 1:
			raise ValueError("Naw Dawg")
		
		major = majorval[majornum-1]
		
		print("You have chosen ", major)

		return (Homestate, GPA, SAT, lat, lon, major)

	except:
		print("You have incorrectly entered info. For our safety reenter information.")
		return getinfo()


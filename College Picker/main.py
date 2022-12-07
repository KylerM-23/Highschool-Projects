
import college as c
import user as u
import info as i
import compare as cd

def rep(x):
	for i in range (x):
		input()

def main():
	CSUB = c.College("California State University Bakersfield (CSUB)", 3.2, 980,35.3517, 119.1041, 'CA',10000, 10000, ['History', 'Computer Engineering', 'Computer Science', 'Spanish', 'Economics', 'Anthropology', 'Physics', 'English', 'Art', 'Psychology', 'Philosophy','Communications','Political Science','Biology','Chemistry','Management','Electrical Engineering','Sociology','Geology','','','','','',''] )

	#Complete
	UCM = c.College("University of California, Merced (UCMerced)", 3.56, 1090, 37.3642, 120.4255, 'CA', 13208, 37916, ['History', 'Computer Engineering', 'Computer Science', 'Spanish', 'Anthropology', 'Physics', 'English', 'Cognitive Science', 'Psychology', 'Philosophy', 'Mathematics', 'Applied Mathematics', 'Bioengineering', 'Biology', 'Chemistry', 'Earth Systems Science', 'Environmental Engineering', 'Global Arts', 'Management', 'Business Economics', 'Materials Science', 'Materials Engineering', 'Political Science', 'Public Health', 'Sociology'])
	
	UCLA = c.College("University of California, Los Angeles (UCLA)", 4.31, 1370, 34.0689, 118.4452, 'CA', 12763, 37471, ['Economics', 'History', 'Anthropology', 'Physics', 'English', 'Cognitive Science', 'Art', 'Psychology', 'Philosophy', 'Mathematics', 'Biology', 'Chemistry', 'Business Economics', 'Political Science', 'Sociology', 'Chinese', 'French ', 'Italian', 'Japanese', 'Jewish Studies', 'Korean', 'Latin', 'Latin America Studies', '', 'Neuroscience', 'African American Studies', 'Chicano Studies', 'Classical Civilization', 'Climate Science', 'Communications', 'Comparative Literature', 'Computational systems', 'Earth Science', 'Environmental Science', 'Ecology', 'Geology', ''])
	
	UCB = c.College("University of California, Berekely (UCBerekely)", 3.87, 1440, 37.8719, 122.2585, 'CA', 13431, 38139,['Economics', 'History', 'Computer Science', 'Spanish', 'Anthropology', 'Physics', 'English', 'Cognitive Science', 'Art', 'Psychology', 'Philosophy', 'Mathematics', 'Italian', 'Mathematics', 'Jewish Studies', 'Latin America Studies', 'Neuroscience', 'African American Studies','Chicano Studies','Communications','Comparative Literature','Civil Engineering','Electrical Engineering','Dance','Political Science','Biology','Mechanical Engineering','Chemistry','Chinese','Environmental Engineering','French','Management','Public Health','Sociology','Earth Science','','','','','','',''])
	
	UCI = c.College("University of California, Irvine (UCIrvine)", 3.94, 1250, 33.6405, 117.8443, 'CA', 13252, 37960, ['Anthropology', 'Computer Engineering', 'Computer Science', 'Economics', 'Physics', 'English', 'Cognitive Science', 'Art', 'Psychology', 'Philosophy', 'Japanese', 'Mathematics', 'Korean', 'African American Studies', 'Chicano Studies', 'Comparative Literature','Computational Systems','Civil Engineering','Dance','Biology','Political Science','Mechanical Engineering','Chemistry','Environmental Engineering','French','Management','Materials Science','Materials Engineering','Electrical Engineering','Public Health','Sociology','Earth Science','Environmental Science', 'Ecology'])
	
	UCR = c.College("University of California, Riverside (UCRiverside)", 3.69, 1190, 33.9737, 117.3281, 'CA', 13527, 38676, ['Computer Engineering', 'Computer Science', 'Anthropology', 'Art', 'Economics', 'English', 'Spanish', 'History', 'Physics', 'Psychology', 'Philosophy', 'Italian', 'Mathematics', 'Japanese', 'Korean', 'Latin America Studies', 'Neuroscience', 'African American Studies', 'Chicano Studies','Climate Science','Comparative Literature','Classical Civilization', 'Electrical Engineering', 'Geology', 'Political Science','Bioengineering','Chemistry','Mechanical Engineering','Environmental Engineering','Chinese','French','Business Economics','Materials Science','Materials Engineering','Sociology','Earth Science','Environmental Science', 'Dance'])

	UCSB= c.College("University of California, Santa Barbara (UCSantaBarbara)", 4.02, 1220, 34.4140, 119.8489, 'CA', 13968, 38676, ['Economics', 'English', 'Art', 'Computer Science', 'Computer Engineering', 'Physics', 'History', 'Philosophy', 'Italian', 'Mathematics', 'Jewish Studies', 'Latin America Studies', 'Chicano Studies', 'Comparative Literature', 'Communications', 'Electrical Engineering', 'Dance', 'Biology', 'Political Science','Mechanical Engineering','Chemistry','French','Management','Sociology','Earth Science','Ecology','','','','','','','',''])
	
	UCD = c.College("University of California, Davis (UCDavis)", 4.0, 1290, 38.5382, 121.7617, 'CA', 13951, 38359, ['Anthropoloy', 'Art', 'Computer Science', 'Computer Engineering', 'English', 'History', 'Economics', 'Physics', 'Psycology', 'Spanish', 'Cognitive Science', 'Philosophy', 'Italian', 'Japanese', 'Mathematics', 'Chicano Studies', 'Classical Civilization', 'Comparative Literature', 'Civil Engineering', 'Electrical Engineering','','Geology','Applied Mathmatics','Political Science','Biology','Chemistry','Mechanical Engineering','Chinese','French','Management','Materials Science','Materials Engineering','Sociology','Ecology','',''] )
	
	CalStateFresno = c.College("California State University, Fresno (CalStateFresno)", 3.07, 990, 36.8124, 119.7458, 'CA', 6311, 17471, ['Anthropoloy', 'Art', 'Cognitive Science', 'Computer Science', 'History', 'English', 'Computer Engineering', 'Philosophy', 'Psycology', 'Spanish', 'Mathematics', 'Latin America Studies', 'Chicano Studies', 'Electrical Engineering', 'Civil Engineering', 'Mechanical Engineering','Chemistry','French','Management','Sociology','Environmental Science', 'Geology'])
	
	CalStateLA = c.College("California State University, Los Angeles (CalStateLA)", 3.21, 980, 34.0668, 118.1671, 'CA', 6355, 17515, ['Anthropology', 'Art', 'Computer Science', 'Economics', 'English', 'History', 'Philosophy', 'Physics', 'Psychology', 'Spanish', 'Japanese', 'Mathematics', 'Latin America Studies', 'African American Studies', 'Civil Engineering','Geology','Dance','Political Science','Biology','Mechanical Engineering','Electrical Engineering','Chemistry','Chinese','French','Public Health','Sociology', 'Chicano Studies'])
	
	Standford = c.College("Standford University (StandfordUniversity)", 3.95, 1520, 37.4275, 122.1697, 'CA', 46320, 46320, ['Physics', 'Spanish', 'History', 'Economics', 'Computer Science', 'Anthropology', 'English', 'Art', 'Psychology', 'Philosophy', 'Italian', 'Mathematics', 'Japanese', 'Jewish Studies', 'Korean', 'Latin America Studies','Chicano Studies','Comparative Literature','Computational Systems','Electrical Engineering','Dance','Biology','Political Science','Mechanical Engineering','Chinese','Environmental Engineering','French','Management','Materials Science','Sociology','','','','','','','','','','','','','','',''])
	
	Harvard = c.College("Harvard University (HarvardUniversity)", 4.1, 1540, 42.3770, 71.1167, 'CA', 45278, 45278, ['Anthropology', 'Computer Science', 'Economics', 'English', 'History', 'Art', 'Psycology', 'Physics','Philosophy', 'African American Studies', 'Comparative Literature', 'Mathematics', 'Dance', 'Applied Mathmatics', 'Biology', 'Chemistry','Mechanical Engineering','Electrical Engineerning','Sociology','Environmental Science','','','','','','',''] )
	
	CalPolySLO = c.College("California Polytechnic State University San Luis Obispo (CalPolySLO)", 3.92, 1300, 35.3050, 120.6625, 'CA', 9001, 20161, ['Computer Science', 'Computer Engineering', 'Art', 'English', 'History', 'Philosophy', 'Psychology', 'Physics', 'Electrical Engineering', 'Mathematics', 'Dance', 'Political Science', 'Mechanical Engineering','Chemistry','Environmental Engineering','Management','Materials Engineering','Public Health','','','','',''])
	
	BC = c.College("Bakersfield College (BC)", 0,0, 35.4079, 118.9718, 'CA', 1326, 8102, ['Art', 'Anthropology', 'Economics', 'English', 'History', 'Philosophy', 'Psychology', 'Spanish', 'Computer Science', 'Mathmatics', 'Physics', 'Communications','Political Science','Biology','Chemistry','Management','Sociology','Earth Science','Geology','','','','','' ])
	
	CalPolyPomona = c.College("Cal Poly Pomona (CalPolyPomona)", 3.49, 1130, 34.0576, 117.8207, 'CA', 7016, 18176, ['Art', 'Computer Science', 'Economics', 'Computer Engineering', 'English', 'Spanish', 'History', 'Philosophy', 'Physics', 'Psychology', 'Civil Engineering', 'Communications', 'Anthropology', 'Mathmatics', 'Political Science','Biology','Chemistry','Mechanical Engineering','French','Electrical Engineering','Management','Materials Engineering','Sociology','','','','','','','Chinese'])
	
	CalStateNorthridge = c.College("California State University, Northridge (CalStateNorthridge)", 3.18, 990, 34.2410, 118.5277, 'CA', 6569, 17729, ['Anthropology', 'Art', 'Computer Science', 'Economics', 'English', 'History', 'Philosophy', 'Physics', 'Computer Engineering', 'Psychology', 'Spanish', 'Chicano Studies', 'Civil Engineerning', 'Italian', 'Japanese', 'Mathmatics', 'Jewish Studies', 'Geology', 'Electrical Engineering', 'Biology','Political Science','Mechanical Engineering','Applied Mathematics','Chemistry','French','Management','Materials Engineering','Public Health','Sociology','Ecology', 'Dance'])
	
	AzusaPacificUniversity = c.College("Azusa Pacific University (Azusa Pacific University)", 3.68, 1130, 34.1301, 117.8884, 'CA', 34754, 34754, ['Art', 'English', 'Psychology', 'Computer Science', 'Physics', 'Spanish', 'Economics', 'History', 'Mathmatics', 'Applied Mathmatics','Political Science','Biology','Chemistry','Sociology','','','','','','',''] )
	
	Fullerton = c.College("Fullerton (Fullerton)", 3.48, 1020, 33.8704, 117.9242, 'CA', 6437, 17597, ['Art', 'Anthropology', 'Computer Science', 'Economics', 'Computer Engineering', 'English', 'History', 'Philosophy', 'Physics', 'Psychology', 'Spanish', 'Civil Engineering', 'Biology', 'Communications', 'Comparative Literature', 'Chicano Studies', 'Electrical Engineering', 'Geology', 'Japanese', 'Latin American Studies' ,'Political Science','Chemistry','French','Public Health','Sociology','Earth Science','Ecology','','','','','','','','','',''])

	CSUSacramento = c.College("California State University, Sacramento (CSUSacramento)", 3.27, 1020, 38.5613, 121.4241, 'CA', 6872, 18032, ['Art', 'English', 'History', 'Philosophy', 'Computer Engineering', 'Computer Science', 'Physics', 'Anthropology', 'Economics', 'Psychology', 'Civil Engineering', 'Mathmatics','Mechanical Engineering','Chemistry','Management','Electrical Engineering','Sociology','Geology','Dance','','','','','','','','','','','','','','','','','',''])
	
	CSULongBeach = c.College("California State University, Long Beach (CSULongBeach)", 3.54, 1060, 33.7701, 118.1937, 'CA', 6452, 17612, ['Anthropology', 'Art', 'Economics', 'English', 'History', 'Philosophy', 'Psychology', 'Spanish', 'Computer Science', 'Physics', 'Psychology', 'Civil Engineering', 'Electrical Engineering','Biology','Political Science','Mechanical Engineering','Chemistry','French','Management','Biology','Public Health','Sociology','Italian', 'Geology', 'Dance'] )
	
	UCSantaCruz = c.College("University of California, Santa Cruz (UCSantaCruz)", 3.76, 1260, 36.9916, 122.0583, 'CA', 13461, 38169, ['Physics', 'Computer Science', 'Spanish', 'Psychology', 'Philosophy', 'History', 'Economics', 'Cognitive Science', 'Art', 'Anthropology','Computer Engineering','Electrical Engineering', 'Mathmatics', 'Political Science', 'Bioengineering', 'Biology', 'Chemistry','Sociology','Latin','Neuroscience', 'Chicano Studies', 'Earth Science', 'Environmental Science', 'Ecology', 'Geology'])
	
	OklahomaStateUniversity = c.College("Oklahoma State University (OklahomaStateUniversity)", 3.52, 1190, 36.1270, 87.5391, 'OK', 10170, 25950, ['Spanish', 'Anthropology', 'English', 'Psychology', 'Physics', 'Philosophy', 'History', 'English', 'Economics', 'Computer Science', 'Computer Engineering', 'Art', 'Civil Engineering', 'Electrical Engineering', 'Mathmatics', 'Ecology','Political Science','Biology','Chemistry','Mechanical Engineering','French','Management','Public Health','Sociology', 'Environmental Science', 'Geology'])
	
	UCSanDiego = c.College("University of California, San Diego (UCSanDiego)", 4.0, 1350, 32.8801, 117.2340, 'CA', 13530, 38238, ['Anthropology', 'Art', 'Cognitive Science', 'Computer Engineering', 'Computer Science', 'Economics', 'English', 'History', 'Philosophy', 'Physics', 'Psychology', 'Civil Engineering', 'Electrical Engineering', 'Ethnic Sudies', 'Mathmatics','Political Science','Bioengineering','Biology','Mechanical Engineering','Chemistry','Chinese','Environmental Engineering','Management','Public Health','Comparative Literature','Sociology','Italian','Japanese','Comparative Literature','Jewish Studies', 'Latin American Studies', 'Neuroscience', 'Earth Science', 'Ecology', 'Dance'] )
	
	UniversityOfOregon = c.College("University of Oregon (UniversityOfOregon)", 3.61, 1190, 44.0448, 123.0726, 'OR', 10287, 32022, ['Art', 'Anthropology', 'Economics', 'English', 'History', 'Philosophy', 'Physics', 'Psychology', 'Spanish', 'Computer Science','Mathematics','Political Science','Biology','Chemistry','Chinese','French','Management','Sociology','Italian','Japanese', 'Latin American Studies', 'Comparative Literature', 'Earth Science', 'Environmental Science'])
	
	GeorgeFoxUniversity = c.College("George Fox University (George Fox University)", 3.56, 1150, 45.3034, 122.9667, 'OR', 32786, 32786, ['Art', 'Cognitive Science', 'Computer Engineering', 'Computer Science', 'Economics', 'History', 'Philosophy', 'Psychology', 'Spanish', 'Civil Engineering', 'Mathmatics', 'Biology','Mechanical Engineering','Political Science','Chemistry','Management','Electrical Engineering','Sociology','Ecology','','','','','','','',''])
	
	UniversityOfHawaiiAtHilo = c.College("University of Hawaii at Hilo (University of Hawaii at Hilo)", 3.36, 1020, 19.7010, 155.0815, 'HI', 7332, 19788, ['Art', 'Anthropology', 'Economics', 'English', 'History', 'Philosophy', 'Psychology', 'Computer Science', 'Physics','Political Science','Biology','Mathematics','','','','','','',''])
	
	SyracuseUniversity = c.College("Syracuse University (Syracuse University)", 3.6, 1270, 43.0392, 76.1351, 'NY', 43318, 43318, ['Anthropology', 'Cognitive Science', 'Economics', 'English', 'History', 'Philospohy', 'Physics', 'Psychology', 'Spanish', 'Political Science', 'Biology', 'Chemistry','Chinese','French','Sociology','Italian','Japanese','Jewish Studies','Latin','Latin American Studies','Neuroscience','African American Studies','Classical Civilization', 'Earth Science'])
	
	WhittierCollege = c.College("Whittier College (Whittier College)", 3.51, 1130, 33.9787, 118.0323, 'CA', 43280, 43280, ['Anthropology', 'Art', 'Economics', 'Computer Science', 'English', 'History', 'Philosophy', 'Physics', 'Spanish', 'Mathematics','Political Science','Biology','Chemistry','Chinese','French','Management','Business Economics','Sociology','Environmental Science'])
	
	SanDiegoState = c.College("San Diego State (San Diego State)", 3.7, 1110, 32.7757, 117.0719, 'CA', 6976, 18136, ['Art', 'Computer Engineering', 'Computer Science', 'Economics', 'English', 'History', 'Philosophy', 'Physics', 'Psychology', 'Spanish', 'Anthropology', 'Dance', 'Applied Mathmatics','Political Science','Biology','Mechanical Engineering','Chemistry','Environmental Engineering','French','Electrical Engineering','Management','Public Health','Sociology','Japanese','Jewish Studies','Latin American Studies', 'Chicano Studies', 'Comparative Literature', 'Environmental Science'] )

	Schools = [CSUB, UCM, UCLA, UCB, UCI, UCR, UCSB, UCD,CalStateFresno, CalStateLA, Standford, Harvard, CalPolySLO, BC, CalPolyPomona, CalStateNorthridge,AzusaPacificUniversity , Fullerton, CSUSacramento, CSULongBeach, UCSantaCruz, OklahomaStateUniversity, UCSanDiego, UniversityOfOregon, GeorgeFoxUniversity, UniversityOfHawaiiAtHilo, SyracuseUniversity, WhittierCollege, SanDiegoState]

	print("Welcome to the college picker program thing. So let's get this over with and figure out some schools you may want to apply to.")
	print("This doesn't mean you will get into the college but may be a good fit since there are many factors that determine admission.")

	print('')
	Homestate, GPA, SAT, lat, lon, major = i.getinfo()
	user = u.User(Homestate, GPA, SAT, lat, lon, major)

	Schools = cd.compareState(user,Schools)

	Schools = cd.compareGPA(user,Schools)

	Schools = cd.compareSAT(user,Schools)

	Schools = cd.compareTUT(user, Schools)

	Schools = cd.compareMajor(user,Schools)

	Schools = cd.compareDistance(user,Schools)

	if Schools == []:
		print("Sorry you aren't getting into college with the parameters we used and the available schools.")
		rep(1)
		print("Ana stop being all mad and hitting buttons, or whoever else decided to do this.")
		rep(2)
		print("Go home or something. The program is done.")
		rep(5)
		print("Why are you doing this to me?")
		rep(10)
		print("Fine fine... You win. I'm just messing around, I don't know what you are getting out of this. What joy comes out of this.")
		rep(20)
		print("Well I hope you enjoyed this, but I'm just going to stop this now because you are just going to do this forever, and I frankly have other important things to do like... um... totally doing work. Well good day.")
	
	else:
		print("Here are the schools that best fit your options.")
		print("")
	

		for w in Schools:
			print(w.getName())
			#print(w)

		rep(1)
		print("What are you doing? I thought you were already happy with seeing your results? You at least got one school, I'm for sure.")
		rep(2)
		print("Go home or something. The program is done.")
		rep(5)
		print("Why are you doing this to me?")
		rep(10)
		print("Fine fine... You win. I'm just messing around, I don't know what you are getting out of this. What joy comes out of this.")
		rep(20)
		print("Well I hope you enjoyed this, but I'm just going to stop this now because you are just going to do this forever, and I frankly have other important things to do like... um... totally doing work. Well good day.")

main()


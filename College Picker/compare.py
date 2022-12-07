import distance as d

def compareState(user, Schools):
	Homestate = user.getState()
	Options = []

	statec = input("Do you need to go to a school in your home state? (Yes or No)")

	statec = statec.lower()

	if statec == 'yes':
		for i in Schools:
			if i.getState() == Homestate:
				Options.append(i)
		
		return Options

	else:
		return Schools

def compareGPA(user, Schools):
	GPA = user.getGPA()
	Options = []
	
	for i in Schools:
		if i.getGPA() <= GPA:
			Options.append(i)
	
	return Options

def compareSAT(user, Schools):
	SAT = user.getSAT()
	Options = []
	for i in Schools:
		if i.getSAT() <= SAT:
			Options.append(i)
	
	return Options

def getTUT():
	try:
		TUT1 = float(input("What is the lowest tuition range?"))
		TUT2 = float(input("What is the highest tuition range?"))
		return TUT1, TUT2
	except:
		TUT1 = 'no'
		TUT2 = 'no'
		return TUT1, TUT2

def compareTUT(user, Schools):
	print("Now we are going to find the tuition range you are looking for?")
	print("If cost doesn't matter to you type letters :)")
	TUT1,TUT2 = getTUT()
	Options = []
	
	if TUT1 == 'no' or TUT2 == 'no':
		return Schools

	else:
		for i in Schools:
			if i.getState() == user.getState():
				Tut = i.getStateTUT()

				if  Tut<= TUT2 and TUT1<= Tut:
					Options.append(i)

			else:
				Tut = i.getOutTUT()
			
				if  (Tut<= TUT2 and TUT1<= Tut):
					Options.append(i)

		return Options
		

def compareMajor(user, Schools):
	major = user.getMajor()
	Options = []
	for i in Schools:
		for w in i.getMajor():
			if w == major:
				Options.append(i)

	return Options

def getdistance():
	try:
		print("Now we are going to get the maximum distance that you want ot be from your college.")
		x = float(input("How many miles do you want to be away from home. Type words if you don't care."))
		return x
	except:
		return 'No'

def compareDistance(user,Schools):
	x = getdistance()

	Options = []

	t1 = user.getLat()
	l1 = user.getLon()
	if x == 'No':
		return Schools
	else:
		for i in Schools:
			t2 = i.getLat()
			l2 = i.getLon()
			dis = d.calcdis(t1,t2,l1,l2)
			
			if dis <= x:
				Options.append(i)

		return Options

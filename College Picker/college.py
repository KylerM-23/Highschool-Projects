class College:
	def __init__(self,Name, GPA, SAT, LAT, LON, STATE, INTUT, OUTTUT, Major):
		self.Name = Name
		self.GPA = GPA
		self.SAT = SAT
		self.LAT = LAT
		self.LON = LON
		self.STATE = STATE
		self.INTUT = INTUT
		self.OUTTUT = OUTTUT
		self.Major = Major

	def getState(self):
		return self.STATE

	def getGPA(self):
		return self.GPA

	def getSAT(self):
		return self.SAT

	def getMajor(self):
		return self.Major

	def getLat(self):
		return self.LAT

	def getLon(self):
		return self.LON

	def getName(self):
		return self.Name

	def getStateTUT(self):
		return self.INTUT

	def getOutTUT(self):
		return self.OUTTUT


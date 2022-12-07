class User:
	def __init__(self, Homestate, GPA, SAT, lat, lon, major):
		self.Homestate = Homestate
		self.GPA = GPA
		self.SAT = SAT
		self.lat = lat
		self.lon = lon
		self.major = major

	def getState(self):
		return self.Homestate

	def getGPA(self):
		return self.GPA

	def getSAT(self):
		return self.SAT

	def getMajor(self):
		return self.major

	def getLat(self):
		return self.lat

	def getLon(self):
		return self.lon

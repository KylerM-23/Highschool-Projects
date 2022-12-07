class Score:
    def __intit__(self):
        self.score = int(0)
    
    def resetScore(self):
        self.score = int(0)

    def increaseScore(self):
        self.score = self.score + int(1)
    
    def getScore(self):
        return self.score
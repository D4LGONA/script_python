class Player:
    UPPER = 6 # upper category 6개
    LOWER = 7 # lower category 7개
    def __init__(self, name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER+self.LOWER)] #13개 category점수
        #13개 category 사용여부
        self.used = [False for i in range(self.UPPER+self.LOWER)]

    def setScore(self, score, index):
        self.scores[index] = score

    def setAtUsed(self, index):
        # used를 true로 만드는 것
        self.used[index] = True

    def getUpperScore(self):
        # 상단 6개 점수 합계
        score = 0
        if self.allUpperUsed():
            for i in range(Player.UPPER):
                score += self.scores[i]
        return score

    def getLowerScore(self):
        # 하단 7개 점수 합계
        score = 0
        if self.allLowerUsed():
            for i in range(Player.LOWER):
                score += self.scores[i]
        return score

    def getUsed(self):
        return self.used

    def getTotalScore(self):
        if self.allLowerUsed() and self.allUpperUsed():
            return self.getLowerScore() + self.getUpperScore()

    def toString(self):
        return self.name

    def allLowerUsed(self): #lower category 7개 모두 사용되었는가 ?
        for i in range(self.LOWER):
            if self.used[i] == False:
                return False
        return True

    def allUpperUsed(self): #upper category 6개 모두 사용되었는가 ?
        #UpperScores, UpperBonus 계산에 활용
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True

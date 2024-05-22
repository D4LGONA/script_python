class Player:
    UPPER = 6
    LOWER = 7
    def __init__(self, name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER + self.LOWER)] # 점수판
        self.used = [False for i in range(self.UPPER + self.LOWER)] # 사용 여부

    def setScore(self, score, index):
        self.scores[index] = score # index 카테고리의 점수 score를 기입

    def getUpperScore(self): # 6개 카테고리 점수 합
        sum = 0
        for i in range(self.UPPER):
            sum += self.scores[i]
        self.upperScore = sum
        return self.upperScore

    def getLowerScore(self): # 7개 카테고리 점수 합
        sum = 0
        for i in range(self.LOWER):
            sum += self.scores[self.UPPER + i]
        self.lowerScore = sum
        return self.lowerScore

    def getUsed(self):
        return self.used

    def getTotalScore(self):
        if self.upperScore > 63:
            self.totalScore = self.upperScore + self.lowerScore + 35 # 보너스 점수
        else:
            self.totalScore = self.upperScore + self.lowerScore
        return self.totalScore

    def allUpperUsed(self): # 상단 6개 카테고리가 모두 사용되었나?
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True

    def allLowerUsed(self): # 상단 6개 카테고리가 모두 사용되었나?
        for i in range(self.LOWER):
            if self.used[i + self.UPPER] == False:
                return False
        return True

    def setAtUsed(self, index):
        self.used[index] = True
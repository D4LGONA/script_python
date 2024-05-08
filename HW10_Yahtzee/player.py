class Player:
    UPPER = 6 # upper category 6개
    LOWER = 7 # lower category 7개
    def __init__(self, name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER+self.LOWER)] #13개 category점수
        #13개 category 사용여부
        self.used = [False for i in range(self.UPPER+self.LOWER)]

    def setScore(self, score, index):
        # 각각의 카테고리별로 점수가 적절하면 적는거? 뭔소리야
        pass

    def setAtUsed(self, index):
        # used를 true로 만드는 것
        self.used[index] = True

    def getUpperScore(self):
        # 상단 6개 점수 합계
        score = 0
        for i in range(Player.UPPER):
            if self.used[i]:
                score += self.scores[i]
        return score

    def getLowerScore(self):
        # 하단 7개 점수 합계
        score = 0
        for i in range(Player.UPPER):
            if self.used[i]:
                score += self.scores[i]
        return score

    def getUsed(self):
        pass

    def getTotalScore(self):
        pass

    def toString(self):
        return self.name

    def allLowerUsed(self): #lower category 7개 모두 사용되었는가 ?
        pass

    def allUpperUsed(self): #upper category 6개 모두 사용되었는가 ?
        #UpperScores, UpperBonus 계산에 활용
        for i in range(self.UPPER):
            if (self.used[i] == False):
                return False
        return True
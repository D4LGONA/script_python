class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self): # a는 11로 계산후 21이 넘으면 1로 수정
        sum = 0
        acecnt = 0
        for i in self.cards:
            if i.getValue() == 1:
                acecnt += 1
                sum += 10
            sum += i.getValue()
        for i in range(acecnt):
            if sum > 21:
                sum -= 10
            else: break
        return sum

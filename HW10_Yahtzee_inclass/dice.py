import random

class Dice:
    def rollDie(self): # 주사위 굴리기
        self.roll = random.randint(1, 6)# [1, 6] 정수

    def getRoll(self):
        return self.roll
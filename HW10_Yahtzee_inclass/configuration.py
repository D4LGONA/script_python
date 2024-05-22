from dice import *


class Configuration:
    configs = ['Category', 'Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes',
               'Upper Scores', 'Upper Bonus(35)', 'Three of a kind', 'Four of a kind',
               'Full House(25)', 'Small Straight(30)', 'Large Straight(40)', 'Yathzee(50)', 'Chance']

    def getConfigs():  # 클래스 메소드, 객체생성없이 클래스를 이용해서 호출
        return Configuration.configs

    def score(row, d):
        if 0 <= row <= 5:  # 상단 6개 카테고리라면
            return Configuration.scoreUpper(d, row + 1)
        elif row == 8:
            return Configuration.scoreThreeOfAKind(d)
        elif row == 9:
            return Configuration.scoreFourOfAKind(d)
        elif row == 10:
            return Configuration.scoreFullHouse(d)
        elif row == 11:
            return Configuration.scoreSmallStraight(d)
        elif row == 12:
            return Configuration.scoreLargeStraight(d)
        elif row == 13:
            return Configuration.scoreYahtzee(d)
        elif row == 14:  # chance
            return Configuration.sumDie(d)
        else:
            return -1

    def scoreThreeOfAKind(self):
        pass

    def scoreUpper(d, num):
        sum = 0
        for i in range(5):
            if d[i].getRoll() == num:
                sum += num
        return sum

    @classmethod
    def scoreFullHouse(cls, d):
        pass

    @classmethod
    def scoreFourOfAKind(cls, d):
        pass

    @classmethod
    def scoreSmallStraight(cls, d):
        pass

    @classmethod
    def scoreLargeStraight(cls, d):
        pass

    @classmethod
    def scoreYahtzee(cls, d):
        for i in range(4):
            if d[i].getRoll() != d[i+1].getRoll():
                return 0
        return 50

    @classmethod
    def sumDie(cls, d):
        sum = 0
        for i in range(5):
            sum += d[i].getRoll()
        return sum

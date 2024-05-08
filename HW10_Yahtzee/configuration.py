from dice import *
class Configuration:
    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
    "Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)",
    "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]
    @staticmethod
    def getConfigs(): # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs

    def score(row, d): # 정적 메소드: 객체생성 없이 사용 가능
    #row에 따라 주사위 점수를 계산 반환. 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
    # 의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지
    # 않아야 하는 버튼 (즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우
    # -1을 반환합니다.
        if (row>=0 and row<=6):
            return Configuration.scoreUpper(d, row+1)
        elif (row==8): # 3oak
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row==10): # fh
            return Configuration.scoreFullHouse(d)
        elif (row == 11): # ss
            return Configuration.scoreSmallStraight(d)
        elif (row == 12): # ls
            return Configuration.scoreLargeStraight(d)
        elif (row == 13): #yz
            return Configuration.scoreYahtzee(d)
        elif (row == 14): #ch
            return Configuration.sumDie(d)

    def scoreUpper(d, num):  # 정적 메소드: 객체생성 없이 사용 가능
        # Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
        # num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.
        score = 0
        for i in d:
            if i.getRoll() == num:
                score += i.getRoll()
        return score

    def scoreThreeOfAKind(d):
        score = 0
        counts = [0] * 6  # 주사위 값이 1부터 6까지이므로 길이 6의 배열을 만듭니다.
        for die in d:
            counts[die.getRoll() - 1] += 1  # 주사위 값이 1부터 시작하므로 1을 뺍니다.
        for i, count in enumerate(counts):
            if count >= 3:  # 3개 이상의 동일한 숫자를 찾았다면
                score = sum(die.getRoll() for die in d)  # 주사위 값의 총합을 계산합니다.
                break  # 루프를 종료합니다.
        return score


    def scoreFourOfAKind(d):
        score = 0
        counts = [0] * 6  # 주사위 값이 1부터 6까지이므로 길이 6의 배열을 만듭니다.
        for die in d:
            counts[die.getRoll() - 1] += 1  # 주사위 값이 1부터 시작하므로 1을 뺍니다.
        for i, count in enumerate(counts):
            if count >= 4:  # 3개 이상의 동일한 숫자를 찾았다면
                score = sum(die.getRoll() for die in d)  # 주사위 값의 총합을 계산합니다.
                break  # 루프를 종료합니다.
        return score

    def scoreFullHouse(d):
        score = 0
        counts = [0] * 6  # 주사위 값이 1부터 6까지이므로 길이 6의 배열을 만듭니다.
        for die in d:
            counts[die.getRoll() - 1] += 1  # 주사위 값이 1부터 시작하므로 1을 뺍니다.
        three_of_a_kind = False
        two_of_a_kind = False
        for count in counts:
            if count >= 3:
                three_of_a_kind = True
            elif count >= 2:
                two_of_a_kind = True
        if three_of_a_kind and two_of_a_kind:
            score = 25  # Full House의 점수는 보통 25점입니다.

        return score

    def scoreSmallStraight(d):
        score = 0
        dice_values = sorted(set([die.getRoll() for die in d]))  # 주사위 값의 중복을 제거하고 정렬합니다.
        if len(dice_values) >= 4:  # 주사위 값이 4개 이상 있어야 Small Straight이 가능합니다.
            if [1, 2, 3, 4] in [dice_values[i:i + 4] for i in range(len(dice_values) - 3)] or \
                    [2, 3, 4, 5] in [dice_values[i:i + 4] for i in range(len(dice_values) - 3)] or \
                    [3, 4, 5, 6] in [dice_values[i:i + 4] for i in range(len(dice_values) - 3)]:
                score = 30  # Small Straight의 점수는 보통 30점입니다.
        return score

    def scoreLargeStraight(d):
        score = 0
        dice_values = sorted(set([die.getRoll() for die in d]))  # 주사위 값의 중복을 제거하고 정렬합니다.
        if len(dice_values) == 5 and (dice_values == [1, 2, 3, 4, 5] or dice_values == [2, 3, 4, 5, 6]):
            score = 40  # Large Straight의 점수는 보통 40점입니다.

        return score

    def scoreYahtzee(d):
        score = 0
        if len(set([die.getRoll() for die in d])) == 1:  # 모든 주사위 값이 동일한지 확인합니다.
            score = 50  # Yahtzee의 점수는 보통 50점입니다.
        return score

    def sumDie(d): # chance : 주사위 숫자의 합
        sum = 0
        for i in d:
            sum += i.getRoll()
        return sum
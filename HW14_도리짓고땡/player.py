import itertools
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

    def check_hand(self):
        # 카드의 month 값을 추출
        months = [card.month for card in self.cards]
        months.sort()

        # 족보 및 점수 판정
        hand_rankings = {
            (1, 1, 8): ("콩콩팔", 1),
            (1, 2, 7): ("삐리칠", 2),
            (1, 3, 6): ("물삼육", 3),
            (1, 4, 5): ("빽새오", 4),
            (1, 9, 10): ("삥구장", 5),
            (2, 2, 6): ("니니육", 6),
            (2, 3, 5): ("이삼오", 7),
            (2, 8, 10): ("이판장", 8),
            (3, 3, 4): ("심심새", 9),
            (3, 7, 10): ("삼칠장", 10),
            (3, 8, 9): ("삼빡구", 11),
            (4, 4, 2): ("살살이", 12),
            (4, 6, 10): ("사륙장", 13),
            (4, 7, 9): ("사칠구", 14),
            (5, 5, 10): ("꼬꼬장", 15),
            (5, 6, 9): ("오륙구", 16),
            (5, 7, 8): ("오리발", 17),
            (6, 6, 8): ("쭉쭉팔", 18),
            (7, 7, 6): ("철철육", 19),
            (8, 8, 4): ("팍팍싸", 20),
            (9, 9, 2): ("구구리", 21)
        }

        best_hand = ["노 메이드", 22, "망통", 22]
        hand_cards = list()

        for comb in itertools.combinations(months, 3):
            comb = tuple(sorted(comb))
            if comb in hand_rankings:
                if hand_rankings[comb][1] < best_hand[1] or best_hand[1] == 22:
                    hand_cards = list(comb)[:]  # hand_cards에 값을 할당하는 부분
                    best_hand[0] = hand_rankings[comb][0] + str(comb)
                    best_hand[1] = hand_rankings[comb][1]

        # 자투리 족보 확인
        if best_hand[1] <= 21:
            i = 0
            while len(self.cards) > 2:
                for j in self.cards:
                    if j.month == hand_cards[i]:
                        hand_cards.pop(i)
                        self.cards.remove(j)
                        break

            ls = [self.cards[0].month, self.cards[1].month]
            ls.sort()

            if ls == [3, 8]:
                best_hand[2] ='38광땡'
                best_hand[3] = 1
            elif ls == [1, 8] or ls == [1,3]:
                best_hand[2] = '광땡'
                best_hand[3] = 2
            elif ls[0] == ls[1]:
                if ls[0] == 1:
                    best_hand[2] = '삥땡'
                    best_hand[3] = 12
                elif ls[0] == 2:
                    best_hand[2] = '이땡'
                    best_hand[3] = 11
                elif ls[0] == 3:
                    best_hand[2] = '삼땡'
                    best_hand[3] = 10
                elif ls[0] == 4:
                    best_hand[2] = '사땡'
                    best_hand[3] = 9
                elif ls[0] == 5:
                    best_hand[2] = '오땡'
                    best_hand[3] = 8
                elif ls[0] == 6:
                    best_hand[2] = '육땡'
                    best_hand[3] = 7
                elif ls[0] == 7:
                    best_hand[2] = '칠땡'
                    best_hand[3] = 6
                elif ls[0] == 8:
                    best_hand[2] = '팔땡'
                    best_hand[3] = 5
                elif ls[0] == 9:
                    best_hand[2] = '구땡'
                    best_hand[3] = 4
                else:
                    best_hand[2] = '장땡'
                    best_hand[3] = 3
            elif (ls[0] + ls[1]) % 10 == 9:
                best_hand[2] = '갑오'
                best_hand[3] = 13
            elif (ls[0] + ls[1]) % 10 == 0:
                best_hand[2] = '망통'
                best_hand[3] = 22
            else:
                if (ls[0] + ls[1]) % 10 == 8:
                    best_hand[2] = '여덟 끗'
                    best_hand[3] = 14
                elif (ls[0] + ls[1]) % 10 == 7:
                    best_hand[2] = '일곱 끗'
                    best_hand[3] = 15
                elif (ls[0] + ls[1]) % 10 == 6:
                    best_hand[2] = '여섯 끗'
                    best_hand[3] = 16
                elif (ls[0] + ls[1]) % 10 == 5:
                    best_hand[2] = '다섯 끗'
                    best_hand[3] = 17
                elif (ls[0] + ls[1]) % 10 == 4:
                    best_hand[2] = '네 끗'
                    best_hand[3] = 18
                elif (ls[0] + ls[1]) % 10 == 3:
                    best_hand[2] = '세 끗'
                    best_hand[3] = 19
                elif (ls[0] + ls[1]) % 10 == 2:
                    best_hand[2] = '두 끗'
                    best_hand[3] = 20
                else:
                    best_hand[2] = '한 끗'
                    best_hand[3] = 21




        return best_hand[0], best_hand[1], best_hand[2], best_hand[3]


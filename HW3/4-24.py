# 4-24
from random import *

cList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
sList = ['하트', '다이아몬드', '스페이드', '클로버']

deck = [i for i in range(52)]
shuffle(deck)

print(sList[deck[0] // 13], cList[deck[0] % 13])

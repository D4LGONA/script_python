# 10-19 (중간고사 문제)
# 슬롯 n개, 못은 n-1, 0 = left, 1 = right
from random import *

b = eval(input("공의 개수: "))
n = eval(input("슬롯의 개수: "))
slots = [ 0 for _ in range(n)]

for i in range(b):
    cnt = 0
    for j in range(n - 1):
        if randint(0, 1) == 1:
            print("R", end = '')
            cnt += 1
        else:
            print("L", end = '')
    slots[cnt] += 1
    print()

for i in range(max(slots), 0, -1):
    for j in range(len(slots)):
        if slots[j] >= i:
            print('o', end = '')
        else:
            print(' ', end = '')
    print("")

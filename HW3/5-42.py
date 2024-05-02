# 5-42
import random

count = 0
for i in range(1000000):
    x = random.random() * 2 - 1 # [-1:1)
    y = random.random() * 2 - 1
    if x < 0: # 1번 영역
        count+= 1
    elif 0 <= x <= 1 and 0 <= y <= 1:
        slope = -1
        b = y - slope * x
        if 0 <= b <= 1: # 3번영역
            count += 1
print("횟수:",count, "확률:", count/1000000)

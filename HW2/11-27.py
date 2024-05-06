# 11-27
import copy

def sortColumns(m):
    a = copy.deepcopy(m)
    for i in range(3):
        for j in range(2):
            if a[j][i] > a[j+1][i]:
                a[j][i], a[j+1][i] = a[j+1][i], a[j][i]

    return a

print("3x3 행렬을 한 행씩 입력하세요:")
r1 = [eval(i) for i in input().split()]
r2 = [eval(i) for i in input().split()]
r3 = [eval(i) for i in input().split()]
a = [r1, r2, r3]

l = sortColumns(a)
for i in l:
    print(*i)


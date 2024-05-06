# 11-1
def sumColumn(m, columnIndex):
    s = 0
    for j in range(3):
        s += m[j][columnIndex]
    return s

l = []

for k in range(3):
    row = [eval(i) for i in input("3x4 행렬의 행 "+ str(k) +"번에 대한 원소를 입력하세요: ").split()]
    l.append(row)

for i in range(4):
    print("열", i, "번 원소의 총 합은", sumColumn(l, i), "입니다.")

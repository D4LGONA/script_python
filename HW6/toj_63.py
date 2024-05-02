def printM(m):
    print('M')
    for i in range(len(m)):
        print(*m[i])

def printR(m):
    print('R')
    for i in range(len(m[0])):
        for j in range(len(m) - 1, -1, -1):
            if j == 0:
                print(m[j][i], end='')
            else:
                print(m[j][i], end=' ')
        print()

def printL(m):
    print('L')
    for i in range(len(m[0])- 1, -1, -1):
        for j in range(len(m)):
            if j == len(m) - 1:
                print(m[j][i], end='')
            else:
                print(m[j][i], end=' ')
        print()

def printT(m):
    print("T")
    for i in range(len(m[0])):
        for j in range(len(m)):
            if j == len(m)-1:
                print(m[j][i], end='')
            else:
                print(m[j][i], end=' ')
        print()

tmp = input().split()
a = int(tmp[0])
b = int(tmp[1])

matrix = []
for i in range(a):
    matrix.append([])
    for j in range(b):
        matrix[i].append(i * b + j + 1)

printM(matrix)
printR(matrix)
printL(matrix)
printT(matrix)
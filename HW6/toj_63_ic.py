def print2DList(M):
    for r in range(len(M)):
        for c in range(len(M[0])):
            if c != len(M[0]) - 1:
                print(M[r][c], end=' ')
            else:
                print(M[r][c])

A, B = map(eval, input().split())
M = []
n = 1
for r in range(A):
    row = []
    for c in range(B):
        row.append(n)
        n += 1
    M.append(row)

print('M')
print2DList(M)

R = [[M[r][c] for r in range(A-1, -1, -1)]for c in range(B)]
print('R')
print2DList(R)

L = [[M[r][c] for r in range(A)]for c in range(B-1, -1, -1)]
print('L')
print2DList(L)

T = [[M[r][c] for r in range(A)]for c in range(B)]
print('T')
print2DList(T)
n = eval(input())

line = input()
M = []
M.append(['.']*n)

r = 0
p = '.'
for i in range(n):
    if line[i] == '+':
        if p == '/': # 전날이 +이면 위 행으로
            if r == 0:
                M.insert(0, ['.'] * n)
            else:
                r -= 1
        p = M[r][i] = '/'

    elif line[i] == '-':
        if p == '\\' or p == '_':
            if r == len(M) - 1:
                M.append(['.'] * n)
            r += 1
        p = M[r][i] = '\\'

    else:
        if p == '/': # 전날이 +이면 위 행으로
            if r == 0:
                M.insert(0, ['.'] * n)
            else:
                r -= 1
        p = M[r][i] = '_'


for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j],end='')
    print()
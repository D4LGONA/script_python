n = eval(input())

ls = []
for i in range(n):
    for j in range(1, n*2):
        if abs(j-n) <= i:
            if j == n*2-1:
                print(abs(j - n) + 1, end='')
            else:
                print(abs(j-n) + 1, end=' ')
        else:
            if j == n * 2 - 1:
                print('.', end='')
            else:
                print('. ', end='')
    if i == n-1: break
    print()
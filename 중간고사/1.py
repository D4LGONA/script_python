n = eval(input())
s = eval(input())

ls = [0] * s
for i in range(n):
    st = input()
    idx = 0
    for j in st:
        if j == 'R':
            idx += 1
    ls[idx] += 1

for i in range(max(ls), 0, -1):
    for j in range(len(ls)):
        if ls[j] >= i:
            print('*', end='')
        else:
            print(".", end='')
    print()


def check_bingo(s):
    # 가로줄 검사
    for i in range(5):
        if d[s][i] == [0, 0, 0, 0, 0]:
            return True
    # 세로줄 검사
    for i in range(5):
        cnt = 0
        for j in range(5):
            if d[s][j][i] == 0:
                cnt += 1
        if cnt == 5:
            return True
    # 대각선 검사
    if [d[s][0][0], d[s][1][1], d[s][2][2], d[s][3][3], d[s][4][4]] == [0, 0, 0, 0, 0]:
        return True
    if [d[s][4][0], d[s][3][1], d[s][2][2], d[s][1][3], d[s][0][4]] == [0, 0, 0, 0, 0]:
        return True
    return False

n = eval(input()) # 플레이어 수
d = {}

for i in range(n):
    name = input()  # 플레이어 이름
    d[name] = []
    for j in range(5):
        ls = [eval(i) for i in input().split()]
        d[name].append(ls)

m = eval(input()) # 공의 개수
b_ls = [eval(i) for i in input().split()]

for j in b_ls:
    for key in d.keys():
        for k in d[key]:
            for l in range(len(k)):
                if j == k[l]:
                    k[l] = 0

res = []
for key in d.keys():
    if check_bingo(key):
        res.append(key)
print(len(res))
if len(res) != 0:
    for i in res:
        print(i, end='')
        if res.index(i) != len(res)-1:
            print()
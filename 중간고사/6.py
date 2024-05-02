def check_score(ls):
    res = 0
    for i in range(4):
        res += ls[i] ** 2
    res += check_krokod(ls)
    return res

def check_krokod(ls):
    cnt = 0
    while True:
        if ls[0] >= 1 and ls[1] >= 2 and ls[2] >= 2 and ls[3] >= 1:
            ls[0] -= 1
            ls[1] -= 2
            ls[2] -= 2
            ls[3] -= 1
            cnt += 1
        else:
            break
    return cnt * 7

def make_comb(lst, n):
    result = [[]]
    for _ in range(n):
        result = [prev + [item] for prev in result for item in lst]
    return result

n, m = map(int, input().split())
s = input()
res = []

ls = [0] * 5 # 0-d, 1-k, 2-o, 3-r, 4-joker
ls[4] = m
ls[0] = s.count('d')
ls[1] = s.count('k')
ls[2] = s.count('o')
ls[3] = s.count('r')

tmplst = [0, 1, 2, 3]
checks = []
if ls[4] != 0:
    checks = make_comb(tmplst, ls[4])

for i in checks:
    res.append(0)
    tmp = ls[:]
    for j in i:
        tmp[j] += 1
    res[-1] = check_score(tmp)
else:
    res.append(0)
    tmp = ls[:]
    res[-1] = check_score(tmp)

print(max(res))
n = eval(input())
d = {}
d_total = {}
ls = []

for i in range(n):
    ip = input().split()
    if ip[0] not in d:
        d[ip[0]] = []
        d_total[ip[0]] = 0
    d[ip[0]].append([i, eval(ip[1])])
    d_total[ip[0]] += eval(ip[1])

for key in d.keys():
    d[key].sort(key=lambda x: (x[1], x[0]), reverse=True)

s_keys = sorted(d.keys(), key=lambda x: d_total[x], reverse=True)

for k in s_keys:
    print(d[k][0][0])
    if len(d[k]) > 1:
        print(d[k][1][0])
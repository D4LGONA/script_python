# 14-2

l = input("정수를 입력하세요: ").split()
d = dict()

for i in l:
    if i not in d:
        d[i] = 0
    else:
        d[i] += 1

maxL = []
m = max(d.values())
for k,v in d.items():
    if v == m:
        maxL.append(eval(k))

print(*maxL)


def compute(d, k, o, r):
    answer = d*d + k*k + o*o + r*r
    answer += 7 * min(k//2, o//2, r, d)
    return answer

n, m = map(eval, input().split())
line = input()
d = 0
k = 0
o = 0
r = 0
for c in line:
    if c == 'd':
        d += 1
    elif c == 'k':
        k += 1
    elif c == 'o':
        o += 1
    else:
        r += 1
answer = 0
for D in range(m+1):
    for K in range(m+1):
        for O in range(m+1):
            for R in range(m+1):
                if D+K+O+R == m:
                    answer = max(answer, compute(d + D, k + K, o + O, r + R))
print(answer)
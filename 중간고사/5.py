def find_max(l, v):
    s_l = sorted(l, reverse=True)
    idx = l.index(s_l[v-1])
    print(idx, l[idx])
    return idx, l[idx]

n = eval(input()) # 참가자 수.
ai = [eval(i) for i in input().split()] # 회장점수
bi = [eval(i) for i in input().split()] # 협회점수
ls = [0] * n # 각 번호의 점수
idxs = [i+1 for i in range(n)]
s_bi = sorted(bi, reverse=True)

for i in range(len(bi)): # 협회점수
    index = bi.index(s_bi[i])
    ls[index] += n-i
idxs.sort(key=lambda x:ls[x-1], reverse=True)

for i in range(len(ai)):
    ls[ai[i] - 1] += n - i # 회장 점수 더하기
idxs.sort(key=lambda x:ls[x-1], reverse=True)

for i in range(len(idxs)):
    val = ls[idxs[i] - 1]
    idx = str(idxs[i]).zfill(2)
    print(str(i+1)+". Kod"+idx+" ("+str(val)+")")

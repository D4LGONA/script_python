N = eval(input())
D = {}

for i in range(N):
    [genre, play] = input().split()
    play = int(play)
    if not genre in D:
        D[genre] = [play, (i, play), (-1, 0)]
    else:
        D[genre][0] += play
        if play > D[genre][1][1]:
            D[genre][2] = D[genre][1]
            D[genre][1] = (i, play)
        elif play > D[genre][2][1]:
            D[genre][2] = (i, play)

G = []
for key, value in D.items():
    G.append((key, value))

G.sort(key=lambda x : x[1])
for i in range(len(G)):
    genre = G[i][0]
    print(D[genre][1][0])
    if D[genre][2][0] != -1:
        print(D[genre][2][0])
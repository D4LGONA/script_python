n = eval(input())
Board = []

for _ in range(n):
    name = input()
    board = [list(map(eval, input().split())) for i in range(5)]
    Board.append((name,board))

m = eval(input())
masterBalls = list(map(eval, input().split()))
nameBingos = []
for name, board in Board:
    # 가로선
    done = False
    for r in range(5):
        if not done:
            Flag = True
            for c in range(5):
                if not board[r][c] in masterBalls:
                    Flag = False
                    break
            if Flag:
                nameBingos.append(name)
                done = True
                break
    # 세로선
    if not done:
        for c in range(5):
            if not done:
                Flag = True
                for r in range(5):
                    if not board[r][c] in masterBalls:
                        Flag = False
                        break
                if Flag:
                    nameBingos.append(name)
                    done = True
                    break
    # 대각선
    if not done:
        Flag = True
        for i in range(5):
            if not board[i][i] in masterBalls:
                Flag = False
                break
        if Flag:
            nameBingos.append(name)
            done = True

    if not done:
        Flag = True
        for i in range(5):
            if not board[i][4 - i] in masterBalls:
                Flag = False
                break
        if Flag:
            nameBingos.append(name)
            done = True
print(len(nameBingos))
for i in nameBingos:
    print(i)
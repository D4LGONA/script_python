import time
matrix = []

def drawBoard():
    for i in range(3):
        print("-------------------")
        for j in range(3):
            print('| ', matrix[i][j], " ", end='')
        print('|')
    print("-------------------")

def check_win():
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != " ":
            return True
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != " ":
            return True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":
        return True
    if matrix[2][0] == matrix[1][1] == matrix[0][2] != " ":
        return True

    return False

def main():
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(" ")
    drawBoard()

    turn = True
    cnt = 0
    while True:
        if cnt == 9: break

        if turn:
            while True:
                row = eval(input("플레이어 x의 행(0,1,2)를 입력하세요: "))
                col = eval(input("플레이어 x의 열(0,1,2)을 입력하세요: "))
                if matrix[row][col] == ' ':
                    cnt += 1
                    break
                else:
                    print("이미 선택된 자리입니다.")
            matrix[row][col] = "x"
            if check_win(): break

        else:
            while True:
                row = eval(input("플레이어 o의 행(0,1,2)를 입력하세요: "))
                col = eval(input("플레이어 o의 열(0,1,2)을 입력하세요: "))
                if matrix[row][col] == ' ':
                    cnt += 1
                    break
                else:
                    print("이미 선택된 자리입니다.")
            matrix[row][col] = "o"
            if check_win(): break

        drawBoard()
        turn = not turn

    drawBoard()
    if cnt == 9:
        print("비겼습니다.")
    elif turn:
        print("플레이어 x가 이겼습니다.")
    else:
        print("플레이어 o가 이겼습니다.")
    time.sleep(5)

main()
import time
matrix = [] # 6행 7열 사목게임
# player는 R(ed), Y(ellow)

def drawBoard():
    for i in range(6):
        for j in range(7):
            print('|', matrix[i][j], "", end='')
        print('|')
    print("-----------------------------")

def check_win():
    for i in range(6): # 가로
        for j in range(4):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i][j+1] and player == matrix[i][j+2] and player == matrix[i][j+3]:
                return True

    for i in range(3): # 세로
        for j in range(7):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i+1][j] and player == matrix[i+2][j] and player == matrix[i+3][j]:
                return True

    for i in range(3):
        for j in range(4):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i+1][j+1] and player == matrix[i+2][j+2] and player == matrix[i+3][j+3]:
                return True

    for i in range(3):
        for j in range(3, 7):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i+1][j-1] and player == matrix[i+2][j-2] and player == matrix[i+3][j-3]:
                return True


    return False


def main():
    for i in range(6):
        matrix.append([])
        for j in range(7):
            matrix[i].append(" ")
    drawBoard()

    turn = True
    cnt = 0
    while True:
        if cnt == 42: break

        if turn:
            while True:
                flag = False
                x = eval(input("열 0-6에 빨간색 디스크를 떨어뜨리세요: "))
                if 0 <= x <= 6:
                    for i in range(5, -1, -1):
                        if matrix[i][x] == ' ':
                            cnt += 1
                            matrix[i][x] = "R"
                            flag = True
                            break
                    else:
                        print("해당 열은 이미 가득 찼네요!")
                else:
                    print("열은 0부터 6까지만 입력 가능합니다.")
                if flag: break
            if check_win(): break

        else:
            while True:
                flag = False
                x = eval(input("열 0-6에 노란색 디스크를 떨어뜨리세요: "))
                if 0 <= x <= 6:
                    for i in range(5, -1, -1):
                        if matrix[i][x] == ' ':
                            cnt += 1
                            matrix[i][x] = "Y"
                            flag = True
                            break
                    else:
                        print("해당 열은 이미 가득 찼네요!")
                else:
                    print("열은 0부터 6까지만 입력 가능합니다.")
                if flag: break
            if check_win(): break

        drawBoard()
        turn = not turn

    drawBoard()
    if cnt == 42:
        print("비겼습니다.")
    elif turn:
        print("Red가 이겼습니다.")
    else:
        print("Yellow가 이겼습니다.")
    time.sleep(3)

main()
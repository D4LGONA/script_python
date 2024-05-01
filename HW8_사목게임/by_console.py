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
    drawBoard()
    # 가로 확인
    combo = 0
    pre = ''
    for i in range(6):
        for j in range(7):
            if matrix[i][j] != ' ':
                if pre == matrix[i][j]:
                    combo += 1
                else:
                    combo = 1
                    pre = matrix[i][j]
            if combo >= 4: return True

        combo = 0
        pre = ' '

    # 세로 확인
    combo = 0
    pre = ''
    for i in range(7):
        for j in range(6):
            if matrix[j][i] != ' ':
                if pre == matrix[j][i]:
                    combo += 1
                else:
                    combo = 1
                    pre = matrix[j][i]
                if combo >= 4: return True

        combo = 0
        pre = ' '

    combo = 0
    pre = ''
    # 가운데로부터 오른쪽 위
    for i in range(4):
        for j in range(7 - i):
            if i == 0 and j == 6: continue
            if matrix[j + i][j] != ' ':
                if pre == matrix[j + i][i]:
                    combo += 1
                else:
                    combo = 1
                    pre = matrix[j + i][i]
                if combo >= 4: return True
        combo = 0
        pre = ''

    combo = 0
    pre = ''

    # 가운데로부터 오른쪽 아래
    for i in range(2):
        for j in range(5 - i):
            if matrix[j][j + i] != ' ':
                if pre == matrix[j][j + i]:
                    combo += 1
                else:
                    combo = 1
                    pre = matrix[j][j + i]
                if combo >= 4: return True
        combo = 0
        pre = ''

    combo = 0
    pre = ''
    # 가운데로부터 왼쪽 위
    # todo: 여기부터 해야 함


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
    time.sleep(5)

main()
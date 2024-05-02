# 15-18

move_cnt = 0
def moveDisks(n, fromTower, toTower, auxTower):
    global move_cnt
    if n == 1: # 정지 조건
        move_cnt += 1
        print("디스크 ", n, "을/를 ", fromTower, "에서", toTower, "로 옮긴다.")
    else:
        moveDisks(n-1, fromTower, auxTower, toTower)
        move_cnt += 1
        print("디스크", n, "을/를 ", fromTower, "에서", toTower, "로 옮긴다.")
        moveDisks(n-1, auxTower, toTower, fromTower)

def main():
    n = eval(input("디스크의 개수를 입력하세요: "))
    #해결 방법을 재귀적으로 찾는다.
    print("옮기는 순서는 다음과 같습니다:")
    moveDisks(n, 'A', 'B', 'C')
    print("디스크를 총", move_cnt, "번 옮겼습니다.")

main()

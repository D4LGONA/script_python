# 4-27

x, y = eval(input("x, y 좌표값을 입력하세요: "))
if x < 0 or x > 200 or y < 0 or y > 100:
    print("점은 삼각형의 외부에 있습니다.")
else:
    slope = -100/200 # -1/2
    b = y - slope*x # x,y를 지나는 기울기 -1/2인 직선의 y절편 구하기
    if b > 0 and b < 100:
        print("점은 삼각형의 내부에 있습니다.")
    else:
        print("점은 삼각형의 외부에 있습니다.")

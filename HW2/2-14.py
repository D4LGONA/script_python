x1, y1, x2, y2, x3, y3 = eval(input("삼각형의 세 꼭짓점을 입력하세요: "))
d1 = ((x2-x1)**2 + (y2-y1) ** 2) ** 0.5
d2 = ((x3-x2)**2 + (y3-y2) ** 2) ** 0.5
d3 = ((x3-x1)**2 + (y3-y1) ** 2) ** 0.5
s = (d1 + d2 + d3) / 2
area = (s*(s-d1)*(s-d2)*(s-d3))**0.5
area = int(area*10) / 10
print("삼각형의 넓이는",area,"입니다.")
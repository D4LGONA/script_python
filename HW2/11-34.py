def getRightmostLowestPoint(points):
    points.sort(key=lambda x: (-x[1], x[0]))
    return points[-1]

l = [float(i) for i in input("6개의 점을 입력하세요: ").split()]
ls = []
for i in range(0, len(l), 2):
    ls.append((l[i], l[i+1]))

t = getRightmostLowestPoint(ls)
print("최우측하단의 점은", t, "입니다.")

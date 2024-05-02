# 6-5

def displaySortedNumbers(num1, num2, num3):
    l = [num1, num2, num3]
    l.sort()
    return l

a, b, c = eval(input("세 개의 수를 입력하세요: "))
res = displaySortedNumbers(a, b, c)
print("정렬된 숫자는", *res,"입니다.")

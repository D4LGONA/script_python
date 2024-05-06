# 6-4

def reverse(number):
    s = str(number)
    s = s[::-1]
    return int(s)

n = eval(input("정수를 입력하세요: "))
print(reverse(n))

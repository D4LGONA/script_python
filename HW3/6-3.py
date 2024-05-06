# 6-3

def reverse(number):
    result = 0
    while number:
        rem = number % 10
        result = result * 10 + rem # 자릿수를 뒤로 미는거
        number //= 10
    return result

def isPalindrome(number):
    if number == reverse(number):
        return True
    return False

n = eval(input("정수 입력: "))
if isPalindrome(n):
    print("대칭수입니다.")
else:
    print("대칭수가 아닙니다.")

# 10-2

numbers = input("정수 리스트 입력: ").split()
numbers = [eval(num) for num in numbers]

print("입력된 숫자의 역순:", numbers[::-1])

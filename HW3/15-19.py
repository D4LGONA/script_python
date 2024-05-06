# 15-19

def decimalToBinary(value):
    return bin(value)

n = eval(input("10진수 입력: "))
print("2진수:",decimalToBinary(n)[2:])

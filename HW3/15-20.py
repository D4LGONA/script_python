# 15-20

def decimalToHex(value):
    return hex(value)

n = eval(input("10진수를 입력하세요: "))
print("16진수:", decimalToHex(n)[2:])

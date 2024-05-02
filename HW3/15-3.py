# 15-3

def gcd(m, n):
    if 0 == m % n:
        return n
    else:
        return gcd(n, m % n)

a, b = eval(input("두 정수를 입력하세요: "))
res = gcd(a, b)
print("최대공약수는", res,"입니다.")

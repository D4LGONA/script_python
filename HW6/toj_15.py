def tton(v, n):
    if n == 0:
        return '0'

    result = []
    while n > 0:
        digit = n % v
        result.append(digit)
        n //= v
    result.reverse()
    return result

def ntot(v, n):
    l = len(n)
    res = 0
    for i in range(l):
        res += int(n[l - i - 1]) * v ** i

    return res


b, N, M = map(int, input().split())

l1 = input().split()
l2 = input().split()
l1_10 = ntot(b, l1)
l2_10 = ntot(b, l2)
res = l1_10 * l2_10
res_b = tton(b, res)
print(len(res_b))
print(*res_b)
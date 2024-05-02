# 6-13

def m(i):
    if i == 1:
        return 1/2
    else:
        return (i / (i+1)) + m(i-1)

print("i\t m(i)")
for i in range(1, 21, 1):
    print(i, "\t",m(i))



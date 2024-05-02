# 15-4

def func(i):
    if i == 1:
        return 1
    else:
        return (1/i) + func(i-1)

for i in range(1,11):
    print(func(i))

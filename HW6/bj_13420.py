n = int(input())

for i in range(n):
    isTrue = False
    ls = input().split()
    l = []
    for j in ls:
        try:
            l.append(int(j))
        except ValueError:
            l.append(j)
    if l[1] == '+':
        if l[0] + l[2] == l[-1]:
            isTrue = True
    elif l[1] == '-':
        if l[0] - l[2] == l[-1]:
            isTrue = True
    elif l[1] == '*':
        if l[0] * l[2] == l[-1]:
            isTrue = True
    elif l[1] == '/':
        if l[2] != 0 and l[0] / l[2] == l[-1]:
            isTrue = True
    if isTrue:
        print("correct")
    else:
        print("wrong answer")

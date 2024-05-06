s = input()
b = input()

while True:
    if b in s:
        s = s.replace(b,"")
    else:
        break
print(s)
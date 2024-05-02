# 6-12

def printChars(ch1, ch2, numberPerLine):
    count = 0
    for i in range(ord(ch1), ord(ch2) + 1):
        print(chr(i), end=' ')
        count += 1
        if 0 == count % numberPerLine:
            print('')
            

c1 = input("ch1 입력: ")
c2 = input("ch2 입력: ")
n = eval(input("numberPerLine 입력: "))
printChars(c1, c2, n)

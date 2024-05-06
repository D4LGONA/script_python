# 10-15
# input: 1 1 3 4 4 5 7 9 10 30 11
#        1 1 3 4 4 5 7 9 10 30

def isSorted(lst): # lst가 오름차순으로 정렬되어 있으면 True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


sList = input("정수들 입력: ").split()
iList = [eval(i) for i in sList]
if isSorted(iList):
    print("이 리스트는 정렬되어 있습니다.")
else:
    print("이 리스트는 정렬되어 있지 않습니다.")

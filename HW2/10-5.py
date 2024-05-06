# 10-5
sList = input("정수를 입력하세요: ").split() # 문자열 리스트가 됨
iList = [eval(i) for i in sList] # 문자열 리스트를 정수로 변환
list2 = list(set(iList))
print("중복을 제거한 고유한 숫자: ",end='')
for i in list2:
    print(i,' ', end='')

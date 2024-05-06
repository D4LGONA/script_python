# 10-4
sList = input("정수를 입력하세요: ").split() # 문자열 리스트가 됨
iList = [eval(i) for i in sList] # 문자열 리스트를 정수로 변환
average = sum(iList) / len(iList)

cnt = 0
for i in iList:
    if i >= average:
        cnt += 1

print("평균이상인 정수 개수:", cnt, "\n평균미만인 정수 개수:", len(iList) - cnt)

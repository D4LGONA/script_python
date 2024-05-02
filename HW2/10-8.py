# 10-8

def indexOfSmallestElement(lst):
    min_idx = 0
    min_el = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < min_el:
            min_idx = i
            min_el = lst[i]

    return min_idx

n = [eval(i) for i in input("정수 리스트를 입력하세요: ").split()]
print("최솟값의 인덱스:", indexOfSmallestElement(n))

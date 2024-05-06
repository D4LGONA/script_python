def solution(id_list, report, k):
    r = list(set(report))
    d = {}
    answer = []
    for i in id_list:
        d[i] = [0, [], 0]  # 신고당한횟수, 내가신고한애들, 정지시킨횟수
    for i in r:
        ls = i.split()
        d[ls[0]][1].append(ls[1])
        d[ls[1]][0] += 1

    print(d)

    for key in d.keys():
        if d[key][0] >= k:
            for j in d.keys():
                if key in d[j][1]:
                    d[j][2] += 1

    for key in d.keys():
        answer.append(d[key][2])

    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
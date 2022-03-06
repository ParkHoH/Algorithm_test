#my solution
def solution(N, stages):
    L = []
    num_person = len(stages)

    for i in range(1, N+1):
        cnt = stages.count(i) / num_person if num_person != 0 else 0
        num_person -= stages.count(i)
        L.append([cnt, i])

    L.sort(reverse=True, key=lambda x: x[0])
    result = [L[i][1] for i in range(len(L))]
    return result


#dictionary solution
def solution(N, stages):
    dic = {}
    num_person = len(stages)
    for stage in range(1, N+1):
        count = stages.count(stage) if num_person != 0 else 0
        dic[stage] = count / num_person
        num_person -= count

    return sorted(dic, key=lambda x : dic[x], reverse=True)
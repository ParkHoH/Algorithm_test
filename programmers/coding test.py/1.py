def solution(money, costs):
    #생산단가 비효율적인 것 빼버리기
    dic_cost = {0: costs[0], 1: costs[1], 2: costs[2], 3: costs[3], 4: costs[4], 5: costs[5]}
    L = [1, 5, 10, 50, 100, 500]
    for i in range(len(costs)):
        if L[i] != 0:
            for j in range(i+1, len(costs)):
                if dic_cost[i] * (L[j]//L[i]) < dic_cost[j]:
                    L[j] = 0

    #화폐단위로 나누면서 생산 비용 구하기
    result = 0
    for i in range(len(L)-1, -1, -1):
        if L[i] != 0:
            result += money//L[i] * dic_cost[i]
            money %= L[i]

    #총 생산비용 리턴
    return result

print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))
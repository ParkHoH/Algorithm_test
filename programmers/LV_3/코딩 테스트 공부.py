# 알고력, 코딩력을 각각 정렬함 (인덱스 포함해야 함)
# 알고력을 기준으로 탐색하되, 알고력이 부족할 경우 heap에 코딩력으로부터 현재 알고력, 코딩력까지 가능한 것을 넣어줌
# <= 이럴 경우 알고력, 

def solution(alp, cop, problems):
    max_alp = max_cop = 0

    for a, c, _, _, _ in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, c)

    alp, cop = min(alp, max_alp), min(cop, max_cop) # 기존 alp, cop가 더 작을 수 있는 경우

    dp = [[float('inf')] * (max_alp+1) for _ in range(max_cop+1)]
    dp[cop][alp] = 0

    for i in range(cop, max_cop+1):
        for j in range(alp, max_alp+1):
            if i+1 <= max_cop:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)

            if j+1 <= max_alp:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for a, c, a_rwd, c_rwd, cost in problems:
                if i >= c and j >= a:
                    min_cop = min(i+c_rwd, max_cop)
                    min_alp = min(j+a_rwd, max_alp)
                    dp[min_cop][min_alp] = min(dp[min_cop][min_alp], dp[i][j] + cost)

    return dp[-1][-1]

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
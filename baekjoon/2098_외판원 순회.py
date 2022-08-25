N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1<<N-1) for _ in range(N)]

def dfs(idx, visited):
    if dp[idx][visited] != 0: # 이전에 방문했던 적이 있는 경우
        return dp[idx][visited]

    if visited == (1<<(N-1)) - 1: # 모든 지점을 방문한 경우
        cost = graph[idx][0]
        if cost != 0: # 시작 지점으로 가는 경로가 있는 경우
            return cost
        else:
            return float('inf')

    num = float('inf')
    for to in range(1, N):
        if graph[idx][to] == 0: # 가는 경로가 없는 경우
            continue
        if visited & 1<<(to-1): # 이전에 방문한 적이 있는 경우
            continue

        num = min(num, dfs(to, visited | (1<<to-1)) + graph[idx][to])
    
    dp[idx][visited] = num
    return num

print(dfs(0, 0))
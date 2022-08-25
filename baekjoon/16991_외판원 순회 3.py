N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

graph = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        dist = ((L[i][0] - L[j][0])**2 + (L[i][1] - L[j][1])**2)**0.5
        graph[i][j] = dist
        graph[j][i] = dist

dp = [[0] * (1 << (N-1)) for _ in range(N)]

def dfs(idx, visited):
    if dp[idx][visited]:
        return dp[idx][visited]

    if visited == (1 << (N-1)) - 1:
        if graph[idx][0]:
            return graph[idx][0]
        else:
            return float('inf')

    min_value = float('inf')

    for i in range(1, N):
        if graph[idx][i] == 0 or visited & (1 << (i-1)):
            continue

        min_value = min(min_value, dfs(i, visited | (1 << (i-1))) + graph[idx][i])

    dp[idx][visited] = min_value
    return min_value

print(dfs(0, 0))
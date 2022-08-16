N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
sum_costs = sum(costs)
dp = [[0] * (sum_costs+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(sum_costs+1):
        memory, cost = memories[i-1], costs[i-1]
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)

for i in range(sum_costs+1):
    if dp[-1][i] >= M:
        print(i)
        break
n = int(input())
L = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)]

dp[0][0] = result = L[0]

for i in range(1, n):
    dp[i][0] = max(L[i], dp[i-1][0] + L[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + L[i])
    result = max(result, max(dp[i]))

print(result)
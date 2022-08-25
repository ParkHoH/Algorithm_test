N = int(input())
L = list(map(int, input().split()))
dp = [0] * N
dp[-1] = L[-1]

for i in range(N-2, -1, -1):
    if dp[i+1] < L[i]:
        dp[i] = L[i]
    else:
        dp[i] = dp[i+1]

for i in range(N):
    if L[i] < dp[i]:
        print(dp[i], end=" ")
    else:
        print(-1, end=" ")
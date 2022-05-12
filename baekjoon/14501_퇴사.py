import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
TP = [0] * (N+1)
for i in range(N):
    TP[i] = list(map(int, input().split()))

for i in range(N-1, -1, -1):
    T, P = TP[i]
    if i+T <= N:
        dp[i] = max(dp[i+T] + P, dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])

N, M = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))

dp = [0] * (M+1)
for i in range(M+1):
    for j in range(len(L)):
        if i - L[j] >= 0:
            if j == 0:
                dp[i] = dp[i-L[j]]+1
            else:
                dp[i] = min(dp[i], dp[i-L[j]]+1)
print(dp[-1])
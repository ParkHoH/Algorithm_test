import sys
input = sys.stdin.readline

N = int(input())
L = [0] * N 

for i in range(N):
    L[i] = int(input())

if N <= 2:
    print(sum(L))

else:
    dp = [0] * N
    dp[0] = L[0]
    dp[1] = dp[0] + L[1]
    dp[2] = max(L[0] + L[2], L[1] + L[2], dp[1])

    for i in range(3, N):
        dp[i] = max(L[i] + dp[i-2], L[i] + L[i-1] + dp[i-3], dp[i-1])

    print(max(dp[-1], dp[-2]))
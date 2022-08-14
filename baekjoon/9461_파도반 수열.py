import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N <= 3:
        print(1)
    
    else:
        dp = [0] * (N+1)
        dp[1] = dp[2] = dp[3] = 1

        for i in range(4, N+1):
            dp[i] = dp[i-2] + dp[i-3]

        print(dp[-1])
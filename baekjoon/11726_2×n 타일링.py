n = int(input())

if n <= 3:
    print(n)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    
    for i in range(4, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    print(dp[-1])
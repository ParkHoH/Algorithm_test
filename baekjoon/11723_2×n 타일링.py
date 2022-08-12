n = int(input())

if n <= 2:
    print(n)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2) + (dp[i-2] - 1)

    print(dp[-1] % 10007)
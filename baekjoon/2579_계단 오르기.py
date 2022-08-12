n = int(input())
stairs = []

for _ in range(n):
    stairs.append(int(input()))

if n <= 2:
    print(sum(stairs))
else:
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])

    print(dp[-1])
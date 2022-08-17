import sys
input = sys.stdin.readline

N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().split())))

result = float('inf')
for i in range(3):
    dp = [[float('inf'), float('inf'), float('inf')] for _ in range(N)]
    dp[0][i] = RGB[0][i]

    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + RGB[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + RGB[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + RGB[j][2]
    
    for j in range(3):
        if i == j: continue
        result = min(result, dp[-1][j])
    
print(result)
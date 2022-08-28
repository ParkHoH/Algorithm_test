import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        if i == 1:
            dp[j][i+j] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
        
        else:
            dp[j][i+j] = float('inf')
            for k in range(j, i+j):
                dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k+1][i+j] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

print(dp[0][-1])
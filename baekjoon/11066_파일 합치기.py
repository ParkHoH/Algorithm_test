import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    files = list(map(int, input().split()))

    sum_files = [0] * (k+1)
    sum_files[1] = files[0]

    for i in range(2, k+1):
        sum_files[i] = sum_files[i-1] + files[i-1]    

    dp = [[0] * k for _ in range(k)]

    for interval in range(1, k):
        for i in range(k-interval):
            if interval == 1:
                dp[i][i+interval] = files[i] + files[i+interval]

            else: 
                dp[i][i+interval] = float('inf')
                for j in range(i, i+interval):
                    dp[i][i+interval] = min(dp[i][i+interval], dp[i][j] + dp[j+1][i+interval] + sum_files[i+interval+1] - sum_files[i])

    print(dp[0][-1])
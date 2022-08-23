import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
M = int(input())
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for start in range(N-i):
        end = start+i

        if start == end:
            dp[start][end] = 1

        elif L[start] == L[end]:
            if end - start == 1:
                dp[start][end] = 1

            if dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])
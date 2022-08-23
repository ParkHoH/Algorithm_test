import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1] * M for _ in range(N)]

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0

        cnt = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue

            if board[nx][ny] < board[x][y]:
                cnt += dfs(nx, ny)

        dp[x][y] = max(dp[x][y], cnt)

    return dp[x][y]

dp[N-1][M-1] = 1

print(dfs(0, 0))
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
visited[0][0] = True

dp = [[-1] * M for _ in range(N)]
dp[0][0] = 0

answer = 1

def dfs(x, y, cnt):
    num = int(board[x][y])

    for i in range(4):
        nx, ny = x + dx[i]*num, y + dy[i]*num

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if board[nx][ny] == "H" or dp[nx][ny] > cnt+1:
            continue

        if visited[nx][ny]:
            print(-1)
            exit()

        global answer
        answer = max(answer, cnt+1)

        dp[nx][ny] = cnt+1
        visited[nx][ny] = True
        dfs(nx, ny, cnt+1)
        visited[nx][ny] = False

dfs(0, 0, 1)
print(answer)

# def check_possible():
#     visited = [[False] * M for _ in range(N)]
#     visited[0][0] = True

#     queue = deque()
#     queue.append((0, 0, 0)) # x, y, dist

#     while queue:
#         x, y, dist = queue.popleft()
#         num = board[x][y]

#         for i in range(4):
#             nx, ny = x + dx[i]*num, y + dy[i]*num

#             if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                 continue
            
#             if visited[nx][ny]:
#                 return -1

#             visited[nx][ny] = True
#             visited[]

#     return dist if dist else -1


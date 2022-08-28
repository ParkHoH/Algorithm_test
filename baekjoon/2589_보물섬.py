from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def bfs(x, y):
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    queue = deque()
    queue.append([x, y, 0])

    while queue:
        x, y, distance = queue.popleft()
        global result
        result = max(result, distance)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny] or board[nx][ny] == "W":
                continue

            visited[nx][ny] = True
            queue.append([nx, ny, distance+1])

for i in range(N):
    for j in range(M):
        if board[i][j] == "L":
            bfs(i, j)

print(result)
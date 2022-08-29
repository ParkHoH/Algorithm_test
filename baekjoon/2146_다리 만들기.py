from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_way(island, idx):
    visited = [[False] * N for _ in range(N)]
    queue = deque()

    for x, y in island:
        queue.append([x, y, 0])

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if board[nx][ny] == 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny, dist+1])

            elif board[nx][ny] != idx:
                global result
                result = min(result, dist)
                return

def group_island(x, y, idx):
    board[x][y] = idx
    island = [[x, y]]

    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            if board[nx][ny] == 1:
                board[nx][ny] = idx
                queue.append([nx, ny])
                island.append([nx, ny])

    find_way(island, idx)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
idx_island = 2
islands = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            group_island(i, j, idx_island)
            idx_island += 1

print(result)
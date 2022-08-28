from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True

    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        cnt_zero = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
                continue
            
            if board[nx][ny] == 0:
                cnt_zero += 1

            else:
                visited[nx][ny] = True
                queue.append([nx, ny])

        change.append([x, y, max(board[x][y] - cnt_zero, 0)])

time = 0

while True:
    cnt_seperated = 0
    visited = [[False] * M for _ in range(N)]
    change = []

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt_seperated += 1

    if cnt_seperated == 0:
        print(0)
        break

    elif cnt_seperated >= 2:
        print(time)
        break
    
    for x, y, v in change:
        board[x][y] = v
    
    time += 1
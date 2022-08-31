from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2]
dy = [0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y):
    visited = [[[False] * (K+1) for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = True

    queue = deque()
    queue.append([x, y, 0, 0])

    while queue:
        x, y, dist, cnt = queue.popleft()

        if x == N-1 and y == M-1:
            return dist
        
        end = 4 if cnt == K else 12

        for i in range(end):
            nx, ny = x + dx[i], y + dy[i]
            plus = 0 if i < 4 else 1

            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny][cnt+plus]:
                continue
            
            if board[nx][ny] == 0:
                queue.append([nx, ny, dist+1, cnt+plus])
                visited[nx][ny][cnt+plus] = True

    return -1

K = int(input())
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

print(bfs(0, 0))
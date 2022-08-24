from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

gram = []
result = float('inf')

visited = [[False] * M for _ in range(N)]
visited[0][0] = True

queue = deque()
queue.append([0, 0, 0])

while queue:
    x, y, dist = queue.popleft()
    
    if x == N-1 and y == M-1: # 공주가 있는 곳
        result = dist
        break

    if board[x][y] == 2: # 그람이 있는 곳
        gram = [x, y, dist]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
            continue
        
        if board[nx][ny] != 1:
            visited[nx][ny] = True
            queue.append([nx, ny, dist+1])

if gram:
    x, y, dist = gram
    result = min(result, dist + abs(N-1 - x) + abs(M-1 - y))

if 0 < result <= T:
    print(result)
else:
    print("Fail")
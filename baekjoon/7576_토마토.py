import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_value = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
            max_value = graph[nx][ny]

zero_in = False
for i in graph:
    if 0 in i:
        zero_in = True
        break
    
if zero_in == True:
    print(-1)
elif max_value == 0:
    print(max_value)
else:
    print(max_value - 1)

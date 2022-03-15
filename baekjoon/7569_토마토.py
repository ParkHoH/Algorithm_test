import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
graph = []
for j in range(H):
    temp_lsit = []
    for i in range(j*N, (j+1)*N):
        temp_lsit.append(list(map(int, sys.stdin.readline().split())))
    graph.append(temp_lsit)

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
max_value = 0
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M or nz < 0 or nz >= H:
            continue
        if graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = graph[z][x][y] + 1
            queue.append((nz, nx, ny))
            max_value = graph[nz][nx][ny]

zero_in = False
for i in graph:
    for j in i:
        if 0 in j:
            zero_in = True
            break
    
if zero_in == True:
    print(-1)
elif max_value == 0:
    print(max_value)
else:
    print(max_value - 1)
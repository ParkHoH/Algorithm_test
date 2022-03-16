from collections import deque
import sys

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    queue = deque()
    queue.append((0, 0, 1))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1
    while queue:
        x, y, w = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 1 and w == 1:
                visited[nx][ny][0] = visited[x][y][w] + 1
                queue.append((nx, ny, 0))
            elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                queue.append((nx, ny, w))
    return -1

print(BFS())


# my solution: 시간 초과
from collections import deque
import sys
import copy

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

L = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            L.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_value = float('inf')
for i, j in L:
    graph_copy = copy.deepcopy(graph)
    graph_copy[i][j] = 0
    queue = deque()
    queue.append((0, 0))
    flag_break = False
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph_copy[nx][ny] == 0:
                graph_copy[nx][ny] = graph_copy[x][y] + 1
                queue.append((nx, ny))
            if nx == N-1 and ny == M-1:
                min_value = min(min_value, graph_copy[N-1][M-1])
                flag_break = True
                break
        if flag_break:  
            break

if min_value == float('inf'):
    print(-1)
else:
    print(min_value + 1)
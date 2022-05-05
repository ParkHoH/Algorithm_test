from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

zero_set = set()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_set.add((i, j))

total_cnt = N * M
one_cnt = total_cnt - len(zero_set) + 3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, copy_graph):
    queue = deque()
    queue.append((x, y))
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue
            
            if not visited[nx][ny] and copy_graph[nx][ny] == 0:
                visited[nx][ny] = True
                copy_graph[nx][ny] = 3
                queue.append((nx, ny))

max_value = 0
for comb in combinations(zero_set, 3):
    for i, j in comb:
        graph[i][j] = 1
    
    copy_graph = deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 2:
                bfs(i, j, copy_graph)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 0:
                cnt += 1
    max_value = max(max_value, cnt)

    for i, j in comb:
        graph[i][j] = 0

print(max_value)
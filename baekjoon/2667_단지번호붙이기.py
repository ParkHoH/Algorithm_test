# DFS solution
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0
    global cnt
    cnt += 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
result = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if dfs(i, j) == True:
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)


# BFS solution
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return cnt

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

L = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            L.append(bfs(i, j))

L.sort()
print(len(L))
for i in range(len(L)):
    print(L[i])
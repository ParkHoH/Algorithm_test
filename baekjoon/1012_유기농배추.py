# DFS solution
import sys

sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True

TC = int(input())
for _ in range(TC):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1
    print(cnt)


# BFS solution
import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
TC = int(input())
for _ in range(TC):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
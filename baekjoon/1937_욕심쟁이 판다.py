# 모든 좌표에서 팬더를 놓아봄
# dfs 를 통해 탐색하는데, 중복 탐색이 있을 수 있어 시간 초과 발생 가능
# dfs 에서 최초의 좌표를 저장하고 막혔을 때 기존 최대 이동횟수를 기존 값과 비교해 저장

import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
dist = [[1] * n for _ in range(n)]

def dfs(x, y, distance):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue
        
        if graph[nx][ny] <= graph[x][y]:
            continue

        if dist[nx][ny] != 1:
            dist[x][y] = max(dist[x][y], distance + 1)

        elif not visited[nx][ny]:
            dist[x][y] = max(dist[x][y], distance + 1)
            visited[nx][ny] = True
            dfs(nx, ny, distance + 1)
            visited[nx][ny] = False

result = 1
for i in range(n):
    for j in range(n):
        visited[i][j] = True
        dfs(i, j, 1)
        result = max(result, dist[i][j])
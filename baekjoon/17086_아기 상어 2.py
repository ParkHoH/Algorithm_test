from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1))
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while queue:
        x, y, distance = queue.popleft()
        for i in range(9):
            dx, dy = direction[i]
            nx, ny = x + dx, y + dy

            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue

            if graph[nx][ny] == 1: # 아기 상어인 경우
                return distance

            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance+1))
            
max_distance = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            max_distance = max(max_distance, bfs(i, j))

print(max_distance)
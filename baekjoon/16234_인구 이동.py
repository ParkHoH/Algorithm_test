from collections import deque

N, L, R = map(int, input().split())
result = 0
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
stack = []

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    plus = graph[x][y]
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue

            if not visited[nx][ny] and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                visited[nx][ny] = True
                stack.append((nx, ny))
                queue.append((nx, ny))
                plus += graph[nx][ny]
                cnt += 1
                
    return plus // cnt

while True:
    changed = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                num = bfs(i, j)
                if stack:
                    graph[i][j] = num
                    changed = True
                    while stack:
                        x, y = stack.pop()
                        graph[x][y] = num

    if not changed:
        break
    
    result += 1
    visited = [[False] * N for _ in range(N)]

print(result)
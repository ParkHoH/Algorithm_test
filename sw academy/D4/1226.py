from copy import deepcopy
from collections import deque

for _ in range(10):
    t = int(input())
    graph = []
    for _ in range(16):
        graph.append(list(map(int, list(input().strip()))))

    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start = [i, j]
            elif graph[i][j] == 3:
                end = [i, j]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    visited = [[False] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = True
    queue = deque()
    queue.append([start[0], start[1], visited])
    while queue:
        if result == 1:
            break

        x, y, visited = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 16 or ny >= 16:
                continue

            if nx == end[0] and ny == end[1]:
                result = 1
                break

            if not visited[nx][ny] and graph[nx][ny] == 0:
                copy_visited = deepcopy(visited)
                copy_visited[nx][ny] = True
                queue.append([nx, ny, copy_visited])

    print(f'#{t} {result}')
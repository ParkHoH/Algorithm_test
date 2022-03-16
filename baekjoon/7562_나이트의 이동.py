from collections import deque
import queue

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

TC = int(input())
for _ in range(TC):
    N = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    a, b = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    graph[a][b] = 0

    def BFS():
        queue = deque()
        queue.append((a, b))
        while queue:
            x, y = queue.popleft()
            if x == dest_x and y == dest_y:
                return graph[x][y]
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    print(BFS())
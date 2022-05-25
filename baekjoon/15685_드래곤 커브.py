n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1
    L = [d]

    for _ in range(g):
        tmp = []
        for i in range(len(L)):
            tmp.append((L[-i - 1] + 1) % 4)
        L.extend(tmp)

    for i in L:
        nx, ny = x + dx[i], y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            result += 1

print(result)
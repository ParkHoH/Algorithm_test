N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dirction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def move(i, j):
    case = set((i, j))
    case.add((i, j))
    location = [i, j]

    while True:
        x, y = location
        dx, dy = dirction[board[x][y]]
        nx, ny = x + dx, y + dy

        if (nx, ny) in case:
            return 1

        if visited[nx][ny]:
            return 0

        visited[nx][ny] = True
        case.add((nx, ny))
        location = [nx, ny]

result = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            result += move(i, j)

print(result)
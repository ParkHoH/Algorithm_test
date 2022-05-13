from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "R":
            red_ball = (i, j)
            graph[i][j] = "."
        elif graph[i][j] == "B":
            blue_ball = (i, j)
            graph[i][j] = "."

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, nx, ny):
    cnt = 0
    while graph[x+nx][y+ny] != "#" and graph[x][y] != "O":
        x += nx
        y += ny
        cnt += 1
    return (x, y, cnt)

def bfs():
    queue = deque()
    r_x, r_y = red_ball
    b_x, b_y = blue_ball
    visited[r_x][r_y][b_x][b_y] = True
    queue.append((r_x, r_y, b_x, b_y, 1))
    while queue:
        r_x, r_y, b_x, b_y, cnt = queue.popleft()
        if cnt > 10:
            continue

        for i in range(4):
            n_r_x, n_r_y, r_cnt = move(r_x, r_y, dx[i], dy[i])
            n_b_x, n_b_y, b_cnt = move(b_x, b_y, dx[i], dy[i])

            if graph[n_b_x][n_b_y] == "O":
                continue
            elif graph[n_r_x][n_r_y] == "O":
                print(cnt)
                return

            if n_b_x == n_r_x and n_b_y == n_r_y:
                if b_cnt > r_cnt:
                    n_b_x -= dx[i]
                    n_b_y -= dy[i]
                else:
                    n_r_x -= dx[i]
                    n_r_y -= dy[i]

            if not visited[n_r_x][n_r_y][n_b_x][n_b_y]:
                visited[n_r_x][n_r_y][n_b_x][n_b_y] = True
                queue.append((n_r_x, n_r_y, n_b_x, n_b_y, cnt+1))
    print(-1)

bfs()
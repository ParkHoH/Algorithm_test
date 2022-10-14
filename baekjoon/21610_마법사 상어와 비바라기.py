from collections import deque

dx = (0, -1, -1, -1, 0, 1, 1, 1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)

ddx = (-1, -1, 1, 1)
ddy = (-1, 1, -1, 1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

water_over = set()
for i in range(N):
    for j in range(N):
        if board[i][j] >= 2: water_over.add((i, j))

def move_cloud(direction, speed):
    new_clouds = []

    for x, y in clouds:
        nx = x + dx[direction] * speed
        ny = y + dy[direction] * speed

        while nx < 0:
            nx += N
        while ny < 0:
            ny += N

        nx %= N
        ny %= N

        new_clouds.append((nx, ny))

    return new_clouds

def increase_water():
    for x, y in clouds:
        board[x][y] += 1

        if board[x][y] == 2:
            water_over.add((x, y))

def water_copy():
    for x, y in clouds:
        cnt = 0

        for i in range(4):
            nx, ny = x + ddx[i], y + ddy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if board[nx][ny]:
                cnt += 1

        board[x][y] += cnt
        if board[x][y] >= 2: water_over.add((x, y))

def make_cloud():
    global clouds

    clouds = set(clouds)
    new_clouds = []
    remove_list = []

    for x, y in water_over:
        if (x, y) in clouds:
            continue
        
        board[x][y] -= 2
        new_clouds.append((x, y))
        if board[x][y] <= 1: remove_list.append((x, y))

    for xy in remove_list:
        water_over.remove(xy)

    clouds = new_clouds

for _ in range(M):
    direction, speed = map(int, input().split())
    direction -= 1

    clouds = move_cloud(direction, speed)
    increase_water()
    water_copy()
    make_cloud()

answer = 0

for i in range(N):
    for j in range(N):
        answer += board[i][j]

print(answer)
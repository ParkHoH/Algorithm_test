from collections import deque
import sys
input = sys.stdin.readline

def fire_expand():
    global fires
    new_fire = []

    for fire in fires:
        for i in range(4):
            x, y = fire
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if miro[nx][ny] == ".":
                miro[nx][ny] = "F"
                new_fire.append([nx, ny])

    fires = new_fire

R, C = map(int, input().split())
miro = []

for _ in range(R):
    miro.append(list(input().rstrip()))

fires = []

for i in range(R):
    for j in range(C):
        if miro[i][j] == "J":
            jihoon = [i, j]
            miro[i][j] = "."

        elif miro[i][j] == "F":
            fires.append([i, j])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
impossible = True
visited = [[False] * C for _ in range(R)]
visited[jihoon[0]][jihoon[1]] = True
queue = deque()
queue.append([jihoon[0], jihoon[1], 0])

while queue:
    x, y, time = queue.popleft()

    if time == cnt:
        fire_expand()
        cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            impossible = False
            break

        if miro[nx][ny] == "." and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append([nx, ny, time+1])

    if not impossible:
        break

if impossible:
    print("IMPOSSIBLE")
else:
    print(time+1)
import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

smell = [[0] * 4 for _ in range(4)]
fish = [[[] for _ in range(4)] for _ in range(4)]
m, s = map(int, input().split())
for _ in range(m):
    x, y, d = map(int, input().split())
    fish[x-1][y-1].append(d-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1


def move_shark(x, y, cnt, del_fish, direction, check):
    global max_del, move_dir
    if cnt == 3:
        if del_fish > max_del:
            move_dir = deepcopy(direction)
            max_del = del_fish
        return

    for d in [2, 0, 6, 4]:
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            continue

        flag = 0
        if [nx, ny] in check:
            flag = 1
        if flag == 0:
            del_fish += len(fish[nx][ny])
        if fish[nx][ny]:
            check.append([nx, ny])
        cnt += 1
        direction.append(d)

        move_shark(nx, ny, cnt, del_fish, direction, check)

        if flag == 0:
            del_fish -= len(fish[nx][ny])
        if fish[nx][ny]:
            check.pop()
        cnt -= 1
        direction.pop()


for k in range(1, s+1):
    fish_before = deepcopy(fish)
    fish_temp = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if fish[i][j]:
                for d in fish[i][j]:
                    flag = 0
                    for _ in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            if not (nx == sx and ny == sy):
                                if smell[nx][ny] == 0:
                                    fish_temp[nx][ny].append(d)
                                    flag = 1
                                    break
                        d = (d + 7) % 8
                    if flag == 0:
                        fish_temp[i][j].append(d)
    fish = fish_temp

    max_del = -1
    move_shark(sx, sy, 0, 0, deque(), deque())

    x, y = sx, sy
    for d in move_dir:
        nx, ny = x + dx[d], y + dy[d]
        if fish[nx][ny]:
            fish[nx][ny] = []
            smell[nx][ny] = k
        x, y = nx, ny
    sx, sy = x, y

    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                if k - smell[i][j] == 2:
                    smell[i][j] = 0

    for i in range(4):
        for j in range(4):
            if fish_before[i][j]:
                for d in fish_before[i][j]:
                    fish[i][j].append(d)

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(fish[i][j])
print(ans)
from copy import deepcopy
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx2 = [1, 0, -1, 0]
dy2 = [0, 1, 0, -1]


def move_beads(sx, sy):
    global a
    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    beads = [a[x][y]] if a[x][y] != 0 else []
    while True:
        nx = x + dx2[idx]
        ny = y + dy2[idx]
        if a[nx][ny] != 0:
            beads.append(a[nx][ny])

        x, y = nx, ny
        if x == 0 and y == 0:
            break

        idx, cnt, move, turn = change_dir(idx, cnt, move, turn)

    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    a = [[0] * n for _ in range(n)]
    if beads:
        a[x][y] = beads[0]
        for b in beads[1:]:
            nx = x + dx2[idx]
            ny = y + dy2[idx]
            a[nx][ny] = b

            x, y = nx, ny
            idx, cnt, move, turn = change_dir(idx, cnt, move, turn)


def del_beads(sx, sy):
    global ans1, ans2, ans3
    x, y = sx, sy - 1
    idx, cnt, move, turn, flag = 0, 0, 1, 1, 0
    q = []
    while True:
        if not q:
            q.append([x, y])
        nx = x + dx2[idx]
        ny = y + dy2[idx]
        if a[nx][ny] == a[x][y]:
            q.append([nx, ny])
            if nx == 0 and ny == 0:
                if len(q) >= 4:
                    flag = 1
                    for i, j in q:
                        if a[i][j] == 1:
                            ans1 += 1
                        elif a[i][j] == 2:
                            ans2 += 1
                        elif a[i][j] == 3:
                            ans3 += 1
                        a[i][j] = 0

        elif a[nx][ny] != a[x][y]:
            if len(q) >= 4:
                flag = 1
                for i, j in q:
                    if a[i][j] == 1:
                        ans1 += 1
                    elif a[i][j] == 2:
                        ans2 += 1
                    elif a[i][j] == 3:
                        ans3 += 1
                    a[i][j] = 0
            q = []

        x, y = nx, ny
        if (x == 0 and y == 0) or a[x][y] == 0:
            return flag

        idx, cnt, move, turn = change_dir(idx, cnt, move, turn)


def change_dir(idx, cnt, move, turn):
    cnt += 1
    if cnt == turn:
        idx = (idx + 1) % 4
        cnt = 0
        move += 1
        if move % 2 == 0:
            turn += 1
            move = 0

    return idx, cnt, move, turn


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
sx, sy = n // 2, n // 2

ans1, ans2, ans3 = 0, 0, 0
for _ in range(m):
    d, s = map(int, input().split())
    d -= 1

    for k in range(1, s + 1):
        nx = sx + k * dx[d]
        ny = sy + k * dy[d]
        if not 0 <= nx < n or not 0 <= ny < n:
            break
        a[nx][ny] = 0

    while True:
        move_beads(sx, sy)
        flag = del_beads(sx, sy)
        if flag == 0:
            break

    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    flag, temp = 0, []
    while True:
        if not flag:
            beads_num, beads_cnt = a[x][y], 1
            flag = 1
        nx = x + dx2[idx]
        ny = y + dy2[idx]
        if a[nx][ny] == a[x][y]:
            beads_cnt += 1
            if nx == 0 and ny == 0:
                temp.append(beads_cnt)
                temp.append(beads_num)
        else:
            temp.append(beads_cnt)
            temp.append(beads_num)
            flag = 0

        x, y = nx, ny
        if (x == 0 and y == 0) or a[x][y] == 0:
            break
        idx, cnt, move, turn = change_dir(idx, cnt, move, turn)

    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    a = [[0] * n for _ in range(n)]
    if temp:
        a[x][y] = temp[0]
        for k in temp[1:]:
            nx = x + dx2[idx]
            ny = y + dy2[idx]
            a[nx][ny] = k

            x, y = nx, ny
            if x == 0 and y == 0:
                break
            idx, cnt, move, turn = change_dir(idx, cnt, move, turn)

print(ans1 + 2 * ans2 + 3 * ans3)
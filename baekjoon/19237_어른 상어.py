import sys

input = sys.stdin.readline
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())

a, shark = [], [[] for _ in range(m)]
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j]:
            shark[a[i][j]-1].extend([i, j])
            a[i][j] = [a[i][j], k]

d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(d[i])

dir = [[] for _ in range(m)]
idx = -1
for i in range(4*m):
    if i % 4 == 0:
        idx += 1
    dir[idx].append(list(map(int, input().split())))

ans = 0
while True:
    ans += 1
    if ans == 1001:
        print(-1)
        break

    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if shark[i] != 0:
            x, y, d, flag = shark[i][0], shark[i][1], shark[i][2], 0
            for j in range(4):
                ndir = dir[i][d-1][j]
                nx, ny = x + dx[ndir], y + dy[ndir]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == 0:
                        flag = 1
                        break
            if flag == 0:
                for j in range(4):
                    ndir = dir[i][d-1][j]
                    nx, ny = x + dx[ndir], y + dy[ndir]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny][0] == i+1:
                            break

            if check[nx][ny]:
                if check[nx][ny] < i+1:
                    shark[i] = 0
                else:
                    shark[check[nx][ny]-1] = 0
            else:
                check[nx][ny] = i+1
                shark[i] = [nx, ny, ndir]

    for i in range(n):
        for j in range(n):
            if a[i][j]:
                a[i][j][1] -= 1
                if a[i][j][1] == 0:
                    a[i][j] = 0

    for i in range(m):
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            a[x][y] = [i+1, k]

    if shark.count(0) == m-1:
        print(ans)
        break
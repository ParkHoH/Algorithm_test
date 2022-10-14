from itertools import combinations
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

board = [list(input()) for _ in range(5)]
candidate = [(x, y) for x in range(5) for y in range(5)]

def check_dasom_cnt(comb):
    cnt = 0

    for x, y in comb:
        if board[x][y] == "S":
            cnt += 1

    return True if cnt >= 4 else False

def check_adj(comb):
    x, y = comb[0]
    cnt = 1

    visited = [[False] * 7 for _ in range(7)]
    visited[x][y] = True

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= 7 or ny >= 7 or visited[nx][ny]:
                continue

            if (nx, ny) in comb:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    return True if cnt == 7 else False

answer = 0

for comb in combinations(candidate, 7):
    if check_dasom_cnt(comb):
        if check_adj(comb):
            answer += 1

print(answer)
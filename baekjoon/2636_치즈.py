from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def mark_outer(x, y):
    board[x][y] = -1

    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if board[nx][ny] == 0:
                board[nx][ny] = -1
                queue.append([nx, ny])

def remove_cheese():
    step = 0
    ori_len = len(cheese)
    remove_list = []

    while step != ori_len:
        x, y = cheese.popleft()
        cnt_outer = 0
        step += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if board[nx][ny] == -1:
                cnt_outer = 1
                break

        if cnt_outer == 1:
            remove_list.append([x, y])
        else:
            cheese.append([x, y])

    for x, y in remove_list:
        mark_outer(x, y)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cheese = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheese.append([i, j])

mark_outer(0, 0)
time = 0
cnt_cheese = 0

while cheese:
    cnt_cheese = len(cheese)
    remove_cheese()
    time += 1

print(time)
print(cnt_cheese)
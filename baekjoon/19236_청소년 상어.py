from copy import deepcopy
from collections import deque

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

board = [[[0, 0] for _ in range(4)] for _ in range(4)]
fishes_xy = {}

for i in range(4):
    info = list(map(int, input().split()))

    for j in range(4):
        fish = info[2*j]
        dir = info[2*j+1]-1

        board[i][j] = [fish, dir]
        fishes_xy[fish] = (i, j)

removed_fish = board[0][0][0]
fishes_xy[removed_fish] = (-1, -1)
board[0][0][0] = -1

fishes = deque()
for i in range(1, 17):
    fishes.append(i)

def move_fish(fishes, board, fishes_xy):
    new_fishes = deque()

    for fish in fishes:
        x, y = fishes_xy[fish]

        if x == -1 and y == -1:
            continue
        
        new_fishes.append(fish)
        dir = board[x][y][1]
        
        for i in range(dir, dir+8):
            nx = x + dx[i%8]
            ny = y + dy[i%8]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or board[nx][ny][0] == -1:
                continue
            
            board[x][y][1] = i % 8
            fishes_xy[board[x][y][0]] = (nx, ny)
            fishes_xy[board[nx][ny][0]] = (x, y)
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            break
    
    return new_fishes

def dfs(x, y, sum_eat, fishes, shark, board, fishes_xy):
    global answer
    answer = max(answer, sum_eat)

    fishes = move_fish(fishes, board, fishes_xy)
    x, y = shark
    dir = board[x][y][1]

    while True:
        x += dx[dir]
        y += dy[dir]

        if x < 0 or y < 0 or x >= 4 or y >= 4:
            break

        if board[x][y][0] > 0:
            new_board = deepcopy(board)

            ori_fish = new_board[x][y][0]
            new_board[x][y][0] = -1
            new_board[shark[0]][shark[1]][0] = 0

            copied_fishes_xy = deepcopy(fishes_xy)
            copied_fishes_xy[ori_fish] = (-1, -1)
            
            dfs(x, y, sum_eat + ori_fish, fishes, (x, y), new_board, copied_fishes_xy)

answer = removed_fish
dfs(0, 0, removed_fish, fishes, (0, 0), board, fishes_xy)

print(answer)
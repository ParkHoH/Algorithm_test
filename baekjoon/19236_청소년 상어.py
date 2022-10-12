# 물고기 번호에 따른 좌표: dict
# board에 물고기 번호 표시, 상어는 -1, 빈칸은 0
# dfs를 통해 모든 경우 탐색
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

fishes = [i for i in range(1, 17)]
fishes_xy = {}
board = [[[] for _ in range(4)] for _ in range(4)] # 물고기 번호, 방향

for i in range(4):
    temp = list(map(int, input().split()))

    for j in range(4):
        idx = 2*j
        board[i][j] = [temp[idx], temp[idx+1]-1]
        fishes_xy[temp[idx]] = (i, j)

# fishes_xy[board[0][0][0]] = (-1, -1)
board[0][0][0] = -1
shark = (0, 0)

def move_fish(shark_x, shark_y, fishes):
    new_fishes = []
    
    for fish in fishes:
        x, y = fishes_xy[fish]

        if x == shark[0] and y == shark[1]:
            continue

        new_fishes.append(fish)
        dir = board[x][y][1]

        for i in range(8):
            nx = x + dx[(dir+i)%8]
            ny = y + dy[(dir+i)%8]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or board[nx][ny][0] == -1:
                continue
            
            board[x][y][1] = (board[x][y][1] + i) % 8
            opp_fish = board[nx][ny][0]
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            fishes_xy[fish], fishes_xy[opp_fish] = fishes_xy[opp_fish], fishes_xy[fish]
            break

    fishes = new_fishes

def dfs(x, y, eat_cnt):
    move_fish(x, y, fishes)

    shark_dir = board[x][y]
    while True:
        i_cnt = 1
        

        nx = x + dx[]

    move_shark()
    return

dfs(0, 0, 1, fishes)
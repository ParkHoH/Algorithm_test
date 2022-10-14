from collections import deque

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
# 동 서 북 남

N, M, K = map(int, input().split()) 
board = [list(map(int, input().split())) for _ in range(N)]
dice = [1, 6, 3, 4, 5, 2] # 0위, 1아래, 2동, 3서, 4남, 5북
    #  (1, 6, 3, 4, 5, 2)

dice_xy = (0, 0)
direction = 1
score = 0

def turn(direction): # 0위, 1아래, 2동, 3서, 4남, 5북
    global dice
    if direction == 1:
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
    elif direction == 2:
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    elif direction == 3:
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    else:
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]

def cal_score(x, y):
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    queue = deque()
    queue.append((x, y))
    
    standard = board[x][y]
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
                continue
            
            if board[nx][ny] == standard:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    return standard * cnt

def decide_dir(direction):
    A = dice[1]
    B = board[dice_xy[0]][dice_xy[1]]
    # 동 서 북 남
    if A > B: # 90도 시계 방향 회전
        if direction == 1:
            direction = 4
        elif direction == 2:
            direction = 3
        elif direction == 3:
            direction = 1
        else:
            direction = 2

    elif A < B: # 90도 반시계 방향 회전
        if direction == 1:
            direction = 3
        elif direction == 2:
            direction = 4
        elif direction == 3:
            direction = 2
        else:
            direction = 1

    return direction

for _ in range(K):
    nx = dice_xy[0] + dx[direction-1]
    ny = dice_xy[1] + dy[direction-1]

    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        nx = dice_xy[0] - dx[direction-1]
        ny = dice_xy[1] - dy[direction-1]

        if direction == 1:
            direction = 2
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 4
        else:
            direction = 3

    dice_xy = (nx, ny)
    
    turn(direction)
    score += cal_score(dice_xy[0], dice_xy[1])
    direction = decide_dir(direction)

print(score)
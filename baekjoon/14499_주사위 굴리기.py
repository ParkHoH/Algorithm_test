dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

N, M, dice_x, dice_y, K = map(int, input().split()) 
board = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0] # 0아래, 1위, 2동, 3서, 4남, 5북
    #  (1, 6, 3, 4, 5, 2)

def turn(order):
    global dice
    if order == 1:
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    elif order == 2:
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
    elif order == 3:
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
    else:
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]

for order in orders:
    nx = dice_x + dx[order-1]
    ny = dice_y + dy[order-1]

    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue

    turn(order)

    if board[nx][ny] == 0:
        board[nx][ny] = dice[0]
    else:
        dice[0] = board[nx][ny]
        board[nx][ny] = 0

    dice_x, dice_y = nx, ny
    print(dice[1])
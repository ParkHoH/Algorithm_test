import sys
input = sys.stdin.readline

dir = {
    1: [-1, 0], # 위
    2: [1, 0], # 아래
    3: [0, 1], # 오른쪽
    4: [0, -1]  # 왼쪽
}
change_dir = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

def move():
    new_board = [[[False, 0, 0, 0] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j][0]: # 상어
                speed, direction, size = board[i][j][1:4]

                if direction == 2:
                    if speed >= R-1-i:
                        direction = change_dir[direction]
                        x = (R-1) - (speed - (R-1-i))
                    else:
                        x = R-1-i + speed

                    new_board = check_exist(x, j, speed, direction, size, new_board)
                
                elif direction == 1:
                    if speed >= i:
                        direction = change_dir[direction]
                        x = 

    return new_board


def check_exist(x, y, speed, direction, size, new_board):
    if new_board[x][y][0]:
        M -= 1
        if size > new_board[x][y][3]:
            new_board[x][y][0] = [True, speed, direction, size]
    else:
        new_board[x][y][0] = [True, speed, direction, size]

    return new_board

R, C, M = map(int, input().split())
board = [[[False, 0, 0, 0] for _ in range(C)] for _ in range(R)] # 방문 여부 / 속력 / 방향 / 크기

r_mod = (R-1) * 2
c_mod = (C-1) * 2

for _ in range(M):
    r, c, speed, direction, size = map(int, input().split())
    if direction == 1 or direction == 2:
        speed %= r_mod
    else:
        speed %= c_mod
    board[r-1][c-1] = [True, speed, direction, size]

result = 0
# 1. 낚시왕 이동
for king in range(C):
    if M == 0:
        break

    # 2. 물고기 잡기
    for i in range(R):
        if board[i][king][0]:
            result += board[i][king][3]
            board[i][king][0] = False
            M -= 1
            break

    # 3. 상어 이동
    board = move()

print(result)
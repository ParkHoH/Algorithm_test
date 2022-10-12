from collections import deque

# board에 물고기 수 count로 기록
# 상어가 이동하면 board 숫자 0 이상이면 0으로 만들기 -> 이 때 시간 기록하기
# 물고기 이동할 때 board가 0이면 continue

dx_fish = (0, -1, -1, -1, 0, 1, 1, 1)
dy_fish = (-1, -1, 0, 1, 1, 1, 0, -1)

dx_shark = (-1, 0, 1, 0)
dy_shark = (0, -1, 0, 1)

M, S = map(int, input().split())
fishes = deque()
board = [[[0, 0] for _ in range(4)] for _ in range(4)] # 물고기 수, 흔적 시간

for _ in range(M):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    fishes.append([x, y, d])
    board[x][y][0] += 1

shark = list(map(int, input().split()))
shark[0] -= 1
shark[1] -= 1

def move_fish(time):
    copied_fishes = []
    cnt = len(fishes)

    while cnt:
        cnt -= 1
        x, y, d = fishes.popleft()

        if board[x][y][0] == 0: # 상어가 먹은 경우
            continue

        copied_fishes.append([x, y, d])
        is_moved = False

        for i in range(8):
            nx = x + dx_fish[d-i]
            ny = y + dy_fish[d-i]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4: # 격자 범위 벗어남
                continue

            if nx == shark[0] and ny == shark[1]: # 상어 자리
                continue

            if board[nx][ny][1] == 0 or board[nx][ny][1] + 2 < time: # 물고기 냄새 없거나 시간 다 된 경우
                board[x][y][0] -= 1
                board[nx][ny][0] += 1
                d = d-i if d-i >= 0 else 8+(d-i)
                fishes.append([nx, ny, d])
                is_moved = True
                break
        
        if not is_moved:
            fishes.append([x, y, d])

    return copied_fishes

def permu(x, y, cnt, eat_cnt, dir):
    if cnt == 3:
        candidate.append([eat_cnt, dir])
        return

    for i in range(4):
        nx = x + dx_shark[i]
        ny = y + dy_shark[i]

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4: # 격자 범위 벗어남
            continue

        temp = board[nx][ny][0]
        board[nx][ny][0] = 0
        permu(nx, ny, cnt+1, eat_cnt+temp, dir+str(i+1))
        board[nx][ny][0] = temp

def move_shark(time):
    global shark, candidate
    x, y = shark
    candidate = []

    permu(x, y, 0, 0, "")
    candidate.sort(key=lambda x: (-x[0], int(x[1])))

    for dir in candidate[0][1]:
        nx = x + dx_shark[int(dir)-1]
        ny = y + dy_shark[int(dir)-1]

        shark = [nx, ny]
        x, y = shark

        if board[x][y][0] != 0:
            board[x][y] = [0, time]

    cnt = len(fishes)
    while cnt:
        cnt -= 1
        x, y, d = fishes.popleft()

        if board[x][y][0] == 0: # 상어가 먹은 경우
            continue
        fishes.append([x, y, d])

def copy_fish(copied_fishes):
    for x, y, d in copied_fishes:
        fishes.append([x, y, d])
        board[x][y][0] += 1

for time in range(1, S+1):
    copied_fishes = move_fish(time)
    move_shark(time)
    copy_fish(copied_fishes)

answer = 0

for i in range(4):
    for j in range(4):
        answer += board[i][j][0]

print(answer)
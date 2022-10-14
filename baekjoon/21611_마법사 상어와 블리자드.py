dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, -1, 1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]

n_to_ball = [-1] * (N**2-1)
xy_to_n = {}
removed_balls = [0, 0, 0, 0]

def init():
    init_dx = (0, 1, 0, -1)
    init_dy = (-1, 0, 1, 0)

    total_cnt = 0
    dir_cnt = 0
    dir = 0
    limit = 1
    limit_cnt = 0

    x = y = int(N/2)

    while total_cnt != N**2-1:
        x += init_dx[dir]
        y += init_dy[dir]

        n_to_ball[total_cnt] = board[x][y]
        xy_to_n[(x, y)] = total_cnt

        total_cnt += 1
        dir_cnt += 1

        if dir_cnt == limit:
            dir = (dir+1) % 4
            dir_cnt = 0
            limit_cnt += 1

        if limit_cnt == 2:
            limit_cnt = 0
            limit += 1

def cast_magic(dir, speed):
    x = y = int(N/2)

    for _ in range(speed):
        x += dx[dir]
        y += dy[dir]

        n = xy_to_n[(x, y)]
        # removed_ball = n_to_ball[n]

        # if removed_ball == -1:
        if n_to_ball[n] == -1:
            break

        # removed_balls[removed_ball] += 1
        n_to_ball[n] = -1

def arrange():
    global n_to_ball

    removed_cnt = n_to_ball.count(-1)
    new_n_to_ball = []

    for ball in n_to_ball:
        if ball != -1:
            new_n_to_ball.append(ball)
    
    new_n_to_ball += [-1] * removed_cnt
    n_to_ball = new_n_to_ball

def remove_candidate(candidate):
    if len(candidate) < 4:
        return False

    removed_balls[n_to_ball[candidate[0]]] += len(candidate)

    for n in candidate:
        n_to_ball[n] = -1

    return True

def explode_marbles():
    candidate = [0]
    exploded = False

    for i in range(1, len(n_to_ball)):
        if n_to_ball[i] <= 0:
            if remove_candidate(candidate):
                exploded = True
            break

        if n_to_ball[i] == n_to_ball[i-1]:
            candidate.append(i)
        else:
            if remove_candidate(candidate):
                exploded = True
            candidate = [i]

    return True if exploded else False

def change_marbles():
    global n_to_ball

    candidate = [0]
    new_n_to_ball = []

    for i in range(1, len(n_to_ball)):
        if n_to_ball[i] <= 0:
            if len(new_n_to_ball) >= N**2: break
            new_n_to_ball.append(len(candidate))

            if len(new_n_to_ball) >= N**2: break
            new_n_to_ball.append(n_to_ball[candidate[0]])

            break

        if n_to_ball[i] == n_to_ball[i-1]:
            candidate.append(i)
        else:
            if len(new_n_to_ball) >= N**2: break
            new_n_to_ball.append(len(candidate))

            if len(new_n_to_ball) >= N**2: break
            new_n_to_ball.append(n_to_ball[candidate[0]])

            candidate = [i]
    
    if len(new_n_to_ball) < N**2 - 1:
        diff = (N**2 - 1) - len(new_n_to_ball)
        new_n_to_ball += [-1] * diff

    n_to_ball = new_n_to_ball

init()
for dir, speed in magics:
    cast_magic(dir, speed)
    arrange()

    while True:
        if not explode_marbles():
            break
        arrange()
    
    change_marbles()

print(sum([removed_balls[i] * i for i in range(1, 4)]))
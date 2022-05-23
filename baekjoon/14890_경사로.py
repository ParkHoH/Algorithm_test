N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0
for i in range(N):
    cnt = 1
    stop = False
    needed_cnt = 0
    for j in range(1, N):
        if board[i][j] == board[i][j-1]:
            if needed_cnt:
                needed_cnt -= 1
                continue
            cnt += 1
        elif board[i][j] - board[i][j-1] == 1 and cnt >= L:
            if needed_cnt:
                stop = True
                break
            cnt = 1
        elif board[i][j] - board[i][j-1] == -1:
            if needed_cnt:
                stop = True
                break
            cnt = 0
            needed_cnt = L-1
        else:
            stop = True
            break

    if stop or needed_cnt: continue
    result += 1

for j in range(N):
    cnt = 1
    stop = False
    needed_cnt = 0
    for i in range(1, N):
        if board[i][j] == board[i-1][j]:
            if needed_cnt:
                needed_cnt -= 1
                continue
            cnt += 1
        elif board[i][j] - board[i-1][j] == 1 and cnt >= L:
            if needed_cnt:
                stop = True
                break
            cnt = 1
        elif board[i][j] - board[i-1][j] == -1:
            if needed_cnt:
                stop = True
                break
            cnt = 0
            needed_cnt = L-1
        else:
            stop = True
            break

    if stop or needed_cnt: continue
    result += 1

print(result)

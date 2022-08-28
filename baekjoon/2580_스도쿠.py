board = [list(map(int, input().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i, j])

def check_row(r, num):
    for i in range(9):
        if board[r][i] == num:
            return False
    
    return True

def check_column(c, num):
    for i in range(9):
        if board[i][c] == num:
            return False
    
    return True

def check_rect(r, c, num):
    mod_r = r // 3
    mod_c = c // 3

    for i in range(3*mod_r, 3*mod_r + 3):
        for j in range(3*mod_c, 3*mod_c + 3):
            if board[i][j] == num:
                return False

    return True

def dfs(cnt):
    if cnt == len(zero):
        return True

    for num in range(1, 10):
        r, c = zero[cnt]
        if check_row(r, num) and check_column(c, num) and check_rect(r, c, num):
            board[r][c] = num
            if dfs(cnt+1):
                return True
            board[r][c] = 0

    return False

dfs(0)

for i in range(9):
    print(*board[i])
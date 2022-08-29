# 주의 사항
# 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.
# 전선은 절대로 교차해서는 안 된다
# 최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이 합을 구하고자 한다.
# 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.

# -----------------------
# 풀이
# 4방향 중에 하나로 연결되는 경우와 연결되지 않는 경우 모두 subset으로 탐색
# 빨리 끝내기 위해 연결이 되는 경우부터 최선의 해를 찾아나가기 시작함
# result에는 [연결 코어수, 라인의 길이]를 저장하고, 만약 남은 걸 다 연결해도 현재 연결 코어수를 넘지 못하는 경우 return

def erase(x, y, idx):
    if idx == 0:
        for i in range(x):
            board[i][y] = 0

    if idx == 1:
        for i in range(x+1, N):
            board[i][y] = 0
    
    if idx == 2:
        for j in range(y):
            board[x][j] = 0
    
    if idx == 3:
        for j in range(y+1, N):
            board[x][j] = 0

def mark(x, y, idx):
    cnt = 0

    if idx == 0:
        for i in range(x):
            if board[i][y] != 0:
                for j in range(i):
                    board[j][y] = 0
                
                return -1
            
            board[i][y] = -1
            cnt += 1

    elif idx == 1:
        for i in range(x+1, N):
            if board[i][y] != 0:
                for j in range(x+1, i):
                    board[j][y] = 0

                return -1

            board[i][y] = -1
            cnt += 1

    elif idx == 2:
        for j in range(y):
            if board[x][j] != 0:
                for i in range(j):
                    board[x][i] = 0
                
                return -1
            
            board[x][j] = -1
            cnt += 1

    elif idx == 3:
        for j in range(y+1, N):
            if board[x][j] != 0:
                for i in range(y+1, j):
                    board[x][i] = 0

                return -1

            board[x][j] = -1
            cnt += 1

    return cnt

def subset(idx, cnt_connected, sum_lines):
    global result

    if idx == len(cores):
        if cnt_connected > result[0]:
            result = [cnt_connected, sum_lines]
        elif cnt_connected == result[0]:
            result[1] = min(result[1], sum_lines)

        return

    if cnt_connected + (len(cores)-idx) < result[0]:
        return

    for i in range(5):
        if i == 4:
            subset(idx+1, cnt_connected, sum_lines)
        
        else:
            standard_x, standard_y = cores[idx]
            plus_line = mark(standard_x, standard_y, i)
            if plus_line != -1:
                subset(idx+1, cnt_connected+1, sum_lines + plus_line)
                erase(standard_x, standard_y, i)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j] == 1:
                cores.append([i, j])

    result = [0, 0] # 연결된 코어 수, 라인의 길이

    subset(0, 0, 0)

    print(f'#{tc} {result[1]}')
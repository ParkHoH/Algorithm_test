from collections import deque

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
score = 0

while True:
    stop = True
    visited = [[False] * N for _ in range(N)]

    max_block = 0
    max_rainbow = 0
    max_group = []

    def bfs(x, y): # 연결된 블록 찾기
        cnt_block = 1
        cnt_rainbow = 0
        color_idx = board[x][y]

        back_rainbow = []
        group = []
        group.append((x, y))

        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                    continue
                
                if board[nx][ny] == 0 or board[nx][ny] == color_idx:
                    if board[nx][ny] == 0: 
                        cnt_rainbow += 1
                        back_rainbow.append((nx, ny))

                    cnt_block += 1
                    group.append((nx, ny))

                    visited[nx][ny] = True
                    queue.append((nx, ny))

        for x, y in back_rainbow:
            visited[x][y] = False

        return (cnt_block, cnt_rainbow, group)

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                visited[i][j] = True
                cnt_block, cnt_rainbow, group = bfs(i, j)
                
                if cnt_block >= 2: 
                    stop = False

                    if max_block < cnt_block:
                        max_block = cnt_block
                        max_rainbow = cnt_rainbow
                        max_group = group

                    elif max_block == cnt_block:
                        if max_rainbow <= cnt_rainbow:
                            max_rainbow = cnt_rainbow
                            max_group = group

    if stop: break
    else: score += max_block ** 2

    for x, y in max_group:
        board[x][y] = -2

    def set_gravity(): # 중력 작용
        for y in range(N):
            queue = deque()

            for x in range(N-1, -1, -1):
                if board[x][y] == -2:
                    queue.append((x, y))
                
                elif board[x][y] == -1:
                    queue = deque()

                elif queue:
                    repl_x, repl_y = queue.popleft()
                    board[repl_x][repl_y], board[x][y] = board[x][y], board[repl_x][repl_y]
                    queue.append((x, y))
    
    set_gravity()

    new_board = [[0] * N for _ in range(N)]

    for x in range(N): # 반시계 방향 회전
        for y in range(N):
            new_board[N-y-1][x] = board[x][y]

    board = new_board

    set_gravity()

print(score)
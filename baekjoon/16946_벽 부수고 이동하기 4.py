from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[False, -1, -1, 0] for _ in range(M)] for _ in range(N)] # 방문 여부, 그룹, cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i_idx, j_idx):
    L = [[i_idx, j_idx]]
    queue = deque()
    queue.append([i_idx, j_idx])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if board[nx][ny] == "1":
                continue

            if not visited[nx][ny][0]:
                visited[nx][ny][0] = True
                visited[nx][ny][1] = i_idx
                visited[nx][ny][2] = j_idx
                L.append([nx, ny])
                queue.append([nx, ny])

    cnt = len(L) % 10
    for x, y in L:
        visited[x][y][3] = cnt

def find_cnt(x, y):
    case = set()
    sum = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if board[nx][ny] != "0":
            continue
        
        r, c = visited[nx][ny][1], visited[nx][ny][2]
        if (r, c) not in case:
            case.add((r, c))
            sum += visited[nx][ny][3]

    return sum % 10

for i in range(N):
    for j in range(M):
        if board[i][j] == "0" and not visited[i][j][0]:
            visited[i][j][0] = True
            visited[i][j][1] = i
            visited[i][j][2] = j
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if board[i][j] == "1":
            board[i][j] = str(find_cnt(i, j))

for i in range(N):
    print(''.join(board[i]))
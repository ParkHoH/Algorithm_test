from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[False, -1, -1, 0] for _ in range(M)] for _ in range(N)] # 방문 여부, 그룹, cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    L = [[i, j]]
    queue = deque()
    queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
        
            if not visited[nx][ny]:
                visited[nx][ny][0] = True
                visited[nx][ny][1] = i
                visited[nx][ny][2] = j
                L.append([nx, ny])
                queue.append([nx, ny])

    


for i in range(N):
    for j in range(M):
        if board[i][j] == "0" and not visited[i][j][0]:
            visited[i][j][0] = True
            visited[i][j][1] = i
            visited[i][j][2] = j
            # dfs(i, j)
            bfs(i, j)

print()
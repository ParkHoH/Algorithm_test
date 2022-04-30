import sys

N, M = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]
result = 0
max_value = max(map(max, L))

def dfs(x, y, cnt, cumu_num):
    global result
    if result >= cumu_num + max_value * (3 - cnt):
        return
    if cnt == 3 and cumu_num > result:
        result = cumu_num
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or ny >= M or nx < 0 or ny < 0:
            continue
        if not visited[nx][ny]:
            if cnt == 1:
                visited[nx][ny] = True
                dfs(x, y, cnt+1, cumu_num+L[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, cumu_num+L[nx][ny])
            visited[nx][ny] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, L[i][j])
        visited[i][j] = False

print(result)
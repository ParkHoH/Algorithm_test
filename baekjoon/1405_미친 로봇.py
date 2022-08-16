temp = list(map(int, input().split()))
N = temp[0]
percent = [] # 동서남북
for i in range(1, 5):
    percent.append(temp[i] / 100)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
visited = [[False] * (2*N + 1) for _ in range(2*N + 1)]
result = cnt = 0

def dfs(x, y, depth, cum_percent):
    if depth == N:
        global result, cnt
        result += cum_percent
        cnt += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if percent[i] == 0:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, cum_percent * percent[i])
            visited[nx][ny] = False

visited[N][N] = True
dfs(N, N, 0, 1)

print(result)
print(cnt)
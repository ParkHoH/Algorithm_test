board = [input() for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt_S, cnt_Y, depth):
    if depth == 7 and cnt_S > cnt_Y:
        global result
        result += 1
        return
    
    if cnt_Y >= 4:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visited[nx][ny]:
            continue

        visited[nx][ny] = True
        
        if board[nx][ny] == "S":
            dfs(nx, ny, cnt_S+1, cnt_Y, depth+1)
        else:
            dfs(nx, ny, cnt_S, cnt_Y+1, depth+1)

        visited[nx][ny] = False

result = 0
visited = [[False] * 5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        visited[i][j] = True

        if board[i][j] == "S":
            dfs(i, j, 1, 0, 1)
        else:
            dfs(i, j, 0, 1, 1)

        visited[i][j] = False

print(result)
def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    min_cost = []

    def dfs(x, y, cost, direction, visited):
        visited[x][y] = True
        if x == y == len(board)-1:
            min_cost.append(cost)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
                continue
            if visited[nx][ny] == False:
                if i == 0 or i == 1:
                    if direction == "" or direction == "updown":
                        dfs(nx, ny, cost+100, "updown", visited)
                    else:
                        dfs(nx, ny, cost+500, "updown", visited)
                else:
                    if direction == "" or direction == "rightleft":
                        dfs(nx, ny, cost+100, "rightleft", visited)
                    else:
                        dfs(nx, ny, cost+500, "rightleft", visited)

    visited = [[False] * len(board) for _ in range(len(board))]
    dfs(0, 0, 0, "", visited)
    return min_cost

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
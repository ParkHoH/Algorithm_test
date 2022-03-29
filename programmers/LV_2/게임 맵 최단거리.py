from collections import deque
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps):
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(maps) or nx < 0 or ny >= len(maps[0]) or ny < 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[-1][-1]

def solution(maps):
    return bfs(maps) if bfs(maps) != 1 else -1
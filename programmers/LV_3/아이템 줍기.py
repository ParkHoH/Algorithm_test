# bfs 솔루션
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = r
        for i in range(x1*2, x2*2 + 1):
            for j in range(y1*2, y2*2 + 1):
                graph[j][i] = 1

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    visited = [[False] * 102 for _ in range(102)]
    visited[characterY][characterX] = True
    queue = deque()
    queue.append([characterX, characterY, 0])
    while queue:
        x, y, cost = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == itemX and ny == itemY:
                return (cost+1) // 2 

            if nx < 0 or ny < 0 or nx >= 101 or ny >= 101:
                continue
            
            if visited[ny][nx] or graph[ny][nx] == 0:
                continue
                
            cnt = 0
            for j in range(8):
                if graph[ny + dy[j]][nx + dx[j]] == 1:
                    cnt += 1
            
            if cnt != 8:
                visited[ny][nx] = True
                queue.append([nx, ny, cost+1])


# dfs 솔루션
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = r
        for i in range(x1*2, x2*2 + 1):
            for j in range(y1*2, y2*2 + 1):
                graph[j][i] = 1

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    visited = [[False] * 102 for _ in range(102)]
    visited[characterY][characterX] = True
    result = []

    def dfs(x, y, cost):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == itemX and ny == itemY:
                result.append((cost+1) // 2)
                return

            if nx < 0 or ny < 0 or nx >= 101 or ny >= 101:
                continue
            
            if visited[ny][nx] or graph[ny][nx] == 0:
                continue
                
            cnt = 0
            for j in range(8):
                if graph[ny + dy[j]][nx + dx[j]] == 1:
                    cnt += 1
            
            if cnt != 8:
                visited[ny][nx] = True
                dfs(nx, ny, cost+1)

    dfs(characterX, characterY, 0)
    return min(result)

print(solution(	[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
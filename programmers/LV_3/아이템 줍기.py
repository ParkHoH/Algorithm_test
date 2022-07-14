from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 101 for _ in range(101)]
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

    visited = [[False] * 101 for _ in range(101)]
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


print(solution(	[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))


# from collections import deque

# def solution(rectangle, characterX, characterY, itemX, itemY):
#     answer = 0
#     board = [[0] * 101 for i in range(101)]
#     cX = 2 * characterX
#     cY = 2 * characterY
#     iX = 2 * itemX
#     iY = 2 * itemY
#     d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     visited = [[0] * 101 for i in range(101)]
#     visited[cX][cY] = 1
#     queue = deque([(cX, cY)])
    
#     for x1, y1, x2, y2 in rectangle:
#         for i in range(2*x1, 2*x2+1):
#             for j in range(2*y1, 2*y2+1):
#                 board[i][j] = 1
    
#     for x1, y1, x2, y2 in rectangle:
#         for i in range(2*x1+1, 2*x2):
#             for j in range(2*y1+1, 2*y2):
#                 board[i][j] = 0
    
#     while queue:
#         x, y = queue.popleft()
        
#         if (x, y) == (iX, iY):
#             answer = (board[x][y] - 1) // 2
#             break
        
#         for i, j in d:
#             xTemp = x + i
#             yTemp = y + j
            
#             if 0 <= xTemp < 101 and 0 <= yTemp < 101 and board[xTemp][yTemp] != 0 and visited[xTemp][yTemp] == 0:
#                 board[xTemp][yTemp] = board[x][y] + 1
#                 visited[xTemp][yTemp] = 1
#                 queue.append((xTemp, yTemp))
        
#     return answer
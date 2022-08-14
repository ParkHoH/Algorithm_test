import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
result = 1

def dfs(x, y):
    if dp[x][y] == 0:
        dp[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if board[nx][ny] > board[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    return dp[x][y]

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
            
print(result)

# from copy import deepcopy
# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# visited = [[False] * n for _ in range(n)]
# dist = [[0] * n for _ in range(n)]

# def dfs(x, y, distance, L):
#     changed = False

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx >= n or ny >= n or nx < 0 or ny < 0:
#             continue
        
#         if graph[nx][ny] <= graph[x][y]:
#             continue

#         if dist[nx][ny] != 0:
#             for i in range(len(L)):
#                 k, l = L[i]
#                 dist[k][l] = max(dist[k][l], distance + dist[nx][ny] - i)
#             changed = True

#         elif not visited[nx][ny]:
#             visited[nx][ny] = True
#             new_L = deepcopy(L)
#             new_L.append([nx, ny])
#             dfs(nx, ny, distance+1, new_L)
#             visited[nx][ny] = False
#             changed = True
    
#     if not changed:
#         for i in range(len(L)):
#             k, l = L[i]
#             dist[k][l] = max(dist[k][l], distance - i)

# result = 1
# for i in range(n):
#     for j in range(n):
#         if dist[i][j] != 0:
#             result = max(result, dist[i][j])
#             continue
        
#         visited[i][j] = True
#         dfs(i, j, 1, [[i, j]])
#         visited[i][j] = False
#         result = max(result, dist[i][j])

# print(result)


# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# visited = [[False] * n for _ in range(n)]
# dist = [[1] * n for _ in range(n)]

# def dfs(x, y, distance):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx >= n or ny >= n or nx < 0 or ny < 0:
#             continue
        
#         if graph[nx][ny] <= graph[x][y]:
#             continue
        
#         dist[nx][ny] = max(dist[nx][ny], dist[x][y]-1)
        
#         global g_distance
#         if dist[nx][ny] != 1:
#             g_distance = max(g_distance, distance + dist[nx][ny])

#         elif not visited[nx][ny]:
#             g_distance = max(g_distance, distance+1)
#             visited[nx][ny] = True
#             dfs(nx, ny, distance+1)
#             visited[nx][ny] = False

# result = 1
# for i in range(n):
#     for j in range(n):
#         if dist[i][j] != 1:
#             continue

#         g_distance = 1
#         visited[i][j] = True
#         dfs(i, j, 1)
#         visited[i][j] = False
#         dist[i][j] = g_distance
#         result = max(result, g_distance)

# print(result)
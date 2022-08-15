from collections import deque

def find_fish(new_x, new_y, time):
    while queue:
        x, y, t = queue.popleft()
        if t > time:
            break
        
        global shark_size
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= N or nx < 0 or ny < 0:  
                continue

            if graph[nx][ny] >= shark_size or graph[nx][ny] == 0:
                continue
            
            if nx < new_x:
                new_x, new_y = nx, ny
            elif nx == new_x and ny < new_y:
                new_y = ny

    return [new_x, new_y]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark = [i, j]
            graph[i][j] = 0
            break

# 북서동남 순서대로..
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cum_time = 0 # 누적 시간(정답)
shark_size = 2 # 현재 아기상어 크기
cnt = 0 # 먹은 물고기 수

while True:
    impossible = True
    x, y = shark
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    queue = deque()
    queue.append([x, y, cum_time])

    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue
            
            fish_size = graph[nx][ny]
            if visited[nx][ny] or fish_size > shark_size: # 이미 방문했거나 물고기 사이즈가 더 큰 경우 스킵
                continue

            if fish_size != 0 and fish_size < shark_size:
                impossible = False
                new_x, new_y = find_fish(nx, ny, time) # 같은 time에 대해 위 먼저, 왼쪽 먼저 원소를 찾기 위해 한번씩만 더 탐색을 해줌
                graph[new_x][new_y] = 0
                shark = [new_x, new_y]
                cnt += 1
                cum_time = time+1

                if shark_size == cnt:
                    shark_size += 1
                    cnt = 0

                queue = []
                break
            
            else:
                visited[nx][ny] = True
                queue.append([nx, ny, time+1])
    
    if impossible: # 물고기 하나도 못 먹은 경우
        break

print(cum_time)

# 위 먼저, 왼쪽 먼저 탐색하는 것을 지키지 않아 오류 발생
# from collections import deque

# N = int(input())
# graph = []

# for _ in range(N):
#     graph.append(list(map(int, input().split())))

# fishes = []
# for i in range(N):
#     for j in range(N):
#         num = graph[i][j]
#         if num == 9:
#             shark = [i, j]
#         elif num != 0:
#             fishes.append(num)

# fishes.sort()
# size = 2
# cum_time = 0
# cnt = 0

# if fishes:
#     dx = [-1, 0, 0, 1]
#     dy = [0, -1, 1, 0]

#     while True:
#         impossible = True
#         visited = [[False] * N for _ in range(N)]
#         visited[shark[0]][shark[1]] = True
#         queue = deque()
#         queue.append([shark[0], shark[1], cum_time])

#         while queue:
#             x, y, time = queue.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if nx >= N or ny >= N or nx < 0 or ny < 0:
#                     continue
                
#                 fish = graph[nx][ny]
#                 if visited[nx][ny] or fish > size:
#                     continue
                

#                 if fish != 0 and fish < size:
#                     graph[shark[0]][shark[1]] = 0
#                     shark = [nx, ny]
#                     graph[nx][ny] = 9
#                     impossible = False
#                     cnt += 1
#                     cum_time = time+1
#                     if size == cnt:
#                         size += 1
#                         cnt = 0
#                     queue = []
#                     break
                
#                 else:
#                     visited[nx][ny] = True
#                     queue.append([nx, ny, time+1])
        
#         if impossible:
#             break

# print(cum_time)



# from collections import deque
# import sys

# input = sys.stdin.readline
# dx = [-1, 0, 0, 1]
# dy = [0, -1, 1, 0]

# def bfs(x, y, weight, time, eat):
#     q, can_eat = deque(), []
#     q.append([x, y])
#     c = [[-1]*n for _ in range(n)]
#     c[x][y] = time
#     while q:
#         qlen = len(q)
#         while qlen:
#             x, y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if c[nx][ny] == -1:
#                         if a[nx][ny] == 0 or a[nx][ny] == weight:
#                             c[nx][ny] = c[x][y] + 1
#                             q.append([nx, ny])
#                         elif 0 < a[nx][ny] < weight:
#                             can_eat.append([nx, ny])
#             qlen -= 1

#         if can_eat:
#             nx, ny = min(can_eat)
#             eat += 1
#             if eat == weight:
#                 eat = 0
#                 weight += 1
#             a[nx][ny] = 0
#             return nx, ny, weight, c[x][y] + 1, eat

#     print(time)
#     sys.exit()

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 9:
#             x, y = i, j
#             a[i][j] = 0

# weight, time, eat = 2, 0, 0
# while True:
#     x, y, weight, time, eat = bfs(x, y, weight, time, eat)
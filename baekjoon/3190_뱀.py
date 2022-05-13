from collections import deque

N = int(input())
graph = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2

L = int(input())
operator = []
for _ in range(L):
    operator.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
h_x = h_y = 0
t_x = t_y = 0
i = 3
stop = False
queue = deque()
queue.append((h_x, h_y))
graph[0][0] = 1

for oper in operator:
    X, C = oper.split()

    while cnt != int(X):
        h_x += dx[i]
        h_y += dy[i]
        cnt += 1

        if h_x >= N or h_y >= N or h_x < 0 or h_y < 0:
            stop = True
            break
        elif graph[h_x][h_y] == 1:
            stop = True
            break
        
        if graph[h_x][h_y] == 2:
            graph[h_x][h_y] = 1
            queue.append((h_x, h_y))
            continue

        graph[h_x][h_y] = 1
        queue.append((h_x, h_y))
        t_x, t_y = queue.popleft()
        graph[t_x][t_y] = 0

    if stop: break

    if i == 0:
        if C == "L":
            i = 2
        elif C == "D":
            i = 3
    
    elif i == 1:
        if C == "L":
            i = 3
        elif C == "D":
            i = 2

    elif i == 2:
        if C == "L":
            i = 1
        elif C == "D":
            i = 0

    elif i == 3:
        if C == "L":
            i = 0
        elif C == "D":
            i = 1

while True:
    if stop: break
    
    h_x += dx[i]
    h_y += dy[i]
    cnt += 1

    if h_x >= N or h_y >= N or h_x < 0 or h_y < 0:
        stop = True
        break
    elif graph[h_x][h_y] == 1:
        stop = True
        break
    
    if graph[h_x][h_y] == 2:
        graph[h_x][h_y] = 1
        queue.append((h_x, h_y))
        continue

    graph[h_x][h_y] = 1
    queue.append((h_x, h_y))
    t_x, t_y = queue.popleft()
    graph[t_x][t_y] = 0

print(cnt)
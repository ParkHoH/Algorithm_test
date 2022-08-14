from collections import deque

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

fishes = []
for i in range(N):
    for j in range(N):
        num = graph[i][j]
        if num == 9:
            shark = [i, j]
        elif num != 0:
            fishes.append(num)

fishes.sort()
size = 2
cum_time = 0
cnt = 0

if fishes:
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    while True:
        impossible = True
        visited = [[False] * N for _ in range(N)]
        visited[shark[0]][shark[1]] = True
        queue = deque()
        queue.append([shark[0], shark[1], cum_time])

        while queue:
            x, y, time = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= N or ny >= N or nx < 0 or ny < 0:
                    continue
                
                fish = graph[nx][ny]
                if visited[nx][ny] or fish > size:
                    continue
                

                if fish != 0 and fish < size:
                    graph[shark[0]][shark[1]] = 0
                    shark = [nx, ny]
                    graph[nx][ny] = 9
                    impossible = False
                    cnt += 1
                    cum_time = time+1
                    if size == cnt:
                        size += 1
                        cnt = 0
                    queue = []
                    break
                
                else:
                    visited[nx][ny] = True
                    queue.append([nx, ny, time+1])
        
        if impossible:
            break

print(cum_time)



from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, weight, time, eat):
    q, can_eat = deque(), []
    q.append([x, y])
    c = [[-1]*n for _ in range(n)]
    c[x][y] = time
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if c[nx][ny] == -1:
                        if a[nx][ny] == 0 or a[nx][ny] == weight:
                            c[nx][ny] = c[x][y] + 1
                            q.append([nx, ny])
                        elif 0 < a[nx][ny] < weight:
                            can_eat.append([nx, ny])
            qlen -= 1

        if can_eat:
            nx, ny = min(can_eat)
            eat += 1
            if eat == weight:
                eat = 0
                weight += 1
            a[nx][ny] = 0
            return nx, ny, weight, c[x][y] + 1, eat

    print(time)
    sys.exit()

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0

weight, time, eat = 2, 0, 0
while True:
    x, y, weight, time, eat = bfs(x, y, weight, time, eat)
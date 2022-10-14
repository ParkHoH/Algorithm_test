from collections import deque

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
taxt_x, taxt_y = map(int, input().split())
taxi = (taxt_x-1, taxt_y-1)

destinations = {}
client_idx = 2

for _ in range(M):
    r, c, dest_x, dest_y = map(int, input().split())
    r -= 1; c -= 1; dest_x -= 1; dest_y -= 1

    board[r][c] = client_idx
    destinations[client_idx] = (dest_x, dest_y)
    client_idx += 1

def find_dest_dist(x, y):
    dest_x, dest_y = destinations[board[x][y]]
    board[x][y] = 0

    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True

    queue = deque()
    queue.append((x, y, 0))

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if visited[nx][ny] or board[nx][ny] == 1:
                continue
            
            if nx == dest_x and ny == dest_y:
                global taxi
                taxi = (nx, ny)
                return dist+1

            visited[nx][ny] = True
            queue.append((nx, ny, dist+1))
    
    return -1

def find_client():
    global taxi
    x, y = taxi
    candidate = []
    min_dist = float('inf') if board[x][y] <= 1 else 0

    if min_dist:
        visited = [[False] * N for _ in range(N)]
        visited[x][y] = True

        queue = deque()
        queue.append((x, y, 0))

        while queue:
            x, y, dist = queue.popleft()

            if dist > min_dist:
                break

            if board[x][y] >= 2:
                candidate.append((x, y))

            if dist == min_dist:
                continue

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if visited[nx][ny] or board[nx][ny] == 1:
                    continue
                
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))

                if board[nx][ny] >= 2:
                    min_dist = dist+1

    else:
        candidate.append((x, y))

    global fuel
    if min_dist > fuel or not candidate:
        return False

    candidate.sort(key=lambda x: (x[0], x[1]))
    x, y = candidate[0]

    dest_dist = find_dest_dist(x, y)

    if dest_dist == -1:
        return False

    total_dist = min_dist + dest_dist

    if total_dist > fuel:
        return False

    else:
        fuel = fuel - min_dist + dest_dist
        return True

cnt = len(destinations)

while cnt:
    if find_client():
        cnt -= 1
    else:
        break

print(fuel if cnt == 0 else -1)
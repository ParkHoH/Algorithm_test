from copy import deepcopy
from itertools import permutations
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

xy = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (1, 1),
}

board = [list(map(int, input().split())) for _ in range(3)]
answer = float('inf')

def check_case(permu):
    new_board = deepcopy(board)
    move_cnt = 0
    
    for idx in permu:
        target_xy = xy[idx]

        for x in range(3):
            for y in range(3):
                if board[x][y] == idx:
                    cur_xy = (x, y)
                    break
        
        changed = False

        visited = [[False] * 3 for _ in range(3)]
        visited[x][y] = True

        queue = deque()
        queue.append((cur_xy[0], cur_xy[1], 0))

        while queue:
            x, y, cnt = queue.popleft()

            if x == target_xy[0] and y == target_xy[1]:
                move_cnt += cnt
                new_board[x][y] = -1
                new_board[cur_xy[0]][cur_xy[1]] = 0
                changed = True
                break

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
                    continue
                
                if new_board[nx][ny] == -1 or visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
        
        if not changed: return

    global answer
    answer = min(answer, move_cnt)

for permu in permutations(range(1, 9), 8):
    check_case(permu)

print(answer if answer != float('inf') else -1)
# 시간 초과 발생 2
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, distance, c_set):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        
        alpabet = board[nx][ny]
        if alpabet in c_set:
            continue

        global result
        result = max(result, distance+1)
        c_set.add(alpabet)
        dfs(nx, ny, distance+1, c_set)
        c_set.remove(alpabet)
            

result = 1
dfs(0, 0, 1, set(board[0][0]))

print(result)


# 시간 초과 발생 1
from collections import defaultdict
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input() for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
checked = defaultdict(bool)


def dfs(x, y, distance):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        
        alpabet = board[nx][ny]
        if not checked[alpabet]:
            global result
            result = max(result, distance+1)
            
            checked[alpabet] = True
            dfs(nx, ny, distance+1)
            checked[alpabet] = False
            

result = 1
checked[board[0][0]] = True
dfs(0, 0, 1)

print(result)

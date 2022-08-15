from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    stop = False
    board[1] = 0
    queue = deque()
    queue.append([1, 0])

    while queue:
        x, cnt = queue.popleft()
        for i in range(6, 0, -1):
            num = x+i
            if num > 100:
                continue
            
            if board[num] <= cnt:
                continue

            board[num] = cnt+1
            if num == 100: 
                stop = True
                break

            if num in ladder:
                board[ladder[num]] = cnt+1
                queue.append([ladder[num], cnt+1])
                if ladder[num] == 100: 
                    stop = True
                    break

            elif num in snake:
                board[snake[num]] = cnt+1
                queue.append([snake[num], cnt+1])
                if snake[num] == 100: 
                    stop = True
                    break
            
            else:
                queue.append([num, cnt+1])
        
        if stop: break

N, M = map(int, input().split())
ladder = {}
snake = {}

for _ in range(N):
    f, t = map(int, input().split())
    ladder[f] = t

for _ in range(M):
    f, t = map(int, input().split())
    snake[f] = t

board = [float('inf')] * 101
bfs()
print(board[-1])
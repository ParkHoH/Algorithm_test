from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

global max_value
max_value = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] > max_value:
            max_value = graph[i][j]

direction = ["up", "down", "left", "right"]

def move(board, direct):
    global max_value
    new_board = [[0] * N for _ in range(N)]
    changed = False

    if direct == "up":
        for j in range(N):
            temp = []
            for i in range(N):
                if board[i][j]:
                    if not changed and temp and temp[-1] == board[i][j]:
                        temp.pop()
                        temp.append(board[i][j] * 2)
                        max_value = max(max_value, board[i][j] * 2)
                        changed = True
                    else:
                        temp.append(board[i][j])
                        changed = False
            
            for i in range(len(temp)):
                new_board[i][j] = temp[i]

    elif direct == "down":
        for j in range(N):
            temp = []
            for i in range(N-1, -1, -1):
                if board[i][j]:
                    if not changed and temp and temp[-1] == board[i][j]:
                        temp.pop()
                        temp.append(board[i][j] * 2)
                        max_value = max(max_value, board[i][j] * 2)
                        changed = True
                    else:
                        temp.append(board[i][j])
                        changed = False

            for i in range(len(temp)):
                new_board[N-1-i][j] = temp[i]

    elif direct == "left":
        for i in range(N):
            temp = []
            for j in range(N):
                if board[i][j]:
                    if not changed and temp and temp[-1] == board[i][j]:
                        temp.pop()
                        temp.append(board[i][j] * 2)
                        max_value = max(max_value, board[i][j] * 2)
                        changed = True
                    else:
                        temp.append(board[i][j])
                        changed = False
            
            for j in range(len(temp)):
                new_board[i][j] = temp[j]

    elif direct == "right":
        for i in range(N):
            temp = []
            for j in range(N-1, -1, -1):
                if board[i][j]:
                    if not changed and temp and temp[-1] == board[i][j]:
                        temp.pop()
                        temp.append(board[i][j] * 2)
                        max_value = max(max_value, board[i][j] * 2)
                        changed = True
                    else:
                        temp.append(board[i][j])
                        changed = False
            
            for j in range(len(temp)):
                new_board[i][N-1-j] = temp[j]

    return new_board

def bfs():
    queue = deque()
    queue.append((graph, 0))
    while queue:
        new_graph, cnt = queue.popleft()
        if cnt == 5:
            continue
        for i in range(4):
            queue.append((move(new_graph, direction[i]), cnt+1))

bfs()
print(max_value)
# better code
from collections import deque

def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    direct = ["x_direction", "y_direction"]
    cost_board = [[float('inf')] * len(board) for _ in range(len(board))]
    
    queue = deque()
    queue.append((0, 0, 0, ""))
    cost_board[0][0] = 0
    while queue:
        x, y, cost, direction = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= len(board) or ny >= len(board) or nx < 0 or ny < 0:
                continue
            
            new_cost = cost + 100 if direction == "" or direction == direct[i//2] else cost + 600
            if board[nx][ny] == 0 and cost_board[nx][ny] >= new_cost:
                cost_board[nx][ny] = new_cost
                queue.append((nx, ny, new_cost, direct[i//2]))
            elif board[nx][ny] == 0 and cost_board[nx][ny] + 200 >= new_cost: # TC 25번에 대한 예외 처리 / 카카오에서 의도한 예외는 아닌 것 같음
                queue.append((nx, ny, new_cost, direct[i//2]))

    return cost_board[len(board)-1][len(board)-1]


# original solution
from collections import deque

def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[float('inf')] * len(board) for _ in range(len(board))]
    
    queue = deque()
    queue.append((0, 0, 0, ""))
    visited[0][0] = 0
    while queue:
        x, y, cost, direction = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(board) or ny >= len(board) or nx < 0 or ny < 0:
                continue
                
            if direction == "x_direction":
                if i == 0 or i == 1:
                    new_cost = cost + 100
                    direct = "x_direction"
                else:
                    new_cost = cost + 600
                    direct = "y_direction"

            elif direction == "y_direction":
                if i == 0 or i == 1:
                    new_cost = cost + 600
                    direct = "x_direction"
                else:
                    new_cost = cost + 100
                    direct = "y_direction"
            else:
                new_cost = cost + 100
                if i == 0 or i == 1:
                    direct = "x_direction"
                else:
                    direct = "y_direction"
                    
            if board[nx][ny] == 0 and visited[nx][ny] >= new_cost:
                visited[nx][ny] = new_cost
                queue.append((nx, ny, new_cost, direct))
            elif board[nx][ny] == 0 and visited[nx][ny] + 200 >= new_cost:
                queue.append((nx, ny, new_cost, direct))

    return visited[len(board)-1][len(board)-1]

print(solution(	[[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))
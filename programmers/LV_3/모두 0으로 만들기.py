import sys
sys.setrecursionlimit(300000)

def dfs(x, a, visited, board):
    global result
    now = a[x]
    visited[x] = 1
    for i in board[x]:
        if visited[i] == 0:
            now += dfs(i, a, visited, board)
            
    result += abs(now)
    return now
    
def solution(a, edges):
    global result
    result = 0
    if sum(a) != 0:
        return -1
    
    board = [[] for _ in range(len(a))]
    for i, j in edges:
        board[i].append(j)
        board[j].append(i)
    
    visited = [0] * len(a)
    dfs(0, a, visited, board)
    return result
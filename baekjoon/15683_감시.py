from copy import deepcopy

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dic = {}
dic[1] = [[0], [1], [2], [3]]
dic[2] = [[0, 1], [2, 3]]
dic[3] = [[2, 1], [0, 2], [3, 0], [1, 3]]
dic[4] = [[0, 1, 2], [0, 2, 3], [0, 1, 3], [1, 2, 3]]
dic[5] = [[0, 1, 2, 3]]

cctv = []
for i in range(N):
    for j in range(M):
        if graph[i][j] in range(1, 6):
            cctv.append([i, j])
visited = [False] * len(cctv)

min_value = float('inf')

def dfs(board, checked):
    for k in range(len(checked)):
        if not checked[k]:
            checked[k] = True
            i, j = cctv[k]
            for direction in dic[board[i][j]]:
                copy_board = deepcopy(board)

                for detail_direction in direction:
                    if detail_direction == 0:
                        for x in range(j-1, -1, -1):
                            if copy_board[i][x] == 0:
                                copy_board[i][x] = "#"
                            elif copy_board[i][x] == 6:
                                break
                            
                    elif detail_direction == 1:
                        for x in range(j+1, M):
                            if copy_board[i][x] == 0:
                                copy_board[i][x] = "#"
                            elif copy_board[i][x] == 6:
                                break

                    elif detail_direction == 2:
                        for y in range(i-1, -1, -1):
                            if copy_board[y][j] == 0:
                                copy_board[y][j] = "#"
                            elif copy_board[y][j] == 6:
                                break

                    elif detail_direction == 3:
                        for y in range(i+1, N):
                            if copy_board[y][j] == 0:
                                copy_board[y][j] = "#"
                            elif copy_board[y][j] == 6:
                                break

                dfs(copy_board, deepcopy(checked))

            return

    global min_value
    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                cnt += 1
    min_value = min(min_value, cnt)

dfs(graph, visited)
print(min_value)
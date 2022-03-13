def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0
    global cnt
    cnt += 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
result = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if dfs(i, j) == True:
            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i)
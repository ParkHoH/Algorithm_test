from collections import deque

def dfs(n):
    visited_dfs[n] = True
    for idx, node_connected in enumerate(graph[n]):
        if node_connected == True and visited_dfs[idx] == False:
            dfs(idx)

def bfs(n):
    queue = deque()
    queue.append(n)
    visited_bfs[n] = True
    while queue:
        n = queue.popleft()
        for idx, node_connected in enumerate(graph[n]):
            if node_connected == True and visited_bfs[idx] == False:
                queue.append(idx)
                visited_bfs[idx] = True

N = int(input())
M = int(input())
graph = [[False]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
dfs(1)
print(visited_dfs.count(True)-1)
bfs(1)
print(visited_bfs.count(True)-1)

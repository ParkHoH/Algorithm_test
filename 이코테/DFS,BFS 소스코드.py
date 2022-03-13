from collections import deque

def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if visited[i] == False:
            dfs(i)

def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = True
    while queue:
        num = queue.popleft()
        print(num, end=' ')
        for i in graph[num]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(1)

print()

visited = [False] * 9
bfs(1)
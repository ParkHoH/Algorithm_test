from collections import deque

N, K = map(int, input().split())

graph = [0 for _ in range(100001)]
graph[N] = 1
dx = [-1, 1]
queue = deque()
queue.append(N)
while queue:
    x = queue.popleft()
    for nx in (x-1, x+1, 2*x):
        if nx < 0 or nx > 100000:
            continue
        if graph[nx] == 0:
            graph[nx] = graph[x] + 1
            queue.append(nx)
        if nx == K:
            break

print(graph[K] - 1)

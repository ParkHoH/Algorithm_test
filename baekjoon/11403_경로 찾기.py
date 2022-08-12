from collections import defaultdict, deque

N = int(input())
graph = []
connected = defaultdict(list)

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 1:
            connected[i].append(j)

result = [[0] * N for _ in range(N)]
for i in range(N):
    queue = deque()
    queue.append(i)

    while queue:
        idx = queue.popleft()
        for node in connected[idx]:
            if result[i][node] == 0:
                result[i][node] = 1
                queue.append(node)

for i in range(N):
    for j in range(N):
        print(result[i][j], end=" ")
    print()
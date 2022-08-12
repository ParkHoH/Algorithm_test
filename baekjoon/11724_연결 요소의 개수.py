from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = 0
cnt = 0

for i in range(1, N+1):
    if cnt == N:
        break

    if visited[i]:
        continue

    result += 1
    queue = deque()
    queue.append(i)
    visited[i] = True
    while queue:
        main_node = queue.popleft()
        for node in graph[main_node]:
            if not visited[node]:
                visited[node] = True
                cnt += 1
                queue.append(node)

print(result)
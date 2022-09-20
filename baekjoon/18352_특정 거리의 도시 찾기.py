from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [float('inf')] * (N+1) 
distance[X] = 0

queue = deque()
queue.append([X, 0])
result = []

while queue:
    node, dist = queue.popleft()

    if dist == K:
        result.append(node)
    elif dist > K:
        break

    if distance[node] < dist: continue

    for c_node in graph[node]:
        total_dist = dist + 1

        if total_dist < distance[c_node]:
            distance[c_node] = total_dist
            queue.append([c_node, total_dist])

result.sort()

if not result:
    print(-1)
else:
    for i in result:
        print(i)
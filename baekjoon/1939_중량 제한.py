import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, input().split())
result = 0

dist = [0] * (N+1)
dist[start] = float('inf')

heap = []
heap.append([-float('inf'), start])

while heap:
    limit, idx = heapq.heappop(heap)
    limit *= -1

    if idx == end:
        result = max(result, limit)

    if result > limit:
        continue

    for i, l in graph[idx]:
        new_limit = min(limit, l)
        if dist[i] < new_limit:
            dist[i] = new_limit
            heapq.heappush(heap, [-min(l, limit), i])

print(result)
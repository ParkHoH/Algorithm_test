import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    indegree[b] += 1

heap = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    idx = heapq.heappop(heap)
    result.append(idx)

    for i in graph[idx]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end=" ")
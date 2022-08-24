import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

dist = [float('inf')] * (n+1)
dist[start] = 0

heap = []
heapq.heappush(heap, [0, start, [start]])

while heap:
    cost, idx, root = heapq.heappop(heap)

    if idx == end: # 정답
        print(cost)
        print(len(root))
        print(*root)
        break

    for node, connect_cost in graph[idx]:
        new_cost = cost + connect_cost

        if new_cost < dist[node]:
            dist[node] = new_cost
            heapq.heappush(heap, [new_cost, node, root + [node]])



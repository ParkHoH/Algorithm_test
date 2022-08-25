import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

dist = [float('inf')] * (N+1)
dist[start] = 0

heap = []
heapq.heappush(heap, [0, start])

while heap:
    cost, idx = heapq.heappop(heap)

    if idx == end:
        print(cost)
        break

    for node, connect_cost in graph[idx]:
        new_cost = cost + connect_cost

        if new_cost < dist[node]:
            dist[node] = new_cost
            heapq.heappush(heap, [new_cost, node])
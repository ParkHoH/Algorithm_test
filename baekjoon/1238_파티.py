import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start, end):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        cost, idx = heapq.heappop(heap)

        if idx == end: # 정답
            return cost

        for node, connect_cost in graph[idx]:
            new_cost = cost + connect_cost

            if new_cost < dist[node]:
                dist[node] = new_cost
                heapq.heappush(heap, [new_cost, node])
    
result = 0

for i in range(1, N+1):
    if i != X:
        result = max(result, dijkstra(i, X) + dijkstra(X, i))

print(result)
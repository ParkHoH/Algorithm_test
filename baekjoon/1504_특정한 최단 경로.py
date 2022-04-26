import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    node1, node2, cost = map(int, sys.stdin.readline().split())
    graph[node1].append([node2, cost])
    graph[node2].append([node1, cost])

node1, node2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    distance = [float('inf')] * (N+1)
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (distance[start], start))
    while heap:
        c, node = heapq.heappop(heap)
        if node == end:
            return distance[end]
        for connected_node, cost in graph[node]:
            if c + cost < distance[connected_node]:
                distance[connected_node] = c + cost
                heapq.heappush(heap, (distance[connected_node], connected_node))
    return distance[end]

result = float('inf')
case1 = dijkstra(1, node1) + dijkstra(node1, node2) + dijkstra(node2, N)
case2 = dijkstra(1, node2) + dijkstra(node2, node1) + dijkstra(node1, N)
result = min(result, case1, case2)
if result < float('inf'):
    print(result)
else:
    print(-1)
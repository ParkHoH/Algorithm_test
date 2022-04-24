import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [float('inf')] * (V+1)
heap = []
for _ in range(E):
    node1, node2, cost = map(int, sys.stdin.readline().split())
    graph[node1].append((node2, cost))

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (distance[start], start))
    while heap:
        dist, node = heapq.heappop(heap)
        visited[node] = True
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (distance[i[0]], i[0]))

dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])


# 시간 초과: 최소값 구하는 것에서 시간 초과 발생
import sys

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [float('inf')] * (V+1)
for _ in range(E):
    node1, node2, cost = map(int, sys.stdin.readline().split())
    graph[node1].append((node2, cost))

def get_smallest_distance():
    min_node = float('inf')
    idx = 0
    for i in range(1, V+1):
        if visited[i] == False and distance[i] < min_node:
            min_node = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for _ in range(V-1):
        node = get_smallest_distance()
        visited[node] = True
        for i in graph[node]:
            cost = distance[node] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost

dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])

import heapq
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + [*map(int, input().split())]
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start):
    distance = [float('inf')]* (n+1)
    distance[start] = 0

    heap = []
    heap.append((0, start))

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distance[node]: continue

        for new_node, new_dist in graph[node]:
            total_dist = dist + new_dist
            
            if distance[new_node] > total_dist and total_dist <= m:
                distance[new_node] = total_dist
                heapq.heappush(heap, (total_dist, new_node))

    sum_items = 0

    for i in range(1, n+1):
        if distance[i] != float('inf'):
            sum_items += items[i]

    return sum_items

answer = 0

for i in range(1, n+1):
    answer = max(answer, dijkstra(i))

print(answer)
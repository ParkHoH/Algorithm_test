import heapq
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[(i+1, 1)] for i in range(D+1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    if a > D or b > D: continue
    graph[a].append((b, c))

distance = [float('inf')] * (D+1)
distance[0] = 0

heap = []
heap.append((0, 0))

while heap:
    node, dist = heapq.heappop(heap)

    if node == D: break
    
    if distance[node] < dist: continue

    for new_node, new_dist in graph[node]:
        total_dist = dist + new_dist

        if total_dist < distance[new_node]:
            distance[new_node] = total_dist
            heapq.heappush(heap, (new_node, total_dist))

print(distance[-1])
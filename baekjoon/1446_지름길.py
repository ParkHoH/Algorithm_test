import heapq
import sys
input = sys.stdin.readline

# 다익스트라 풀이
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


# dp 풀이
N, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

distance = [float('inf')] * (D+1)
distance[0] = 0

for i in range(D+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1] + 1)

    for a, b, dist in graph:
        if a == i and a <= D and b <= D:
            distance[b] = min(distance[b], distance[a] + dist)

print(distance[-1])
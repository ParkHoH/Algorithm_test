import heapq
import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    warm_holes = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    for _ in range(W):
        a, b, cost = map(int, input().split())
        warm_holes[a].append((b, -cost))

    for i in range(1, N+1):
        graph[i].sort(key=lambda x: x[1])

    answer = "NO"

    def check_possible(idx):
        distance = [float('inf')] * (N+1)
        
        heap = []
        heap.append((0, idx))

        while heap:
            dist, cur = heapq.heappop(heap)

            if distance[cur] < dist: continue

            # if cur == idx and distance[cur] != float('inf'):
            #     return True if dist < 0 else False

            for next, new_dist in warm_holes[cur]:
                total_dist = dist + new_dist

                if distance[next] > total_dist:
                    distance[next] = total_dist
                    heapq.heappush(heap, (total_dist, next))

            for next, new_dist in graph[cur]:
                total_dist = dist + new_dist

                if distance[next] > total_dist:
                    distance[next] = total_dist
                    heapq.heappush(heap, (total_dist, next))

        return True if distance[idx] < 0 else False

    # for i in range(1, N+1):
    if check_possible(1):
        answer = "YES"
        break

    print(answer)

# 벨만-포드 풀이
import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [10001 for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

def bellman_ford(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0

    # for v in range(1, n+1):
    #     for

    return False

print("YES" if bellman_ford(1) else "END")

# 틀린 풀이
# import heapq
# import sys
# input = sys.stdin.readline

# TC = int(input())

# for _ in range(TC):
#     N, M, W = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
#     warm_holes = [[] for _ in range(N+1)]

#     for _ in range(M):
#         a, b, cost = map(int, input().split())
#         graph[a].append((b, cost))
#         graph[b].append((a, cost))

#     for _ in range(W):
#         a, b, cost = map(int, input().split())
#         warm_holes[a].append((b, -cost))

#     for i in range(1, N+1):
#         graph[i].sort(key=lambda x: x[1])

#     answer = "NO"

#     def check_possible(idx):
#         distance = [float('inf')] * (N+1)
        
#         heap = []
#         heap.append((0, idx))

#         while heap:
#             dist, cur = heapq.heappop(heap)

#             if distance[cur] < dist: continue

#             # if cur == idx and distance[cur] != float('inf'):
#             #     return True if dist < 0 else False

#             for next, new_dist in warm_holes[cur]:
#                 total_dist = dist + new_dist

#                 if distance[next] > total_dist:
#                     distance[next] = total_dist
#                     heapq.heappush(heap, (total_dist, next))

#             for next, new_dist in graph[cur]:
#                 total_dist = dist + new_dist

#                 if distance[next] > total_dist:
#                     distance[next] = total_dist
#                     heapq.heappush(heap, (total_dist, next))

#         return True if distance[idx] < 0 else False

#     # for i in range(1, N+1):
#     if check_possible(1):
#         answer = "YES"
#         break

#     print(answer)
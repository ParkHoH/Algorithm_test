# from collections import deque
# N, K = map(int, input().split())

# visited = [False] * 100001
# visited[N] = True

# queue = deque()
# queue.append([N, 0])

# while queue:
#     x, cost = queue.popleft()

#     if x == K:
#         print(cost)
#         break

#     nx = 2*x
#     if 0 <= nx <= 100000:
#         visited[nx] = True
#         heapq.heappush(heap, [cost, nx])

#     for nx in [x-1, x+1]:
#         if 0 <= nx <= 100000:
#             visited[nx] = True
#             heapq.heappush(heap, [cost+1, nx])

import heapq

N, K = map(int, input().split())

visited = [False] * 100001
visited[N] = True

heap = []
heapq.heappush(heap, [0, N])

while heap:
    cost, x = heapq.heappop(heap)

    if x == K:
        print(cost)
        break

    nx = 2*x
    if 0 <= nx <= 100000 and not visited[nx]:
        visited[nx] = True
        heapq.heappush(heap, [cost, nx])

    for nx in [x-1, x+1]:
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            heapq.heappush(heap, [cost+1, nx])
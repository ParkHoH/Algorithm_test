import heapq

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, list(input().strip()))))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = float('inf')

    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = 0
    heap = []
    heap.append([0, 0, 0, visited])
    while heap:
        time, x, y, visited = heapq.heappop(heap)
        if time >= result:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if nx == ny == N-1:
                result = min(result, time)
                continue

            if time + graph[nx][ny] >= visited[nx][ny]:
                continue

            visited[nx][ny] = time + graph[nx][ny]
            heapq.heappush(heap, [time + graph[nx][ny], nx, ny, visited])

    print(f'#{t} {result}')

# import heapq
# from copy import deepcopy

# TC = int(input())
# for t in range(1, TC+1):
#     N = int(input())
#     graph = []
#     for _ in range(N):
#         graph.append(list(map(int, list(input().strip()))))

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     result = float('inf')

#     visited = [[False] * N for _ in range(N)]
#     visited[0][0] = True
#     heap = []
#     heap.append([0, 0, 0, visited])
#     while heap:
#         time, x, y, visited = heapq.heappop(heap)
#         if time >= result:
#             continue

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= N or ny >= N:
#                 continue

#             if nx == ny == N-1:
#                 result = min(result, time)
#                 continue

#             if time + graph[nx][ny] >= result:
#                 continue

#             if not visited[nx][ny]:
#                 copy_visited = deepcopy(visited)
#                 copy_visited[nx][ny] = True
#                 heapq.heappush(heap, [time + graph[nx][ny], nx, ny, copy_visited])

#     print(f'#{t} {result}')

# from collections import deque
# from copy import deepcopy

# TC = int(input())
# for t in range(1, TC+1):
#     N = int(input())
#     graph = []
#     for _ in range(N):
#         graph.append(list(map(int, list(input().strip()))))

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     result = float('inf')

#     visited = [[False] * N for _ in range(N)]
#     visited[0][0] = True
#     queue = deque()
#     queue.append((0, 0, 0, visited))
#     while queue:
#         x, y, time, c_visited = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= N or ny >= N:
#                 continue

#             if nx == ny == N-1:
#                 result = min(result, time)
#                 continue

#             if time + graph[nx][ny] >= result:
#                 continue

#             if not c_visited[nx][ny]:
#                 copy_visited = deepcopy(visited)
#                 copy_visited[nx][ny] = True
#                 queue.append((nx, ny, time + graph[nx][ny], copy_visited))

#     print(f'#{t} {result}')
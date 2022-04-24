import heapq

def solution(N, road, K):
    visited = [False] * (N+1)
    distance = [float('inf')] * (N+1)
    heap = []
    graph = [[] for _ in range(N+1)]
    for node1, node2, cost in road:
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))
        
    def dijkstra():
        heapq.heappush(heap, (0, 1))
        distance[1] = 0
        while heap:
            c, node = heapq.heappop(heap)
            visited[node] = True
            for i in graph[node]:
                if visited[i[0]]:
                    continue
                cost = c + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(heap, (distance[i[0]], i[0]))

    dijkstra()
    result = 0
    for i in range(1, len(distance)):
        if distance[i] != float('inf') and distance[i] <= K:
            result += 1
    return result

# 시간 초과: 다익스트라 알고리즘 풀이 필요
from collections import deque

set_result = set()
set_except = set()

def bfs(n, K, total_cost, graph, visited, cost_list):
    queue = deque()
    queue.append((n, total_cost))
    visited[n] = True
    while queue:
        n, cost = queue.popleft()
        for dest, cost2 in graph[n]:
            if visited[dest] == False:
                visited[dest] = True
                cost_list[dest] = cost+cost2
                queue.append((dest, cost2))
            
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for r in road:
        start, end, cost = r
        is_new = True
        for i in range(len(graph[start])):
            if graph[start][i][0] == end:
                graph[start][i][1] = min(graph[start][i][1], cost)
                for j in range(len(graph[end])):
                    if graph[end][j][0] == start:
                        graph[end][j][1] = min(graph[end][j][1], cost)
                is_new = False
                break
        if is_new:
            graph[start].append([end, cost])
            graph[end].append([start, cost])
    for i in range(len(graph)):
        graph[i].sort(key=lambda x: x[1])
    return graph

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))

# set_result = set()

# def dfs(n, K, total_cost, graph, visited):
#     set_result.add(n)
#     for dest, cost in graph[n]:
#         if visited[dest] == True or total_cost+cost > K:
#             continue
#         visited[dest] = True
#         dfs(dest, K, total_cost+cost, graph, visited)
#         visited[dest] = False
            
# def solution(N, road, K):
#     graph = [[] for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for r in road:
#         start, end, cost = r
#         graph[start].append([end, cost])
#         graph[end].append([start, cost])

#     visited[1] = True
#     dfs(1, K, 0, graph, visited)
#     return len(set_result)


# from collections import deque

# def solution(N, road, K):
#     graph = [[] for _ in range(N+1)]
#     visited = [0] * (N+1)
#     for i in road:
#         a, b, c = i
#         graph[a].append([b, c])
#         graph[b].append([a, c])
#     for i in range(1, len(graph)):
#         graph[i].sort(key=lambda x: x[1])
        
#     total_length = [float('inf')] * (N+1)
#     def bfs():
#         queue = deque()
#         queue.append(1)
#         visited[1] = 1
#         while queue:
#             village = queue.popleft()
#             for connected_village, length in graph[village]:
#                 if visited[connected_village] == 0:
#                     visited[connected_village] = 1
#                     total_length[connected_village] = total_length[village] + length
#                     queue.append(connected_village)
#     bfs()
#     result = 1
#     for i in range(2, len(total_length)):
#         if total_length[i] <= K:
#             result += 1
#     return result
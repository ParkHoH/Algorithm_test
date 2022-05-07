import sys
sys.setrecursionlimit(10**6)

def solution(n, paths, gates, summits):
    visited = [False] * (n+1)
    for gate in gates:
        visited[gate] = True
    for summit in summits:
        visited[summit] = "summit"
    
    graph = [[] for _ in range(n+1)]
    for path in paths:
        node1, node2, cost = path
        graph[node1].append([node2, cost])
        graph[node2].append([node1, cost])

    for i in range(len(graph)):
        graph[i].sort(key=lambda x: x[1])

    def dfs(n, max_intensity):
        global result, direction
        if max_intensity < result[1] and visited[n] == "summit":
            result = [n, max_intensity]
            return
        elif max_intensity == result[1] and n < result[0] and visited[n] == "summit":
            result = [n, max_intensity]
            return

        for node, cost in graph[n]:
            if cost > result[1] or (n, node) in direction:
                continue

            if not visited[node]:
                direction.add((n, node))
                visited[node] = True
                dfs(node, max(max_intensity, cost))
                visited[node] = False

            if visited[node] == "summit":
                dfs(node, max(max_intensity, cost))
    
    global result, direction
    result = [float('inf'), float('inf')] # 산봉우리의 번호, intensity의 최솟값
    direction = set()
    for gate in gates:
        dfs(gate, 0)

    return result

print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))



        # queue = deque()
        # queue.append((n, cummu_cost))
        # visited = [[False] * (n+1)]
        # visited[n] = True
        # while queue:
        #     n, cummu_cost = queue.popleft()
        #     for node, cost in graph[n]:
        #         if node in gates:
        #             continue

                
        #         if not visited[node]:
        #             visited[node] = True
        #             queue.append((node, cummu_cost + cost))
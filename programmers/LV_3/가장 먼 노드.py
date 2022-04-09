from collections import deque
        
def bfs(graph, visited, distance):
    queue = deque()
    visited[1] = True
    queue.append((1, 0))
    while queue:
        start, total_distance = queue.popleft()
        for end in graph[start]:
            if not visited[end]:
                visited[end] = True
                distance[end] = total_distance+1
                queue.append((end, total_distance+1))

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)

    bfs(graph, visited, distance)
    max_distance = max(distance)
    cnt = 0 
    for d in distance:
        if d == max_distance:
            cnt += 1
    return cnt
from collections import deque

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for i in road:
        a, b, c = i
        graph[a].append([b, c])
        graph[b].append([a, c])
    for i in range(1, len(graph)):
        graph[i].sort(key=lambda x: x[1])
        
    total_length = [0] * (N+1)
    def bfs():
        queue = deque()
        queue.append(1)
        visited[1] = 1
        while queue:
            village = queue.popleft()
            for connected_village, length in graph[village]:
                if visited[connected_village] == 0:
                    visited[connected_village] = 1
                    total_length[connected_village] = total_length[village] + length
                    queue.append(connected_village)
    bfs()
    result = 1
    for i in range(2, len(total_length)):
        if total_length[i] <= K:
            result += 1
    return result
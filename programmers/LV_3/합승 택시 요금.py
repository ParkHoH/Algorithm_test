import heapq

def solution(n, s, a, b, fares):
    # 다익스트라 알고리즘
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        node1, node2, cost = fare
        graph[node1].append([node2, cost])
        graph[node2].append([node1, cost])
        
    def dijkstra(start, end):
        distance = [float('inf')] * (n+1)
        distance[start] = 0
        heap = []
        heapq.heappush(heap, [distance[start], start])
        while heap:
            d, node = heapq.heappop(heap)
            if node == end:
                return distance[node]
            for connected_node, cost in graph[node]:
                if d + cost < distance[connected_node]:
                    distance[connected_node] = d + cost
                    heapq.heappush(heap,[distance[connected_node], connected_node])
        return "Not connected"
    
    result = float('inf')
    for i in range(1, n+1):
        if dijkstra(s, i) == "Not connected" or dijkstra(i, a) == "Not connected" or dijkstra(i, b) == "Not connected":
            continue
        num = dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b)
        if num < result:
            result = num
    return result

print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
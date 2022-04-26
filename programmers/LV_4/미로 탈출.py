import heapq

def solution(n, start, end, roads, traps):
    # 함정으로 이동하면, 이동한 함정과 연결된 모든 화살표의 방향이 바뀝니다.
    trap = {t: [[], []] for t in traps} # end / start
    distance = [float('inf')] * (n+1)
    graph = [[] for _ in range(n+1)]
    for road in roads:
        node1, node2, cost = road
        graph[node1].append([node2, cost])
        if node1 in trap:
            trap[node1][0].append([node2, cost])
        elif node2 in trap:
            trap[node2][1].append([node1, cost])
    
    def dijkstra(start, end):
        heap = []
        distance[start] = 0
        direction = 0
        heapq.heappush(heap, (distance[start], start))
        while heap:
            d, node = heapq.heappop(heap)
            if node in trap:
                if direction == 0:
                    direction = 1
                    graph[node] = trap[node][1]
                    for i in trap[node][0]:
                        graph[i[0]].append([node, i[1]])
                    for i in trap[node][1]:
                        for j in graph[i[0]]:
                            if j[0] == node:
                                graph[i[0]].remove(j)
                                break
                else:
                    direction = 0
                    graph[node] = trap[node][0]
                    for i in trap[node][1]:
                        graph[i[0]].append([node, i[1]])
                    for i in trap[node][0]:
                        for j in graph[i[0]]:
                            if j[0] == node:
                                graph[i[0]].remove(j)
                                break
            
            for connected_node, dist in graph[node]:
                if distance[connected_node] > dist + d:
                    distance[connected_node] = dist + d
                    heapq.heappush(heap, (distance[connected_node], connected_node))

        return distance[end]
        
    return dijkstra(start, end)

print(solution(	4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
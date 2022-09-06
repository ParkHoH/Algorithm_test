import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]

    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])

    summits = set(summits)
    dp = [float('inf')] * (n+1)
    heap = []

    for gate in gates:
        dp[gate] = 0
        heapq.heappush(heap, [0, gate])

    while heap:
        intensity, g = heapq.heappop(heap)

        if dp[g] < intensity: # 힙을 갱신하는 동안 값이 달라질 수 있으므로 한 번 더 확인
            continue

        for new_g, new_intensity in graph[g]:
            max_intensity = max(intensity, new_intensity)

            if max_intensity < dp[new_g]: # 같은 경우는 이전에 탐색했다고 가정
                dp[new_g] = max_intensity

                if new_g not in summits:
                    heapq.heappush(heap, [max_intensity, new_g])

    result = [float('inf'), float('inf')]

    for summit in summits:
        if dp[summit] == result[1]:
            result[0] = min(result[0], summit)
        elif dp[summit] < result[1]:
            result = [summit, dp[summit]]

    return result

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))

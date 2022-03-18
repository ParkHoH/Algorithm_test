from collections import deque
from itertools import combinations

def solution(n, wires):
    wires_combination = list(combinations(wires, len(wires)-1))
    min_value = float('inf')
    for wire_combination in wires_combination:
        graph = [[] for _ in range(n+1)]
        visited = [0 for _ in range(n+1)]
        for wire in wire_combination:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)

        queue = deque()
        queue.append(1)
        visited[1] = 1
        cnt = 1
        while queue:
            x = queue.popleft()
            for node in graph[x]:
                if visited[node] == 0:
                    queue.append(node)
                    visited[node] = 1
                    cnt += 1
        
        a, b = cnt, n - cnt
        if n % 2 == abs(a-b):
            return n % 2
        min_value = min(min_value, abs(a-b))

    return min_value

print(solution(2,[[1,2]]))
from collections import deque

for t in range(1, 11):
    case, start = map(int, input().split())
    L = list(map(int, input().split()))
    graph = {}
    visited = {}
    for i in range(0, case, 2):
        if L[i] in graph and L[i+1] not in graph[L[i]]:
            graph[L[i]].append(L[i+1])
            visited[L[i+1]] = False
        elif L[i] not in graph:
            graph[L[i]] = [L[i+1]]
            visited[L[i]] = False
            visited[L[i+1]] = False

    result = [0, start]
    queue = deque()
    queue.append([start, 0])
    visited[start] = True
    while queue:
        node, cnt = queue.popleft()
        if cnt > result[0] or (cnt == result[0] and node > result[1]):
            result = [cnt, node]

        if node in graph:
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, cnt+1])

    print(f'#{t} {result[1]}')
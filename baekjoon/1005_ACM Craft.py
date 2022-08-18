from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    dp = [0] * (N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    W = int(input())
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        idx = queue.popleft()
        dp[idx] += cost[idx]

        if idx == W:
            break

        for i in graph[idx]:
            dp[i] = max(dp[i], dp[idx])
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    print(dp[W])
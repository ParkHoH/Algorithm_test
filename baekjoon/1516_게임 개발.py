from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
previous = [[] for _ in range(N+1)]
costs = [0] * (N+1)
indegree = [0] * (N+1)

for i in range(1, N+1):
    cost, *L = list(map(int, input().split()))
    costs[i] = cost
    previous[i] = L[:-1]

    for idx in range(len(L)-1):
        graph[L[idx]].append(i)
        indegree[i] += 1

queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    idx = queue.popleft()

    for i in graph[idx]:
        indegree[i] -= 1

        if indegree[i] == 0:
            queue.append(i)
            max_value = 0
            
            for pre_node in previous[i]:
                max_value = max(max_value, costs[pre_node])

            costs[i] += max_value

for i in range(1, N+1):
    print(costs[i])
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
children = [[] for _ in range(N+1)]
parents = [[]]
indegree = [0] * (N+1)
costs = [0] * (N+1)

for i in range(1, N+1):
    cost, n, *list_connected = map(int, input().split())
    costs[i] = cost
    indegree[i] += n
    parents.append(list_connected)

    for node in list_connected:
        children[node].append(i)

queue = deque()
time = [0] * (N+1)

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append([costs[i], i])
        time[i] = costs[i]

while queue:
    cost, node = queue.popleft()

    for child in children[node]:
        indegree[child] -= 1

        if indegree[child] == 0:
            queue.append([costs[child], child])

            for parent in parents[child]:
                time[child] = max(time[child], costs[child] + time[parent])

print(max(time))
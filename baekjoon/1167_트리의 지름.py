import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    L = list(map(int, input().split()))
    node = L[0]

    for i in range(1, len(L), 2):
        c_node = L[i]
        if c_node == -1:
            break

        graph[node].append([c_node, L[i+1]])

def dfs(node, dist):
    if distance[node] == -1:
        distance[node] = dist

        for i, new_dist in graph[node]:
            if distance[i] == -1:
                dfs(i, dist + new_dist)


distance = [-1] * (V+1)
dfs(1, 0)

max_dist = 0
max_idx = 0

for i in range(1, V+1):
    if distance[i] > max_dist:
        max_dist = distance[i]
        max_idx = i

distance = [-1] * (V+1)
dfs(max_idx, 0)
print(max(distance))

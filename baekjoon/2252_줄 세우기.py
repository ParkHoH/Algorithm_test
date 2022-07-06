import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
L = []
degree = [0] * 32001
graph = [[] for _ in range(32001)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    L.append([a, b])

for a, b in L:
    degree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    for j in graph[student]:
        degree[j] -= 1
        if degree[j] == 0:
            queue.append(j)
            
    print(student, end = ' ')
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indgree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indgree[b] += 1

queue = deque()
for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append(i)

result = []
while queue:
    idx = queue.popleft()
    result.append(idx)

    for i in graph[idx]:
        indgree[i] -= 1
        if indgree[i] == 0:
            queue.append(i)

for i in result:
    print(i, end=" ")



# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# L = []
# degree = [0] * 32001
# graph = [[] for _ in range(32001)]
# queue = deque()

# for i in range(m):
#     a, b = map(int, input().split())
#     L.append([a, b])

# for a, b in L:
#     degree[b] += 1
#     graph[a].append(b)

# for i in range(1, n + 1):
#     if degree[i] == 0:
#         queue.append(i)

# while queue:
#     student = queue.popleft()
#     for j in graph[student]:
#         degree[j] -= 1
#         if degree[j] == 0:
#             queue.append(j)
            
#     print(student, end = ' ')
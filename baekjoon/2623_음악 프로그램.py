from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indgree = [0] * (N+1)

for _ in range(M):
    length, *L = list(map(int, input().split()))
    for i in range(length-1):
        a, b = L[i], L[i+1]
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
        indgree[i] -= 1.
        if indgree[i] == 0:
            queue.append(i)

if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)
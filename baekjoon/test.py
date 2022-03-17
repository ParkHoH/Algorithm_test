# DEF solution
import sys

sys.setrecursionlimit(10**6)
TC = int(input())
for _ in range(TC):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    flag = True
    def dfs(x):
        visited[x] = 1 if visited[x] == 0 else visited[x]
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                dfs(i)
            elif visited[i] == visited[x]:
                global flag
                flag = False

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            if not flag:
                break
    print("YES" if flag else "NO")


# BFS solution
import sys
from collections import deque

TC = int(input())
for _ in range(TC):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    def bfs(x):
        queue = deque()
        queue.append(x)
        visited[x] = 1
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if visited[i] == 0:
                    visited[i] = -visited[x]
                    queue.append(i)
                elif visited[i] == visited[x]:
                    return False
        return True

    flag = True
    for i in range(1, N+1):
        if visited[i] == 0:
            if not bfs(i):
                flag = False
                break
    print("YES" if flag else "NO")
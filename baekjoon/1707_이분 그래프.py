from collections import deque
import sys

TC = int(input())
for _ in range(TC):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    flag = True
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    def BFS(x):
        visited[x] = 1
        queue = deque()
        queue.append(x)
        while queue:
            x = queue.popleft()
            for node in graph[x]:
                if visited[node] == 0:
                    visited[node] = -visited[x]
                    queue.append(node)
                elif visited[node] == visited[x]:
                    return False
        return True

    for i in range(1, N+1):
        if visited[i] == 0:
            if not BFS(i):
                flag = False
                break

    print("YES" if flag else "NO")


# my solution: 문제에서 이분 그래프에 대한 정의가 제대로 되어 있어야 함. 
# 이분 그래프는 다른 색깔로 칠해져 있는 꼭지점의 개수가 같거나 1개만 차이나야 함. 
from collections import deque
import sys

TC = int(input())
for _ in range(TC):
    N, M = map(int, sys.stdin.readline().split())
    color = [0 for _ in range(N+1)]
    queue = deque()
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        queue.append((x, y))
    
    def BFS():
        while queue:
            x, y = queue.popleft()
            if color[x] == color[y] == 0:
                color[x] = 1
                color[y] = -1
            elif color[x] == 0:
                color[x] = color[y] * (-1)
            elif color[y] == 0:
                color[y] = color[x] * (-1)
            else:
                return "NO"
        return "YES"
    print(BFS())
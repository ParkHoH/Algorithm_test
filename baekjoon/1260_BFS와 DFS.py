from collections import deque

def dfs(n):
    visited_dfs[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if visited_dfs[i] == False:
            dfs(i)

def bfs(n):
    queue = deque()
    queue.append(n)
    visited_bfs[n] = True
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if visited_bfs[i] == False:
                queue.append(i)
                visited_bfs[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
dfs(V)
print()
bfs(V)


# 위 방법은 정렬이 들어가기 때문에 시간복잡도 부분에서 비효율적임
# 초기 배열에 순서를 고려해 할당할 필요가 있음
# 단, 메모리 사용 부분은 효과적이지 않음
def dfs(n):
    visited_dfs[n] = True
    print(n, end=' ')
    for idx, value in enumerate(graph[n]):
        if value == True and visited_dfs[idx] == False:
            dfs(idx)

def bfs(n):
    queue = deque()
    queue.append(n)
    visited_bfs[n] = True
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for idx, value in enumerate(graph[n]):
            if value == True and visited_bfs[idx] == False:
                queue.append(idx)
                visited_bfs[idx] = True

N, M, V = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
dfs(V)
print()
bfs(V)

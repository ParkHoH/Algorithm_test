import heapq
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(N+1)]
heap = []

for i in range(1, N):
    heapq.heappush(heap, (board[0][i], 0, i))

answer = 0
cnt = 1

visited = [False] * N
visited[0] = True

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def append_node(node):
    for i in range(N):
        if i != node and find_parent(node) != find_parent(i):
            heapq.heappush(heap, (board[node][i], node, i))

while heap:
    if cnt == N: break

    dist, p1, p2 = heapq.heappop(heap)

    parent_p1 = find_parent(p1)
    parent_p2 = find_parent(p2)

    if parent_p1 != parent_p2:
        parent[parent_p1] = parent_p2
        answer += dist

        if not visited[p1]:
            visited[p1] = True
            append_node(p1)
            cnt += 1

        if not visited[p2]:
            visited[p2] = True
            append_node(p2)
            cnt += 1

print(answer)
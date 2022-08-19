import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key=lambda x: x[2]) # 크루스칼을 위한 정렬
parent = [i for i in range(N+1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

result = []
for a, b, c in graph:
    x = find_parent(a)
    y = find_parent(b)

    if x > y:
        parent[x] = y
        result.append(c)
    elif x < y:
        parent[y] = x
        result.append(c)

print(sum(result[:-1]))
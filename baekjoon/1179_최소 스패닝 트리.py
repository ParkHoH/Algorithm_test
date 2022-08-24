import sys
input = sys.stdin.readline

V, E = map(int, input().split())
parent = list(range(V+1))

graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

result = 0

for a, b, v in graph:
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b
        result += v

print(result)
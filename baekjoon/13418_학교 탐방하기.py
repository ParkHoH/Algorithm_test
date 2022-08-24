import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M+1)]
graph.sort(key=lambda x: x[2])

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

min_value = max_value = 0
parent = list(range(N+1))

for a, b, v in graph: # 최선의 경우
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b
        min_value += v

parent = list(range(N+1))

for a, b, v in graph[::-1]: # 최악의 경우
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b
        max_value += v

print(((N-min_value)**2) - (N-max_value)**2)
# print(max_value**2 - min_value**2)
import sys
input = sys.stdin.readline

N = int(input())
x_list, y_list, z_list = [], [], []

for i in range(N):
    x, y, z = map(int, map(int, input().split()))
    x_list.append([x, i])
    y_list.append([y, i])
    z_list.append([z, i])

x_list.sort()
y_list.sort()
z_list.sort()
graph = []

for dist_list in x_list, y_list, z_list:
    for i in range(1, N):
        v1, a = dist_list[i]
        v2, b = dist_list[i-1]
        graph.append([a, b, abs(v1-v2)])

graph.sort(key=lambda x: x[2])
parent = [i for i in range(N)]

def find_parent(x):
    if x != parent[x]:  
        parent[x] = find_parent(parent[x])
    return parent[x]

result = 0
for a, b, cost in graph:
    x = find_parent(a)
    y = find_parent(b)

    if x > y:
        parent[x] = y
        result += cost
    elif x < y:
        parent[y] = x
        result += cost

print(result)
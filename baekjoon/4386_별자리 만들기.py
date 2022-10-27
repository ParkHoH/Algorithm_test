import sys
input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

parent = [i for i in range(n+1)]
dist_list = []

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]

        dist_list.append((round(((abs(x1-x2))**2 + (abs(y1-y2))**2 )**(1/2), 2), i, j))

dist_list.sort()
answer = 0

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for distance, i, j in dist_list:
    parent_i = find(i)
    parent_j = find(j)

    if parent_i != parent_j:
        parent[parent_i] = parent_j
        answer += distance

print(answer)
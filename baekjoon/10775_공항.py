import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

G = int(input())
P = int(input())
gate = [False] * (G+1)
parent = [i for i in range(G+1)]
planes = [0] * P

for i in range(P):
    planes[i] = int(input())

def union_find(x):
    if x == parent[x]:
        return x

    parent[x] = union_find(parent[x])
    return parent[x]

result = 0
for plane in planes:
    cnt = union_find(plane)
    if cnt == 0:
        break
    
    parent[cnt] -= 1
    result += 1

print(result)
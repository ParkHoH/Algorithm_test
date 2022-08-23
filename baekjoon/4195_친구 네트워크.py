import sys
input = sys.stdin.readline


def find(x):
    if x != parent[x][0]:
        parent[x][0] = find(parent[x][0])

    return parent[x][0]


T = int(input())

for _ in range(T):
    F = int(input())
    dic_idx = {}
    parent = []
    idx = 0

    for _ in range(F):
        a, b = input().split()
        
        if a not in dic_idx:
            dic_idx[a] = idx
            parent.append([idx, 1])
            idx += 1

        if b not in dic_idx:
            dic_idx[b] = idx
            parent.append([idx, 1])
            idx += 1

        a, b = find(dic_idx[a]), find(dic_idx[b])

        if a != b:
            parent[b][0] = a
            parent[a][1] += parent[b][1]

        print(parent[a][1])
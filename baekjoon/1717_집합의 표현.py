import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def union_find(x):
    if x != parent[x]:
        parent[x] = union_find(parent[x])

    return parent[x]

for _ in range(m):
    oper, a, b = map(int, input().split())
    a = union_find(a)
    b = union_find(b)

    if oper == 0: # 합집합
        if a > b:
            parent[a] = b
        elif a < b:
            parent[b] = a

    else: # 같은 집합에 포함되어 있는지 확인
        if a == b:
            print("YES")
        else:
            print("NO")
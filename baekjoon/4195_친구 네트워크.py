import sys
input = sys.stdin.readline

T = int(input())
F = int(input())
parent = [i for i in range(N)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

for i in range(N):
    L = list(map(int, input().split()))

    for j in range(i+1, N):
        if L[j] == 1:
            a = find(i)
            b = find(j)

            if a > b:
                parent[a] = b
            elif a < b:
                parent[b] = a

def check():
    L = list(map(int, input().split()))
    standard = find(L[0]-1)

    for i in range(1, M):
        if find(L[i]-1) != standard:
            return False
            
    return True

if check():
    print("YES")
else:
    print("NO")
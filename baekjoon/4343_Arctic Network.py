import sys
input = sys.stdin.readline

for _ in range(int(input())):
    S, P = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(P)]

    dist = []

    for i in range(P):
        for j in range(i+1, P):
            if i == j:
                continue
            
            d = round(((L[i][0] - L[j][0])**2 + (L[i][1] - L[j][1])**2)**0.5, 2)
            dist.append([d, i, j])

    dist.sort()
    parent = [i for i in range(P)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])

        return parent[x]

    target = P-S
    result = [0, 0]

    for d, a, b in dist:
        a = find(a)
        b = find(b)

        if result[0] == target:
            break

        if a != b:
            parent[a] = b
            result[0] += 1
            result[1] = d

    print(f"%0.2f" %result[1])
N, K = map(int, input().split())
stuff = [[0, 0]]
L = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = stuff[i][0] 
        value = stuff[i][1]
        if j < weight:
            L[i][j] = L[i - 1][j]
        else:
            L[i][j] = max(value + L[i - 1][j - weight], L[i - 1][j])

print(L[N][K])
N = int(input())
L = [[0 for _ in range(2)] for _ in range(N)]

for i in range(N):
    L[i][0], L[i][1] = map(int, input().split())

for i in range(N):
    rank = 1
    for j in range(N):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            rank += 1
    print(rank, end=' ')
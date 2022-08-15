n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(L[i])):
        if j == 0:
            L[i][j] += L[i-1][j]
        elif j == len(L[i])-1:
            L[i][j] += L[i-1][j-1]
        else:
            L[i][j] += max(L[i-1][j-1], L[i-1][j])

print(max(L[-1]))
N, M = map(int, input().split())
L = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i]+L[j]+L[k] <= M and L[i]+L[j]+L[k] > result:
                result = L[i]+L[j]+L[k]

print(result)
n = int(input())
L = list(map(int, input().split()))

for i in range(1, n):
    L[i] = max(L[i], L[i-1] + L[i])

print(max(L))
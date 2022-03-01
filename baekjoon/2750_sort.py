N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

#Just Sort
L.sort()

#Bubble Sort
for i in range(N):
    for j in range(N):
        if L[i] < L[j]:
            L[i], L[j] = L[j], L[i]

#Insert Sort
for i in range(N):
    while i > 0 and L[i] < L[i-1]:
        L[i], L[i-1] = L[i-1], L[i]
        i -= 1

for i in range(N):
    print(L[i])
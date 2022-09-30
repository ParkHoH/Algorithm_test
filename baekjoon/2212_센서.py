N = int(input())
K = int(input())
L = set(map(int, input().split()))

L = sorted(L)
size = []

for i in range(len(L)-1):
    size.append(L[i+1] - L[i])

size.sort(reverse=True)
print(sum(size[K-1:]))
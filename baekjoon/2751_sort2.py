import sys

N = int(input())
L = []
for _ in range(N):
    L.append(int(sys.stdin.readline()))

#Just Sort
L.sort()

for i in range(N):
    print(L[i])
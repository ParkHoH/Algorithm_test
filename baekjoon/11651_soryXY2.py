import sys

N = int(sys.stdin.readline())
L = [0] * N
for i in range(N):
    L[i] = list(map(int, sys.stdin.readline().split()))

L.sort(key=lambda x : (x[1], x[0]))

for i in range(N):
    print(L[i][0], L[i][1])
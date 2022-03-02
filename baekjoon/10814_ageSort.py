import sys

N = int(sys.stdin.readline())
L = [0] * N

#my solution
for i in range(N):
    L[i] = (list(map(str, sys.stdin.readline().split())), i)

L.sort(key=lambda x : (int(x[0][0]), x[1]))

for i in range(N):
    print(L[i][0][0], L[i][0][1])


#better solution
for i in range(N):
    L[i] = list(map(str, sys.stdin.readline().split()))

L.sort(key=lambda x : int(x[0]))

for i in range(N):
    print(L[i][0], L[i][1])
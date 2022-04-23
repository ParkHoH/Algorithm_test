import sys

N, M = map(int, sys.stdin.readline().split())
L = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(len(L)-1):
    L[i+1] += L[i]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(L[end] - L[start-1])
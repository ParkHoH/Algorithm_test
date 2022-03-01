import sys

N = int(input())
XY = [0] * N

for i in range(N):
    XY[i] = list(map(int, sys.stdin.readline().split()))

XY.sort()

for i in range(N):
    print(XY[i][0], XY[i][1])
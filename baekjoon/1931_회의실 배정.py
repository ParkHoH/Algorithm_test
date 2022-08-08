import sys
input = sys.stdin.readline

N = int(input())
L = []

for _ in range(N):
    L.append(list(map(int, input().split())))

L.sort(key=lambda x: (x[1], x[0]))
result = 1
standard = L[0][1]

for i in range(1, len(L)):
    if L[i][0] >= standard:
        standard = L[i][1]
        result += 1

print(result)
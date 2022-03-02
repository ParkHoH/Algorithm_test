import sys

N = int(sys.stdin.readline())
L = [0] * N

for i in range(N):
    L[i] = sys.stdin.readline()

L = list(set(L))

#첫 번째 풀이
L.sort(key=lambda x : (len(x), x))
print(''.join(L))

#두 번째 풀이
for i in range(len(L)):
    L[i] = (L[i], len(L[i]))
L.sort(key=lambda x : (x[1], x[0]))

for i in range(len(L)):
    print(L[i][0], end='')
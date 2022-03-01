import sys
from collections import Counter

N = int(sys.stdin.readline())
L = []

for _ in range(N):
    L.append(int(sys.stdin.readline()))

L.sort()

#average
print(round(sum(L)/N))

#median
print(L[N//2])

#mode
L_mode = Counter(L).most_common(2)
if len(L_mode) > 1 and L_mode[0][1] == L_mode[1][1]:
    print(L_mode[1][0])
else:
    print(L_mode[0][0])

#interval
print(max(L) - min(L))
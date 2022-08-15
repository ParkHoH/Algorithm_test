from itertools import combinations

N, M = map(int, input().split())
L = sorted(list(combinations(range(1, N+1), M)))
for comb in L:
    for i in comb:
        print(i, end=" ")
    print()
from itertools import combinations_with_replacement

N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))

for cp in combinations_with_replacement(L, M):
    for i in cp:
        print(i, end=" ")
    print()
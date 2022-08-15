from itertools import permutations

N, M = map(int, input().split())
L = list(map(int, input().split()))
L = sorted(list(permutations(L, M)))

for permu in L:
    for i in permu:
        print(i, end=" ")
    print()
from itertools import permutations

N, M = map(int, input().split())
L = list(map(int, input().split()))

for permu in sorted(set(permutations(L, M))):
    for i in permu:
        print(i, end=" ")
    print()
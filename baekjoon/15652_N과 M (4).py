from itertools import combinations_with_replacement

N, M = map(int, input().split())
for prod in combinations_with_replacement(range(1, N+1), M):
    for i in prod:
        print(i, end=" ")
    print()
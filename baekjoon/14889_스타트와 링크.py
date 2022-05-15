from itertools import combinations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

min_value = float('inf')
for comb in combinations(range(N), N//2):
    set_N = set(range(N))
    for i in comb:
        set_N.remove(i)

    score1 = 0
    for i in comb:
        for j in comb:
            if i == j: continue
            score1 += S[i][j]

    score2 = 0
    for i in set_N:
        for j in set_N:
            if i == j: continue
            score2 += S[i][j]

    min_value = min(min_value, abs(score2-score1))
    if min_value == 0: break
    
print(min_value)
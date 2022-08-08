import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input().rstrip()))

max_cnt_species = min(k, d) + 1
cnt_species = result = 0
dic = defaultdict(int)
dic[c] += 1
cnt_species += 1

for i in range(k):
    if dic[L[i]] == 0:
        cnt_species += 1
    dic[L[i]] += 1

for i in range(k, N+k-1):
    if dic[L[i-k]] == 1:
        cnt_species -= 1
    dic[L[i-k]] -= 1
    
    if dic[L[i%N]] == 0:
        cnt_species += 1
    dic[L[i%N]] += 1

    result = max(result, cnt_species)
    if result == max_cnt_species:
        break

print(result)
from collections import defaultdict
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

choose = defaultdict(int)
cnt_species = 0

for i in range(k):
    if choose[sushi[i]] == 0:
        cnt_species += 1

    choose[sushi[i]] += 1

max_value = cnt_species + 1 if choose[c] == 0 else cnt_species

for i in range(1, N-1):
    left, right = (i-1) % N, (i+k-1) % N

    choose[sushi[left]] -= 1
    if choose[sushi[left]] == 0:
        cnt_species -= 1

    choose[sushi[right]] += 1
    if choose[sushi[right]] == 1:
        cnt_species += 1
    
    max_value = max(max_value, cnt_species + 1 if choose[c] == 0 else cnt_species)

print(max_value)
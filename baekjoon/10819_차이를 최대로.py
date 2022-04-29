from itertools import permutations

N = int(input())
L = list(map(int, input().split()))
result = 0
for permu in permutations(L, N):
    num = 0
    for i in range(len(permu)-1):
        num += abs(permu[i] - permu[i+1])
    if num > result:
        result = num
        
print(result)
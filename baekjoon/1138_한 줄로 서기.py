from itertools import permutations

N = int(input())
L = list(map(int, input().split()))
for permu in permutations(range(1, N+1), N):
    skip = False
    for i in range(len(permu)):
        left_cnt = L[permu[i]-1]
        cnt = 0
        for j in range(i):
            if permu[i] < permu[j]:
                cnt += 1
        if cnt != left_cnt:
            skip = True
            break
    if not skip:
        for i in permu:
            print(i, end=" ")
        break
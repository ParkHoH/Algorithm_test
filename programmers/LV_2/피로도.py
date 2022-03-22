from itertools import permutations
from collections import deque

# My solution: permutation
def solution(k, dungeons):
    max_value = 0
    for i in range(len(dungeons), 0, -1):
        p = list(permutations(dungeons, i))
        for j in p:
            queue = deque()
            for l in j: 
                queue.append(l)
            remained_fati = k
            cnt = 0
            stop = False
            while queue:
                min_fati, cons_fati = queue.popleft()
                if remained_fati < min_fati:
                    break
                else:
                    remained_fati -= cons_fati
                    cnt += 1
            max_value = max(max_value, cnt)
            if max_value == len(dungeons):
                stop = True
                break
        if stop:
            break
    return max_value
    
    
print(solution(80, [[80,20],[50,40],[30,10]]))
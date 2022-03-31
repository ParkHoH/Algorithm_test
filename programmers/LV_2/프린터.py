from collections import deque

def solution(priorities, location):
    L = deque()
    for i in range(len(priorities)):
        L.append((priorities[i], i))
    cnt = 0
    while True:
        cnt += 1
        if len(L) == 1: return cnt
        priority, idx = L.popleft()
        check = idx
        max_priority = max([i for i, _ in L])
        if max_priority > priority: 
            L.append((priority, idx))
            check = -1
        if check == location:
            return cnt

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
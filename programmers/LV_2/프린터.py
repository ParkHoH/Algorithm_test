from collections import deque

def solution(priorities, location):
    L = deque()
    for i in range(len(priorities)):
        L.append((priorities[i], i))
    cnt = 0
    while True:
        if len(L) == 1: 
            return cnt+1
        priority, idx = L.popleft()
        for i in range(len(L)):
            if L[i][0] > priority:
                L.append((priority, idx))
                idx = -1
                break
        else:
            cnt += 1
        if idx == location: 
            return cnt

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
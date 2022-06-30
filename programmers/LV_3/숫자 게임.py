from collections import deque

def solution(A, B):
    result = 0
    A.sort(reverse=True)
    B = deque(sorted(B, reverse=True))
    for i in A:
        if i >= B[0]:
            continue
        else:
            result += 1
            B.popleft()
    
    return result
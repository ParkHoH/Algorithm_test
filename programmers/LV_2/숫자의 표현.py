def solution(n):
    cnt = 1
    for i in range(1, n+1):
        result = i
        for j in range(i+1, n+1):
            if result == n:
                cnt += 1
                break
            elif result > n:
                break
            else:
                result += j
    return cnt


#better code
def solution(n):
    cnt = 0
    for i in range(1, n+1):
        result = 0
        for j in range(i, n+1):
            result += j
            if result == n:
                cnt += 1
                break
            elif result > n:
                break
    return cnt


# 투포인터
def solution(n):
    L = list(range(1, n+1))
    start = end = 0
    result = 0
    num = L[0]
    while end < n:
        if num == n:
            result += 1
            end += 1
            if end != n:
                num += L[end]
        
        elif num < n:
            end += 1
            num += L[end]
            
        else:
            num -= L[start]
            start += 1
            
    return result
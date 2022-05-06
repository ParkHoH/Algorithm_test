def solution(n, s):
    if s < n:
        return [-1]
    
    share = s // n
    remainder = s % n
    result = [share] * n
    idx = len(result)-1
    
    for _ in range(remainder):
        result[idx] += 1
        idx -= 1
        
    return result
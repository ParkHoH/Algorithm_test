def solution(a):
    result = [0] * len(a)
    left_min = right_min = float('inf')
    for i in range(len(a)):
        if a[i] < left_min:
            left_min = a[i]
            result[i] = 1
        
        if a[-1-i] < right_min:
            right_min = a[-1-i]
            result[-1-i] = 1
        
    return sum(result)
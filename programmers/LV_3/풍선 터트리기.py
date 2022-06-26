def solution(a):
    result = [0] * len(a)
    min_value = max_value = float("inf")
    for i in range(len(a)):
        if a[i] < min_value:
            min_value = a[i]
            result[i] = 1
            
        if a[-1-i] < max_value:
            max_value = a[-1-i]
            result[-1-i] = 1
            
    return sum(result)
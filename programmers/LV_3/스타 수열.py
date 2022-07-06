from collections import Counter

def solution(a):
    result = -1
    if len(a) == 1:
        return 0
    
    dic = Counter(a)
    for key in dic.keys():
        if dic[key] * 2 < result:
            continue
            
        max_value = key
        idx = length = 0
        while idx < len(a) - 1:
            if (a[idx] != max_value and a[idx + 1] != max_value) or a[idx] == a[idx+1]:
                idx += 1
            length += 2
            idx += 2
        
        result = max(result, length)
        
    return result
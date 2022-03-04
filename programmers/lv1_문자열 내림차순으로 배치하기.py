def solution(s):
    s_upper = []
    s_lower = []
    for i in s:
        s_upper.append(i) if i.isupper() else s_lower.append(i)
        
    s_upper.sort(reverse=True)
    s_lower.sort(reverse=True)
    
    return ''.join(s_lower) + ''.join(s_upper)


#better solution
def solution(s):
    return ''.join(sorted(s, reverse=True))

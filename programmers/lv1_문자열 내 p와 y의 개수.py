def solution(s):
    s = s.lower()
    
    if s.count('p') == s.count('y'):
        return True
    else:
        return False


#short code
def solution(s):
    s = s.sort()
    return s.count('p') == s.count('y')
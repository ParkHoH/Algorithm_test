def solution(n):
    L = []
    for i in str(int(n)):
        L.append(i)
    L.sort(reverse=True)
    
    return int(''.join(L))

#better code
def solution(n):
    a = sorted(str(int(n)), reverse=True)
    return int(''.join(a))

#short code
def solution(n):
    return int(''.join(sorted(str(int(n)), reverse=True)))
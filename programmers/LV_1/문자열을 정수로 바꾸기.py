#fixed solution
def solution(s):
    if s[0] == '+':
        return int(s[1:])
    elif s[0] == '-':
        return 0 - int(s[1:])
    else:
        return int(s)

#original solution
def solution(s):
    s = list(s)
    
    if s[0] == '+':
        return int(''.join(map(str, s[1:])))
    elif  s[0] == '-':
        return 0 - int(''.join(map(str, s[1:])))
    else:
        return int(''.join(map(str, s)))

#best solution
def solution(s):
    return int(s)
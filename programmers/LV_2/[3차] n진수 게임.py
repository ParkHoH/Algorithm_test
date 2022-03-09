def notationChange(n, base):
    digits = '0123456789ABCDEF'
    s = '' if n > 0 else digits[0]
    while n > 0:
        s += digits[n%base]
        n //= base
    return s[::-1]

def solution(n, t, m, p):
    s = ''
    num = 0
    while len(s) <= m*t:
        s += notationChange(num, n)
        num += 1
    
    result = ''
    for i in range(t):
        result += s[m*i + (p-1)]
    return result
    
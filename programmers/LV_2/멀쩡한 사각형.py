def solution(w,h):
    if w == h:
        return w * h - w
    w_set = set()
    h_set = set()
    for i in range(1, w+1):
        if w%i == 0:
            w_set.add(i)
    for i in range(1, h+1):
        if h%i == 0:
            h_set.add(i)
            
    gcd = max(w_set.intersection(h_set))
    return w * h - (w + h - gcd)


# short, better solution
from math import gcd
import math

def solution(w,h):
    return w * h - (w + h - gcd(w,h))


# recursion solution
def gcd(a, b):
    return b if a == 0 else gcd(b%a, a)

def solution(w,h):
    return w * h - (w + h - gcd(w,h))


print(solution(8, 12))
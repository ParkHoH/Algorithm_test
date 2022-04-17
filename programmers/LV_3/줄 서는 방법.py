import math

def solution(n, k):
    result = []
    num = list(range(1, n+1))
    while n:
        temp = math.factorial(n) // n
        n -= 1
        idx = k // temp
        k = k % temp
        if k == 0:
            result.append(num.pop(idx-1))
        else :
            result.append(num.pop(idx))
    return result

print(solution(3, 5))
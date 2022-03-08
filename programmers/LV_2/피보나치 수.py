def solution(n):
    a, b = 0, 1
    cnt = 1
    while True:
        c = a + b
        cnt += 1
        if cnt == n:
            return c % 1234567
        a, b = b, c


#better code
def solution(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return a+b % 1234567
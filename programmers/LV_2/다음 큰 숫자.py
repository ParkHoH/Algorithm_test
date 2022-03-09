def solution(n):
    cnt = bin(n)[2:].count("1")
    
    while n <= 1000001:
        n += 1
        if bin(n)[2:].count("1") == cnt:
            return n

print(solution(15))
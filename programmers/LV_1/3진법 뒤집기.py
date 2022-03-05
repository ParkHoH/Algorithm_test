def solution(n):
    new_n = ''
    while n:
        new_n += str(n%3)
        n = n//3
    
    return int(new_n, 3)


#just implemetation
def solution(n):
    new_n = ''
    while n:
        new_n += str(n%3)
        n = n//3

    new_n = new_n[::-1]
    
    result = 0
    for i in range(len(new_n)):
        result += (int(new_n[i]) * 3**i)
    
    return result

print(solution(45))
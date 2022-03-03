def solution(n):
    a = list(str(n))
    return sum(list(map(int, a)))

#better code
def solution(n):
    return sum(map(int, str(n)))

print(solution(123))
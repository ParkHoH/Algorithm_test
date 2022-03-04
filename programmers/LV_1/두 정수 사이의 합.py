def solution(a, b):
    a, b = min(a, b), max(a, b)
    answer = [i for i in range(a, b+1)]
    return sum(answer)


#better solution
def solution(a, b):
    a, b = min(a, b), max(a, b)
    return sum(range(a, b+1))
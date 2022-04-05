answer = 0

def dfs(n, numbers, target, result):
    if n == len(numbers):
        if result == target:
            global answer
            answer += 1
        return
    dfs(n+1, numbers, target, result+numbers[n])
    dfs(n+1, numbers, target, result-numbers[n])
    

def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return answer


# other solution: product
from itertools import product

def solution(numbers, target):
    L = [(x, -x) for x in numbers]
    result = list(map(sum, product(*L)))
    return result.count(target)


print(solution([1, 1, 1, 1, 1],3))
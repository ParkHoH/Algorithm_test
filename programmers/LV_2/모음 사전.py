from itertools import product

def solution(word):
    result = []
    for i in range(1, 6):
        result += map(''.join, product('AEIOU', repeat=i))
    result = sorted(list(result))
    return result.index(word) + 1


# short code
from itertools import product

def solution(word):
    return sorted([''.join(j) for i in range(1, 6) for j in product('AEIOU', repeat=i)]).index(word) + 1

print(solution('AAAE'))
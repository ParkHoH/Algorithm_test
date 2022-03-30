
# my solution
from itertools import permutations
def solution(numbers):
    dic = {}
    cnt = 0
    for permutation_cnt in range(1, len(numbers)+1):
        for num in list(permutations(numbers, permutation_cnt)):
            num = int(''.join(num))
            if num < 2 or num in dic:
                continue
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                cnt += 1
                dic[num] = 0
    return cnt


# 에라토스테네스의 체 solution
from itertools import permutations
def solution(n):
    set_result = set()
    for i in range(len(n)):
        set_result |= set(map(int, map("".join, permutations(n, i + 1))))
    set_result -= set(range(0, 2))
    for i in range(2, int(max(set_result) ** 0.5) + 1):
        set_result -= set(range(i * 2, max(set_result) + 1, i))
    return len(set_result)


print(solution("17"))
print(solution("011"))
def solution(nums):
    n = len(set(nums))
    answer = len(nums)/2 if n >= len(nums)/2 else n
    return answer
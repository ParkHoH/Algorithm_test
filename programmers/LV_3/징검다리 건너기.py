def solution(stones, k):
    max_value = float('inf')
    for i in range(len(stones)-k+1):
        if max(stones[i:i+k]) < max_value:
            max_value = max(stones[i:i+k])
    return max_value

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
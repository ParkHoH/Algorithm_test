def solution(brown, yellow):
    for x in range(2, brown-1):
        y = brown - x
        if (x//2-2) * (y//2) == yellow:
            return [max(x//2, y//2+2), min(x//2, y//2+2)]
            
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(18, 6))
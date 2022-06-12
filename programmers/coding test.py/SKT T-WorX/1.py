def solution(p):
    # 1번 과정
    i = 0
    result = [0] * len(p)

    # 알고리즘 종료 전까지 반복
    while i < len(p):
        j = i
        # 2번 과정
        for num in range(i, len(p)):
            if p[num] < p[j]:
                j = num

        # 3번 과정
        if i != j:
            p[i], p[j] = p[j], p[i]
            result[i] += 1
            result[j] += 1

        # 4번 과정
        i += 1

    return result

print(solution([2, 5, 3, 1, 4]))
print(solution([2, 3, 4, 5, 6, 1]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
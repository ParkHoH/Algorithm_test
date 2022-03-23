# 최종 solution
def solution(number, k):
    result = ''
    start = 0
    while len(result) != len(number)-k:
        target_range = number[start:k+len(result)+1]
        if len(target_range) == 1:
            result += number[start:]
            break
        for i in range(9, -1, -1):
            if str(i) in target_range:
                idx = target_range.index(str(i))
                break
        result += str(target_range[idx])
        start += idx + 1
    return result


# 시간 초과 solution
def solution(number, k):
    number = list(map(int, number))
    result = ''
    start = 0
    while len(result) != len(number)-k:
        target_range = number[start:k+len(result)+1]
        if len(target_range) == 1:
            result += ''.join(map(str, number[start:]))
            break
        idx = target_range.index(max(target_range))
        result += str(target_range[idx])
        start += idx + 1
    return result


# 시간 초과 solution
def solution(number, k):
    number = list(map(int, number))
    result = ''
    start = 0
    while len(result) != len(number)-k:
        target_range = number[start:k+len(result)+1]
        idx = target_range.index(max(target_range))
        result += str(target_range[idx])
        start += idx + 1
    return result

print(solution("1231234",3))
print(solution("1924",2))
print(solution("4177252841",4))

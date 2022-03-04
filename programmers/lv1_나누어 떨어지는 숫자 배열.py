def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)


#better code
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)


#short code
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]
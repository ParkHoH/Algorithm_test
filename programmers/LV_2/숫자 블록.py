def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue
        
        stop = False
        for num in range(2, int(i**0.5)+1):
            if i % num == 0:
                if i // num > 10000000:
                    continue
                answer.append(i // num)
                stop = True
                break
        
        if not stop:
            answer.append(1)
        
    return answer
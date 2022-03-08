def solution(n):
    cnt = 1
    for i in range(1, n+1):
        result = i
        for j in range(i+1, n+1):
            if result == n:
                cnt += 1
                break
            elif result > n:
                break
            else:
                result += j
    return cnt


#better code
def solution(n):
    cnt = 0
    for i in range(1, n+1):
        result = 0
        for j in range(i, n+1):
            result += j
            if result == n:
                cnt += 1
                break
            elif result > n:
                break
    return cnt
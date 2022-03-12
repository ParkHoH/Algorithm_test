def solution(n):
    result = 0
    while True:
        if n == 1:
            result += 1
            break
        else:
            if n/2 == int(n/2):
                n //= 2
            else:
                n -= 1
                result += 1
    return result


#better solution
def solution(n):
    return bin(n).count("1")
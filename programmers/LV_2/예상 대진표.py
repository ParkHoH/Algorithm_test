# my solution
def solution(n,a,b):
    criteria = n // 2
    divide = n // 2
    n //= 2
    while True:
        if divide == 1:
            return 1
        if a <= criteria and b <= criteria:
            criteria = criteria - divide//2
            divide //= 2
            continue
        elif a > criteria and b > criteria:
            criteria = criteria + divide//2
            divide //= 2
            continue
        else:
            num = 1
            cnt = 0
            while divide*2 != num:
                num *= 2
                cnt += 1
            return cnt


# bit solution
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()


# other solution
def solution(n,a,b):
    cnt = 0
    a -= 1
    b -= 1
    while a != b:
        cnt += 1
        a //= 2
        b //= 2
    return cnt


print(solution(16,9,12))
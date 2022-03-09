def solution(n, k):
    k_n = ''
    while n > 0:
        k_n += str(n % k)
        n = n // k
    k_n = k_n[::-1]
    
    split_n = k_n.split("0")
    cnt = 0
    for num in split_n:
        flag_prime = True
        if num != "" and num != "1":
            for i in range(2, int(int(num)**0.5) + 1):
                if int(num) % i == 0:
                    flag_prime = False
                    break
            cnt = cnt + 1 if flag_prime == True else cnt
    
    return cnt

print(solution(110011, 10))
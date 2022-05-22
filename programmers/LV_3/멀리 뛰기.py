import math

def solution(n):
    result = 1
    cnt_two = 0
    
    while n >= 2:
        n -= 2
        cnt_two += 1
        result += math.factorial(n+cnt_two) // (math.factorial(n) * math.factorial(cnt_two))
        
    return result % 1234567

print(solution(100))


# dp 풀이
def solution(n):
    dp = [0] * (n+1)
    if n == 1: return n
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n] % 1234567
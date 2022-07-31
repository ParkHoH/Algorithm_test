def solution(N, number):
    answer = -1
    dp = []
    
    for i in range (1,9):
        all_case = set()
        check_number = int(str(N)* i)
        all_case.add(check_number)
        
        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1] :
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
                        
        if number in all_case:
            answer = i
            break
            
        dp.append(all_case) 
        

    return answer

# 추가 풀이
def solution(N, number):
    dp = [set() for i in range(9)] # 사용횟수에 따라 가능한 숫자를 담을 리스트
    for i in range(1, 9): # 1~8
        dp[i].add(int(str(N)*i)) # 단순히 이어붙인 숫자
        for j in range(i//2 + 1):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(second - first)
                    dp[i].add(first * second)
                    if second != 0 :
                        dp[i].add(first // second)
                    if first != 0 :
                        dp[i].add(second // first)
                    
        if number in dp[i]:
            return i
    return -1
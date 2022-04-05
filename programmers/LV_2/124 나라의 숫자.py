def solution(n):
    dic = {1: "1", 2: "2", 0: "4"}
    answer = ''
    while n:
        answer += dic[n%3]
        n = n//3 if n%3 else n//3-1
    return answer[::-1]


# other solution
def solution(n):
    dic = {0: "1", 1: "2", 2: "4"}
    answer = ''
    while n:
        n -= 1
        answer += dic[n%3]
        n = n//3
    return answer[::-1]
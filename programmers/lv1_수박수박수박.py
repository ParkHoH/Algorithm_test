def solution(n):
    answer = ["수" if i%2==0 else "박" for i in range(n)]
    return ''.join(answer)

#better solution
def solution(n):
    answer = '수박' * (n//2) + '수' * (n%2)
    return answer[:n]

print(solution(4))
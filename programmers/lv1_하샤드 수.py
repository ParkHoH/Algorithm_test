#my solution
def solution(x):
    answer = False
    sum_x = 0
    
    for i in range(len(str(x))):
        sum_x += int(str(x)[i])
    
    if x % sum_x == 0:
        answer = True

    return answer

#short solution
def solution(x):
    return x % sum([int(i) for i in len(str(x))]) == 0
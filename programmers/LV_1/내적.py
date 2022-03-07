def solution(a, b):
    for i in range(len(a)):
        a[i] *= b[i]
    return sum(a)


#zip function
def solution(a, b):
    return sum([i*j for i, j in zip(a, b)])

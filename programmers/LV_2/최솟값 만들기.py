def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    result = 0
    
    for i in range(len(A)):
        result += A[i] * B[i]
    return result


#short code
def solution(A,B):
    return sum([i+j for i, j in zip(sorted(A), sorted(B, reverse=True))])
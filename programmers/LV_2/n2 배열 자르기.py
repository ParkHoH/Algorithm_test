def solution(n, left, right):
    q_left, r_left = int(left) // n, int(left) % n
    q_right, r_right = int(right) // n, int(right) % n
    L = []
    
    for a in range(q_left, q_right+1):
        L += [a+1 for _ in range(1, a+2)] + [i for i in range(a+2, n+1)]

    return L[r_left : int(right) - q_left*n + 1]

print(solution(2,1,1))
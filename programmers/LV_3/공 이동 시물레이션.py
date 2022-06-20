def solution(n, m, x, y, queries):
    result = 0
    t, l, r, b = x, y, y, x
    queries.reverse()

    for i, j in queries:
        if i == 0:
            if r + j < m:
                temp = r + j
            else:
                temp = m - 1
            if l == 0: 
                r = temp
            else: 
                l += j
                r = temp

        if i == 1:
            if l - j>=0:
                temp = l - j
            else:
                temp = 0
            if r == m - 1: 
                l = temp
            else: 
                l = temp
                r -= j

        if i == 2:
            if b + j < n:
                temp = b + j
            else:
                temp = n - 1
            if t == 0:
                b = temp
            else:
                t += j
                b = temp

        if i == 3:
            if t - j >= 0:
                temp = t - j
            else:
                temp = 0
            if b == n - 1:
                t = temp
            else:
                t = temp
                b -= j

        if l > m - 1 or r < 0 or t > n - 1 or b < 0:
            break
        
    else:
        result = ((b - t) + 1) * ((r - l) + 1)

    return result
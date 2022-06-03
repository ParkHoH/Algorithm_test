def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j-1 >= 0:
                a = triangle[i-1][j-1]
            else:
                a = 0
                
            if j < len(triangle[i])-1:
                b = triangle[i-1][j]
            else:
                b = 0
                
            triangle[i][j] += max(a, b)
    
    result = 0
    for i in triangle[-1]:
        result = max(result, i)
    
    return result
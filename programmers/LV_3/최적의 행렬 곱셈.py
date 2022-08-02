def solution(sizes):
    dp = [[0] * len(sizes) for _ in range(len(sizes))]
    
    for i in range(1, len(sizes)): 
        for j in range(0, len(sizes) - i): 
            num = i + j
            L = []
            
            for k in range(j, num):
                L.append(sizes[j][0] * sizes[k][1] * sizes[num][1] + dp[j][k] + dp[k+1][num])
                
            dp[j][num] = min(L)
            
    return dp[0][-1]


# 틀린 풀이
def solution(matrix_sizes):
    result = 0
    while len(matrix_sizes) >= 2:
        max_value = 0
        max_idx = 0
        for i in range(len(matrix_sizes) - 1):
            if matrix_sizes[i][1] > max_value:
                max_value = matrix_sizes[i][1]
                max_idx = i

        result += matrix_sizes[max_idx][0] * matrix_sizes[max_idx][1] * matrix_sizes[max_idx + 1][1]
        matrix_sizes[max_idx] = [matrix_sizes[max_idx][0], matrix_sizes[max_idx+1][1]]
        matrix_sizes.pop(max_idx + 1)

    return result

print(solution([[5,3],[3,10],[10,6]]))
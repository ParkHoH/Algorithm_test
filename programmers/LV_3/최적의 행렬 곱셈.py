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
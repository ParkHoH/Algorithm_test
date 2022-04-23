def solution(board, skill):
    new_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for type_12, r1, c1, r2, c2, degree in skill:
        new_board[r1][c1] += degree if type_12 == 2 else -degree
        new_board[r1][c2 + 1] -= degree if type_12 == 2 else -degree
        new_board[r2 + 1][c1] -= degree if type_12 == 2 else -degree
        new_board[r2 + 1][c2 + 1] += degree if type_12 == 2 else -degree
    
    # 부분합 가로 방향
    for i in range(len(new_board)-1):
        for j in range(len(new_board[0])-1):
            new_board[i][j+1] += new_board[i][j]
    
    # 부분합 세로 방향
    result = 0
    for j in range(len(new_board[0])-1):
        for i in range(len(new_board)-1):
            new_board[i+1][j] += new_board[i][j]
            board[i][j] += new_board[i][j]
            if board[i][j] >= 1:
                result += 1
                
    return result


# 시간 초과 / 정확성 통과
def solution(board, skill):
    result = len(board) * len(board[0])
    for sk in skill:
        type_12, r1, c1, r2, c2, degree = sk
        if type_12 == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if board[i][j] >= 1 and board[i][j] - degree < 1:
                        result -= 1
                    board[i][j] -= degree
                    
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if board[i][j] < 1 and board[i][j] + degree >= 1:
                        result += 1
                    board[i][j] += degree

    return result

print(solution(	[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
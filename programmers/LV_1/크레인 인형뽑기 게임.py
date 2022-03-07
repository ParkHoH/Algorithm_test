def solution(board, moves):
    cnt = 0
    L = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(L) > 0 and L[-1] == board[j][i-1]:
                    L.pop()
                    cnt += 2
                else:
                    L.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return cnt

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
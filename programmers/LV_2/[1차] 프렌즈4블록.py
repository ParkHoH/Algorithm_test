def solution(m, n, board):
    n, m = m, n
    cnt = 0
    board = [list(i) for i in board]

    while True:
        # 지워질 블록 찾기
        list_delete = set()
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] != '0': # 0인 경우 스킵
                    if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                        list_delete.add((i, j))
                        list_delete.add((i+1, j))
                        list_delete.add((i, j+1))
                        list_delete.add((i+1, j+1))

        # 지워질 블록이 없는 경우 종료
        if len(list_delete) == 0:
            break
        
        # 지워질 블록들 '0'으로 만들기
        cnt += len(list_delete)
        for i, j in list_delete:
            board[i][j] = '0'
        
        # 블록 아래로 내리기
        for j in range(m):
            for i in range(n-1, -1, -1):
                if board[i][j] == '0':
                    for k in range(i-1, -1, -1):
                        if board[k][j] != '0':
                            board[k][j], board[i][j] = board[i][j], board[k][j]
                            break
    return cnt

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
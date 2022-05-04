def ckeck_possible(n, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # 기둥 설치되어 있는 경우
            if board[i][j][0] == True:
                if (i == 0) or (board[i][j][1] == True) or (board[i][j-1][1] == True) or (board[i-1][j][0] == True):
                    continue
                return False
            
            # 보 설치되어 있는 경우
            if board[i][j][1] == True:
                if (board[i-1][j][0] == True) or (board[i-1][j+1][0] == True) or (board[i][j+1][1] == True and board[i][j-1][1] == True):
                    continue
                return False
    return True
                
def solution(n, build_frame):
    board = [[[False, False] for _ in range(n+1)] for _ in range(n+1)] # 기둥, 보 설치 여부
    result = []
    for b_frame in build_frame:
        x, y, a, b = b_frame
        # 설치
        if b == 1:
            if a == 0: # 기둥
                board[y][x][0] = True
                if not ckeck_possible(n, board):
                    board[y][x][0] = False
            else: # 보
                board[y][x][1] = True
                if not ckeck_possible(n, board):
                    board[y][x][1] = False
        # 제거
        else:
            if a == 0: # 기둥
                board[y][x][0] = False
                if not ckeck_possible(n, board):
                    board[y][x][0] = True
            else: # 보
                board[y][x][1] = False
                if not ckeck_possible(n, board):
                    board[y][x][1] = True
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == True:
                result.append([j, i, 0])
            elif board[i][j][1] == True:
                result.append([j, i, 1])
    
    result.sort()
    return result